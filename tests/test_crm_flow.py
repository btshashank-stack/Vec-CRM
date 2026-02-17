from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine

from app.db import get_session
from app.main import app


def test_end_to_end_sales_flow():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)

    def get_session_override():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)

    register = client.post(
        "/auth/register",
        json={"email": "rep@example.com", "full_name": "Sales Rep", "password": "test1234"},
    )
    assert register.status_code == 201

    login = client.post("/auth/login", json={"email": "rep@example.com", "password": "test1234"})
    assert login.status_code == 200
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    account = client.post(
        "/accounts",
        headers=headers,
        json={"name": "Acme Corp", "industry": "Software", "website": "https://acme.test"},
    )
    assert account.status_code == 200

    contact = client.post(
        "/contacts",
        headers=headers,
        json={"first_name": "Jane", "last_name": "Doe", "email": "jane@acme.test"},
    )
    assert contact.status_code == 200

    lead = client.post(
        "/leads",
        headers=headers,
        json={
            "first_name": "Alex",
            "last_name": "Buyer",
            "email": "alex@buyer.test",
            "status": "qualified",
        },
    )
    assert lead.status_code == 200

    opportunity = client.post(
        "/opportunities",
        headers=headers,
        json={"name": "Acme Expansion", "amount": 25000, "stage": "proposal"},
    )
    assert opportunity.status_code == 200

    summary = client.get("/dashboard/summary", headers=headers)
    assert summary.status_code == 200
    payload = summary.json()
    assert payload["accounts"] == 1
    assert payload["contacts"] == 1
    assert payload["leads"] == 1
    assert payload["qualified_leads"] == 1
    assert payload["opportunities"] == 1
    assert payload["open_pipeline"] == 25000

    app.dependency_overrides.clear()

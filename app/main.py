from fastapi import FastAPI

from .db import create_db_and_tables
from .routers import accounts, auth, contacts, dashboard, leads, opportunities

app = FastAPI(title="Vec CRM API", version="0.1.0")


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(contacts.router)
app.include_router(leads.router)
app.include_router(opportunities.router)
app.include_router(dashboard.router)

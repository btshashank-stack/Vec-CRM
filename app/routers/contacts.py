from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..deps import get_current_user
from ..models import Contact, User
from ..schemas import ContactCreate, ContactRead

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("", response_model=ContactRead)
def create_contact(
    payload: ContactCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    contact = Contact(**payload.model_dump(), owner_id=user.id)
    session.add(contact)
    session.commit()
    session.refresh(contact)
    return contact


@router.get("", response_model=list[ContactRead])
def list_contacts(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    return list(session.exec(select(Contact).where(Contact.owner_id == user.id)).all())

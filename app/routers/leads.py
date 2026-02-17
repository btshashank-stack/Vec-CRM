from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..deps import get_current_user
from ..models import Lead, User
from ..schemas import LeadCreate, LeadRead

router = APIRouter(prefix="/leads", tags=["leads"])


@router.post("", response_model=LeadRead)
def create_lead(
    payload: LeadCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    lead = Lead(**payload.model_dump(), owner_id=user.id)
    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead


@router.get("", response_model=list[LeadRead])
def list_leads(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    return list(session.exec(select(Lead).where(Lead.owner_id == user.id)).all())

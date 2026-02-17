from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..deps import get_current_user
from ..models import Opportunity, User
from ..schemas import OpportunityCreate, OpportunityRead

router = APIRouter(prefix="/opportunities", tags=["opportunities"])


@router.post("", response_model=OpportunityRead)
def create_opportunity(
    payload: OpportunityCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    opp = Opportunity(**payload.model_dump(), owner_id=user.id)
    session.add(opp)
    session.commit()
    session.refresh(opp)
    return opp


@router.get("", response_model=list[OpportunityRead])
def list_opportunities(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    return list(session.exec(select(Opportunity).where(Opportunity.owner_id == user.id)).all())

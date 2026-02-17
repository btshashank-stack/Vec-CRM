from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..deps import get_current_user
from ..models import Account, Contact, Lead, Opportunity, OpportunityStage, User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def summary(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    leads = session.exec(select(Lead).where(Lead.owner_id == user.id)).all()
    opportunities = session.exec(select(Opportunity).where(Opportunity.owner_id == user.id)).all()
    won_pipeline = sum(o.amount for o in opportunities if o.stage == OpportunityStage.won)
    open_pipeline = sum(
        o.amount
        for o in opportunities
        if o.stage not in {OpportunityStage.won, OpportunityStage.lost}
    )

    return {
        "accounts": len(session.exec(select(Account).where(Account.owner_id == user.id)).all()),
        "contacts": len(session.exec(select(Contact).where(Contact.owner_id == user.id)).all()),
        "leads": len(leads),
        "qualified_leads": len([lead for lead in leads if lead.status == "qualified"]),
        "opportunities": len(opportunities),
        "won_pipeline": won_pipeline,
        "open_pipeline": open_pipeline,
    }

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..deps import get_current_user
from ..models import Account, User
from ..schemas import AccountCreate, AccountRead

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("", response_model=AccountRead)
def create_account(
    payload: AccountCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    account = Account(**payload.model_dump(), owner_id=user.id)
    session.add(account)
    session.commit()
    session.refresh(account)
    return account


@router.get("", response_model=list[AccountRead])
def list_accounts(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    return list(session.exec(select(Account).where(Account.owner_id == user.id)).all())

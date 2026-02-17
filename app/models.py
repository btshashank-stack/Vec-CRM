from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class LeadStatus(str, Enum):
    new = "new"
    qualified = "qualified"
    unqualified = "unqualified"
    converted = "converted"


class OpportunityStage(str, Enum):
    prospecting = "prospecting"
    proposal = "proposal"
    negotiation = "negotiation"
    won = "won"
    lost = "lost"


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    industry: Optional[str] = None
    website: Optional[str] = None
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field(index=True)
    phone: Optional[str] = None
    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Lead(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field(index=True)
    company: Optional[str] = None
    source: Optional[str] = None
    status: LeadStatus = LeadStatus.new
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Opportunity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    amount: float = 0
    stage: OpportunityStage = OpportunityStage.prospecting
    close_date: Optional[datetime] = None
    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

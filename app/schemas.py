from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from .models import LeadStatus, OpportunityStage


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str


class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AccountCreate(BaseModel):
    name: str
    industry: Optional[str] = None
    website: Optional[str] = None


class AccountRead(AccountCreate):
    id: int
    owner_id: int
    created_at: datetime


class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    account_id: Optional[int] = None


class ContactRead(ContactCreate):
    id: int
    owner_id: int
    created_at: datetime


class LeadCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    company: Optional[str] = None
    source: Optional[str] = None
    status: LeadStatus = LeadStatus.new


class LeadRead(LeadCreate):
    id: int
    owner_id: int
    created_at: datetime


class OpportunityCreate(BaseModel):
    name: str
    amount: float = 0
    stage: OpportunityStage = OpportunityStage.prospecting
    account_id: Optional[int] = None


class OpportunityRead(OpportunityCreate):
    id: int
    owner_id: int
    created_at: datetime

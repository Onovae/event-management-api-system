from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from uuid import UUID


class RegistrationBase(BaseModel):
    id: UUID
    user_id: UUID
    event_id: UUID
    registration_date: datetime
    attended: bool = False

class RegistrationCreate(BaseModel):
    user_id: UUID
    event_id: UUID

class RegistrationUpdate(BaseModel):
    attended: Optional[bool] = None


class Registration(RegistrationBase):
    id: UUID
    registration_date: datetime
    attended: bool = False





from pydantic import BaseModel
from uuid import UUID
from datetime import date

class EventBase(BaseModel):
    title: str
    location: str
    date: date

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    is_open: bool

class Event(EventBase):
    id: UUID
    is_open: bool = True

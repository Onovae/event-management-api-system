from pydantic import BaseModel
from uuid import UUID
from datetime import date

from schemas.speaker import Speaker

class EventBase(BaseModel):
    title: str
    location: str
    date: date
    speaker_id: UUID

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    is_open: bool

class Event(EventBase):
    id: UUID
    is_open: bool = True

class EventWithSpeaker(Event):
    speaker: Speaker 

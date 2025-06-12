from pydantic import BaseModel
from uuid import UUID


class Speaker(BaseModel):
    id: UUID
    name: str
    topic: str

class SpeakerCreate(BaseModel):
    name: str
    topic: str

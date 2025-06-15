from typing import List, Optional
from uuid import uuid4, UUID
from schemas.event import Event, EventCreate, EventUpdate
from db import get_db
from services.speaker_service import get_speaker 

def get_events() -> List[Event]:
    return [Event(**event) for event in get_db()["events"]]

def get_event(event_id: UUID) -> Optional[Event]:
    return next(
        (Event(**event) for event in get_db()["events"] if str(event["id"]) == str(event_id)),
        None
    )

def create_event(event_data: EventCreate) -> Optional[Event]:
    db = get_db()
    # Validate speaker
    speaker = get_speaker(event_data.speaker_id)  
    if not speaker:
        return None 

    new_event = Event(id=uuid4(), is_open=True, **event_data.model_dump())
    db["events"].append(new_event.model_dump())
    return new_event

def update_event(event_id: UUID, event_data: EventUpdate) -> Optional[Event]:
    db = get_db()
    for i, event in enumerate(db["events"]):
        if str(event["id"]) == str(event_id):
            updated_data = event.copy()
            updated_data.update(event_data.model_dump(exclude_unset=True))
            db["events"][i] = updated_data
            return Event(**updated_data)
    return None

def delete_event(event_id: UUID) -> bool:
    db = get_db()
    before = len(db["events"])
    db["events"] = [e for e in db["events"] if str(e["id"]) != str(event_id)]
    return len(db["events"]) < before

def close_event(event_id: UUID) -> Optional[Event]:
    db = get_db()
    for i, event in enumerate(db["events"]):
        if str(event["id"]) == str(event_id):
            event["is_open"] = False
            db["events"][i] = event
            return Event(**event)
    return None

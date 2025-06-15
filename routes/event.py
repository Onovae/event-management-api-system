from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID

from schemas.event import Event, EventCreate, EventUpdate, EventWithSpeaker
from services import event_service, speaker_service

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=List[Event])
def get_events():
    return event_service.get_events()

@router.get("/{event_id}", response_model=Event)
def get_event(event_id: UUID):
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/", response_model=Event, status_code=201)
def create_event(event: EventCreate):
    created = event_service.create_event(event)
    if not created:
        raise HTTPException(status_code=400, detail="Invalid speaker ID")
    return created


@router.put("/{event_id}", response_model=Event)
def update_event(event_id: UUID, event: EventUpdate):
    updated = event_service.update_event(event_id, event)
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated

@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: UUID):
    success = event_service.delete_event(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")

@router.patch("/{event_id}/close", response_model=Event)
def close_event(event_id: UUID):
    closed = event_service.close_event(event_id)
    if not closed:
        raise HTTPException(status_code=404, detail="Event not found")
    return closed
@router.get("/{event_id}/with-speaker", response_model=EventWithSpeaker)
def get_event_with_speaker(event_id: UUID):
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    speaker = speaker_service.get_speaker(event.speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="Speaker not found")

    return EventWithSpeaker(**event.model_dump(), speaker=speaker)


@router.get("/by-speaker/{speaker_id}", response_model=List[EventWithSpeaker])
def get_events_by_speaker(speaker_id: UUID):
    events = [e for e in event_service.get_events() if e.speaker_id == speaker_id]
    result = []
    for event in events:
        speaker = speaker_service.get_speaker(event.speaker_id)
        if speaker:
            result.append(EventWithSpeaker(**event.model_dump(), speaker=speaker))
    return result

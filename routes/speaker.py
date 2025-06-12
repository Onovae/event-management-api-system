from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from schemas.speaker import Speaker
from services import speaker_service

router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.get("/", response_model=List[Speaker])
def get_speakers():
    return speaker_service.get_speakers()

@router.get("/{speaker_id}", response_model=Speaker)
def get_speaker(speaker_id: UUID):
    speaker = speaker_service.get_speaker(speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return speaker

from typing import List, Optional
from uuid import UUID
from schemas.speaker import Speaker
from db import get_db

def get_speakers() -> List[Speaker]:
    return [Speaker(**s) for s in get_db()["speakers"]]

def get_speaker(speaker_id: UUID) -> Optional[Speaker]:
    return next(
        (Speaker(**s) for s in get_db()["speakers"] if str(s["id"]) == str(speaker_id)),
        None
    )

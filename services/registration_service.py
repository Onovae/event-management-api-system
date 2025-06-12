from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from schemas.registration import Registration, RegistrationCreate
from schemas.user import User
from db import get_db
from services.user_service import get_user
from services.event_service import get_event

def get_registrations() -> List[Registration]:
    return [Registration(**r) for r in get_db()["registrations"]]

def get_registration(registration_id: UUID) -> Optional[Registration]:
    return next(
        (Registration(**r) for r in get_db()["registrations"] if str(r["id"]) == str(registration_id)),
        None
    )

def get_user_registrations(user_id: UUID) -> List[Registration]:
    return [
        Registration(**r)
        for r in get_db()["registrations"]
        if str(r["user_id"]) == str(user_id)
    ]

def register_user(reg_data: RegistrationCreate) -> Optional[Registration]:
    db = get_db()
    user = get_user(reg_data.user_id)
    event = get_event(reg_data.event_id)

    if not user or not user.is_active or not event or not event.is_open:
        return None

    # prevent duplicate registration
    for r in db["registrations"]:
        if str(r["user_id"]) == str(reg_data.user_id) and str(r["event_id"]) == str(reg_data.event_id):
            return None

    new_registration = Registration(
        id=uuid4(),
        user_id=reg_data.user_id,
        event_id=reg_data.event_id,
        registration_date=datetime.utcnow(),
        attended=False
    )

    db["registrations"].append(new_registration.model_dump())
    return new_registration

def mark_attendance(registration_id: UUID) -> Optional[Registration]:
    db = get_db()
    for i, r in enumerate(db["registrations"]):
        if str(r["id"]) == str(registration_id):
            r["attended"] = True
            db["registrations"][i] = r
            return Registration(**r)
    return None

def get_users_who_attended() -> List[User]:
    db = get_db()
    attended_user_ids = {
        str(r["user_id"])
        for r in db["registrations"]
        if r.get("attended")
    }
    return [User(**u) for u in db["users"] if str(u["id"]) in attended_user_ids]

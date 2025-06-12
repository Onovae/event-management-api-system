from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from schemas.registration import Registration, RegistrationCreate
from services import registration_service
from services.user_service import get_user

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.post("/", response_model=Registration, status_code=201)
def register_user(registration: RegistrationCreate):
    result = registration_service.register_user(registration)
    if not result:
        raise HTTPException(
            status_code=400,
            detail="Invalid registration: duplicate, inactive user, or closed event"
        )
    return result

@router.patch("/{registration_id}/attend", response_model=Registration)
def mark_attendance(registration_id: UUID):
    registration = registration_service.mark_attendance(registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration

@router.get("/", response_model=List[Registration])
def get_all_registrations():
    return registration_service.get_registrations()

@router.get("/user/{user_id}", response_model=List[Registration])
def get_user_registrations(user_id: UUID):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="User is not active")

    registrations = registration_service.get_user_registrations(user_id)
    if not registrations:
        raise HTTPException(status_code=404, detail="User has no registrations")

    return registrations

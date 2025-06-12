from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID

from schemas.user import User, UserCreate, UserUpdate
from services import user_service
from services.registration_service import get_users_who_attended

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[User])
def get_users():
    return user_service.get_users()

@router.get("/attended", response_model=List[User])
def users_who_attended():
    return get_users_who_attended()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User, status_code=201)
def create_user(user: UserCreate):
    return user_service.create_user(user)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: UUID, user: UserUpdate):
    updated = user_service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")

@router.patch("/{user_id}/deactivate", response_model=User)
def deactivate_user(user_id: UUID):
    user = user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

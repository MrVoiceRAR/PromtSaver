from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.database import get_db
from server.schemas import UserCreate, UserResponse
from server.crud import create_user, get_users

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db=db)

from sqlalchemy.orm import Session
from server.models import User, Prompt
from server.schemas import UserCreate, PromptCreate
from datetime import datetime


def create_user(db: Session, user: UserCreate):
    db_user = User(
        **user.dict(),
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

from datetime import datetime

def create_prompt(db: Session, prompt: PromptCreate):
    db_prompt = Prompt(
        **prompt.dict(),
        created_at=datetime.utcnow(),  
        updated_at=datetime.utcnow()
    )
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt


def get_prompts(db: Session):
    return db.query(Prompt).all()

def get_prompt_by_id(db: Session, prompt_id: int):
    return db.query(Prompt).filter(Prompt.prompt_id == prompt_id).first()

def delete_prompt(db: Session, prompt_id: int):
    prompt = db.query(Prompt).filter(Prompt.prompt_id == prompt_id).first()
    if prompt:
        db.delete(prompt)
        db.commit()
        return True
    return False
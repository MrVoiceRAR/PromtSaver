from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str
    profile_picture_url: Optional[str] = None

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    profile_picture_url: Optional[str] = None

    class Config:
        from_attributes = True  

class PromptCreate(BaseModel):
    title: str
    content: str
    user_id: int
    category_id: Optional[int] = None

class PromptResponse(BaseModel):
    prompt_id: int
    title: str
    content: str
    user_id: int
    category_id: Optional[int] = None

    class Config:
        from_attributes = True

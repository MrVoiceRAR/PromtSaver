from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from server.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    profile_picture_url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)

    prompts = relationship("Prompt", back_populates="user")
    
class Prompt(Base):
    __tablename__ = "prompts"
    prompt_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    category_id = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=True)

    user = relationship("User", back_populates="prompts")

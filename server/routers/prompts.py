from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.database import get_db
from server.schemas import PromptCreate, PromptResponse
from server.crud import create_prompt, delete_prompt, get_prompts, get_prompt_by_id

router = APIRouter()

@router.post("/", response_model=PromptResponse)
def create_new_prompt(prompt: PromptCreate, db: Session = Depends(get_db)):
    return create_prompt(db=db, prompt=prompt)

@router.get("/", response_model=list[PromptResponse])
def read_prompts(db: Session = Depends(get_db)):
    return get_prompts(db=db)

@router.get("/{prompt_id}", response_model=PromptResponse)
def read_prompt(prompt_id: int, db: Session = Depends(get_db)):
    prompt = get_prompt_by_id(db=db, prompt_id=prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt

@router.delete("/{prompt_id}", status_code=204)
def delete_prompt_by_id(prompt_id: int, db: Session = Depends(get_db)):
    success = delete_prompt(db=db, prompt_id=prompt_id)
    if not success:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return

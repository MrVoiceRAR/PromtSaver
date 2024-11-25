from fastapi import FastAPI
from server.routers import users, prompts
from server.database import Base, engine, initialize_database


app = FastAPI()
initialize_database()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(prompts.router, prefix="/prompts", tags=["Prompts"])

@app.get("/")
def root():
    return {"message": "Welcome to the AI Prompts API!"}

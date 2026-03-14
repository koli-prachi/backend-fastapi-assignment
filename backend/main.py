from fastapi import FastAPI
from backend.routers import user_routes, task_routes
from backend.database import Base, engine
from backend import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Backend Assignment Running"}

app.include_router(user_routes.router, prefix="/api/v1")
app.include_router(task_routes.router, prefix="/api/v1")


from fastapi import FastAPI
from app.models import Base
from app.database import engine
from app.controllers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api")

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.repositories import MovieRepository
from pydantic import BaseModel

router = APIRouter()

class MovieRequest(BaseModel):
    title: str | None = None
    description: str | None
    year: int | None = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/movies/")
def create_movie(movie_request: MovieRequest, db: Session = Depends(get_db)):
    repository = MovieRepository(db)
    return repository.create_movie(movie_request.title, movie_request.description, movie_request.year)

@router.get("/movies/")
def read_movies(db: Session = Depends(get_db)):
    repository = MovieRepository(db)
    return repository.get_movies()





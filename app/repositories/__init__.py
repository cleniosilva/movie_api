from sqlalchemy.orm import Session
from app.models import Movie

class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_movie(self, title: str, description: str, year: int) -> Movie:
        db_movie = Movie(title=title, description=description, year=year)
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)
        return db_movie

    def get_movies(self):
        return self.db.query(Movie).all()
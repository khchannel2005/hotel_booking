from sqlalchemy.orm import Session
from app.models import models
from app.database import SessionLocal

def seed_data():
    db: Session = SessionLocal()
    hotel = models.Hotel(name="Hotel Paradise", city="Kyiv", rating=4.5)
    db.add(hotel)
    db.commit()
    db.refresh(hotel)

if __name__ == "__main__":
    seed_data()

from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

def get_hotels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Hotel).offset(skip).limit(limit).all()

def create_hotel(db: Session, hotel: schemas.HotelCreate):
    new_hotel = models.Hotel(**hotel.dict())
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel

def get_hotel_by_id(db: Session, hotel_id: int):
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()

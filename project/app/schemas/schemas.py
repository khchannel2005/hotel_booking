from pydantic import BaseModel
from typing import List, Optional

class RoomBase(BaseModel):
    number: str
    price: float

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int
    hotel_id: int
    class Config:
        orm_mode = True

class HotelBase(BaseModel):
    name: str
    city: str
    rating: Optional[float]

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    id: int
    rooms: List[Room] = []
    class Config:
        orm_mode = True

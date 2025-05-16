from pydantic import BaseModel

class CarCreate(BaseModel):
    brand: str
    model: str
    year: int

class Car(CarCreate):
    id: int

    class Config:
        from_attributes = True

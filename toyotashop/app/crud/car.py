from sqlalchemy.orm import Session
from app.models.car import Car
from app.schemas.car import CarCreate

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Car).offset(skip).limit(limit).all()

def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()

def create_car(db: Session, car: CarCreate):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: Session, car_id: int, car: CarCreate):
    db_car = get_car(db, car_id)
    if not db_car:
        return None
    db_car.brand = car.brand
    db_car.model = car.model
    db_car.year = car.year
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db: Session, car_id: int):
    db_car = get_car(db, car_id)
    if not db_car:
        return False
    db.delete(db_car)
    db.commit()
    return True

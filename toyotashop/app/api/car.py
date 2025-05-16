from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.car import Car, CarCreate
from app.db.database import get_db
from app.crud.car import get_cars, get_car, create_car, update_car, delete_car

router = APIRouter(prefix="/cars", tags=["Cars"])

@router.get("/", response_model=list[Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_cars(db, skip=skip, limit=limit)

@router.get("/{car_id}", response_model=Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = get_car(db, car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.post("/", response_model=Car)
def create_car_view(car: CarCreate, db: Session = Depends(get_db)):
    return create_car(db, car)

@router.put("/{car_id}", response_model=Car)
def update_car_view(car_id: int, car: CarCreate, db: Session = Depends(get_db)):
    updated = update_car(db, car_id, car)
    if not updated:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated

@router.delete("/{car_id}")
def delete_car_view(car_id: int, db: Session = Depends(get_db)):
    success = delete_car(db, car_id)
    if not success:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"message": "Car deleted successfully"}

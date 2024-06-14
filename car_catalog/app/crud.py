from sqlalchemy.orm import Session
from . import models, schemas

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(name=car.name, power=car.power, price=car.price)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: Session, car_id: int, car: schemas.CarUpdate):
    db_car = get_car(db, car_id)
    if db_car:
        db_car.name = car.name
        db_car.power = car.power
        db_car.price = car.price
        db.commit()
        db.refresh(db_car)
        return db_car
    return None

def delete_car(db: Session, car_id: int):
    db_car = get_car(db, car_id)
    if db_car:
        db.delete(db_car)
        db.commit()
        return db_car
    return None

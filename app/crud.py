from sqlalchemy.orm import Session

import models
import schemas
import auth


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()


def create_owner_car(db: Session, car: schemas.CarCreate, user_id: int):
    db_car = models.Car(**car.dict(), owner_id=user_id)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def update_car(db: Session, car: schemas.Car, car_id: int):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()

    if db_car:
        for attr, value in car.dict().items():
            setattr(db_car, attr, value)

        db.commit()
        db.refresh(db_car)
        return db_car


def delete_car(db: Session, car_id: int):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    db.delete(db_car)
    db.commit()
    return db_car

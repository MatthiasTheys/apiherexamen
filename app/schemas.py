from pydantic import BaseModel


class CarBase(BaseModel):
    title: str
    description: str | None = None


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    cars: list[Car] = []

    class Config:
        orm_mode = True

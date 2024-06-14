from pydantic import BaseModel

class CarBase(BaseModel):
    name: str
    power: int
    price: float

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

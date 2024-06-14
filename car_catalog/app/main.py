from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_cars(request: Request, db: Session = Depends(get_db)):
    cars = crud.get_cars(db)
    return templates.TemplateResponse("index.html", {"request": request, "cars": cars})

@app.get("/cars/create")
def create_car_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/cars/create")
def create_car(request: Request, db: Session = Depends(get_db), name: str = Form(...), power: int = Form(...), price: float = Form(...)):
    car = schemas.CarCreate(name=name, power=power, price=price)
    crud.create_car(db, car)
    return RedirectResponse("/", status_code=303)

@app.get("/cars/{car_id}")
def read_car(car_id: int, request: Request, db: Session = Depends(get_db)):
    car = crud.get_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return templates.TemplateResponse("update.html", {"request": request, "car": car})

@app.post("/cars/{car_id}")
def update_car(car_id: int, request: Request, db: Session = Depends(get_db), name: str = Form(...), power: int = Form(...), price: float = Form(...)):
    car = schemas.CarUpdate(name=name, power=power, price=price)
    updated_car = crud.update_car(db, car_id, car)
    if updated_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return RedirectResponse("/", status_code=303)

@app.post("/cars/{car_id}/delete")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    crud.delete_car(db, car_id)
    return RedirectResponse("/", status_code=303)

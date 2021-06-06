from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import modelo.database as database

# Controlador
import controlador.car as car_controller
import controlador.oauth2 as oauth2

# Models
from modelo.schemas.Car import CarSchema
from modelo.cars import Car
from modelo.schemas.User import UserSchema

# Oauth2

get_db = database.get_db

router_cars = APIRouter(
    prefix='/api/cars'
)

@router_cars.post("/")
def create_car(request:CarSchema,db:Session=Depends(get_db),current_user: UserSchema = Depends(oauth2.get_scope_admin)): 
    response = car_controller.create(request.dict(),db=db)
    return response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Controlador
import controlador.car as car_controller
import controlador.oauth2 as oauth2

# Models
import modelo.database as database
from modelo.schemas.Car import CarSchema
from modelo.schemas.User import UserSchema

# Oauth2

get_db = database.get_db

router_cars = APIRouter(
    prefix='/api/cars'
)

#Crear cars
@router_cars.post("/")
def create_car(request:CarSchema,db:Session=Depends(get_db),current_user: UserSchema = Depends(oauth2.get_scope_admin)): 
    response = car_controller.create(request.dict(),db=db)
    return response

#Mostrar cars
@router_cars.get("/")
def show_car(request:CarSchema,db:Session=Depends(get_db),current_user: UserSchema = Depends(oauth2.get_scope_user_admin)): 
    response = car_controller.show(request.dict(),db=db)
    return response

#Borrar cars
@router_cars.delete("/{id}")
def delete(request:CarSchema,db:Session=Depends(get_db),current_user: UserSchema = Depends(oauth2.get_scope_user_admin)): 
    response = car_controller.delete(request.dict(),db=db)
    return response

#actualizar cars
@router_cars.post("/{id}")
def de(request:CarSchema,db:Session=Depends(get_db),current_user: UserSchema = Depends(oauth2.get_scope_user_admin)): 
    response = car_controller.update(request.dict(),db=db)
    return response
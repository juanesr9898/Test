from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
import modelo.database as database
from modelo.cars import Car
from datetime import datetime


get_db = database.get_db

def create(data:dict, db: Session = Depends(get_db)):
    #Errores por si falta un atributo 
    #Error 120 La lista de selección para la instrucción INSERT contiene menos elementos que la lista de inserción.
    # El número de valores de SELECT debe coincidir con el de columnas de INSERT.
    if not data.get("model"):
        return {
        "msg":"Faltan el modelo",
        "code":120
        }
    
    if not data.get("color"):
        return {
        "msg":"Faltan el color",
        "code":120
        }
    new_car = Car(model=data.get("model"),color=data.get("color"))
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return {
        "msg":"Car agregado con exito!",
        "car":new_car,
        "code":200
    }
    
def show(data:dict, db: Session = Depends(get_db)):
    return db.query(Car).all()

def delete(data:dict, db: Session = Depends(get_db)):
    #Errores por si falta la id
    if not data.get("id"):
        return {
        "msg":"Faltan la ID",
        "code":120
        }
    car = db.query(Car).filter(Car.id == data.get('id')).first() #Busco el carro por ID
    #Si no se encuentra mensaje
    if not car:
        return {
        "msg":"ID not found",
        "code":404
    }
        
    db.delete(car)
    db.commit()

    return {
        "msg":"Car eliminado con exito!",
        "car":car,
        "code":200
    }
    
def update(data:dict, db: Session = Depends(get_db)):
    #Errores por si falta un atributo 
    if not data.get("model"):
        return {
        "msg":"Faltan el modelo",
        "code":120
        }
    
    if not data.get("color"):
        return {
        "msg":"Faltan el color",
        "code":120
        }
        
    if not data.get("id"):
        return {
        "msg":"Faltan la ID",
        "code":120
        }
        
    car = db.query(Car).filter(Car.id == data.get('id')).first() #Busco el carro por ID
    #Si no se encuentra el car
    if not car:
        return {
        "msg":"ID not found",
        "code":404
    }

    #Asignamos los nuevos valores
    car.color = data.get("color")
    car.id = data.get("id")
    car.model = data.get("model")
    car.date = datetime.utcnow()
    
    db.add(car)
    db.commit()
    
    db.refresh(car)
    return {
        "msg":"Car actualizado con exito!",
        "car":car,
        "code":200
    }
    

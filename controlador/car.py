from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
import modelo.database as database
from modelo.cars import Car


get_db = database.get_db


def create(data:dict,db: Session = Depends(get_db)):
    new_car = Car(model=data.get("model"),color=data.get("color"))
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return {
        "msg":"Car agregado con exito!",
        "car":new_car,
        "code":200
    }
from fastapi import APIRouter, Depends
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

#Controlador
import controlador.token_authoritation as ta

# Models
import modelo.database as database
from modelo.schemas.User import UserLoginSchema
from modelo.user import User

get_db = database.get_db

router_auth = APIRouter(
    prefix='/api/token'
)

@router_auth.post("/")
def login(request:UserLoginSchema,db:Session=Depends(get_db)):
    request = request.dict()
    user = db.query(User).filter(User.email == request.get("email")).first()
    
    #Errores 
    if not user:
        return{
            "msg":"Usuario no valido",
            "code":400
        }

    if not user.password == request.get("password"):
        return{
            "msg":"Contraseña incorrecta",
            "code":400
        }
    
    if not user.email == request.get("email"):
        return{
            "msg":"Correo incorrecto",
            "code":400
        }

    data = {"sub":user.email,"scopes":[user.role]}
    access_token = ta.create_access_token(data=data,db=db) #Desde el controlador se hace el llamado para crear el token
    hour = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second) #Hora actual 
    hour_expire = datetime.now() + timedelta(minutes = ta.ACCESS_TOKEN_EXPIRES) #Hora en la que expira el token
    hour_expire = str(hour_expire.hour) + ":" + str(hour_expire.minute) + ":" + str(hour_expire.second)
    
    return {
        "access_token":access_token,
        "token_type":"bearer",
        "Hour": hour,
        "Hour expires token" : hour_expire
    }
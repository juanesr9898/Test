from fastapi import APIRouter, Depends
import controlador.hasing as hs
import controlador.token_authoritation as ta
from modelo.tokens_model import Token
from sqlalchemy.orm import Session
import modelo.database as database
from modelo.schemas.User import UserLoginSchema

# Models
from modelo.user import User

get_db = database.get_db

router_auth = APIRouter(
    prefix='/api/token'
)

@router_auth.post("/")
def login(request:UserLoginSchema,db:Session=Depends(get_db)): #Obtenemos el token 
    request = request.dict()
    user = db.query(User).filter(User.email == request.get("email")).first()
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

    data = {"sub":user.email,"scopes":[user.role]}

    access_token = ta.create_access_token(data=data,db=db) #Desde el controlador se hace el llamado para crear el token

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }


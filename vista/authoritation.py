from fastapi import APIRouter, Depends
import controlador.hasing as hs
import controlador.token_authoritation as ta
from modelo.tokens_model import Token
from sqlalchemy.orm import Session
import modelo.database as database


get_db = database.get_db

router_auth = APIRouter(
    prefix='/api/token'
)

@router_auth.get("/")
def get_token(db:Session=Depends(get_db)): #Obtenemos el token 
    data = {"sub":"juan@gmail.com"}
    access_token = ta.create_access_token(data=data,db=db) #Desde el controlador se hace el llamado para crear el token
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
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
    access_token = ta.create_access_token(data={"sub":"juan@gmail.com"}) #Desde el controlador se hace el llamado para crear el token
    new_access_token = Token(token = access_token, expire = 5)
    db.add(new_access_token)
    db.commit()
    db.refresh(new_access_token)
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
from jose import JWTError, jwt
from datetime import datetime, timedelta
import modelo.database as database
from modelo.tokens_model import Token
from sqlalchemy.orm import Session
from fastapi import Depends

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES = 5 


def create_access_token(data:dict): #Creamos el token de acceso, la data es un diccionario
    to_encode = data.copy() #copiamos lo que se tenga en la data
    expires = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRES) #La hora local del server se le suma el tiempo estipulado en la variable ACCESS_TOKEN_EXPIRES
    to_encode.update({"exp" : expires}) #Actualizamos el tiempo de expiracion 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # enviamos to_encode con el tiempo de expiracion
    return encoded_jwt

def verify_token(token : str, credentials_exception): #Verificamos el token y manejamos raise para errores
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) #Cargamos  el token descodificado con los algoritmos con los cuales se usó
        email:str = payload.get("sub")
        if email is None: #Si no existe correo se lanza error
            raise credentials_exception
        return email
    except:
        raise credentials_exception
from fastapi import FastAPI
from sqlalchemy import engine
from vista.authoritation import router_auth
import modelo.tokens_model as tkm
from modelo.database import engine

app = FastAPI()


tkm.Base.metadata.create_all(engine)

app.include_router(router_auth) #Ruta con el prefix de router_auth

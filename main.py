from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from vista.authoritation import router_auth
from vista.cars import router_cars
import modelo.tokens_model as tkm
import modelo.cars as car
import modelo.user as user
from modelo.database import engine
from fastapi_utils.session import FastAPISessionMaker
from sqlalchemy.orm import Session
from controlador.token_authoritation import verify_token_delete

database_uri = f"sqlite:///./base.db"
sessionmaker = FastAPISessionMaker(database_uri)

app = FastAPI()

def remove_expired_tokens(db: Session) -> None:
    print("---------------------------------------")
    tokens = db.query(tkm.Token).all()
    for token in tokens:
        response = verify_token_delete(token.token) #Verifico si el token esta activo o no
        if not response: #Si el token no esta activo es decir si ha expirado
            # Eliminar el token
            token_to_delete = db.query(tkm.Token).filter(tkm.Token.id == token.id) #Cojo el token que cumpla con la regla de filtrado
            if token_to_delete.first(): #Verifico que el token si exista
                token_to_delete.delete(synchronize_session=False)  #Elimina el token
                db.commit()
                print("Eliminado el token")
    

@app.on_event("startup")
@repeat_every(seconds=60, raise_exceptions=True)  # cada minuto
def remove_expired_tokens_task() -> None:
    with sessionmaker.context_session() as db:
        remove_expired_tokens(db=db)
    
tkm.Base.metadata.create_all(engine)
car.Base.metadata.create_all(engine)
user.Base.metadata.create_all(engine)

app.include_router(router_auth) #Ruta con el prefix de router_auth
app.include_router(router_cars) #Ruta con el prefix de router_auth
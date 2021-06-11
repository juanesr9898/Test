from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from fastapi_utils.session import FastAPISessionMaker
from sqlalchemy.orm import Session

#Vista
from vista.authoritation import router_auth
from vista.cars import router_cars

#Models
from modelo.database import engine
import modelo.tokens_model as tkm
import modelo.cars as car
import modelo.user as user

#Controller
from controlador.token_authoritation import verify_token_delete
from controlador.email import send_mail

database_uri = f"sqlite:///./base.db"
sessionmaker = FastAPISessionMaker(database_uri)

app = FastAPI()

async def remove_expired_tokens(db: Session) -> None:
    print("---------------------------------------")
    tokens = db.query(tkm.Token).all()
    for token in tokens:
        response = verify_token_delete(token.token) #Verifico si el token esta activo o no
        if not response: #Si el token no esta activo es decir si ha expirado
            # Eliminar el token
            token_to_delete = db.query(tkm.Token).filter(tkm.Token.id == token.id) #Cojo el token que cumpla con la regla de filtrado
            if token_to_delete.first(): #Verifico que el token si exista
                email = token_to_delete.first().sub
                token_to_delete.delete(synchronize_session=False)  #Elimina el token
                db.commit()
                print("Eliminado el token")
                print("Enviado email a ", email) 
                await send_mail(email) #Envia Email notificando que se eliminó el token y que debe usar otro otro  
                            
    

@app.on_event("startup")
@repeat_every(seconds=60, raise_exceptions=True)  # cada minuto
async def remove_expired_tokens_task() -> None:
    with sessionmaker.context_session() as db:
        await remove_expired_tokens(db=db)
 
#Models   
tkm.Base.metadata.create_all(engine)
car.Base.metadata.create_all(engine)
user.Base.metadata.create_all(engine)

#Rutas
app.include_router(router_auth)
app.include_router(router_cars)
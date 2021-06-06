from logging import raiseExceptions
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from sqlalchemy import engine
from vista.authoritation import router_auth
import modelo.tokens_model as tkm
from modelo.database import engine, get_db

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=5, raise_exceptions=True)  # cada minuto
def remove_expired_tokens_task(db:router_auth.Session=router_auth.Depends(get_db)) -> None:
    tokens = db.query(tkm.Token).all()
    print(tokens)
    print("\n\n")
    print("H")
    

tkm.Base.metadata.create_all(engine)

app.include_router(router_auth) #Ruta con el prefix de router_auth

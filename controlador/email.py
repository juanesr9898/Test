from fastapi import Depends, APIRouter
from fastapi_mail import FastMail, MessageSchema
from pydantic import EmailStr, BaseModel
from typing import List
from starlette.responses import JSONResponse

# Models
from modelo.schemas.Email import conf

fm = FastMail(conf)

#Forma del mensaje
template = """
        <html>
        <body>
          
<p>Hi!
        <br>Your token has just expired</p>
  
        </body>
        </html>
        """
#Clase donde recipients recibe el dato
#Ver documentacion fastapi email
class EmailSchema(BaseModel):
    email: List[EmailStr]

async def send_mail(email):
    email = EmailSchema(email=[email]) #Convierto el email en EmailSchema para que recipents coja el dato
    print("correo =", email)
    #Mensaje
    message = MessageSchema(
        subject="Your token has just expired",
        recipients= email.dict().get("email"),
        body=template,
        subtype="html"
        )
    
    await fm.send_message(message)
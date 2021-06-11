from fastapi_mail import ConnectionConfig

#Cambiar valores de ser necesarios de
conf = ConnectionConfig(
    MAIL_USERNAME = "Example@gmail.com",
    MAIL_PASSWORD = "password", 
    MAIL_FROM = "Example@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER="smtp.gmail.com", 
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True
)

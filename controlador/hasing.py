from passlib.context import CryptContext #Encargada de encriptar

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto") #Esquema de encriptamiento bcrypt y sera auto

class Hash():
    
    def bcrypt(password : str): #Paremetro de tipo string y encripta pass
        return pwd_cxt.hash(password)
    
    def verify(hashpassword, password): #Verificación del password con el hash password
        return pwd_cxt.verify(password, hashpassword)
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
import controlador.token_authoritation as tk_auth
from modelo.schemas.User import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token/login")

def get_current_user(security_scopes:SecurityScopes, token:str=Depends(oauth2_scheme)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f'Bearer'
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    response = tk_auth.verify_token(token)
    if not response:
        raise credentials_exception
    return response

def get_scope_admin(current_user:User=Security(get_current_user, scopes=["admin"])):
    return current_user

def get_scope_user(current_user:User=Security(get_current_user, scopes=["user"])):
    return current_user

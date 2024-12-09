from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.config.settings import auth_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print(token)
        payload = jwt.decode(token, auth_settings.SECRET_KEY, algorithms=[auth_settings.ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("id")
        print(payload)

        if username is None or user_id is None:
            print("?")
            raise credentials_exception

        return payload
    except JWTError:
        raise credentials_exception


user_dependency = Annotated[dict, Depends(get_current_user)]

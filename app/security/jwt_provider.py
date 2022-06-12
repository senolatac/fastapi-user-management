from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import get_app_settings
from datetime import datetime, timedelta
from jose import JWTError, jwt

from app.security.user_principle import UserPrinciple

SETTINGS = get_app_settings()

SECRET_KEY = SETTINGS.jwt_secret_key
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = SETTINGS.jwt_expire_minutes


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authentication/token")


def generate_token(auth: UserPrinciple):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {
        'sub': auth.username,
        'user_id': auth.id,
        'role': auth.role,
        'exp': datetime.utcnow() + expires_delta
    }

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_authentication(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get("sub")
        role: str = payload.get("role")
        user_id: int = int(payload.get("user_id"))

        if username is None:
            raise credentials_exception

        return UserPrinciple(username=username, id=user_id, role=role)
    except JWTError:
        raise credentials_exception

from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette import status

from app.core.settings import config


@dataclass
class Auth:
    token: str


def get_token(
    token_header: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]
) -> Auth:
    if token_header is None or token_header.credentials != config.AUTH.TOKEN:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "UNAUTHORIZED")
    return Auth(token=token_header.credentials)

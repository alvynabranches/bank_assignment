from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

T = TypeVar('T')

class Parameter(BaseModel):
    data = dict[str, str] = None

class RequestSchema(BaseModel):
    parameter: Parameter = Field(...)

class ResponseSchema(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
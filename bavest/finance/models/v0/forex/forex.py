from typing import Union
from pydantic import BaseModel, Field


class QueryItem(BaseModel):
    frm: str = Field(None, alias="from")
    to: str


class InfoItem(BaseModel):
    timestamp: str
    rate: float


class Forex(BaseModel):
    success: bool
    query: Union[QueryItem, None]
    info: Union[InfoItem, None]
    date: str
    result: float


def fromjson(json_response):
    if json_response is not None:
        user = Forex(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

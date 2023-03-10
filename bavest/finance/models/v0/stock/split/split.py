from typing import List
from pydantic import BaseModel


class SplitsItem(BaseModel):
    date: str
    symbol: str
    fromFactor: int
    toFactor: int


class Split(BaseModel):
    event: str
    splits: List[SplitsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Split(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

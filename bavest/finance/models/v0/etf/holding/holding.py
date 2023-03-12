from typing import List
from pydantic import BaseModel


class HoldingsItem(BaseModel):
    symbol: str
    cusip: str
    name: str
    share: float
    percent: float
    value: float
    isin: str


class EtfHolding(BaseModel):
    holdings: List[HoldingsItem] = []
    atDate: str
    symbol: str


def fromjson(json_response):
    if json_response is not None:
        user = EtfHolding(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user



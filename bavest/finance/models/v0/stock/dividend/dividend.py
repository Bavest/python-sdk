from typing import List
from pydantic import BaseModel


class DividendsItem(BaseModel):
    date: str
    recordDate: str
    amount: float
    declarationDate: str
    adjustedAmount: float
    payDate: str


class Dividend(BaseModel):
    dividends: List[DividendsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Dividend(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


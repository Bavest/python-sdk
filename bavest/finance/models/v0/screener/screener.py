from typing import List
from pydantic import BaseModel


class ScreenerItem(BaseModel):
    interestIncomeExpense: float
    symbol: str
    name: str
    isin: str


class Screener(BaseModel):
    statusCode: int
    results: List[ScreenerItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Screener(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

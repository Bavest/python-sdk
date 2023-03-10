from typing import List
from pydantic import BaseModel


class IpoCalendarItem(BaseModel):
    date: str
    exchange: str
    name: str
    numberOfShares: float
    price: float
    status: str
    symbol: str
    totalSharesValue: float


class IpoCalendar(BaseModel):
    ipoCalendar: List[IpoCalendarItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = IpoCalendar(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

from typing import List
from pydantic import BaseModel


class EconomicCalendarItem(BaseModel):
    date: str
    country: str
    actual: float
    price: float
    prev: float
    percentage: float
    impact: float
    estimate: float
    event: str


class EconomicCalendar(BaseModel):
    event: str
    economicCalendar: List[EconomicCalendarItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = EconomicCalendar(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


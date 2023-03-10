from typing import List
from pydantic import BaseModel


class EarningsConfirmedItem(BaseModel):
    date: str
    symbol: str
    exchange: str
    time: str
    title: str
    when: str
    publicationDate: str
    url: str


class EarningsConfirmed(BaseModel):
    event: str
    earningsConfirmed: List[EarningsConfirmedItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = EarningsConfirmed(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

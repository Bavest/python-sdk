from typing import List
from pydantic import BaseModel


class TranscriptItem(BaseModel):
    date: str
    transcript: str
    year: int
    quarter: int


class Earnings(BaseModel):
    symbol: str
    transcript: List[TranscriptItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Earnings(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

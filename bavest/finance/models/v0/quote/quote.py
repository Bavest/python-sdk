from typing import Union
from pydantic import BaseModel, Field


class HistoricalPrice(BaseModel):
    day: float
    fifty_days: float = Field(None, alias="50days")
    two_hundred_days: float = Field(None, alias="200days")


class Metrics(BaseModel):
    marketCapitalization: float
    avgVolume: float
    eps: float
    pe_ratio: float = Field(None, alias="pe/ratio")
    sharesOutstanding: float


class Quote(BaseModel):
    c: float
    d: float
    dp: float
    h: float
    l: float
    o: float
    pc: float
    t: float
    v: float
    historical_price: Union[HistoricalPrice, None]
    metrics: Union[Metrics, None]
    exchange: str
    earningsAnnouncement: str


def fromjson(json_response):
    if json_response is not None:
        user = Quote(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

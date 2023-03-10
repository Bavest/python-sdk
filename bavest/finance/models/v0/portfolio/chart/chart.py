from typing import List
from pydantic import BaseModel, Field


class PortfolioChartsItem(BaseModel):
    symbol: str
    amount: float
    buy_date: float


class PortfolioChart(BaseModel):
    currency: str
    frm: float = Field(None, alias="from")
    to: float
    resolution: str
    portfolio_items: List[PortfolioChartsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioChart(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

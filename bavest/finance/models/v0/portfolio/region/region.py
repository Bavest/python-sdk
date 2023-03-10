from typing import List
from pydantic import BaseModel


class PortfolioRegionsItem(BaseModel):
    region: str
    percentage: float


class PortfolioRegion(BaseModel):
    portfolio_regions: List[PortfolioRegionsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioRegion(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

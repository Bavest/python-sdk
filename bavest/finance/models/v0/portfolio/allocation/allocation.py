from typing import List
from pydantic import BaseModel


class PortfolioAllocationsItem(BaseModel):
    symbol: str
    percentage: float


class PortfolioAllocation(BaseModel):
    portfolio_allocations: List[PortfolioAllocationsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioAllocation(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


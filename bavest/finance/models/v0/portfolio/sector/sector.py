from typing import List
from pydantic import BaseModel


class PortfolioSectorItem(BaseModel):
    sector: str
    percentage: float


class PortfolioSector(BaseModel):
    portfolioSectors: List[PortfolioSectorItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioSector(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

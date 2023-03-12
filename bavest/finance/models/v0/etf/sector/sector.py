from typing import List
from pydantic import BaseModel


class SectorExposureItem(BaseModel):
    weightPercentage: float
    sector: str


class EtfSector(BaseModel):
    sectorExposure: List[SectorExposureItem] = []
    symbol: str


def fromjson(json_response):
    if json_response is not None:
        user = EtfSector(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


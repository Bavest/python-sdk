from typing import List
from pydantic import BaseModel


class CountryExposureItem(BaseModel):
    exposure: float
    country: str


class EtfCountry(BaseModel):
    countryExposure: List[CountryExposureItem] = []
    symbol: str


def fromjson(json_response):
    if json_response is not None:
        user = EtfCountry(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

from typing import Union
from pydantic import BaseModel


class ProfileItem(BaseModel):
    assetClass: str
    aum: float
    avgVolume: float
    cusip: str
    description: str
    domicile: str
    etfCompany: str
    expenseRatio: float
    inceptionDate: str
    isin: str
    name: str
    nav: float
    navCurrency: str
    website: str
    holdingsCount: float


class EtfProfile(BaseModel):
    profile: Union[ProfileItem, None]
    symbol: str


def fromjson(json_response):
    if json_response is not None:
        user = EtfProfile(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

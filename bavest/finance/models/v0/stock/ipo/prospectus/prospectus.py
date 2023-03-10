from typing import List
from pydantic import BaseModel


class ProspectusItem(BaseModel):
    symbol: str
    cik: str
    filingDate: str
    discountsAndCommissionsTotal: float
    proceedsBeforeExpensesTotal: float
    acceptedDate: str
    discountsAndCommissionsPerShare: float
    url: str
    form: str
    pricePublicTotal: float
    pricePublicPerShare: float
    proceedsBeforeExpensesPerShare: float
    ipoDate: str


class Prospectus(BaseModel):
    event: str
    prospectus: List[ProspectusItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Prospectus(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

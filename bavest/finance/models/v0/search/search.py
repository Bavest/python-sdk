from typing import List
from pydantic import BaseModel
from pydantic.schema import Optional


class ResultsItem(BaseModel):
    symbol: str
    companyName: str
    isin: Optional[str]
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool
    currency: str
    marketCapitalization: float


class Search(BaseModel):
    statusCode: int
    results: List[ResultsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Search(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

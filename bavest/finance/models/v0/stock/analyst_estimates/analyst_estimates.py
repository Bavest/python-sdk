from typing import List
from typing import Union

from pydantic import BaseModel


class EstimateValueItem(BaseModel):
    low: int or None
    high: int or None
    avg: int or None


class EstimateItem(BaseModel):
    date: str
    revenue: Union[EstimateValueItem, None]
    ebitda: Union[EstimateValueItem, None]
    ebit: Union[EstimateValueItem, None]
    netIncome: Union[EstimateValueItem, None]
    sgaExpense: Union[EstimateValueItem, None]
    eps: Union[EstimateValueItem, None]
    numberAnalystEstimatedRevenue: int
    numberAnalystsEstimatedEps: int


class AnalystEstimates(BaseModel):
    symbol: str
    estimates: List[EstimateItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = AnalystEstimates(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


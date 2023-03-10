from typing import List
from typing import Union

from pydantic import BaseModel, Field


class Multiples(BaseModel):
    equityReturn: float
    salesReturn: float
    ebitMargin: float
    capitalTurnover: float
    assetsReturn: float
    ev: float
    ev_revenue: float = Field(None, alias="ev/revenue")
    ev_ebit: float = Field(None, alias="ev/ebit")
    ev_fcf: float = Field(None, alias="ev/fcf")
    ev_ebitda: float = Field(None, alias="ev/ebitda")
    priceEarningsRatio: float
    priceBookRatio: float
    priceCashflowRatio: float
    priceSalesRatio: float
    peg: float


class Stability(BaseModel):
    equityRatio: float
    debtRatio: float
    debtToEquityRatio: float
    dynamicLeverage: float
    currentRatio: float
    fixedAssetIntensity: float
    capitalExpenditureRatio: float
    assetCoverage1: float
    assetCoverage2: float


class Revenue(BaseModel):
    equityReturn: float
    salesReturn: float
    ebitMargin: float
    ebitdaMargin: float
    capitalTurnover: float
    assetsReturn: float


class MetricsItem(BaseModel):
    multiples: Union[Multiples, None]
    stability: Union[Stability, None]
    revenue: Union[Revenue, None]
    period: str


class Fundamentals(BaseModel):
    metrics: List[MetricsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Fundamentals(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

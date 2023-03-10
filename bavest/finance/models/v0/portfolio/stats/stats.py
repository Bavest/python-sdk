from typing import List
from typing import Union

from pydantic import BaseModel, Field


class RiskReturnRatio(BaseModel):
    ABEA_DE: float = Field(None, alias="ABEA.DE")
    ADS_DE: float = Field(None, alias="ADS.DE")
    AMD: float
    DEQ_DE: float = Field(None, alias="DEQ.DE")
    total: float


class Correlation(BaseModel):
    ABEA_DE: Union[RiskReturnRatio, None] = Field(None, alias="ABEA.DE")
    ADS_DE: Union[RiskReturnRatio, None] = Field(None, alias="ADS.DE")
    AMD: Union[RiskReturnRatio, None]
    DEQ_DE: Union[RiskReturnRatio, None] = Field(None, alias="DEQ.DE")
    total: Union[RiskReturnRatio, None]


class Series(BaseModel):
    t: List[float]
    c: List[float]
    h: List[float]
    l: List[float]
    o: List[float]
    s: str
    v: List[float]


class Stats(BaseModel):
    riskFree: float
    totalReturn: float
    cagr: float
    maxDrawdown: float
    calmar: float
    mtd: float
    threeMonth: float
    sixMonth: float
    ytd: float
    oneYear: float
    threeYear: float
    fiveYear: float
    tenYear: float
    inception: float
    dailySharpe: float
    dailySortino: float
    dailyMean: float
    dailyVolume: float
    dailySkew: float
    dailyKurt: float
    bestDay: float
    worstDay: float
    monthlySharpe: float
    monthlySortino: float
    monthlyMean: float
    monthlyVol: float
    monthlySkew: float
    monthlyKurt: float
    bestMonth: float
    worstMonth: float
    yearlySharpe: float
    yearlySortino: float
    yearlyMean: float
    yearlyVol: float
    yearlySkew: float
    yearlyKurt: float
    bestYear: float
    worstYear: float
    avgDrawdown: float
    avgDrawdownDays: float
    avgUpMonth: float
    avgDownMonth: float
    winYearPerc: float
    twelveMonthWinPerc: float


class PortfolioStats(BaseModel):
    riskReturnRatio: Union[RiskReturnRatio, None]
    correlation: Union[Correlation, None]
    series: Union[Series, None]
    stats: Union[Stats, None]


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioStats(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

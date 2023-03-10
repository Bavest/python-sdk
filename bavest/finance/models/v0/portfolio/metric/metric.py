from pydantic import BaseModel, Field


class PortfolioMetric(BaseModel):
    beta: float
    twentySixWeekPriceReturnDaily: float = Field(None, alias="26WeekPriceReturnDaily")
    fiveDayPriceReturnDaily: float = Field(None, alias="5DayPriceReturnDaily")
    fiftyTwoWeekPriceReturnDaily: float = Field(None, alias="52WeekPriceReturnDaily")
    dividendPerShareAnnual: float
    treynorQuotient: float
    sharpeRatio: float
    alpha: float


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioMetric(**json_response)
        return user
    else:
        return {"error": 404, "body": "Bavest api error"}

from pydantic import BaseModel


class PortfolioPrice(BaseModel):
    c: float
    o: float
    l: float
    h: float
    dp: float
    d: float
    pc: float
    t: float


def fromjson(json_response):
    if json_response is not None:
        user = PortfolioPrice(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

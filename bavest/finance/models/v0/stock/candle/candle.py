from pydantic import BaseModel, Field


class Candle(BaseModel):
    c: list[float] = []
    h: list[float] = []
    l: list[float] = []
    o: list[float] = []
    s: str
    t: list[float] = []
    v: list[float] = []
    frm: int = Field(None, alias="from")
    to: float
    resolution: str


def fromjson(json_response):
    if json_response is not None:
        user = Candle(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


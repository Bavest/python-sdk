from pydantic import BaseModel


class Sentiment(BaseModel):
    statusCode: float
    symbol: str
    score: float
    len: float
    positive: float
    neutral: float
    negative: float


def fromjson(json_response):
    if json_response is not None:
        user = Sentiment(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


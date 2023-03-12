from typing import List
from pydantic import BaseModel


class SentimentItem(BaseModel):
    date: str
    impressions: float
    sentiment: float
    comments: float
    likes: float
    posts: float


class SocialSentiment(BaseModel):
    stockwits: List[SentimentItem] = []
    symbol: str
    twitter: List[SentimentItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = SocialSentiment(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user


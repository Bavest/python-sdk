from typing import List
from pydantic import BaseModel, Field


class NewsItem(BaseModel):
    category: str
    date_time: float = Field(None, alias="datetime")
    headline: str
    id: float
    image: str
    related: str
    source: str
    summary: str
    url: str


class News(BaseModel):
    news: List[NewsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = News(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

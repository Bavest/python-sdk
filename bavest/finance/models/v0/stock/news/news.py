from typing import List
from pydantic import BaseModel


class NewsItem(BaseModel):
    symbol: str
    publishedDate: str
    title: str
    image: str
    site: str
    text: str
    url: str


class News(BaseModel):
    news: List[NewsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = News(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

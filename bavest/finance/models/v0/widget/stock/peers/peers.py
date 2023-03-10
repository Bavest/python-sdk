from typing import List
from pydantic import BaseModel


class StockPeersItem(BaseModel):
    symbol: str
    name: str
    category: str
    close: float
    priceChange: float


class StockPeers(BaseModel):
    stock_peers: List[StockPeersItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = StockPeers(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

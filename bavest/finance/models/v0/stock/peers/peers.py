from typing import List
from pydantic import BaseModel


class Peers(BaseModel):
    peers: List[str] = []


def fromjson(json_response):
    if json_response is not None:
        user = Peers(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

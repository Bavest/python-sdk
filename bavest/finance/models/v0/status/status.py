from pydantic import BaseModel


class Status(BaseModel):
    statusCode: int
    body: str


def fromjson(json_response):
    if json_response is not None:
        user = Status(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

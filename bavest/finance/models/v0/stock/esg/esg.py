from typing import List
from typing import Union
from pydantic import BaseModel, Field


class DataItem(BaseModel):
    formType: str
    acceptedDate: str
    date: str


class ScoreItem(BaseModel):
    score: float
    date: str


class SectorScore(BaseModel):
    score: float
    d: float


class Sector(BaseModel):
    year: int
    sector: str
    environmentalScore: Union[SectorScore, None]
    socialScore: Union[SectorScore, None]
    governanceScore: Union[SectorScore, None]
    totalESGScore: Union[SectorScore, None]


class Series(BaseModel):
    totalESGScore: List[ScoreItem] = []
    socialScore: List[ScoreItem] = []
    governanceScore: List[ScoreItem] = []
    environmentScore: List[ScoreItem] = []


class RankObj(BaseModel):
    pos: float
    total: float


class IndustrieRating(BaseModel):
    symbol: str
    cik: str
    companyName: str
    industry: str
    year: int
    ESGRiskRating: str
    industryRank: Union[RankObj, None]


class Esg(BaseModel):
    data: List[DataItem] = []
    series: Union[Series, None]
    sector: Union[Sector, None]
    industrie_rating: Union[IndustrieRating, None] = Field(None, alias="industrie-rating")
    environmentScore: float
    governanceScore: float
    socialScore: float
    symbol: str
    totalESGScore: float


def fromjson(json_response):
    if json_response is not None:
        user = Esg(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

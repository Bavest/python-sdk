from pydantic import BaseModel


class Profile(BaseModel):
    symbol: str
    beta: float
    price: float
    volAvg: float
    lastDiv: float
    range: str
    changes: float
    companyName: str
    currency: str
    cik: str
    isin: str
    cusip: str
    exchange: str
    exchangeShortName: str
    industry: str
    website: str
    description: str
    ceo: str
    sector: str
    country: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    dcfDiff: float
    dcf: float
    isEtf: bool
    isActivelyTrading: bool
    isAdr: bool
    isFund: bool
    marketCapitalization: float
    employeeTotal: float
    ipo: str


def fromjson(json_response):
    if json_response is not None:
        user = Profile(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

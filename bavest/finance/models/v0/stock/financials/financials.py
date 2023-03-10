from typing import List
from pydantic import BaseModel


class FinancialsItem(BaseModel):
    date: str
    symbol: str
    reportedCurrency: str
    cik: float
    fillingDate: str
    acceptedDate: str
    calendarYear: str
    period: str
    stockBasedCompensation: float
    accountsReceivables: float
    inventory: float
    accountsPayables: float
    otherWorkingCapital: float
    otherNonCashItems: float
    netCashProvidedByOperatingActivities: float
    investmentsInPropertyPlantAndEquipment: float
    acquisitionsNet: float
    purchasesOfInvestments: float
    salesMaturitiesOfInvestments: float
    otherInvestingActivites: float
    debtRepayment: float
    commonStockIssued: float
    otherFinancingActivites: float
    effectOfForexChangesOnCash: float
    cashAtEndOfPeriod: float
    cashAtBeginningOfPeriod: float
    link: str
    finalLink: str
    capex: float
    cashDividendsPaid: float
    changeinCash: float
    changesinWorkingCapital: float
    deferredTaxesInvestmentTaxCredit: float
    depreciationAmortization: float
    fcf: float
    issuanceReductionCapitalStock: float
    netCashFinancingActivities: float
    netIncomeStartingLine: float
    netInvestingCashFlow: float
    netOperatingCashFlow: float


class Financials(BaseModel):
    financials: List[FinancialsItem] = []


def fromjson(json_response):
    if json_response is not None:
        user = Financials(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

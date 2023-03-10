from pydantic import BaseModel, Field


class Metric(BaseModel):
    symbol: str
    date: str
    period: str
    revenueGrowth: float
    grossProfitGrowth: float
    ebitgrowth: float
    operatingIncomeGrowth: float
    netIncomeGrowth: float
    epsgrowth: float
    epsdilutedGrowth: float
    weightedAverageSharesGrowth: float
    weightedAverageSharesDilutedGrowth: float
    dividendsperShareGrowth: float
    operatingCashFlowGrowth: float
    freeCashFlowGrowth: float
    tenYRevenueGrowthPerShare: float
    fiveYRevenueGrowthPerShare: float
    threeYRevenueGrowthPerShare: float
    tenYOperatingCFGrowthPerShare: float
    fiveYOperatingCFGrowthPerShare: float
    threeYOperatingCFGrowthPerShare: float
    tenYNetIncomeGrowthPerShare: float
    fiveYNetIncomeGrowthPerShare: float
    threeYNetIncomeGrowthPerShare: float
    tenYShareholdersEquityGrowthPerShare: float
    fiveYShareholdersEquityGrowthPerShare: float
    threeYShareholdersEquityGrowthPerShare: float
    tenYDividendperShareGrowthPerShare: float
    fiveYDividendperShareGrowthPerShare: float
    threeYDividendperShareGrowthPerShare: float
    receivablesGrowth: float
    inventoryGrowth: float
    assetGrowth: float
    bookValueperShareGrowth: float
    debtGrowth: float
    rdexpenseGrowth: float
    sgaexpensesGrowth: float
    revenuePerShare: float
    netIncomePerShare: float
    operatingCashFlowPerShare: float
    freeCashFlowPerShare: float
    cashPerShare: float
    bookValuePerShare: float
    tangibleBookValuePerShare: float
    shareholdersEquityPerShare: float
    interestDebtPerShare: float
    marketCap: float
    enterpriseValue: float
    peRatio: float
    priceToSalesRatio: float
    pocfratio: float
    pfcfRatio: float
    pbRatio: float
    ptbRatio: float
    evToSales: float
    enterpriseValueOverEBITDA: float
    evToOperatingCashFlow: float
    evToFreeCashFlow: float
    earningsYield: float
    freeCashFlowYield: float
    debtToEquity: float
    debtToAssets: float
    netDebtToEBITDA: float
    currentRatio: float
    interestCoverage: float
    incomeQuality: float
    dividendYield: float
    dividendYieldPercentage: float
    payoutRatio: float
    salesGeneralAndAdministrativeToRevenue: float
    researchAndDevelopementToRevenue: float
    intangiblesToTotalAssets: float
    capexToOperatingCashFlow: float
    capexToRevenue: float
    capexToDepreciation: float
    stockBasedCompensationToRevenue: float
    grahamNumber: float
    roic: float
    returnOnTangibleAssets: float
    grahamNetNet: float
    workingCapital: float
    tangibleAssetValue: float
    netCurrentAssetValue: float
    investedCapital: float
    averageReceivables: float
    averagePayables: float
    averageInventory: float
    daysSalesOutstanding: float
    daysPayablesOutstanding: float
    daysOfInventoryOnHand: float
    receivablesTurnover: float
    payablesTurnover: float
    inventoryTurnover: float
    roe: float
    capexPerShare: float
    dividendPerShare: float
    debtToMarketCap: float
    oneDayPriceReturnDaily: float = Field(None, alias="1DayPriceReturnDaily")
    fiveDayPriceReturnDaily: float = Field(None, alias="5DayPriceReturnDaily")
    fourWeekPriceReturnDaily: float = Field(None, alias="4WeekPriceReturnDaily")
    thirteenWeekPriceReturnDaily: float = Field(None, alias="13WeekPriceReturnDaily")
    twentysixWeekPriceReturnDaily: float = Field(None, alias="26WeekPriceReturnDaily")
    yearToDatePriceReturnDaily: float
    oneyearPriceReturnDaily: float = Field(None, alias="1yearPriceReturnDaily")
    threeyearPriceReturnDaily: float = Field(None, alias="3yearPriceReturnDaily")
    fiveyearPriceReturnDaily: float = Field(None, alias=" 5yearPriceReturnDaily")
    tenyearPriceReturnDaily: float = Field(None, alias="10yearPriceReturnDaily")
    maxPriceReturnDaily: float


def fromjson(json_response):
    if json_response is not None:
        user = Metric(**json_response)
    else:
        return {"error": 404, "body": "Bavest api error"}
    return user

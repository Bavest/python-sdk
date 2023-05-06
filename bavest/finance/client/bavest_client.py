import json
from datetime import datetime
from enum import Enum
import sys

import requests.exceptions
from . import urls
from bavest import api
from bavest.errors import *

sys.tracebacklimit = 0


class Freq(Enum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"


class Statement(Enum):
    BALANCE = "bs"
    INCOME = "ic"
    CASHFLOW = "cf"


class Resolution(Enum):
    ONE = "1"
    FIVE = "5"
    SIXTY = "60"
    DAILY = "D"
    WEEKLY = "W"
    MONTHLY = "M"


class Operator(Enum):
    LESSER = "lt"
    GREATER = "gt"
    LESSER_AND_EQUAL = "lte"
    GREATER_AND_EQUAL = "gte"
    EQUAL = "eq"


class Metric(Enum):
    EQUITY_RATIO = "equityRatio"
    DEBT_RATIO = "debtRatio"
    DEBT_TO_EQUITY_RATIO = "debtToEquityRatio"
    DYNAMIC_LEVERAGE = "dynamicLeverage"
    CATA_RATIO = "cataRatio"
    CURRENT_RATIO = "currentRatio"
    FIXED_ASSET_INTENSITY = "fixedAssetIntensity"
    PPE_RATIO = "ppeRatio"
    ASSET_COVERAGE1 = "assetCoverage1"
    ASSET_COVERAGE2 = "assetCoverage2"
    CASH_RATIO = "cashRatio"
    QUICK_RATIO = "quickRatio"

    RETURN_ON_EQUITY = "returnOnEquity"
    SALES_RETURN = "salesReturn"
    EBIT_MARGIN = "ebitMargin"
    EBITA_MARGIN = "ebitdaMargin"
    CAPITAL_TURNOVER = "capitalTurnover"
    ASSETS_RETURN = "assetsReturn"

    EV = "ev"
    EV_REVENUE = "ev/revenue"
    EV_EBIT = "ev/ebit"
    EV_FCF = "ev/fcf"
    EV_EBITDA = "ev/ebitda"
    PRICE_EARNINGS_RATIO = "priceEarningsRatio"
    PRICE_BOOK_RATIO = "priceBookRatio"
    PRICE_CASHFLOW_RATIO = "priceCashflowRatio"
    PRICE_SALES_RATIO = "priceSalesRatio"
    PROPERTY_PLANT_EQUIPMENT = "propertyPlantEquipment"


class TransactionItem:
    symbol = None
    amount = 0.0
    buy_date = 0

    def __init__(self, symbol, amount, buy_date):
        self.symbol = symbol
        self.amount = amount
        self.buy_date = datetime.timestamp(buy_date)

    def get(self):
        return {"symbol": self.symbol, "amount": self.amount, "buy_date": self.buy_date}


class QueryItem:
    metric = None
    operator = None
    value = 1

    def __init__(self, metric, operator, value):
        if not isinstance(operator, Operator):
            raise TypeError("Operator must be a enum")
        if not isinstance(metric, Metric):
            raise TypeError("Metric must be a enum")
        self.metric = metric.value
        self.operator = operator.value
        self.value = value

    def get(self):
        return {"metric": self.metric, "operator": self.operator, "value": self.value}


class SortItem:
    metric = None
    order = None

    def __init__(self, metric, order):
        self.metric = metric
        self.order = order

    def get(self):
        return {"metric": self.metric, "order": self.order}


class Stock:
    response = {}

    def __init__(self, headers):
        self.headers = headers

    def profile(self, symbol):
        """
        returns stock profile for specific stock ticker symbol
        :param symbol:string
        :return stock profile:
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_profile, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def metric(self, symbol, currency="EUR"):
        """
        returns the stock metrics for specific stock ticker symbol
        currency is optional with default unit Euro
        :param symbol:string
        :param currency:string
        :return stock metrics:
        """
        try:
            body = {"symbol": symbol, "currency": currency}
            self.response = api.post(urls.stock_metric, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def dividend(self, symbol, currency="EUR"):
        """
        returns the stock dividends for specific stock ticker symbol
        currency is optional with default unit Euro
        :param symbol:string
        :param currency:string
        :return: stock dividends
        """
        try:
            body = {"symbol": symbol, "currency": currency}
            self.response = api.post(urls.stock_dividend, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def news(self, symbol):
        """
        returns the stock news for specific stock ticker symbol
        :param symbol:string
        :return stock news:
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_news, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def calendaripo(self, frm_date, to_date):
        """
        returns the stock calendarIpo for specific from and to dates
        :param frm_date:datetime
        :param to_date:datetime
        :return: calenderIpo
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"from": frm_time, "to": to_time}
            self.response = api.post(urls.stock_calender_ipo, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def peers(self, symbol):
        """
        returns a list of stock peers for specific stock ticker symbol
        :param symbol:string
        :return:peers
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_peers, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def financials(self, symbol, freq, statement, currency="EUR"):
        """
        returns the stock financials for specific stock ticker symbol
        currency is optional with default unit Euro
        :param symbol:string
        :param freq:an enum instance of class Freq
        :param statement: an enum instance of class Statement
        :param currency:optional
        :return:stock financials
        """
        try:
            body = {"symbol": symbol, "freq": freq.name, "statement": statement.name, "currency": currency}
            self.response = api.post(urls.stock_financials, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def candles(self, symbol, frm_date, to_date, resolution, currency="EUR"):
        """
        returns the stock candles for specific stock ticker symbol
        currency is optional with default unit Euro
        :param symbol:string
        :param frm_date:datetime
        :param to_date:datetime
        :param resolution:an enum instance of class Resolution
        :param currency:string
        :return: stock candles
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"symbol": symbol, "from": frm_time, "to": to_time, "resolution": resolution.name,
                    "currency": currency}
            self.response = api.post(urls.stock_candle, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def fundamentals(self, symbol):
        """
        returns the stock fundamentals for specific stock ticker symbol
        :param symbol:string
        :return:stock fundamentals
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_profile, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def esg(self, symbol):
        """
        returns the stock esg for specific stock ticker symbol
        :param symbol: string
        :return: stock esg
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_esg, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def transcript(self, symbol):
        """
        returns the stock transcript for specific stock ticker symbol
        :param symbol:string
        :return:stock transcript
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_earnings_transcript, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def economics(self, frm_date, to_date, event="economics"):
        """
        returns the economics data for specific duration between dates
        :param frm_date: datetime
        :param to_date: datetime
        :param event:economics:optional
        :return: economics
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"event": event, "from": frm_time, "to": to_time}
            self.response = api.post(urls.stock_economics_calendar, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def earnings(self, frm_date, to_date, event="earnings"):
        """
        returns the earnings data for the specific duration between dates
        :param frm_date:datetime
        :param to_date:datetime
        :param event:optional
        :return:earnings
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"event": event, "from": frm_time, "to": to_time}
            self.response = api.post(urls.stock_earnings_confirmed, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def prospectus(self, frm_date, to_date):
        """
        returns the prospectus data for the specific duration between dates
        :param frm_date:datetime
        :param to_date: datetime
        :return:prospectus
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"from": frm_time, "to": to_time}
            self.response = api.post(urls.stock_ipo_prospectus, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def split(self, symbol, frm_date, to_date):
        """
        returns the splits data of the ticker symbol for the specific duration between dates
        :param symbol:string
        :param frm_date:datetime
        :param to_date: datetime
        :return:splits
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"symbol": symbol, "from": frm_time, "to": to_time}
            self.response = api.post(urls.stock_split, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def estimates(self, symbol):
        """
        returns the estimates data of the specific ticker symbol
        :param symbol:
        :return:estimates
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_estimates, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")


class Portfolio:
    response = {}

    def __init__(self, headers):
        self.headers = headers

    def region(self, transaction_items):
        """
        returns the portfolio region data for each input TransactionItems
        :param transaction_items:List of TransactionItem
        :return:portfolio region
        """
        try:
            body = {"portfolio_items": transaction_items}
            self.response = api.post(urls.portfolio_region, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def stats(self, frm_date, to_date, resolution, transaction_items, currency="EUR"):
        """
        returns the stats data for transaction items for specific duration and resolution
        :param frm_date: datetime
        :param to_date:datetime
        :param resolution:an enum instance of class Resolution
        :param transaction_items:List of TransactionItem
        :param currency:optional
        :return: stats
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"portfolio_items": transaction_items, "from": frm_time, "to": to_time,
                    "resolution": resolution.name,
                    "currency": currency}
            self.response = api.post(urls.portfolio_stats, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def chart(self, frm_date, to_date, resolution, transaction_items, currency="EUR"):
        """
        returns the chart data for transaction items for specific duration and resolution
        :param frm_date: datetime
        :param to_date:datetime
        :param resolution:an enum instance of class Resolution
        :param transaction_items:List of TransactionItem
        :param currency:optional
        :return: charts
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"portfolio_items": transaction_items, "from": frm_time, "to": to_time,
                    "resolution": resolution.name,
                    "currency": currency}
            self.response = api.post(urls.portfolio_chart, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def price(self, transaction_items, currency="EUR"):
        """
        returns the prices for inputs of TransactionItems
        :param transaction_items: List of TransactionItem
        :param currency:optional
        :return: prices
        """
        try:
            body = {"portfolio_items": transaction_items, "currency": currency}
            self.response = api.post(urls.portfolio_price, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def sector(self, transaction_items):
        """
        returns the sectors for inputs of TransactionItems
        :param transaction_items: List of TransactionItem
        :return:sectors
        """
        try:
            body = {"portfolio_items": transaction_items}
            self.response = api.post(urls.portfolio_sector, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def metric(self, transaction_items, currency="EUR"):
        """
        returns the metrics for inputs of TransactionItems
        :param transaction_items: List of TransactionItem
        :param currency:optional
        :return: metrics
        """
        try:
            body = {"portfolio_items": transaction_items, "currency": currency}
            self.response = api.post(urls.portfolio_metric, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def allocation(self, transaction_items, currency="EUR"):
        """
        returns the allocations for inputs of TransactionItems
        :param transaction_items: List of TransactionItem
        :param currency:optional
        :return: allocations
        """
        try:
            body = {"portfolio_items": transaction_items, "currency": currency}
            self.response = api.post(urls.portfolio_allocation, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")


class Widget:
    response = {}

    def __init__(self, headers):
        self.headers = headers

    def peers(self, symbol, currency="EUR"):
        """
        returns the peers for specific ticker symbol
        :param symbol:string
        :param currency:optional
        :return: peers
        """
        try:
            body = {"symbol": symbol, "currency": currency}
            self.response = api.post(urls.widget_stock_peers, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")


class Sentiment:
    response = {}

    def __init__(self, headers):
        self.headers = headers

    def sentiment(self, symbol):
        """
        returns sentiments for the specific ticker symbol
        :param symbol:string
        :return: sentiment
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.sentiment, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def social(self, symbol):
        """
        returns social sentiments for the specific ticker symbol
        :param symbol:string
        :return:social sentiments
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.social_sentiment, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")


class ETF:
    response = {}

    def __init__(self, headers):
        self.headers = headers

    def profile(self, symbol):
        """
        returns etf profile for the specific ticker symbol
        :param symbol:string
        :return:etf profile
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.etf_Profile, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def holdings(self, symbol):
        """
        returns etf holdings for the specific ticker symbol
        :param symbol:string
        :return:etf holdings
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.etf_holding, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def sector(self, symbol):
        """
        returns etf sector for the specific ticker symbol
        :param symbol:string
        :return:etf sector
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.etf_sector, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def country(self, symbol):
        """
        returns etf country for the specific ticker symbol
        :param symbol:string
        :return:etf country
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.etf_country, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")


class Forex:
    response = {}

    def __init__(self, headers):
        self.headers = headers

    def quote(self, frm, to):
        """
        returns the exchange rates of input specific from and to currency units
        :param frm:string
        :param to:string
        :return: exchange quote
        """
        try:
            body = {"from": frm, "to": to}
            self.response = api.post(urls.forex, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")


class BavestRESTClient:
    headers = {}
    response = {}
    stock = None
    portfolio = None
    widget = None
    sentiment = None
    etf = None
    forex = None

    def __init__(self, key):
        self.headers = {'Content-Type': 'application/json', 'x-api-key': key}
        self.stock = Stock(self.headers)
        self.portfolio = Portfolio(self.headers)
        self.widget = Widget(self.headers)
        self.sentiment = Sentiment(self.headers)
        self.etf = ETF(self.headers)
        self.forex = Forex(self.headers)

    def quote(self, symbol, currency="EUR"):
        """
        returns quote for specific ticker symbol
        :param symbol:string
        :param currency:optional
        :return:quote
        """
        try:
            body = {"symbol": symbol, "currency": currency}
            self.response = api.post(urls.quote_url, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def candles(self, symbol, frm_date, to_date, resolution, currency="EUR"):
        """
        returns stock candles for the specific duration
        :param symbol:string
        :param frm_date: datetime
        :param to_date: datetime
        :param resolution:an enum of class Resolution
        :param currency:optional
        :return:
        """
        try:
            frm_time = datetime.timestamp(frm_date)
            to_time = datetime.timestamp(to_date)
            body = {"symbol": symbol, "from": frm_time, "to": to_time, "resolution": resolution.name,
                    "currency": currency}
            self.response = api.post(urls.candle_url, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def news(self, symbol):
        """
        returns stock specific news for the specific ticker symbol
        :param symbol:string
        :return:stock news
        """
        try:
            body = {"symbol": symbol}
            self.response = api.post(urls.stock_news, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def screener(self, query_items, offset=0, limit=100):
        """
        returns a list of companies based on QueryItems
        :param query_items:List of QueryItem
        :param offset:optional
        :param limit:optional
        :return:screened results
        """
        try:
            body = {"query": query_items, "offset": offset, "limit": limit}
            self.response = api.post(urls.screener, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def search(self, query):
        """
        returns search results for the specific search query
        :param query:string
        :return:search results
        """
        try:
            body = {"query": query}
            self.response = api.post(urls.search, self.headers, body)
            content = check_response(json.loads(self.response.content))
            return content
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

    def status(self):
        """
        returns the status of the API
        :return:API status
        """
        try:
            self.response = api.get(urls.api_status, self.headers)
            return json.loads(self.response.content)
        except requests.exceptions.Timeout:
            print("Timeout Error")
        except requests.exceptions.TooManyRedirects:
            print("Exceeded redirects:Bad URL, please try different URL")

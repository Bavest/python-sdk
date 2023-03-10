import unittest
from bavest.finance.models.v0.candle import candle
from bavest.finance.models.v0.etf.country import country
from bavest.finance.models.v0.etf.holding import holding
from bavest.finance.models.v0.etf.profile import profile
from bavest.finance.models.v0.etf.sector import sector
from bavest.finance.models.v0.forex import forex
from bavest.finance.models.v0.market import news
from bavest.finance.models.v0.portfolio.allocation import allocation
from bavest.finance.models.v0.portfolio.chart import chart
from bavest.finance.models.v0.portfolio.metric import metric
from bavest.finance.models.v0.portfolio.price import price
from bavest.finance.models.v0.portfolio.region import region
from bavest.finance.models.v0.portfolio.sector import sector as portfoliosector
from bavest.finance.models.v0.portfolio.stats import stats
from bavest.finance.models.v0.quote import quote
from bavest.finance.models.v0.screener import screener
from bavest.finance.models.v0.search import search
from bavest.finance.models.v0.sentiment.sentiment import sentiment
from bavest.finance.models.v0.sentiment.social_sentiment import social_sentiment
from bavest.finance.models.v0.status import status
from bavest.finance.models.v0.stock.analyst_estimates import analyst_estimates
from bavest.finance.models.v0.stock.calendar.earnings import earnings
from bavest.finance.models.v0.stock.calendar.economics import economics
from bavest.finance.models.v0.stock.calendar.ipo import ipo
from bavest.finance.models.v0.stock.candle import candle as stockcandle
from bavest.finance.models.v0.stock.dividend import dividend
from bavest.finance.models.v0.stock.earnings_transcript import earnings_transcript
from bavest.finance.models.v0.stock.esg import esg
from bavest.finance.models.v0.stock.financials import financials
from bavest.finance.models.v0.stock.fundamentals import fundamentals
from bavest.finance.models.v0.stock.ipo.prospectus import prospectus
from bavest.finance.models.v0.stock.metric import metric as stockmetric
from bavest.finance.models.v0.stock.news import news as stocknews
from bavest.finance.models.v0.stock.peers import peers as stockpeers
from bavest.finance.models.v0.stock.profile import profile as stockprofile
from bavest.finance.models.v0.stock.split import split
from bavest.finance.models.v0.widget.stock.peers import peers

import data


def candles():
    model_obj = candle.fromjson(data.candle_data)
    assert model_obj.s == "ok"


def etf_country():
    model_obj = country.fromjson(data.etf_country_data)
    assert len(model_obj.countryExposure) > 0


def etf_holding():
    model_obj = holding.fromjson(data.etf_holding_data)
    assert len(model_obj.holdings) > 0


def etf_profile():
    model_obj = profile.fromjson(data.etf_profile_data)
    assert model_obj.profile.aum == 0


def etf_sector():
    model_obj = sector.fromjson(data.etf_sector_data)
    assert len(model_obj.sectorExposure) > 0


def forex_test():
    model_obj = forex.fromjson(data.forex_data)
    assert model_obj.info.rate == 86.104


def news_test():
    model_obj = news.fromjson(data.news_data)
    assert model_obj.news[0].category == "top news"


def portfolio_sector():
    model_obj = portfoliosector.fromjson(data.portfolio_sector_data)
    assert model_obj.portfolioSectors[0].percentage == 39.3792


def portfolio_allocation():
    model_obj = allocation.fromjson(data.portfolio_allocation_data)
    assert len(model_obj.portfolio_allocations) > 0


def portfolio_chart():
    model_obj = chart.fromjson(data.portfolio_chart_data)
    assert model_obj.portfolio_items[0].amount == 5


def portfolio_metric():
    model_obj = metric.fromjson(data.portfolio_metric_data)
    assert model_obj.fiveDayPriceReturnDaily == 4.93


def portfolio_price():
    model_obj = price.fromjson(data.portfolio_price_data)
    assert model_obj.c == 180.02


def portfolio_region():
    model_obj = region.fromjson(data.portfolio_region_data)
    assert model_obj.portfolio_regions[0].region == "DE"


def portfolio_stats():
    model_obj = stats.fromjson(data.portfolio_stats_data)
    assert model_obj.riskReturnRatio.ABEA_DE == -0.0311456871


def quote_test():
    model_obj = quote.fromjson(data.quote_data)
    assert model_obj.historical_price.fifty_days == 230.01


def screener_test():
    model_obj = screener.fromjson(data.screener_data)
    assert model_obj.results[0].symbol == "CBDL"


def search_test():
    model_obj = search.fromjson(data.search_data)
    assert model_obj.results[0].companyName == "Apple Inc."


def sentiment_test():
    model_obj = sentiment.fromjson(data.sentiment_data)
    assert model_obj.positive == 0.62


def social_sentiment_test():
    model_obj = social_sentiment.fromjson(data.social_sentiment_data)
    assert model_obj.stockwits[0].impressions == 1000
    assert model_obj.twitter[0].impressions == 1200


def status_test():
    model_obj = status.fromjson(data.status_data)
    assert model_obj.statusCode == 200


def stock_estimates_test():
    model_obj = analyst_estimates.fromjson(data.stock_estimates_data)
    assert len(model_obj.estimates) > 0


def stock_calendar_earnings_test():
    model_obj = earnings.fromjson(data.stock_calendar_earnings_data)
    assert model_obj.earningsConfirmed[0].exchange == "NYSE"


def stock_calendar_economics_test():
    model_obj = economics.fromjson(data.stock_calendar_economics_data)
    assert model_obj.economicCalendar[0].country == "JP"


def stock_calendar_ipo_test():
    model_obj = ipo.fromjson(data.stock_calendar_ipo_data)
    assert model_obj.ipoCalendar[0].numberOfShares == 3000000


def stock_candle_test():
    model_obj = stockcandle.fromjson(data.stock_candle_data)
    assert len(model_obj.c) > 0


def stock_dividend_test():
    model_obj = dividend.fromjson(data.stock_dividend_data)
    assert model_obj.dividends[0].adjustedAmount == 0.23


def stock_transcript_test():
    model_obj = earnings_transcript.fromjson(data.stock_transcript_data)
    assert model_obj.transcript[0].year == 2022


def stock_esg_test():
    model_obj = esg.fromjson(data.stock_esg_data)
    assert model_obj.data[0].formType == "10-K"
    assert model_obj.environmentScore == 62.77


def stock_financials_test():
    model_obj = financials.fromjson(data.stock_financial_data)
    assert model_obj.financials[0].symbol == "VOW3.DE"
    assert model_obj.financials[1].inventory == 1334


def stock_fundamentals_test():
    model_obj = fundamentals.fromjson(data.stock_fundamentals_data)
    assert model_obj.metrics[0].multiples.equityReturn == 1.7543
    assert model_obj.metrics[1].stability.debtToEquityRatio == 4.5635


def stock_ipo_prospectus_test():
    model_obj = prospectus.fromjson(data.stock_prospectus_data)
    assert model_obj.prospectus[0].discountsAndCommissionsTotal == 3600000


def stock_metric_test():
    model_obj = stockmetric.fromjson(data.stock_metric_data)
    assert model_obj.epsdilutedGrowth == 0.26


def stock_news_test():
    model_obj = stocknews.fromjson(data.stock_news_data)
    assert model_obj.news[0].title == "Spotify CEO renews attack on Apple after Musk's salvo"


def stock_peers_test():
    model_obj = stockpeers.fromjson(data.stock_peers_data)
    assert len(model_obj.peers) > 0


def stock_profile_test():
    model_obj = stockprofile.fromjson(data.stock_profile_data)
    assert model_obj.companyName == "Microsoft"


def stock_profile_split_test():
    model_obj = split.fromjson(data.stock_split_data)
    assert model_obj.splits[0].symbol == "NEW"


def widget_stock_peers_test():
    model_obj = peers.fromjson(data.widget_stock_peers_data)
    assert model_obj.stock_peers[0].name == "Apple"


if __name__ == '__main__':
    candles()
    etf_country()
    etf_holding()
    etf_profile()
    etf_sector()
    forex_test()
    news_test()
    portfolio_sector()
    portfolio_allocation()
    portfolio_chart()
    portfolio_metric()
    portfolio_price()
    portfolio_region()
    portfolio_stats()
    quote_test()
    screener_test()
    search_test()
    sentiment_test()
    social_sentiment_test()
    status_test()
    stock_estimates_test()
    stock_calendar_earnings_test()
    stock_calendar_economics_test()
    stock_calendar_ipo_test()
    stock_candle_test()
    stock_dividend_test()
    stock_transcript_test()
    stock_esg_test()
    stock_financials_test()
    stock_fundamentals_test()
    stock_ipo_prospectus_test()
    stock_metric_test()
    stock_news_test()
    stock_peers_test()
    stock_profile_test()
    stock_profile_split_test()
    widget_stock_peers_test()

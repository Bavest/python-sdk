<p align="center">
  <img wsymbolth="300" alt="posthoglogo" src="https://i.imgur.com/z4ZPmGN.png">
</p>

# Bavest Finance SDK

**The Bavest Finance SDK is an open-source library to create finance products in weeks. Bavest offers:**

* Financial api with 99.999% uptime
* Easy to integrate and use
* Free for open-source projects

## Get started for free

### Personal API key

First, you need to create an account on [Bavest](https://www.dashboard.bavest.com).
After registration, you will find your api key in the dashboard.

### Open-Source projects

If you are working on an open-source project, you can use the SDK for free.
Just send us an email to `support@bavest.co` with the following information:

* Your GitHub username
* The name of your project
* The link to your project on GitHub
* A description of your project

### Install the package

First install the python package:

 ```python 
pip install bavest 
 ```

### Usage

1. Now, use the package in your project:

 ```python 
from bavest import BavestRESTClient
 ```

2. Create a finance `client`:

 ```python
from bavest import BavestRESTClient

client = BavestRestClient(apiKey)
  ```

3. Now you can use it to get data from the api:

```python
from bavest import BavestRESTClient

client = BavestRestClient(apiKey)
quote = client.quote("AAPL")
```

### Examples

```python
to = datetime.now()
frm = to + dateutil.relativedelta.relativedelta(days=-20)
resolution = Resolution.MONTHLY
candles = client.candles(symbol, frm, to, resolution)
news = client.news(symbol)
search = client.search(symbol)
forex = client.forex(frm, to)

# ETF
etfSector = client.etf.sector(symbol)
etfCountry = client.etf.country(symbol)
etfHoldings = client.etf.holdings(symbol)
etfProfile = client.etf.profile(symbol)

# Portfolio Items
transactionItem = TransactionItem("MSFT", 2, frm).get()
transactionList = [transactionItem]

portfolioRegion = client.portfolio.region(TransactionList)
portfolioStats = client.portfolio.stats(frm, to, resolution, transactionList, "USD")
portfolioChart = client.portfolio.chart(frm, to, resolution, transactionList)
 ```

<p align="center">
  <img  src="https://www.bavest.co/images/api-home.png">
</p>

# Bavest Python SDK

<img wsymbolth=300 src="https://img.shields.io/badge/license-MIT-brightgreen" > <img wsymbolth=300 src="https://img.shields.io/badge/tests-passing-brightgreen" > <img src="https://img.shields.io/github/issues/Bavest/python-sdk"> <img src="https://img.shields.io/pypi/pyversions/bavest"> <img src="https://img.shields.io/pypi/wheel/bavest">

**The Bavest Finance SDK is an open-source library to create finance products in weeks. Bavest offers:**

* Financial api with 99.95% uptime
* Easy to integrate and use
* Free for open-source projects

## Get API key

First, you need to create a [Bavest](https://www.dashboard.bavest.com) account.
After registration, you will find your api key in the dashboard.

### Free API key for Open-Source projects

First, use the [TypeForm](https://e0nemwrtihz.typeform.com/to/xT8KfS0I) to provide all required information.
After, you will receive an API key via E-Mail.

### Template
````python
import os
import dateutil
from bavest import BavestRESTClient, Resolution
from datetime import datetime
import dateutil.relativedelta as relativedelta

BAVEST_API_KEY = os.environ.get('BAVEST_API_KEY')
client = BavestRESTClient(BAVEST_API_KEY)

if __name__ == "__main__":
    to = datetime.now()
    frm = to + dateutil.relativedelta.relativedelta(days=-2)
    to = to + dateutil.relativedelta.relativedelta(days=-1)
    resolution = Resolution.DAILY
    candles = client.candles("AAPL", frm, to, resolution)
````

### Install the package

First install the python package using [pip](https://pypi.org/project/bavest):

 ```python 
pip install bavest 
 ```
 
 
### Documentation
See [here](https://docs.bavest.co/) for more information. 

### Usage

1. Now, use the package in your project:

 ```python 
from bavest import BavestRESTClient
 ```

2. Create a finance `client`:

 ```python
client = BavestRestClient(apiKey)
  ```

3. Now you can use it to get data from the api:

```python
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

portfolioRegion = client.portfolio.region(transactionList)
portfolioStats = client.portfolio.stats(frm, to, resolution, transactionList, "USD")
portfolioChart = client.portfolio.chart(frm, to, resolution, transactionList)
 ```
 
# :octocat: Credits
1. William Todt <william.todt@bavest.co> - Maintainer
2. Hisham Parveez <hisham.parveez@bavest.co> - Maintainer

# Contact
Please open a Github issue or send us an email at `support@bavest.co`.
 
 

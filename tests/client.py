import os

from bavest import BavestRESTClient, TransactionItem
from datetime import datetime
import dateutil.relativedelta

to = datetime.now()
frm = to + dateutil.relativedelta.relativedelta(days=-20)
key = os.environ.get('x_api_key', '/home/')

client = BavestRESTClient(key)
esg = client.stock.esg("AAPL")
d1 = TransactionItem("MSFT", 2, frm).get()
lst = [d1]
client.portfolio.region(lst)
client.etf.profile()


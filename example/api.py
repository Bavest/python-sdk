import os
import dateutil
from bavest import BavestRESTClient, Resolution
from datetime import datetime
import dateutil.relativedelta as relativedelta

BAVEST_API_KEY = os.environ.get("BAVEST_API_KEY")
client = BavestRESTClient(BAVEST_API_KEY)

if __name__ == "__main__":
    to = datetime.now()
    frm = to + dateutil.relativedelta.relativedelta(days=-2)
    to = to + dateutil.relativedelta.relativedelta(days=-1)
    resolution = Resolution.DAILY
    candles = client.candles("AAPL", frm, to, resolution)

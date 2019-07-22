import pandas_datareader.data as pdr
import datetime

end = datetime.date.today()

start = end - datetime.timedelta(days=30)

data = pdr.DataReader("AAPL", 'yahoo', start, end)
print(data)


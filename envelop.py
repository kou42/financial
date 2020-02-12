import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mpl_finance
from datetime import datetime

google = pdr.DataReader('GOOGL', 'yahoo', '2015/1/1', '2016/1/1')

g=pd.DataFrame(google,columns=['Open','High','Low','Close'],index=google.index)
g_ = g.copy()
g_.index = mdates.date2num(g_.index)
data = g_.reset_index().values

g25=google["Close"].fillna(method='ffill').rolling(window=25,center=False).mean()
upperband=g25*1.05
lowerband=g25*0.95

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

ax.plot(upperband,label='upperband',color='g')
ax.plot(lowerband,label='lowerband',color='g')
ax.plot(g25,label='twenty-five average')
ax.legend(loc='best')

mpl_finance.candlestick_ohlc(ax,data,width=0.5, alpha=0.5, colorup='r', colordown='b')

plt.show()

# financial

import talib as ta
import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mpl_finance
from datetime import datetime

google = pdr.DataReader('GOOGL', 'yahoo', '2015/1/1', '2016/1/1')
g=pd.DataFrame(google,columns=['Open','High','Low','Close'],index=google.index)

g.index=mdates.date2num(g.index)
data=g.reset_index().values

close=google['Close']
upperband,middleband,lowerband=ta.BBANDS(close,timeperiod=20,nbdevup=2,nbdevdn=2,matype=0)
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(1,1,1)
mpl_finance.candlestick_ohlc(ax,data,width=1, alpha=0.5, colorup='r', colordown='b')
ax.plot(middleband,label='middleband',color='g')
ax.plot(upperband,label='upperband',color='g')
ax.plot(lowerband,label='lowerband',color='g')
ax.set_title('Bollinger Band')
ax.legend()

plt.show()

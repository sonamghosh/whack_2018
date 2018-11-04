import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt 

import plotly
plotly.tools.set_credentials_file(username='sonamghosh', api_key='PacsVoWuRF2Fe0hSFcwz')

plotly.tools.set_config_file(world_readable=True, sharing='public')
from grab_data import get_quote_data

import plotly.plotly as py 
import plotly.graph_objs as go 
import datetime

from pandas_datareader import data

from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
import seaborn as sns 
sns.set(style="darkgrid")



def plot_and_save_plot(ticker, source):
    if source == 'yahoo':
        d = get_quote_data(ticker, '1y', '1d')
        # Remove timestamp and keep only dates
        d.index = d.index.normalize()
        print(d.columns)
        d2 = d[['CLOSE']]
        d2 = d2.reset_index()
        #print(d2)
        g = sns.relplot(x='Datetime', y='CLOSE', kind='line', data=d2)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Stock price of ' + ticker + ' from 11-06-2017 to 11-02-2018')
        plt.show()




if __name__ == "__main__":
    tickers = ['TSLA', 'MSFT', 'AAPL', 'GOOG', 'NFLX', 'TRIP', 'AMZN']
    plot_and_save_plot('TSLA', 'yahoo')


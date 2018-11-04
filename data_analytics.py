
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
        #print(d2)
        #fig, ax = plt.subplots()
        #g = sns.relplot(x='Datetime', y='CLOSE', kind='line', data=d2)
        wide_df = d[['CLOSE', 'LOW', 'HIGH']]
        #wide_df = wide_df.reset_index()
        ax = sns.lineplot(data=wide_df)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Stock price of ' + ticker + ' from 11-06-2017 to 11-02-2018')
        plt.savefig(ticker+'_graph.png')
        plt.show()




if __name__ == "__main__":
    tickers = ['TSLA', 'MSFT', 'AAPL', 'GOOG', 'NFLX', 'TRIP', 'AMZN', 'FTQGX']
    plot_and_save_plot('FTQGX', 'yahoo')
    #fmri = sns.load_dataset("fmri")
    #print(fmri)
    #ax = sns.lineplot(x="timepoint", y="signal", data=fmri)
    #plt.show()


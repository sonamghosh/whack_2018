
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

import csv
from datetime import datetime
import requests
import sys

import pyEX as p

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

def get_analyst_rec(ticker):
    get_date = lambda : datetime.utcnow().strftime('%d-%m-%Y')
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'
    url = lhs_url + ticker + rhs_url
    r = requests.get(url)
    if not r.ok:
        return -1

    result = r.json()['quoteSummary']['result'][0]
    yahoo_industry_analyst_rec = result['financialData']['recommendationMean']['fmt']

    return float(yahoo_industry_analyst_rec)

def get_sector_perf(sector=None):
    if sector == None:
        d = pd.DataFrame(p.sectorPerformanceDF())
        return d
    d = pd.DataFrame(p.sectorPerformanceDF())
    lst_of_industries = ['Consumer Discretionary', 'Financials', 'Industrials', 'Materials',
                         'Energy', 'Consumer Staples', 'Utilities', 'Health Care',
                         'Real Estate', 'Communication Services', 'Technology']
    idx = d.index[d['name'] == sector].tolist()
    idx = idx[0]
    perf = d['performance'][idx]

    return perf

def eps_stats(ticker):
    get_date = lambda : datetime.utcnow().strftime('%d-%m-%Y')
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
              'modules=upgradeDowngradeHistory,recommendationTrend,' \
              'financialData,earningsHistory,earningsTrend,industryTrend&' \
              'corsDomain=finance.yahoo.com'
    url = lhs_url + ticker + rhs_url
    r = requests.get(url)
    if not r.ok:
        return -1
    result = r.json()['quoteSummary']['result'][0]
    eps_surprise_start = result['earningsHistory']['history'][0]['surprisePercent']['raw']
    eps_surprise_end = result['earningsHistory']['history'][3]['surprisePercent']['raw']
    print(eps_surprise_start)
    print(eps_surprise_end)
    print('percent change: ', (eps_surprise_end - eps_surprise_start) / eps_surprise_end ) 
    #print(len(eps_surprise_start))
    perc_change = (eps_surprise_end - eps_surprise_start) / eps_surprise_end 
    return perc_change, eps_surprise_end

def metric(analy_rec, eps_qtr_change, eps_surprise_end):
    if 1 <= analy_rec <= 2 and eps_qtr_change >= 0.25:
        output = 'Strong Buy'
    elif 1 <= analy_rec <= 2 and -0.75 <= eps_qtr_change < 0.25:
        output = 'Buy'
    elif 1 <= analy_rec <= 2 and -1 <= eps_qtr_change < -0.75:
        output = 'Hold'
    elif 2 < analy_rec <= 3 and eps_qtr_change >= 0.75:
        output = 'Strong Buy'
    elif 2 < analy_rec <= 3 and 0.5 <= eps_qtr_change < 0.75:
        output = 'Buy'
    elif 2 < analy_rec <= 3 and 0 <= eps_qtr_change < 0.5:
        output = 'Hold'
    elif 2 < analy_rec <=3 and eps_qtr_change < 0:
        output = 'Underperforming'
    elif 3 < analy_rec <= 4 and eps_qtr_change >= 0.75:
        output = 'Buy'
    elif 3 < analy_rec <= 4 and 0.25 <= eps_qtr_change < 0.75:
        output = 'Underperforming'
    elif 3 < analy_rec <= 4 and eps_qtr_change < 0.25:
        output = 'Sell'
    elif 4 < analy_rec <= 5 and eps_qtr_change >= 0.75:
        output = 'Hold'
    elif 4 < analy_rec <= 5 and 0.5 <= eps_qtr_change < 0.75:
        output = 'Underperforming'
    elif 4 < analy_rec <= 5 and eps_qtr_change < 0.5:
        output = 'sell'
    else:
        print('Not Available')

    if round(analy_rec) == 1:
        fin_outcome = 'Strong Buy'
    elif round(analy_rec) == 2:
        fin_outcome = 'Buy'
    elif round(analy_rec) == 3:
        fin_outcome = 'Hold'
    elif round(analy_rec) == 4:
        fin_outcome = 'Underperforming'
    elif round(analy_rec) == 5:
        fin_outcome = 'Sell'
    else:
        print('Invalid')

    dict_vals = {'FAR': analy_rec,
            'EPSSurpriseChange': eps_qtr_change,
            'EPSSurpriseCurrent': eps_surprise_end,
            'FARM': fin_outcome,
            'PMO': output
            }

    return dict_vals
    





def trade_volume_plot(ticker, source):
    if source == 'yahoo':
        d = get_quote_data(ticker, '1y', '1d')
        d.index = d.index.normalize()
        d = d[['VOLUME']]

        print(d)
        #volume_by_assets = d.sum()
        #print(volume_by_assets)
        #highestVolume = d.loc[d['VOLUME'].idxmax()]
        #print(highestVolume['VOLUME'])
        #print(highestVolume['VOLUME'] / volume_by_assets)





if __name__ == "__main__":
    tickers = ['TSLA', 'MSFT', 'AAPL', 'GOOG', 'NFLX', 'TRIP', 'AMZN', 'FTQGX']
    """
    for ticker in tickers:
        plot_and_save_plot(ticker, 'yahoo')
    """
    trade_volume_plot('aapl', 'yahoo')

    #a, b= eps_stats('AAPL')
    #c = get_analyst_rec('AAPL')
    #print(type(a), type(b), type(c))
    #d = metric(c, a, b)
    #print(d)
    #plot_and_save_plot('FTQGX', 'yahoo')
    #fmri = sns.load_dataset("fmri")
    #print(fmri)
    #ax = sns.lineplot(x="timepoint", y="signal", data=fmri)
    #plt.show()


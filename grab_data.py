import quandl

# Trying to grab data from Quandl API

#data = quandl.get('NSE/OIL')
#data = quandl.get('NASDAQ/AAPL')
"""
quandl.ApiConfig.api_key = 'LUVbz_yxakRtBTbaX4sn'
data = quandl.get_table('NDX', ticker='AAPL')
print(data)
"""
#from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

import requests
from datetime import datetime
import pandas as pd


def get_price_data(query):
    r = requests.get(
        "https://finance.google.com/finance/getprices", params=query)
    lines = r.text.splitlines()
    data = []
    index = []
    basetime = 0
    for price in lines:
        cols = price.split(",")
        if cols[0][0] == 'a':
            basetime = int(cols[0][1:])
            index.append(datetime.fromtimestamp(basetime))
            data.append([float(cols[4]), float(cols[2]), float(
                cols[3]), float(cols[1]), int(cols[5])])
        elif cols[0][0].isdigit():
            date = basetime + (int(cols[0]) * int(query['i']))
            index.append(datetime.fromtimestamp(date))
            data.append([float(cols[4]), float(cols[2]), float(
                cols[3]), float(cols[1]), int(cols[5])])
    return pd.DataFrame(data, index=index, columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def get_closing_data(queries, period):
    closing_data = []
    for query in queries:
        query['i'] = 86400
        query['p'] = period
        r = requests.get(
            "https://finance.google.com/finance/getprices", params=query)
        lines = r.text.splitlines()
        data = []
        index = []
        basetime = 0
        for price in lines:
            cols = price.split(",")
            if cols[0][0] == 'a':
                basetime = int(cols[0][1:])
                date = basetime
                data.append(float(cols[1]))
                index.append(datetime.fromtimestamp(date).date())
            elif cols[0][0].isdigit():
                date = basetime + (int(cols[0]) * int(query['i']))
                data.append(float(cols[1]))
                index.append(datetime.fromtimestamp(date).date())
        s = pd.Series(data, index=index, name=query['q'])
        closing_data.append(s[~s.index.duplicated(keep='last')])
    return pd.concat(closing_data, axis=1)


def get_open_close_data(queries, period):
    open_close_data = pd.DataFrame()
    for query in queries:
        query['i'] = 86400
        query['p'] = period
        r = requests.get(
            "https://finance.google.com/finance/getprices", params=query)
        lines = r.text.splitlines()
        data = []
        index = []
        basetime = 0
        for price in lines:
            cols = price.split(",")
            if cols[0][0] == 'a':
                basetime = int(cols[0][1:])
                date = basetime
                data.append([float(cols[4]), float(cols[1])])
                index.append(datetime.fromtimestamp(date).date())
            elif cols[0][0].isdigit():
                date = basetime + (int(cols[0]) * int(query['i']))
                data.append([float(cols[4]), float(cols[1])])
                index.append(datetime.fromtimestamp(date).date())
        df = pd.DataFrame(data, index=index, columns=[
                          query['q'] + '_Open', query['q'] + '_Close'])
        open_close_data = pd.concat(
            [open_close_data, df[~df.index.duplicated(keep='last')]], axis=1)
    return open_close_data


def get_prices_data(queries, period):
    prices_data = pd.DataFrame()
    for query in queries:
        query['i'] = 86400
        query['p'] = period
        r = requests.get(
            "https://finance.google.com/finance/getprices", params=query)
        lines = r.text.splitlines()
        data = []
        index = []
        basetime = 0
        for price in lines:
            cols = price.split(",")
            if cols[0][0] == 'a':
                basetime = int(cols[0][1:])
                date = basetime
                data.append([float(cols[4]), float(cols[2]), float(
                    cols[3]), float(cols[1]), int(cols[5])])
                index.append(datetime.fromtimestamp(date).date())
            elif cols[0][0].isdigit():
                date = basetime + (int(cols[0]) * int(query['i']))
                data.append([float(cols[4]), float(cols[2]), float(
                    cols[3]), float(cols[1]), int(cols[5])])
                index.append(datetime.fromtimestamp(date).date())
        df = pd.DataFrame(data, index=index, columns=[
                          query['q'] + '_Open', query['q'] + '_High', query['q'] + '_Low', query['q'] + '_Close', query['q'] + '_Volume'])
        prices_data = pd.concat(
            [prices_data, df[~df.index.duplicated(keep='last')]], axis=1)
    return prices_data


def get_prices_time_data(queries, period, interval):
    prices_time_data = pd.DataFrame()
    for query in queries:
        query['i'] = interval
        query['p'] = period
        r = requests.get(
            "https://finance.google.com/finance/getprices", params=query)
        lines = r.text.splitlines()
        data = []
        index = []
        basetime = 0
        for price in lines:
            cols = price.split(",")
            if cols[0][0] == 'a':
                basetime = int(cols[0][1:])
                date = basetime
                data.append([float(cols[4]), float(cols[2]), float(
                    cols[3]), float(cols[1]), int(cols[5])])
                index.append(datetime.fromtimestamp(date))
            elif cols[0][0].isdigit():
                date = basetime + (int(cols[0]) * int(query['i']))
                data.append([float(cols[4]), float(cols[2]), float(
                    cols[3]), float(cols[1]), int(cols[5])])
                index.append(datetime.fromtimestamp(date))
        df = pd.DataFrame(data, index=index, columns=[
                          query['q'] + '_Open', query['q'] + '_High', query['q'] + '_Low', query['q'] + '_Close', query['q'] + '_Volume'])
        prices_time_data = pd.concat(
            [prices_time_data, df[~df.index.duplicated(keep='last')]], axis=1)
    return prices_time_data

"""
params = {
    'q': ".DJI",  # Stock symbol (ex: "AAPL")
    'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
    # Stock exchange symbol on which stock is traded (ex: "NASD")
    'x': "INDEXDJX",
    'p': "1Y"  # Period (Ex: "1Y" = 1 year)
}
df = get_price_data(params)
print(df)
"""

#from pandas_datareader import data
#import matplotlib.pyplot as plt
#import pandas as pd

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
#tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
#start_date = '2016-07-26'
#end_date = '2016-07-26'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
#panel_data = data.DataReader('AAPL', 'yahoo', start_date, end_date)
#print(panel_data)

"""
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='4TK1KOUKLTB2RUG3', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='AAPL',interval='1min', outputsize='compact')
print(data.head())
data, meta_data = ts.get_daily_adjusted(symbol='AAPL', outputsize='full')
print(data.head())
"""

import requests
import pandas as pd
import arrow
import datetime

def get_quote_data(symbol='SBIN.NS', data_range='1d', data_interval='1m'):
    res = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={data_range}&interval={data_interval}'.format(**locals()))
    data = res.json()
    body = data['chart']['result'][0]    
    dt = datetime.datetime
    dt = pd.Series(map(lambda x: arrow.get(x).datetime.replace(tzinfo=None), body['timestamp']), name='Datetime')
    df = pd.DataFrame(body['indicators']['quote'][0], index=dt)
    dg = pd.DataFrame(body['timestamp'])    
    df = df.loc[:, ('open', 'high', 'low', 'close', 'volume')]
    df.dropna(inplace=True)     #removing NaN rows
    df.columns = ['OPEN', 'HIGH','LOW','CLOSE','VOLUME']    #Renaming columns in pandas
    
    return df

data = get_quote_data('AAPL', '1y', '1m')
print(data)
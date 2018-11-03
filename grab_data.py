import requests
import pandas as pd
import arrow
import datetime
import os
import glob

# This script fetches up to date datasets

def get_quote_data(symbol='SBIN.NS', data_range='1d', data_interval='1m'):
    """
    Def:
    Grabs stock data of a particular ticker symbol within a date range and date interval

    Params:
    symbol - Which stock
    date_range - How far back starting from latest closing time
    date_interval - rate at which stock data is aggregated 

    Constraints:
    1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo - possible values for date_interval
    1m date_interval has max of date_range = 1wo
    5m, 15m date_interval has max date_range = 1mo

    Returns:
    Pandas dataframe containing Opening Price High Price Low Price Closing Price and Volume
    with the time stamp givne as YYYY-MM-DD HH:MM:SS

    """

    res = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={data_range}&interval={data_interval}'.format(**locals()))
    print(res.raise_for_status())  # error checking
    data = res.json()
    body = data['chart']['result'][0]    
    print(body['meta']['validRanges'])
    dt = datetime.datetime
    dt = pd.Series(map(lambda x: arrow.get(x).datetime.replace(tzinfo=None), body['timestamp']), name='Datetime')
    df = pd.DataFrame(body['indicators']['quote'][0], index=dt)
    dg = pd.DataFrame(body['timestamp'])    
    df = df.loc[:, ('open', 'high', 'low', 'close', 'volume')]
    df.dropna(inplace=True)     #removing NaN rows
    df.columns = ['OPEN', 'HIGH','LOW','CLOSE','VOLUME']    #Renaming columns in pandas
    
    return df

def get_close_price(dataframe):
    # Grabs only the closing price column of dataframe
    df = dataframe[['CLOSE']]

    return df

def grab_tickers(filename='stock_name.txt'):
    # Parses all the stock ticker names and puts it into a list
    # Make sure filename is accurate and has correct path

    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    return content


def save_csv(dataset, symbol):
    directory = './data/sub_data'
    if symbol == '^NDX':
        symbol = 'NDX'
    # Create sub directory to save individual csvs
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Rename CLOSE name to Ticker name
    dataset = dataset.rename(columns={'CLOSE': symbol})
    #print(dataset)
    # File name in format of ticker + date range .csv
    filename = symbol + '_' + dataset.index[0].date().strftime('%Y_%m_%d') + '_to_' + dataset.index[-1].date().strftime('%Y_%m_%d') +'.csv'
    dataset.to_csv(directory + '/' + filename)



def grab_from_iex(symbol, start, end):
    # Create range of dates of only week days (holidays not supported)
    dates = pd.date_range(start=start, end=end, freq='B')
    # Convert to strings
    t = [i.strftime('%Y%m%d') for i in dates]
    # empty list to put dataframes in
    dfs = []
    # Make HTTPS request
    for i in t:
        print(i)
        res = requests.get('https://api.iextrading.com/1.0/stock/'+symbol+'/chart/date/'+i)
        req_data = res.json()
        # Error Checker for nulls
        if req_data == []:
            raise ValueError('The following stock has no data on IEX: ', symbol)
        df = pd.DataFrame(req_data)
        df = df[['close']]
        df = df.rename(columns={'close':symbol.upper()})
        #print(df.shape)
        dfs.append(df)
    #print(dfs)
    # Concat into one dataframe
    tot_df = pd.concat(dfs, axis=0)
    print(tot_df)

    directory = './data/sub_data'





def create_dataset():
    print('Hello World')
    path = './data/sub_data'
    all_files = glob.glob(path + "/*.csv")
    dframe = pd.DataFrame()
    lst = []
    for file in all_files:
        df = pd.read_csv(file, index_col=None, header=0)
        lst.append(df)
    #dframe = pd.merge(lst[0], lst[1])
    dframe = pd.concat(lst, join='inner',axis=1).drop(['Datetime'], axis=1)
    dframe.set_index('AAL', inplace=True)
    print(dframe)
    path_2 = './data/'
    dframe.to_csv(path_2 + 'full_nasdaq100_dataset.csv')

# Testing
#data = get_quote_data('AAPL', '1d', '1m')
#print(data)
#d = get_close_price(data)
#print(d)
if __name__ == "__main__":
    grab_from_iex('aal', start='2018-10-02', end='2018-11-02')
    """
    data = get_quote_data('AAPL', '1y', '1h')
    print(type(data.index[0].date().strftime('%Y_%m_%d')))
    print(data.index[-1].date())
    data = get_close_price(data)
    print(data.shape)
    save_csv(data, 'AAPL')
    d2 = get_quote_data('AAL', '1y', '1h')
    d2 = get_close_price(d2)
    print(d2.shape)
    save_csv(d2, 'AAL')
    import numpy as np
    #print(pd.merge(data, d2))
    create_dataset()
    """

    """
    ticks = grab_tickers(filename='stock_name.txt')
    for tick in ticks:
        print('Starting this stock: ', tick)
        data = get_quote_data(tick, '1y', '1h')
        data = get_close_price(data)
        save_csv(data, tick)
    create_dataset()
    """
    
    #data = get_quote_data('^NDX', '1y', '30m')
    #print(data)
    #print(data.shape)

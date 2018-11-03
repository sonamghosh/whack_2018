import requests
import pandas as pd
import arrow
import datetime
import os

# This script fetches up to date datasets

def get_quote_data(symbol='SBIN.NS', data_range='1d', data_interval='1m'):
    """
    Def:
    Grabs stock data of a particular ticker symbol within a date range and date interval

    Params:
    symbol - Which stock
    date_range - How far back starting from latest closing time (1d, 1m, 1Y, 5Y are choices)
    date_interval - rate at which stock data is aggregated (1m, 15m, 60m are the choices)

    Returns:
    Pandas dataframe containing Opening Price High Price Low Price Closing Price and Volume
    with the time stamp givne as YYYY-MM-DD HH:MM:SS
    """

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
    # Create sub directory to save individual csvs
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Rename CLOSE name to Ticker name
    dataset = dataset.rename(columns={'CLOSE': symbol})
    print(dataset)
    # File name in format of ticker + date range .csv
    filename = symbol + '_' + dataset.index[0].date().strftime('%Y_%m_%d') + '_to_' + dataset.index[-1].date().strftime('%Y_%m_%d') +'.csv'
    dataset.to_csv(directory + '/' + filename)



# Testing
#data = get_quote_data('AAPL', '1d', '1m')
#print(data)
#d = get_close_price(data)
#print(d)
if __name__ == "__main__":
    data = get_quote_data('AAPL', '1Y', '1m')
    print(type(data.index[0].date().strftime('%Y_%m_%d')))
    print(data.index[-1].date())
    data = get_close_price(data)
    save_csv(data, 'AAPL')

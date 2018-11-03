import plotly
plotly.tools.set_credentials_file(username='sonamghosh', api_key='PacsVoWuRF2Fe0hSFcwz')

plotly.tools.set_config_file(world_readable=True, sharing='public')


import plotly.plotly as py 
import plotly.graph_objs as go 
import numpy as np 
import pandas as pd 


#df = pd.read_csv('./data/iex_nasdaq100.csv')

def nice_plot(dataframe, symbol='AAPL'):
    dflist = dataframe[symbol].tolist()
    x = np.arange(0, len(dflist))
    y = np.array(dflist)

    trace0 = go.Scatter(x=x, y=y)
    data = [trace0]
    py.iplot(data, filename=symbol+'-stockplot', auto_open=True)


if __name__ == "__main__":
    df = pd.read_csv('./data/iex_nasdaq100_dataset.csv')
    nice_plot(df, symbol='AAPL')
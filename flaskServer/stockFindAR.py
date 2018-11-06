from flask import Flask, request
from flask_cors import CORS
import requests
import json
import data_analytics as da

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getStock", methods=['POST'])
def getStock():
    symbol = request.form['symbol']
    range = request.form['range']
    print("Symbol: " + symbol + " Range: " + range)
    res = requests.get('https://api.iextrading.com/1.0/stock/'+symbol+'/chart/'+range)
    print(res.json())
    req_data = res.json()
    # Error Checker for nulls
    if req_data == []:
        raise ValueError('The following stock has no data on IEX: ', symbol)
    req_data = json.dumps(req_data)
    return req_data

@app.route("/getAI", methods=['POST'])
def getAI():
    symbol = request.form['symbol']
    #range = request.form['range']
    print("Symbol: " + symbol)
    # Function calls
    a, b = da.eps_stats(symbol.upper())
    c = da.get_analyst_rec(symbol.upper())
    result = da.metric(c, b, a)  # returns dictionary
    result = json.dumps(result)

    return result

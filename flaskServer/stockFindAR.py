from flask import Flask, request
import requests
import json


app = Flask(__name__)

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

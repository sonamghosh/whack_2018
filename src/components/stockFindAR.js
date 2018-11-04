import React, { Component } from 'react';
import {Chart, Lines} from 'orama';

const data = [
  {date: new Date('2010-01-01'), value: 10},
  {date: new Date('2010-02-01'), value: 17},
  {date: new Date('2010-03-01'), value: 9},
  {date: new Date('2010-04-01'), value: 12},
  {date: new Date('2010-05-01'), value: 20},
]

class StockFindAR extends Component {
  // Constructor to set initial states
  constructor(props){
    super(props);
    this.state = {
      symbol: "",
      range: "",
    };
    this.handleChangeSymbol = this.handleChangeSymbol.bind(this);
    this.handleChangeRange = this.handleChangeRange.bind(this);
  };

  getStock = () => {
    fetch('https://localhost:5000/getStock', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/multipart-form',
      },
      body: JSON.stringify({
        symbol: this.state.symbol,
        range: this.state.range,
      })
    })
  }

  handleChangeSymbol(event){
    this.setState({symbol: event.target.value});
  }
  handleChangeRange(event){
    this.setState({range: event.target.value});
  }

  render() {
    return(
      <div className="stockFindAR">
        <h1>Your Discovered Stocks</h1>
        <div className="chart">
          <Chart>
            <Lines data={data} x="date" y="value" />
          </Chart>
          <form onSubmit={(e) => {this.getStock(); e.preventDefault();}}>
            <input type="text" name="symbol" placeholder="symbol" className="symbol" onChange={this.handleChangeSymbol}/>
            <input type="text" name="range" placeholder="range" className="range" onChange={this.handleChangeRange}/>
            <input type="submit" value="Get Info" className="submit" />
          </form>
        </div>
      </div>
    );
  }
}

export default StockFindAR;

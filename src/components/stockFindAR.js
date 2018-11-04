import React, { Component } from 'react';
import {Chart, Lines} from 'orama';

class StockFindAR extends Component {
  // Constructor to set initial states
  constructor(props){
    super(props);
    this.state = {
      symbol: "",
      range: "",
      data: [
        {date: 0, high: 0},
      ],
    };
    this.handleChangeSymbol = this.handleChangeSymbol.bind(this);
    this.handleChangeRange = this.handleChangeRange.bind(this);
  };

  getStock = () => {
    let symbol = this.state.symbol;
    let range = this.state.range;
    console.log(symbol + range)
    fetch('http://localhost:5000/getStock', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: '&symbol='+symbol+'&range='+range
    })
      .then(res => res.json())
      .then((resp) => {
        this.setState({data: resp});
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
        <div className="stockFindARContainer">
          <h1>Discover Stock Information</h1>
          <div className="chart">
            <Chart>
              <Lines data={this.state.data} x="date" y="high" />
            </Chart>
            <form onSubmit={(e) => {this.getStock(); e.preventDefault();}}>
              <input type="text" name="symbol" placeholder="Symbol" className="symbol" onChange={this.handleChangeSymbol}/>
              <select onChange={this.handleChangeRange} className="range">
                <option value="1d">One day</option>
                <option value="1m">One month</option>
                <option selected value="3m">Three months</option>
                <option value="6m">Six months</option>
                <option value="ytd">Year-to-date</option>
                <option value="1y">One year</option>
                <option value="2y">Two years</option>
                <option value="5y">Five years</option>
              </select>
              <input type="submit" value="Get Info" className="submitStock" />
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default StockFindAR;

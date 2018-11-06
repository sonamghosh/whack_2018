import React, { Component } from 'react';

class Prediction extends Component {
  render() {
    return(
      <div className="prediction">
        <div className="predictionContainer">
          <h1>Prediction (BETA)</h1>
          <h3>Use DA-RNN LSTM Model through Pytorch to predict stocks</h3>
          <h3>Demo: Apple Stocks</h3>
          <iframe width="70%" height="800" frameborder="0" scrolling="no" src="//plot.ly/~sonamghosh/2.embed"></iframe>
        </div>
      </div>
    );
  }
}

export default Prediction;

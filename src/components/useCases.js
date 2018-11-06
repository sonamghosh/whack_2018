import React, { Component } from 'react';

class UseCases extends Component {
  render() {
    return(
      <div className="useCases">
        <div className="useCasesContainer">
          <h1>Use Cases</h1>
          <h3>Phone:</h3>
            <p>Use your phone camera to scan around you. </p>
            <p>When an identified object has a stock behind it, a UI will appear.</p>
            <p>Interact with the UI to view past trades and even purchase a stock.</p>
            <p>More detailed data and actions can be achieved on the website after logging in.</p>
          <br/>
          <h3>Augmented Reality Glasses:</h3>
            <p>Look around and break the barrier between the physical object and the stocks behind it.</p>
            <p>Use your eye's gaze or your fingers to interact with the UI.</p>
          <br/>
          <h3>Virtual Reality Glasses:</h3>
            <p>Enter a premade realm littered with items.</p>
            <p>Approach an item and interact with the UI pop-up with your gaze.</p>
        </div>
      </div>
    );
  }
}

export default UseCases;

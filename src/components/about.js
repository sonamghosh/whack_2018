import React, { Component } from 'react';

class About extends Component {
  render() {
    return(
      <div className="about">
        <div className="aboutContainer">
          <h1>About Us</h1>
            <h2>We're a rapidly growing startup founded by 3 people at Hack Wellesley 2018.</h2>
            <h3>Sonam Ghosh</h3>
              <p>Machine Learning developer</p>
            <h3>Brian He</h3>
              <p>Augmented Reality developer</p>
            <h3>Halmon Lui</h3>
              <p>FullStack developer</p>
        </div>
      </div>
    );
  }
}

export default About;

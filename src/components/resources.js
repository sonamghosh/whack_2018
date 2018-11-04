import React, { Component } from 'react';

class Resources extends Component {
  render() {
    return(
      <div className="resources">
        <div className="resourcesContainer">
          <h1>Resources</h1>
          <h3>Technology we used to create this app</h3>
          <br/>
          <h4>Front End:</h4>
            <p>ReactJS</p>
            <p>React Native</p>
          <br/>
          <br/>
          <h4>Back End:</h4>
            <p>Python3</p>
            <p>Flask</p>
            <p>Viro React</p>
            <p>Orama</p>
            <p>PyTorch</p>
            <p>Google Cloud Platform</p>
          <br/>
          <br/>
          <h4>APIs:</h4>
            <p>IEX API</p>
            <p>WayFair API</p>
            <p>Algolia API</p>
            <p>Authorize.net API</p>

        </div>
      </div>
    );
  }
}

export default Resources;

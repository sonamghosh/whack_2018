import React, { Component } from 'react';

import musicBoi from '../images/musicBoiLogo2.png';

class Header extends Component {
  render() {
    return(
      <div className="header">
        <div className="headerContainer">
          <h1>Join Stock FindAR</h1>
          <h3>Only 54% of Americans own stocks.</h3>
          <h3>Let's increase that percentage by educating through everyday interactions.</h3>
        </div>
      </div>
    );
  }
}

export default Header;

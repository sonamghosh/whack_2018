import React, { Component } from 'react';

class Footer extends Component {
  render() {
    return(
      <div className="footer">
        <div className="footerContainer">
          <p>&copy; {new Date().getFullYear()} STOCK FINDAR. ALL RIGHTS RESERVED. </p>
        </div>
      </div>
    );
  }
}

export default Footer;

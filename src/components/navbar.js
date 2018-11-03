import React, { Component } from 'react';

import musicBoi from '../images/musicBoiLogo2.png';

class Navbar extends Component {
  mainTab = function() {
    this.props.mainTab(this.state.view);
    this.setState({view: 1});
  }

  render() {
    return(
      <div className="navbar">
        <a className="logo">
          <p>Stock FindAR</p>
        </a>
        <div>
          <form>
            <input
              type="text"
              placeholder="Search..."
              className="search"
            />
          </form>
        </div>
        <div className="navTab">
          <a onClick={this.props.changeStockFindAR} className="navLink">
            <p> Stock FindAR </p>
          </a>
        </div>
        <div className="navTab">
          <a onClick={this.props.changeUseCases} className="navLink">
            <p> Use Cases </p>
          </a>
        </div>
        <div className="navTab">
          <a onClick={this.props.changeResources} className="navLink">
            <p> Resources </p>
          </a>
        </div>
        <div className="navTab">
          <a onClick={this.props.changeAbout} className="navLink">
            <p> About </p>
          </a>
        </div>
        {
          !this.props.loggedOn &&
          <div className="loginContainer">
            <form>
              <input type="text" name="username" placeholder="username" className="username"/>
              <input type="password" name="password" placeholder="password" className="password"/>
              <input type="submit" value="Submit" className="submit"/>
            </form>
          </div>
        }
      </div>
    );
  }
}

export default Navbar;

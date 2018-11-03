import React, { Component } from 'react';
import AgAutocomplete from 'react-algoliasearch';
import musicBoi from '../images/musicBoiLogo2.png';

class Navbar extends Component {
  render() {
    return(
      <div className="navbar">
        <a className="logo" onClick={this.props.changeHome}>
          <p>Stock FindAR</p>
        </a>
        <div>
          <AgAutocomplete
            apiKey={"6dc685dc57968d5a67e816916887382c"}
            appId={"F7HFR1MH0G"}
            displayKey="name"
            indices={[{index: 'stocks'}]}
            inputId="input-search"
            placeholder="Search Stocks..."
            keyName="stock"
            options={{autoselectOnBlur: true, hint: true, debug: false, autoselect: true, tabAutocomplete: true}}
          />
      </div>
        {
          this.props.loggedOn &&
          <div className="navTab">
            <a onClick={this.props.changeStockFindAR} className="navLink">
              <p> Stock FindAR </p>
            </a>
          </div>
        }
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
        {
          this.props.loggedOn &&
          <form>
            <input type="submit" value="Submit" className="submit"/>
          </form>
        }
      </div>
    );
  }
}

export default Navbar;

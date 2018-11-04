import React, { Component } from 'react';
import AgAutocomplete from 'react-algoliasearch';

class Navbar extends Component {
  constructor(props){
    super(props);
    this.state = {
      currentScrollHeight: 0,
    }
  }

  componentDidMount () {
     window.onscroll = () => {
      const newScrollHeight = Math.ceil(window.scrollY / 50) *50;
      if (this.state.currentScrollHeight != newScrollHeight){
          this.setState({currentScrollHeight: newScrollHeight})
      }
    }
  }
  render() {
    const opacity = Math.min(100 / this.state.currentScrollHeight  , 1)

    return(
      <div className="navbar" style={{opacity}}>
        <a className="logo" onClick={this.props.changeHome}>
          <img src={require('../images/stockfindar_straightlogo.png')} />
        </a>
        <div>
          <form>
          <AgAutocomplete
            apiKey={"6dc685dc57968d5a67e816916887382c"}
            appId={"F7HFR1MH0G"}
            displayKey="Company Name"
            indices={[{index: 'stocks'}]}
            inputId="input-search"
            placeholder="Search Stocks..."
            keyName="Company Name"
            hitsPerPage="10"
            selected={this.suggestionSelected}
            options={{autoselectOnBlur: true, hint: true, debug: false}}
          />
          </form>
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
          <a onClick={this.props.changePrediction} className="navLink">
            <p> Prediction (BETA) </p>
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
            <form onSubmit={this.props.login}>
              <input type="text" name="username" placeholder="username" className="username"/>
              <input type="password" name="password" placeholder="password" className="password"/>
              <input type="submit" value="Login" className="submit"/>
            </form>
            <div id="LoginForm">
            </div>
          </div>
        }
        {
          this.props.loggedOn &&
          <div className="loginContainer">
            <h3>Welcome Hacker!</h3>
            <form onSubmit={this.props.logoff}>
              <input type="submit" value="Log Off" className="submit"/>
            </form>
          </div>
        }
      </div>
    );
  }
}

export default Navbar;

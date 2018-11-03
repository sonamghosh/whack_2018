import React, { Component } from 'react';
import './content/App.css';
import Navbar from './components/navbar';
import Header from './components/header';
import StockFindAR from './components/stockFindAR';
import UseCases from './components/useCases';
import Resources from './components/resources';
import About from './components/about';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      view: "main",
    }
  }

  changeTab = (tabName) => {
    this.setState({view: [tabName]});
  }

  render() {
    return (
      <div className="App">
        <Navbar
          changeStockFindAR={() => this.changeTab("stockFindAR")}
          changeUseCases={() => this.changeTab("useCases")}
          changeResources={() => this.changeTab("resources")}
          changeAbout={() => this.changeTab("about")}
        />
        <header className="App-header">

        </header>

        <body className="App-body">
          {(this.state.view == "main") && <Header />}
          {(this.state.view == "stockFindAR") && <StockFindAR />}
          {(this.state.view == "useCases") && <UseCases />}
          {(this.state.view == "resources") && <Resources />}
          {(this.state.view == "about") && <About />}
        </body>

        <footer>

        </footer>
      </div>
    );
  }
}

export default App;

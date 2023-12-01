import React, { Component } from 'react';
import Home from "./Home";
import Header from "./Header";


class App extends Component {
  pages = {
    home: <Home />,
  }
  constructor(props) {
    super(props);
    this.state = {
      page: props.page
    }
  };
  componentDidMount() {
  };
  render() {
    return (
        <div>
          <Header/>
          {this.pages[this.state.page]}
        </div>
    )
  };
}

export default App;

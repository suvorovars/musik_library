import React, {useState} from 'react';
import './styles/Home.css';

class Home extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
      inputValue: '' // начальное значение input
    };
  }

  handleChange = (event) => {
    this.setState({ inputValue: event.target.value });
  }
  handleSubmit = (event) => {
    event.preventDefault();
    // Достаем данные из input, например, можем их вывести в консоль
    console.log("Input value:", this.state.inputValue);
    // Дальнейшие действия с данными
  }
    render() {
        return (
            <div className='home'>
                <div>
                    <h1></h1>
                    <label className="switch">
                    <input type="checkbox" value={this.state.inputValue} onChange={this.handleChange}/>
                    <span className="slider round"></span>
                    </label>
                </div>

            </div>
        );
    }
}

export default Home;
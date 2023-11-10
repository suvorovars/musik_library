import React from 'react';
import Header from "./Header";
import Home from "./Home";


class App extends React.Component {
    state = {
    jsonData: null,
    };

    componentDidMount() {
        this.fetchData();
    }
    fetchData = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/get/strings');
            const data = await response.json();

            this.setState({ jsonData: data });
        }
        catch (error) {
            console.error('Ошибка при запросе:', error);
        }
    };
    render() {
        return (
            <div>
                <Header/>
                <Home/>
            </div>
        );
    }
}

export default App;

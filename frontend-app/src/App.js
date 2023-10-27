import React from 'react';
import Header from './Header'
import Disk from './Disk'

import * as styles from './App.css';

class App extends React.Component {
    response = {
        disk: {
            disk_title: '',
            strings:[],
        }
    }
    componentDidMount() {
        fetch('http://localhost:5000/api/strings')
    }
    render() {

        return (
            <div>
                <Header/>
                <Disk/>
                <Disk/>
                <Disk/>
            </div>
        );
    }
}

export default App;

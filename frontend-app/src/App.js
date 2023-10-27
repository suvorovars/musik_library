import React from 'react';
import Header from './Header'
import Disk from './Disk'

import * as styles from './App.css';

class App extends React.Component {


    render() {
        const someData = "Home";
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

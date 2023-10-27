import * as style from './Disk.css';
import React from 'react';
import Table from'./Table';

class Disk extends React.Component {
    render() {
        return (
            <div className="disk">
                <div className="disk_name">
                    <h1>Сборник Ремиксов 2.0</h1>
                    <h2>2018</h2>
                </div>

                <div className="disk_content">
                    <Table/>
                </div>
            </div>
        );
    }
}

export default Disk;
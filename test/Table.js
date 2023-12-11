import React, { Component} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import BootstrapTable from 'react-bootstrap-table-next';

class Table extends Component {
    constructor(props) {
        super(props);
        this.data = props.data;
        this.columns = props.columns;
    }

    render() {
    return (
      <div className="App">
        <p className="Table-header">Basic Table</p>

        <BootstrapTable keyField='id' data={ this.data } columns={ this.columns } />
      </div>
    );
  }
}

export default Table;
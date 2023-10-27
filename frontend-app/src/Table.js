import React from 'react';
import * as style from './table.css'

class Table extends React.Component {
    render() {
        return (
            <table className='table'>
                <thead>
                    <tr>
                        <th>№</th>
                        <th>Title</th>
                        <th>Artist</th>
                        <th>Genre</th>
                        <th>Duration</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Title 1</td>
                        <td>Artist 1</td>
                        <td>Genre 1</td>
                        <td>4:06</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Title 1</td>
                        <td>Artist 1</td>
                        <td>Genre 1</td>
                        <td>4:06</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Title 1</td>
                        <td>Artist 1</td>
                        <td>Genre 1</td>
                        <td>4:06</td>
                    </tr>
                </tbody>
            </table>
        )
    }
}

export default Table;
import React from 'react';
import * as style from './header.css';

class Header extends React.Component {
    render() {
        return (
            <div className="header">
            <a className="logo">Music Library</a>
            <div className="header_right">
                <a className="active">Create Disk</a>
                <a>Home</a>
                <a>FAQ</a>
            </div>
        </div>
        );
    }
}
export default Header;
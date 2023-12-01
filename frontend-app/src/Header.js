import { PageHeader } from 'antd';
import React, { Component } from 'react';

class Header extends Component {
    render () {
        return (
            <PageHeader className="site-page-header" onBack={() => null} title="Title" subTitle="This is a subtitle"></PageHeader>
        )
    }
}
import React from 'react';
import * as ReactDOMClient from 'react-dom/client';

const app = ReactDOMClient.createRoot(document.getElementById('app'));

app.render(<h1>Hello</h1>);


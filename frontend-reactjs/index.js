import React from "react";
import ReactDOM from 'react-dom';
import App from './components/App.js';

fetch('127.0.0.1:8000/api/get/listing/all', {
    method: 'GET',
    headers: {
        'Accept': 'application/json'.
    },
})
.then(response => response.json())
.then(response => console.log(JSON.stringify(response)))

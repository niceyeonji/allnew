const express = require('express');
const bodyParser = require('body-parser');
const CircularJSON = require('circular-json');
const request = require('request');
const mysql = require('sync-mysql');
const env = require('dotenv').config({path: '../../.env'});

var connection = new mysql({
  host: process.env.host,
  user: process.env.user,
  password: process.env.password,
  database: process.env.database,
});

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.get('/Hello', (req, res) => {
  res.send('Hello World');
});

// Select all rows from st_info table
app.get('/select', (req, res) => {
  const result = connection.query('SELECT * FROM st_info');
  console.log(result);
  res.send(result);
});

// insert data into st_info table
app.get('/insert', (req, res) => {
  const {ST_ID, NAME, DEPT} = req.query;
  const result = connection.query('INSERT INTO st_info values (?, ?, ?)', [
    ST_ID,
    NAME,
    DEPT,
  ]);
});

module.exports = app;

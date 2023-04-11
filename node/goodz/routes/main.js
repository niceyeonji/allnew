const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
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

app.get('/hello', (req, res) => {
  res.send('Hello Edam ent.');
});

// request 1, query 0
app.get('/select', (req, res) => {
  const result = connection.query('select * from productTable');
  console.log(result);
  res.send(result);
});

// request 1, query 1
app.get('/selectQuery', (req, res) => {
  const prodId = req.query.prodId;
  const result = connection.query('select * from productTable where prodId=?', [
    prodId,
  ]);
  console.log(result);
  res.send(result);
});

// request 1, query 1
app.post('/insert', (req, res) => {
  const {id, name, price, arti} = req.body;
  const result = connection.query(
    'insert into productTable values (?, ?, ?, ?)',
    [id, name, price, arti],
  );
  console.log(result);
  res.redirect('selectQuery?prodId=' + req.body.id);
});

// request 1, query 1
app.post('/update', (req, res) => {
  const {id, name, price, arti} = req.body;
  const result = connection.query(
    'update productTable set prodName=?, prodPrice=?, prodArti=? where prodId=?',
    [name, price, arti, id],
  );
  console.log(result);
  res.redirect('selectQuery?prodId=' + req.body.id);
});

// request 1, query 1
app.post('/delete', (req, res) => {
  const {id, name, price, arti} = req.body;
  const result = connection.query('delete from productTable where prodId=?', [
    id,
  ]);
  console.log(result);
  res.redirect('/select');
});

module.exports = app;

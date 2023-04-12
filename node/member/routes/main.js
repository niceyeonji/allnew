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
  res.send('Hello World~!!');
});

// login
app.post('/login', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query(
    'select * from user where userid=? and passwd=?',
    [id, pw],
  );
  if (result.length == 0) {
    res.redirect('error.html');
  }
  if (id == 'admin' || id == 'root') {
    console.log(id + ' => Administrator Logined');
    res.redirect('member.html');
  } else {
    console.log(id + ' => User Logined');
    res.redirect('main.html');
  }
});

// register
app.post('/register', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query('insert into user values (?, ?)', [id, pw]);
  console.log(result);
  res.redirect('/');
});

// request O, query X
app.get('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  res.send(result);
});

// request O, query X
app.post('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  res.send(result);
});

// request O, query O
app.get('/selectQuery', (req, res) => {
  const id = req.query.id;
  const result = connection.query('select * from user where userid=?', [id]);
  console.log(result);
  res.send(result);
});

// request O, query O
app.post('/selectQuery', (req, res) => {
  const id = req.body.id;
  // console.log(req.body);
  const result = connection.query('select * from user where userid=?', [id]);
  console.log(result);
  res.send(result);
});

// request O, query O
app.post('/insert', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query('insert into user values (?, ?)', [id, pw]);
  console.log(result);
  res.redirect('/selectQuery?id=' + req.body.id);
});

// request O, query O
app.post('/update', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query('update user set passwd=? where userid=?', [
    pw,
    id,
  ]);
  console.log(result);
  res.redirect('/selectQuery?id=' + req.body.id);
});

// request O, query O
app.post('/delete', (req, res) => {
  const id = req.body.id;
  const result = connection.query('delete from user where userid=?', [id]);
  console.log(result);
  res.redirect('/select');
});

module.exports = app;

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

// request 1, query 0
app.get('/select', (req, res) => {
  const result = connection.query('select * from user;');
  console.log(result);
  res.send(result);
});

// request 1, query 0
app.post('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  res.send(result);
});

// request 1, query 1
app.post('/selectQuery', (req, res) => {
  const userid = req.body.userid;
  const result = connection.query('select * from user where userid=?', [
    userid,
  ]);
  console.log(result);
  res.send(result);
});

// request 1, query 1
app.get('/selectQuery', (req, res) => {
  const userid = req.query.userid;
  // console.log(req.body);
  const result = connection.query('select * from user where userid=?', [
    userid,
  ]);
  // console.log(res);
  // res.send(res);
  console.log(result);
  res.send(result);
});

// request 1, query 1
app.post('/insert', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query('insert into user values (?, ?)', [id, pw]);
  console.log(result);
  res.redirect('selectQuery?userid=' + req.body.id);
});

// request 1, query 1
app.post('/update', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query('update user set passwd=? where userid=?', [
    pw,
    id,
  ]);
  console.log(result);
  res.redirect('selectQuery?userid=' + req.body.id);
});

// request 1, query 1
app.post('/delete', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query('delete from user where userid=?', [id]);
  console.log(result);
  res.redirect('/select');
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
    console.log(id + ' => Aministrator Logined');
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

module.exports = app;

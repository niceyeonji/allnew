const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const mysql = require('../../auth/node_modules/sync-mysql/lib');
const env = require('../../auth/node_modules/dotenv/lib/main').config({
  path: '../../.env',
});

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
  const result = connection.query('select * from user');
  console.log(result);
  // res.send(result);
  res.writeHead(200);
  var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
                <link type="text/css" rel="stylesheet" href="mystyle.css" />
            <meta charset="utf-8">
        </head>
        <body>
        <table border="1" style="margin:auto; text-align:center;">
        <thead>
            <tr><th>User ID</th><th>Password</th></tr>
        </thead>
        <tbody>
        `;
  for (var i = 0; i < result.length; i++) {
    template += `
        <tr>
            <td>${result[i]['userid']}</td>
            <td>${result[i]['passwd']}</td>
        </tr>
        `;
  }
  template += `
        </tbody>
        </table>
        </body>
        </html>
    `;
  res.end(template);
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
  console.log(req.query);
  const userid = req.query.userid;
  const result = connection.query('select * from user where userid=?', [
    userid,
  ]);
  console.log(result.length);
  if (result.length == 0) {
    res.send('데이터가 존재하지 않습니다');
  } else {
    console.log(result);
    res.writeHead(200);
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
                <link type="text/css" rel="stylesheet" href="mystyle.css" />
            <meta charset="utf-8">
        </head>
        <body>
        <table border="1" style="margin:auto; text-align:center;">
        <thead>
            <tr><th>User ID</th><th>Password</th></tr>
        </thead>
        <tbody>
        `;
    for (var i = 0; i < result.length; i++) {
      template += `
        <tr>
            <td>${result[i]['userid']}</td>
            <td>${result[i]['passwd']}</td>
        </tr>
        `;
    }
    template += `
        </tbody>
        </table>
        </body>
        </html>
    `;
    res.send(template);
  }
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

module.exports = app;

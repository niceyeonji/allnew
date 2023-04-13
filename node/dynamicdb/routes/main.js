const express = require('express');
const bodyParser = require('body-parser');
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

// request O, query X
app.get('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  // res.send(result);
  res.writeHead(200);
  if (result.length == 0) {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>
        </body>
        </html>
        `;
    res.end(template);
  } else {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
        <table border="1" style="margin:auto;">
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
  }
});

// request O, query X
app.post('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  // res.send(result);
  res.writeHead(200);
  if (result.length == 0) {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>
        </body>
        </html>
        `;
    res.end(template);
  } else {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
        <table border="1" style="margin:auto;">
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
  }
});

// request O, query O
app.get('/selectQuery', (req, res) => {
  const id = req.query.id;
  const result = connection.query('select * from user where userid=?', [id]);
  console.log(result);
  // res.send(result);
  res.writeHead(200);
  if (result.length == 0) {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>
        </body>
        </html>
        `;
    res.end(template);
  } else {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
        <table border="1" style="margin:auto;">
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
  }
});

// request O, query O
app.post('/selectQuery', (req, res) => {
  const id = req.body.id;
  // console.log(req.body);
  const result = connection.query('select * from user where userid=?', [id]);
  console.log(result);
  // res.send(result);
  res.writeHead(200);
  if (result.length == 0) {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>
        </body>
        </html>
        `;
    res.end(template);
  } else {
    var template = `
        <!doctype html>
        <html>
        <head>
            <title>Result</title>
            <meta charset="utf-8">
            <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
        <table border="1" style="margin:auto;">
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
  }
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

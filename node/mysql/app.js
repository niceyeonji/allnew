var express = require('express');
var mysql = require('mysql');
const env = require('dotenv').config({path: '../../.env'});

var connection = mysql.createConnection({
  host: process.env.host,
  user: process.env.user,
  port: process.env.port,
  password: process.env.password,
  database: process.env.database,
});

var app = express();

connection.connect(function (err) {
  if (!err) {
    console.log('Database is connected....\n\n');
  } else {
    console.log('Error connecting Database....\n\n');
  }
});

app.get('/', function (req, res) {
  connection.query('select * from st_info', function (err, row, fields) {
    connection.end();
    if (!err) {
      res.send(rows);
      console.log('The solution is : ', rows);
    } else {
      console.log('Error while performing Query ');
    }
  });
});

app.listen(8000, function () {
  console.log('8000 Port : Server Started...');
});

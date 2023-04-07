var oracledb = require('oracledb');
var dbConfig = require('./dbConfig');
var express = require('express');
var path = require('path');

var app = express();

app.set('port', process.env.PORT || 3000);

var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

oracledb.autoCommit = true;

app.get('/', (req, res) => {
    res.send('Web Server started~!!')
})

app.all('*', function (req, res) {
    res.status(404).send('<h1>ERROR - Page is not found.</h1>');
});

app.listen(app.get('port'), function () {
    console.log("Express server listening on port" + app.get('port'));
})
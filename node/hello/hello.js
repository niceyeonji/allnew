var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Hello Node JS~!!');
});

app.listen(3000, function () {
  console.log('3000 Port : Server Started~!!');
});

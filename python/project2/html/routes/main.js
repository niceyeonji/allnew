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

function template_nodata(res) {
  res.writeHead(200);
  var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
        <h2>데이터가 존재하지 않습니다.</h2>
    </body>
    </html>
    `;
  res.end(template);
}

function template_result(result, res) {
  res.writeHead(200);
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

app.get('/hello', (req, res) => {
  res.send('Hello World~!!');
});

app.get('/thanks', (req, res) => {
  res.send('방문해주셔서 압도적 감사');
});

// login
app.post('/login', (req, res) => {
  const {id, pw} = req.body;
  const result = connection.query(
    'select * from user where userid=? and passwd=?',
    [id, pw],
  );
  // console.log(result);
  if (result.length == 0) {
    res.redirect('error.html');
  }
  if (id == 'admin' || id == 'root') {
    console.log(id + ' => Administrator Logined');
    res.redirect('member.html?id=' + id);
  } else {
    console.log(id + ' => User Logined');
    res.redirect('main.html?id=' + id);
  }
});

// register
app.post('/register', (req, res) => {
  const {id, pw} = req.body;
  if (id == '') {
    res.redirect('register.html');
  } else {
    let result = connection.query('select * from user where userid=?', [id]);
    if (result.length > 0) {
      res.writeHead(200);
      var template = `
        <!doctype html>
        <html>
        <head>
            <title>Error</title>
            <meta charset="utf-8">
        </head>
        <body>
            <div>
                <h3 style="margin-left: 30px">Registrer Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
                <a href="register.html" style="margin-left: 30px">다시 시도하기</a>
            </div>
        </body>
        </html>
        `;
      res.end(template);
    } else {
      result = connection.query('insert into user values (?, ?)', [id, pw]);
      console.log(result);
      res.redirect('/');
    }
  }
});

// request O, query X
app.get('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  // res.send(result);
  if (result.length == 0) {
    template_nodata(res);
  } else {
    template_result(result, res);
  }
});

// request O, query X
app.post('/select', (req, res) => {
  const result = connection.query('select * from user');
  console.log(result);
  // res.send(result);
  if (result.length == 0) {
    template_nodata(res);
  } else {
    template_result(result, res);
  }
});

// request O, query O
app.get('/selectQuery', (req, res) => {
  const id = req.query.id;
  if (id == '') {
    // res.send('User-id를 입력하세요.')
    res.write("<script>alert('User-id를 입력하세요.')</script>");
  } else {
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    // res.send(result);
    if (result.length == 0) {
      template_nodata(res);
    } else {
      template_result(result, res);
    }
  }
});

// request O, query O
app.post('/selectQuery', (req, res) => {
  const id = req.body.id;
  if (id == '') {
    // res.send('User-id를 입력하세요.');
    res.write("<script>alert('User-id를 입력하세요.')</script>");
  } else {
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    // res.send(result);
    if (result.length == 0) {
      template_nodata(res);
    } else {
      template_result(result, res);
    }
  }
});

// request O, query O
app.post('/insert', (req, res) => {
  const {id, pw} = req.body;
  if (id == '' || pw == '') {
    // res.send('User-id와 Password를 입력하세요.');
    res.write("<script>alert('User-id와 Password를 입력하세요.')</script>");
  } else {
    let result = connection.query('select * from user where userid=?', [id]);
    if (result.length > 0) {
      res.writeHead(200);
      var template = `
        <!doctype html>
        <html>
        <head>
            <title>Error</title>
            <meta charset="utf-8">
        </head>
        <body>
            <div>
                <h3 style="margin-left: 30px">Registrer Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
            </div>
        </body>
        </html>
        `;
      res.end(template);
    } else {
      result = connection.query('insert into user values (?, ?)', [id, pw]);
      console.log(result);
      res.redirect('/selectQuery?id=' + req.body.id);
    }
  }
});

// request O, query O
app.post('/update', (req, res) => {
  const {id, pw} = req.body;
  if (id == '' || pw == '') {
    // res.send('User-id와 Password를 입력하세요.');
    res.write("<script>alert('User-id와 Password를 입력하세요.')</script>");
  } else {
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    // res.send(result);
    if (result.length == 0) {
      template_nodata(res);
    } else {
      const result = connection.query(
        'update user set passwd=? where userid=?',
        [pw, id],
      );
      console.log(result);
      res.redirect('/selectQuery?id=' + id);
    }
  }
});

// request O, query O
app.post('/delete', (req, res) => {
  const id = req.body.id;
  if (id == '') {
    res.write("<script>alert('User-id와 Password를 입력하세요.')</script>");
  } else {
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    // res.send(result);
    if (result.length == 0) {
      template_nodata(res);
    } else {
      const result = connection.query('delete from user where userid=?', [id]);
      console.log(result);
      res.redirect('/select');
    }
  }
});

app.get('/temperature', (req, res) => {
  axios
    .get('http://192.168.1.58:3000/tempmongo')
    .then(response => {
      console.log(`상태 코드: ${response.status}`);
      console.log(response.data);

      const temperatureData = response.data;

      // 기온 데이터를 HTML 형식의 문자열로 변환합니다.
      let temperatureHTML = '';
      for (const [date, temperature] of Object.entries(temperatureData)) {
        temperatureHTML += `<p>${date}: ${temperature}</p>`;
      }

      res.send(temperatureHTML);
    })
    .catch(error => {
      console.log(error);
      res.status(500).send('기온 데이터를 가져오는 중에 오류가 발생했습니다.');
    });
});

module.exports = app;

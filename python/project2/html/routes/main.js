const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({path: '../../../.env'});
const axios = require('axios');
const fs = require('fs');
const {promisify} = require('util');
const writeFrileAsync = promisify(fs.writeFile);

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

app.get('/tempmongo', (req, res) => {
  axios
    .get('http://192.168.1.58:3000/tempmongo')
    .then(response => {
      console.log(`statusCode : ${response.status}`);
      console.log(response.data);
      res.send(response.data);
    })
    .catch(error => {
      console.log(error);
    });
});

app.get('/temp_graph', async (req, res) => {
  const {year1, year2} = req.query;

  // FastAPI 엔드포인트에 GET 요청을 보내서 기온 그래프를 생성합니다.
  const fastAPIUrl = `http://192.168.1.58:3000/temp_graph?year1=${year1}&year2=${year2}`;
  const response = await axios.get(fastAPIUrl, {responseType: 'arraybuffer'});

  // 서버에 그래프 이미지를 저장합니다.
  const filename = `tempGraph_${year1}_${year2}.png`;
  await writeFileAsync(filename, response.data);

  // 응답으로 파일 이름을 전송합니다.
  res.send(filename);
});

app.get('/gettemp', async (req, res) => {
  const {year} = req.query;

  if (!year) {
    return res.send("'년도(ex,2018)의 입력을 확인해주세요");
  } else {
    const months = Array.from({length: 12}, (_, i) =>
      String(i + 1).padStart(2, '0'),
    );
    const result = await tempmongo();
    const data = Object.entries(result)
      .filter(([key]) => {
        const [keyYear, keyMonth] = key.split('-');
        return keyYear === year && months.includes(keyMonth);
      })
      .reduce((obj, [key, value]) => {
        obj[key] = value;
        return obj;
      }, {});

    res.json(data);
  }
});

module.exports = app;

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const pool = require('../../config/pool');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.get('/Hello', (req, res) => {
  res.send('Hello World');
});

// Select all rows from st_info table
app.get('/select', async (req, res) => {
  const [rows, fields] = await pool.query('SELECT * FROM st_info');
  console.log(rows);
  res.writeHead(200);
  var template = `
  <!doctype html>
  <html>
  <head>
    <title>Result</title>
    <meta charset="utf-8">
  </head>
  <body>
   <table border="1" margin:auto; text-align:center;>
     <tr>
       <th>ST_ID</th>
       <th>NAME</th>
       <th>DEPT</th>
     </tr>
   `;
  for (var i = 0; i < rows.length; i++) {
    template += `
     <tr>
       <th>${rows[i]['ST_ID']}</th>
       <th>${rows[i]['NAME']}</th>
       <th>${rows[i]['DEPT']}</th>
     </tr>
    `;
  }
  template += `
     </table>
  </body>
  </html>
 `;
  res.end(template);
});

// insert data into st_info table
app.get('/insert', async (req, res) => {
  const {ST_ID, NAME, DEPT} = req.query;
  const [rows, fields] = await pool.query(
    'INSERT INTO st_info values (?, ?, ?)',
    [ST_ID, NAME, DEPT],
  );

  res.redirect('/select');
});

// update row from st_info table
app.get('/update', async (req, res) => {
  const {ST_ID, NAME, DEPT} = req.query;
  const [rows, fields] = await pool.query(
    'UPDATE st_info SET NAME=?, DEPT=? WHERE ST_ID=?',
    [NAME, DEPT, ST_ID],
  );

  res.redirect('/select');
});

// delete row from st_info table
app.get('/delete', async (req, res) => {
  const ST_ID = req.query.ST_ID;
  const [results] = await pool.query('DELETE FROM st_info WHERE ST_ID=?', [
    ST_ID,
  ]);

  res.redirect('/select');
});

module.exports = app;

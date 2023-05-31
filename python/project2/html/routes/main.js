const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({path: '../../../.env'});
const axios = require('axios');
const app = express();
const cors = require('cors'); // cors 모듈 추가

var connection = new mysql({
  host: process.env.host,
  user: process.env.user,
  password: process.env.password,
  database: process.env.database,
});

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(express.json());
app.use(express.urlencoded({extended: true}));

// app.get('/tempmongo', (req, res) => {
//   axios
//     .get('http://192.168.1.58:3000/tempmongo')
//     .then(response => {
//       console.log(`statusCode : ${response.status}`);
//       console.log(response.data);
//       res.send(response.data);
//     })
//     .catch(error => {
//       console.log(error);
//     });
// });

app.get('/temp_graph', async (req, res) => {
  const {year1, year2} = req.query;

  try {
    const response = await axios.get(
      `http://192.168.1.58:3000/temp_graph?year1=${year1}&year2=${year2}`,
    );
    const {message, filename} = response.data;
    res.json({message, filename});
  } catch (error) {
    console.error(error);
    res.status(500).json({error: 'Internal Server Error'});
  }
});

app.get('/combined_frame/:year1/:year2', (req, res) => {
  const {year1, year2} = req.params;
  const apiUrl = `http://192.168.1.58:3000/combined_frame/${year1}/${year2}`;

  axios
    .get(apiUrl)
    .then(response => {
      const data = response.data;
      res.send(data);
    })
    .catch(error => {
      console.error('Error:', error);
      res.status(500).send('Internal Server Error');
    });
});

app.get('/pie_charts', async (req, res) => {
  const {year1, year2} = req.query;

  try {
    const response = await axios.get(
      `http://192.168.1.58:3001/pie_charts/${year1}/${year2}`,
    );
    const {message, filename} = response.data;
    res.json({message, filename});
  } catch (error) {
    console.error(error);
    res.status(500).json({error: 'Failed to generate pie charts.'});
  }
});

app.get('/combined_frame2/:year1/:year2', (req, res) => {
  const {year1, year2} = req.params;
  const apiUrl = `http://192.168.1.187:3001/combined_frame2/${year1}/${year2}`;

  axios
    .get(apiUrl)
    .then(response => {
      const data = response.data;
      res.send(data);
    })
    .catch(error => {
      console.error('Error:', error);
      res.status(500).send('Internal Server Error');
    });
});

app.get('/combined_frame3/:year1/:year2', (req, res) => {
  const {year1, year2} = req.params;
  const apiUrl = `http://192.168.1.187:3000/combined_frame3/${year1}/${year2}`;

  axios
    .get(apiUrl)
    .then(response => {
      const data = response.data;
      res.send(data);
    })
    .catch(error => {
      console.error('Error:', error);
      res.status(500).send('Internal Server Error');
    });
});

app.get('/month_tempmongo', (req, res) => {
  const {year1, year2} = req.query;
  const apiUrl = `http://192.168.1.58:3000/month_tempmongo?year1=${year1}&year2=${year2}`;

  axios
    .get(apiUrl)
    .then(response => {
      const data = response.data;
      res.json(data);
    })
    .catch(error => {
      console.error(error);
      res.status(500).send('Internal Server Error');
    });
});

app.get('/month_firemongo', (req, res) => {
  const {year1, year2} = req.query;
  const apiUrl = `http://192.168.1.187:3001/result_fire?year1=${year1}&year2=${year2}`;

  axios
    .get(apiUrl)
    .then(response => {
      const data = response.data;
      res.json(data);
    })
    .catch(error => {
      console.error(error);
      res.status(500).send('Internal Server Error');
    });
});

app.get('/month_ufmongo', (req, res) => {
  const {year1, year2} = req.query;
  const apiUrl = `http://192.168.1.187:3000/result_uf?year1=${year1}&year2=${year2}`;

  axios
    .get(apiUrl)
    .then(response => {
      const data = response.data;
      res.json(data);
    })
    .catch(error => {
      console.error(error);
      res.status(500).send('Internal Server Error');
    });
});

module.exports = app;

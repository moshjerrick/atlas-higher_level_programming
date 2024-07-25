#!/usr/bin/node
// script that displays the status code of a GET request.
const URL = process.argv[2];
const request = require('request');

request.get(URL, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
}
);
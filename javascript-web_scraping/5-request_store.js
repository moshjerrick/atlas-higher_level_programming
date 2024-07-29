#!/usr/bin/node
// script that writes the contents of a webpage to a file.
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filePath = process.argv[3];

request.get(URL, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  }
  );
});

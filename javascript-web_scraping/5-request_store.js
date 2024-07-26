#!/usr/bin/node
// script that writes the contents of a webpage to a file.
const require = require('request');
const fs = require('fs');
const { request } = require('http');

const URL = process.argv[2];
const filePath = process.argv[3];

request.get(URL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile

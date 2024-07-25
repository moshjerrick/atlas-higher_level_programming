#!/usr/bin/node
//  a script that writes a string to a file.
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];
fs.writeFile(filePath, string, 'utf8', (err) => {
    if (err) {
        console.log(err);
      } else {
        //console.log(string);
      }
    });

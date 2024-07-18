#!/usr/bin/node
// Concatenates two arguments passed to it
const [,, firstArg, secondArg] = process.argv;
console.log(firstArg + ' is ' + secondArg);

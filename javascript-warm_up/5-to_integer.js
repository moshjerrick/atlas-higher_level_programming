#!/usr/bin/node
// prints my number: <first argument converted in integer>
const [,, firstArg] = process.argv;
const num = parseInt(firstArg);
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}

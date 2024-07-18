#!/usr/bin/node
// Script that prints the first argument passed to it
const [, , firstArg] = process.argv;
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}

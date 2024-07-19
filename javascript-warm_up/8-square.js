#!/usr/bin/node
// script that prints a square
const [,, x] = process.argv;
const num = parseInt(x);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}

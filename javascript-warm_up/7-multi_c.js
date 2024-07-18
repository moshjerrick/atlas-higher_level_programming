#!/usr/bin/node
// script that prints x times "C is fun"
const [,, x] = process.argv;
const num = parseInt(x);
const langs = ['C is fun'];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(langs[0]);
  }
}

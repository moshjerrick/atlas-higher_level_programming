#!/usr/bin/node
// prints the addition of two ints
const [,, a, b] = process.argv;
const num1 = parseInt(a);
const num2 = parseInt(b);
function add(a, b) {
  return a + b;
}
console.log(add(num1, num2));

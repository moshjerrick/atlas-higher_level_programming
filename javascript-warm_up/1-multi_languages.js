#!/usr/bin/node
// Prints message based on number of arguments
console.log('Script started');
if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

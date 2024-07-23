#!/usr/bin/node
// funtion that prints the number of args alrady printed and the new arg value
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(this.count + ': ' + item);
  this.count++;
};

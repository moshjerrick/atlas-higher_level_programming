#!/usr/bin/node
// funtion that prints the number of args alrady printed and the new arg value
exports.logMe = function (item) {
  console.log(this.count + ': ' + item);
  this.count++;
};

#!/usr/bin/node
// class Square that defines a square and inherits from Square
const parentSquare = require('./5-square');

module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

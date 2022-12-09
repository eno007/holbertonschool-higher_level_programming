#!/usr/bin/node
// class Square that inherits from Rectangle
const Squar = require('./5-square');
class Square extends Squar {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;

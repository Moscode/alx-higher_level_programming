#!/usr/bin/node
const Square = require('./5-square.js');
class Square1 extends Square {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log('C'.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square1;

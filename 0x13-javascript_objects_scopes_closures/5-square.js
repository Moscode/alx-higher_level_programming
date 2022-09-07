#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Square;

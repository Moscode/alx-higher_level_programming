#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) && !isNaN(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;

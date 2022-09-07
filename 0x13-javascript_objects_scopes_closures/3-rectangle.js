#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) && !isNaN(h) && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      const store = [];
      for (let j = 0; j < this.width; j++) {
        store.push('X');
      }
      console.log(`${store.join('')}`);
    }
  }
}
module.exports = Rectangle;

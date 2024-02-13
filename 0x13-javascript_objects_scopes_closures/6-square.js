#!/usr/bin/node
const OrigSquare = require('./5-square');

class Square extends OrigSquare {
  charPrint (c = 'X') {
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        square += c;
      }
      if (i < this.height - 1) square += '\n';
    }
    console.log(square);
  }
}

module.exports = Square;

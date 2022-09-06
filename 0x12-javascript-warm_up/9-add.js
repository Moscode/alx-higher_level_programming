#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}
const firstVal = process.argv[2];
const secondVal = process.argv[3];
add(firstVal, secondVal);

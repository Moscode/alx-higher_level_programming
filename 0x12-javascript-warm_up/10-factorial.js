#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  if (num < 0) {
    return;
  }
  return num * factorial(num - 1);
}
const facNum = process.argv[2];
console.log(factorial(facNum));

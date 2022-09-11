#!/usr/bin/node
const argLength = process.argv.length;
const arg = process.argv;
const storeInput = [];
if (argLength < 4) {
  console.log(0);
}
for (let j = 2; j < argLength; j++) {
  storeInput.push(arg[j]);
}
storeInput.sort();
for (let i = storeInput.length - 2; i > 1; i--) {
  if (storeInput[i] !== storeInput[argLength - 1]) {
    console.log(storeInput[i]);
    break;
  }
}

#!/usr/bin/node
const arg = process.argv[2];
if (arg) {
  const intVersion = Math.floor(arg);
  for (let i = 0; i < intVersion; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) console.log('Missing size');
const intVersion = Math.floor(arg);
for (let i = 0; i < intVersion; i++) {
  const temp = [];
  for (let j = 0; j < intVersion; j++) {
    temp.push('X');
  }
  console.log(temp.join(''));
}

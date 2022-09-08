#!/usr/bin/node
const ls = require('./100-data.js').list;
const solution = ls.map((ele, index) => ele * index);
console.log(ls);
console.log(solution);

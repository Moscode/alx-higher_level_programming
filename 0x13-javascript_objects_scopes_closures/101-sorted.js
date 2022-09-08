#!/usr/bin/node
const dictOccurrence = require('./101-data.js').dict;
const sortedDict = {};
for (const [val, id] of Object.entries(dictOccurrence)) {
  if (sortedDict[id]) {
    sortedDict[id].push(val);
  } else {
    sortedDict[id] = [val];
  }
}
console.log(sortedDict);

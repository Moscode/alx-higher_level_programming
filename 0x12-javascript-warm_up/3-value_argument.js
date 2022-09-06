#!/usr/bin/node
const store = process.argv[2];
if (store) {
  console.log(store);
} else {
  console.log('No argument');
}

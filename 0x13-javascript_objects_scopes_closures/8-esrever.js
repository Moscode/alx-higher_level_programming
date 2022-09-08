#!/usr/bin/node
exports.esrever = function (list) {
  const end = list.length;
  const storeReverse = [];
  for (let i = end; i > 0; i--) {
    storeReverse.push(list[i - 1]);
  }
  return storeReverse;
};

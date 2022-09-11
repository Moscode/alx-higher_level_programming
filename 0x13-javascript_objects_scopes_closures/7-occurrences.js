#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const storeOccurences = [];
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      storeOccurences.push(searchElement);
    }
  }
  return (storeOccurences.length);
};

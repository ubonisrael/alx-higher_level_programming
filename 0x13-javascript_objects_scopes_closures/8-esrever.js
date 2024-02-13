#!/usr/bin/node
exports.esrever = function (list) {
  const revArr = list.slice();
  for (let i = 0; i < list.length / 2; i++) {
    revArr[i] = list[list.length - 1 - i];
    revArr[list.length - 1 - i] = list[i];
  }
  return revArr;
};

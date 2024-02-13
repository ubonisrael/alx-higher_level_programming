#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
for (const key in dict) {
  const v = dict[key];
  newDict[`${v}`] = newDict[`${v}`] || [];
  newDict[`${v}`] = [...newDict[`${v}`], key];
}
console.log(newDict);

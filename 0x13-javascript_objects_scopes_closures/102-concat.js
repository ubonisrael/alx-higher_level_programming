#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');

try {
  const fileOne = readFileSync(process.argv[2], { encoding: 'utf-8' });
  const fileTwo = readFileSync(process.argv[3], { encoding: 'utf-8' });
  writeFileSync(process.argv[4], fileOne + fileTwo, {
    encoding: 'utf-8',
    flag: 'w'
  });
} catch (err) {
  console.log(err);
}

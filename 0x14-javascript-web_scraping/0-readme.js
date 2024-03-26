#!/usr/bin/node
const readFile = require('fs').readFile;

readFile(process.argv[2], { encoding: 'utf8', flag: 'r' }, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

#!/usr/bin/node
const { createWriteStream } = require('fs');
const request = require('request');

request(process.argv[2])
  .on('error', (error) => console.log(error))
  .pipe(createWriteStream(process.argv[3]));

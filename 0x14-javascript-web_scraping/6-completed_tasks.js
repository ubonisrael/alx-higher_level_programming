#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const dict = {};
    data.forEach(element => {
      if (element.completed) {
        dict[element.userId] = (dict[element.userId] || 0) + 1;
      }
    });
    console.log(dict);
  }
});

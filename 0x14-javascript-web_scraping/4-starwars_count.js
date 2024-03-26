#!/usr/bin/node
const request = require('request');

request(`${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let apps = 0;
    data.results.forEach(movie => {
      movie.characters.forEach(char => {
        if (char.includes('18')) apps++;
      });
    });
    console.log(apps);
  }
});

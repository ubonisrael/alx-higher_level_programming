#!/usr/bin/node
const request = require('request');

request(`${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    // const wedge_antills_app = data.results.filter()
    const apps = data.results.filter(movie => {
      const id = 'https://swapi-api.alx-tools.com/api/people/18/';
      if (movie.characters.indexOf(id) >= 0) return true;
      return false;
    });
    console.log(apps.length);
  }
});

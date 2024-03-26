#!/usr/bin/node
const request = require('request');
const util = require('util');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const requestUtil = util.promisify(request);
    for (const character of data.characters) {
      try {
        const res = await requestUtil(character);
        const data = await JSON.parse(res.body);
        console.log(data.name);
      } catch (err) {
        console.error(err);
      }
    }
  }
});

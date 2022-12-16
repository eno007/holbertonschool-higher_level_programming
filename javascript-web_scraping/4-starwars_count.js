#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    throw new Error(err);
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film in films) {
    const characters = films[film].characters;
    for (const id in characters) {
      if (characters[id].includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
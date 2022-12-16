#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    throw new Error(err);
  }
  const data = JSON.parse(body);
  const results = {};
  for (const user in data) {
    if (data[user].completed) {
      if (results[data[user].userId] === undefined) {
        results[data[user].userId] = 1;
      } else {
        results[data[user].userId] += 1;
      }
    }
  }
  console.log(results);
});
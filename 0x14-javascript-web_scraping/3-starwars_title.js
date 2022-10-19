#!/usr/bin/node
// This is a script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

const request = require('request');
const cmd = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + cmd[0];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});

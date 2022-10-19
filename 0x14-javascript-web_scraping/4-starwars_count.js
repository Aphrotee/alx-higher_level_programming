#!/usr/bin/node
// This is a script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

const request = require('request');
const cmd = process.argv.slice(2);
const url = cmd[0];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let i = 0;
    let j = 0;
    let n = 0;
    let res = [];
    const ch = 'https://swapi-api.hbtn.io/api/people/18/';
    for (i = 0; i < JSON.parse(body).count; i++) {
      res = JSON.parse(body).results[i];
      for (j = 0; j < res.characters.length; j++) {
        if (res.characters[j] === ch) n++;
      }
    }
    console.log(n);
  }
});

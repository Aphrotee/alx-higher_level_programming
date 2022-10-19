#!/usr/bin/node
// This is a script that display the status code of a GET request.

const request = require('request');
const cmd = process.argv.slice(2);
const urll = cmd[0];

request(urll, function (error, response, body) {
  if (error) console.error(error); // Print the error if one occurred
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});

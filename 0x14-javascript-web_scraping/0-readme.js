#!/usr/bin/node
// This is a script that reads and prints the content of a file.

const fs = require('fs');
const cmd = process.argv.slice(2);
const filename = cmd[0];
fs.readFile(filename, 'utf-8', (err, cont) => {
  if (err) console.log(err);
  else console.log(cont.toString());
});

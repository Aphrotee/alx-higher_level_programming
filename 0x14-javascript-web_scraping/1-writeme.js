#!/usr/bin/node
// This is a script that writes to a file.

const fs = require('fs');
const cmd = process.argv.slice(2);
const filename = cmd[0];
const cont = cmd[1];
fs.writeFile(filename, cont, (err) => {
  if (err) console.log(err);
});

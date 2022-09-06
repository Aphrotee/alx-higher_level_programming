#!/usr/bin/node

const argv = process.argv;
const nargv = process.argv.length - 2;
if (nargv === 0) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}

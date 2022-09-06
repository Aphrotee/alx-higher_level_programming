#!/usr/bin/node

const argv = process.argv;

let i = 2;
if (argv.length > 3) {
  let a = parseInt(argv[2]);
  let b;
  while (i < argv.length) {
    if (parseInt(argv[i]) > a) {
      b = a;
      a = parseInt(argv[i]);
    }
    i++;
  }
  if (argv[i - 1] > b) {
    b = argv[i - 1];
  }
  console.log(b);
} else {
  console.log(0);
}

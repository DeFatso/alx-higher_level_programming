#!/usr/bin/node

function add (a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);
  const c = numA + numB;
  console.log(c);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add(arg1, arg2);

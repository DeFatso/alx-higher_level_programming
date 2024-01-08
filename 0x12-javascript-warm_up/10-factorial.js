#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const num = process.argv[2];

if (isNaN(num)) {
  console.log(1);
} else {
  const result = factorial(parseInt(num));
  console.log(result);
}

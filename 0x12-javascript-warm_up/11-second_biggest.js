#!/usr/bin/node

const index = process.argv.length - 2;
const args = process.argv.slice(2);

if (index < 2) {
  console.log(0);
} else {
  args.sort(function (a, b) {
    return a - b;
  });
  const second = args[1];
  console.log(second);
}

#!/usr/bin/node

const index = process.argv[2];

if (isNaN(index)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < index; i++) {
    let line = '';
    for (let j = 0; j < index; j++) {
      line += 'X';
    }
    console.log(line);
  }
}

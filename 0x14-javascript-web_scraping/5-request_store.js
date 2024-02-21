#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
   console.log(`Body content successfully stored in ${filePath}`);
  }
});

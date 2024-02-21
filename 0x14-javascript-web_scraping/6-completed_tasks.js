#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    const tasksData = JSON.parse(body);
    const completedTasksByUser = {};

    tasksData.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});

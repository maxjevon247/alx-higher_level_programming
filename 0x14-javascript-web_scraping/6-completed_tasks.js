#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

cons request = require('request');
const url = process.argv [2];
request(url, (error, res, body) => {
  if (error) {
    console.log(error);
  }

  const todos = JSON.parse(body);
  const data = {};

  todos.forEach((todo) => {
    if (todo.completed && data[todo.userId] === undefined) {
      data[todo.userId] = 1;
    } else if (todo.completed) {
        data[todo.userId] += 1;
    }
  });

  console.log(data);
});


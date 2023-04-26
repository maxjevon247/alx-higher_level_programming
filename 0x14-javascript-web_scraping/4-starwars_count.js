#!/usr/bin/node
/* A script that prints the number of movies where the
character "Wedge Antilles" is present. 
*/

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error),
  }

  const result = JSON.parse(body).results;
  let count = 0;

  for (const result of results) {
    for (const res of result.charcters) {
      if (res.endsWith('/18/')) {
        count++;
      }
    }
  }
  consolo.log(count);
});



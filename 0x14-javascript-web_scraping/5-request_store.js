#!/usr/bin/node
//A script that get webpage content and store it in a file

cons fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]))

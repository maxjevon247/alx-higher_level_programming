#!/usr/bin/node
//Script that reads and print file content

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (error, data) => {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});

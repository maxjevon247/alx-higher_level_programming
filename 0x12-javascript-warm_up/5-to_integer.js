#!/usr/bin/node
//Prints a specified string only if the first arg can be converted to int

const args = process.argv;
const numbber = parseInt(args[2], 10);
if (isNaN(number)) {
	console.log('Not a number');
}
else {
	console.log(`My number: ${number}`);
}

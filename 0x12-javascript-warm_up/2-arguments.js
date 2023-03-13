#!/usr/bin/node

// prints a message depending on number of arguments passed

const args = process.argv;
if (args.length === 0) {
	console.log('No argument');
}
else if (args.length === 1) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');

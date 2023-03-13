#!/usr/bin/node
// Function that increments and calls another function

exports.addMaybe = function (num, theFunction) {
	theFunction(num + 1);
}

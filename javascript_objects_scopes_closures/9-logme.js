#!/usr/bin/node
// prints the num of args and the arg

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};

#!/usr/bin/node
// reverses a list

exports.esrever = function (list) {
  let len = list.length - 1;
  for (let i = 0; i < len; i++, len--) {
    const tmp = list[i];
    list[i] = list[len];
    list[len] = tmp;
  }
  return list;
};

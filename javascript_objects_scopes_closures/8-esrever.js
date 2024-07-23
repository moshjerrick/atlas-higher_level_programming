#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  let i = 0;
  let j = 0;
  let temp = 0;
  for (i = 0, j = list.length - 1; i < j; i++, j--) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};

#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = process.argv[3]; // parseInt sera fait lors de l'appel

console.log(add(arg1, parseInt(arg2)));

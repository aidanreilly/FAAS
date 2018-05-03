'use strict';

module.exports.endpoint = (event, context, callback) => {

var http = require('http')
var fork = require('child_process').fork;

function fib(n) {
  if (n < 2) {
    return 1;
  } else {
    return fib(n - 2) + fib(n - 1);
  }
}

if (process.argv[2] == 'fib') {
  var r = fib(10);
  process.send({ result: r });
  process.exit(0);
} else {
  const result = {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {},
    "body": 'Calculated Fibonacci to 40 places using a recursive algorithm, the final calculated value is: ' + r
  }
}

  callback(null, result);
};







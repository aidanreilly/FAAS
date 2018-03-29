'use strict';

/* eslint-disable no-param-reassign */

module.exports.cFibonacci = function (context) {
  context.log('JavaScript HTTP trigger function processed a request.');

  const fibo = fib()
  for (let i=0; i<50; i++){
    console.log(fibo())
  } 
  const result = {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {},
    "body": "done"
  }

  function fib() {
  let x = 0
  let y = 1
  return function () {    
    const temp = x;
    x = x + y;
    y = temp;
    return y
  }
}

  context.res = {
    // status: 200, /* Defaults to 200 */
    body: 'Calculated Fibonacci to 50 places, last value is '(result),
  };

  context.done();
};

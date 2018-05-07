'use strict';

/* eslint-disable no-param-reassign */

module.exports.calFib = function (context) {

  const fibo = fib()
  for (let i=0; i<40; i++){
    fibo()
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
    body: 'Calculated Fibonacci to 40 places, the final calculated value is: ' + (fibo())
  };

  context.done();
};

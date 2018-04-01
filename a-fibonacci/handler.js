'use strict';

module.exports.endpoint = (event, context, callback) => {
  const fibo = fib()
  for (let i=0; i<150; i++){
    console.log(fibo())
  } 
  const result = {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {},
    "body": 'Calculated Fibonacci to 150 places, the final calculated value is: ' + (fibo())
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

  callback(null, result);
};


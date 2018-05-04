'use strict';

exports.handler = (event, context, callback) => {
  //https://hackernoon.com/aws-lambda-go-vs-node-js-performance-benchmark-1c8898341982
  for (let i=0; i<30; i++){
    console.log(fib(i))
  } 

  const result = {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {},
    "body": 'Calculated Fibonacci to 150 places, the final calculated value is: '
  }

  function fib(n) {
    if(n > 1){
      return fib(n-1) + fib(n-2)
    } else {
      return n;
    }
  }
  
  callback(null, result);
};


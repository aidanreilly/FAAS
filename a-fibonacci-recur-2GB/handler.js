'use strict';

module.exports.endpoint = (event, context, callback) => {
  //https://hackernoon.com/aws-lambda-go-vs-node-js-performance-benchmark-1c8898341982
  //https://stackoverflow.com/questions/11455430/javascript-storing-for-loop-result
  var fibOut = [];
  for (let i=0; i<40; i++){
    fibOut.push(fib(i))
  } 

  const result = {
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {},
    "body": 'Calculated Fibonacci to 40 places with recursion (2GB RAM), the final calculated value is: ' + (fibOut[39])
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
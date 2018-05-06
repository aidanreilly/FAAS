'use strict';

exports.http = (request, response) => {

  var fibOut = [];
  for (let i=0; i<40; i++){
    fibOut.push(fib(i))
  } 

  function fib(n) {
    if(n > 1){
      return fib(n-1) + fib(n-2)
    } else {
      return n;
    }
  }

  response.status(200).send('Calculated Fibonacci to 40 places using recursion, the final calculated value is: ' + String(fibOut[39]));
};

exports.event = (event, callback) => {
  callback();
};
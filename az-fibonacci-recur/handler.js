'use strict';

/* eslint-disable no-param-reassign */

module.exports.calFibRecur = function (context) {

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


  context.res = {
    // status: 200, /* Defaults to 200 */
    body: 'Calculated Fibonacci to 40 places using recursion, the final calculated value is: ' + (fibOut[39])
  };

  context.done();
};

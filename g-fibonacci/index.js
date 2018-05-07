'use strict';

exports.http = (request, response) => {

  const fibo = fib()
  for (let i=0; i<40; i++){
    fibo()
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

response.status(200).send('Calculated Fibonacci to 40 places, the final calculated value is: ' + String(fibo()));
};

exports.event = (event, callback) => {
  callback();
};
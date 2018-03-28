'use strict';

module.exports.endpoint = (event, context, callback) => {
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

  callback(null, result);
};


'use strict';

/* eslint-disable no-param-reassign */

module.exports.calcFibonacci = function (context) {
  context.log('JavaScript HTTP trigger function processed a request.');

  context.res = {
    // status: 200, /* Defaults to 200 */
    body: 'Argh',
  };

  context.done();
};

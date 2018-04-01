Hello world AWS example in NodeJS to calculate Fibonacci to 1500 places
layout: Doc
-->

## Function load test

- Calculates fibonacci to 150 places

## Invoke the function locally

```bash
serverless invoke local --function calculateFibonacci
```

## Deploy

In order to deploy the you endpoint simply run

```bash
serverless deploy
```

## Usage

You can now invoke the function directly and even see the resulting log via

```bash
serverless invoke --function calculateFibonacci --log
```

or as send an HTTP request directly to the endpoint using a tool like curl

```bash
curl https://61y5mcy9j7.execute-api.us-east-1.amazonaws.com/dev/ping


```
Needs curl and abs obvs
```bash
abs -k -c 20 -n 250 https://61y5mcy9j7.execute-api.us-east-1.amazonaws.com/dev/ping

```
Originally described:
https://hackernoon.com/aws-lambda-go-vs-node-js-performance-benchmark-1c8898341982

## Scaling

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

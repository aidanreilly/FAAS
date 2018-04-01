### Deploying the service

Once your credentials are set, you can immediately deploy your service via the following command:

```shell
serverless deploy
```

This will create the necessary resources to support the service and events that are defined in `serverless.yml`.

### Invoking and inspecting a function

With the service deployed, you can test it's functions using the following command:

```shell
serverless invoke -f 
```

Additionally, if you'd like to view the logs that a function generates (either via the runtime, or create by your handler by calling `context.log`), you can simply run the following command:

```shell
serverless logs -f calcFibonacci
```

### Cleaning up

Once you're finished with your service, you can remove all resources by simply running the following command:

```shell
serverless remove
```

###Testing

https://cfibonacci.azurewebsites.net/api/calcFibonacci

serverless invoke local --function calcFibonacci

https://az-fibonacci.scm.azurewebsites.net/DebugConsole
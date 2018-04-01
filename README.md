### Load testing identical functions on AWS, Google Cloud, and Azure

All functions are hosted out of EU-West (Ireland) data centers.

Each service can be deployed with serverless: 

```shell
serverless deploy
```

This will create the necessary resources to support the service and events that are defined in `serverless.yml`.

### Invoking and inspecting a function

When the service is deployed, test using the following command:

```shell
serverless invoke -f 
```

Additionally, if you'd like to view the logs that a function generates (either via the runtime, or create by your handler by calling `context.log`), you can simply run the following command:

```shell
serverless logs -f <your-servce>
```

### Cleaning up

Once you're finished with your service, you can remove all resources by simply running the following command:

```shell
serverless remove
```

###Testing
* Google cloud: https://us-central1-go-fibonacci.cloudfunctions.net/http
* AWS: https://v78v2mvnb5.execute-api.eu-west-1.amazonaws.com/dev/ping
* Azure: https://calfibonacci.azurewebsites.net/api/calcFibonacci

Test using curl and abs: 

serverless invoke local --function <your-service> --log

```bash
abs -k -c 20 -n 250 https://61y5mcy9j7.execute-api.us-east-1.amazonaws.com/dev/ping

```

To execute the locally installed Serverless executable you have to reference the binary out of the node modules directory.

Example:

node ./node_modules/serverless/bin/serverless deploy


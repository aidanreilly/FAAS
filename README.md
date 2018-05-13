### Load testing identical functions on AWS, Google Cloud, and Azure

Each function calculates the fibonacci sequence to 40 places. All functions are hosted in US East or US central data centers. Data center locations:

* AWS: US-East-1
* Google-Cloud: US-Central1 
* Azure: East US

*Note*: Google cloud is (at time of testing) only available in the central-US region. Azure and AWS functions are hosted in similar US locations to ensure comparable latency when testing.   

Services are deployed with the serverless framework: https://serverless.com/ 

The necessary resources to support the service and events are defined in serverless.yml for each function.

### Invoking and inspecting a function

When the service is deployed, test using the following command:

```shell
serverless invoke -f <your-servce>
```

Additionally, if you'd like to view the logs that a function generates (either via the runtime, or create by your handler by calling context.log), you can simply run the following command:

```shell
serverless logs -f <your-servce>
```

### Cleaning up

Once you're finished with your service, you can remove all resources by simply running the following command:

```shell
serverless remove
```

### Testing

*Google cloud* 
* Linear function https://us-central1-go-fibonacci.cloudfunctions.net/http
* Recursive function, 256 MB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http
* Recursive function, 512 MB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-512
* Recursive function, 1 GB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB
* Recursive function, 2 GB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-2GB

*AWS*
* Linear function https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping
* Recursive function, 256 MB https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping
* Recursive function, 512 MB https://0qwlklexf2.execute-api.us-east-1.amazonaws.com/dev/ping
* Recursive function, 1 GB https://1fd9j85pbj.execute-api.us-east-1.amazonaws.com/dev/ping
* Recursive function, 2 GB https://l1zp09xozj.execute-api.us-east-1.amazonaws.com/dev/ping

*Azure* 
* Linear function https://calfibonacci.azurewebsites.net/api/calcFibonacci
* Recursive function https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci
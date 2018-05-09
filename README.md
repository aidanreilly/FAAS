### Load testing identical functions on AWS, Google Cloud, and Azure

Each function calculates the fibonacci sequence to 150 places when it is invoked. All functions are hosted out of US East or US central data centers. Data center locations:

* AWS: US-East-1
* Google-Cloud: US-Central1 
* Azure: East US

VM login

aidan_reilly
0{1B)PC(t>}#taC

AWS
User name   Administrator
Password    
LF8ti3Tx39*

Azure
aidan-admin
Hotbooty1234

g
aidan_reilly
).mZ=mhS$x~8gUH

https://cloud.google.com/about/locations/?region=americas#region

*Note*: Google cloud is (at time of testing) only available in the central-US region. Azure and AWS functions are hosted in similar US locations to ensure comparable latency.   

Each service can be deployed with serverless: 

```shell
serverless deploy
```

This creates the necessary resources to support the service and events that are defined in `serverless.yml`.

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
Google cloud: 
* simple https://us-central1-go-fibonacci.cloudfunctions.net/http
* 256 MB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http
* 512 MB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-512
* 1 GB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB
* 2 GB https://us-central1-go-fibonacci-recur.cloudfunctions.net/http-1GB

AWS: 
* simple https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping
* 256 MB https://k9kec8cpgc.execute-api.us-east-1.amazonaws.com/dev/ping
* 512 MB https://0qwlklexf2.execute-api.us-east-1.amazonaws.com/dev/ping
* 1 GB https://1fd9j85pbj.execute-api.us-east-1.amazonaws.com/dev/ping
* 2 GB https://l1zp09xozj.execute-api.us-east-1.amazonaws.com/dev/ping

Azure: 
* https://calfibonacci.azurewebsites.net/api/calcFibonacci
* https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci

Azure automatically scales the function depending on demand. The container size setting is a hold-over from an early preview of Azure Functions where you had to set the memory limit of your function and that setting was what determined how you were billed. If you'd like some more context on the change that happened see this post. The fact that its still present in our REST API is just an API cleanup issue. The important thing to note is that this setting is not honored any more. Instead you are billed for your actual memory usage. The closest thing we have to an enforced limit is that you can specify a max daily GBsec. This feature is in the settings tab.

abs -k -c 20 -n 250 https://calfibonacci.azurewebsites.net/api/calcFibonacci



```bash
abs -k -c 20 -n 20 https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping
abs -k -c 20 -n 250 https://8s6r4ur3g6.execute-api.us-east-1.amazonaws.com/dev/ping

```


https://calfibonacci.azurewebsites.net/api/calcFibonacci
https://calfibonacci.azurewebsites.net/api/DebugConsole

Test using curl and abs: 

serverless invoke local --function <your-service> --log

```bash
abs -k -c 20 -n 250 https://g8h74so6w0.execute-api.us-east-1.amazonaws.com/dev/ping
abs -k -c 20 -n 250 https://8s6r4ur3g6.execute-api.us-east-1.amazonaws.com/dev/ping

abs -k -c 20 -n 250 https://calfibonacci.azurewebsites.net/api/calcFibonacci
abs -k -c 20 -n 250 https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci

abs -k -c 20 -n 250 https://us-central1-go-fibonacci.cloudfunctions.net/http
abs -k -c 20 -n 250

```

C:\xampp\apache\bin\abs.exe -k -c 20 -n 250 https://calfibonaccirecur.azurewebsites.net/api/calcFibonacci > az-local20.txt

To execute the locally installed Serverless executable you have to reference the binary out of the node modules directory.

Example:

```bash
node ./node_modules/serverless/bin/serverless deploy

```

https://console.cloud.google.com/appengine/taskqueues/cron?project=go-fibonacci

#Changing projects on gcloud

the gcloud project must be switch

Azure uses two models for scaling, consumption plan and app servcies plan
https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale

https://devops.stackexchange.com/questions/255/how-to-performance-test-aws-lambda-functions/259
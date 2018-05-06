simple cron job for google cloud function.
based on:
https://medium.com/@earlg3/google-cloud-functions-scheduled-trigger-915b5fb8310f

https://console.cloud.google.com/appengine/taskqueues/cron?project=go-fibonacci
    
    gcloud init

change to go-fibonacci project
  
    gcloud app deploy app.yaml C:\git\FAAS\google-cron\cron.yaml

from cmd to see logs:

    gcloud app logs tail -s default 
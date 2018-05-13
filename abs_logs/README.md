AWS tested on Win Server 2012 hosted in same location on AWS
GCloud tested on same location in GCloud
AZ tested on same location on AWS  - need ot redo this one.

All tested Sunday/Moday may bank holiday weekend.

https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html

Amazon hits concurrency limitts at 1000.
Account Level Concurrent Execution Limit
By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 1000. You can view the account level setting by using the GetAccountSettings API and viewing the AccountLimit object. This limit can be raised as described below:
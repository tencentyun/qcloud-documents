## 1. Preparations
Complete the preparatory work as instructed in [Preparations](https://cloud.tencent.com/document/product/599/10548), and understand how to configure the general parameters of custom information.

## 2. View and Modify Demo
Open file 1_SimpleStart.py with an editor.
```
 # custom (Change to your info)
imageId = "img-m4q71qnf"
Application = {
    "DeliveryForm": "LOCAL",
    "Command": " python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "
}
secretId_COS = "your secretId"
secretKey_COS = "your secretKey"
StdoutRedirectPath = "your cos path"
StderrRedirectPath = "your cos path"
```
In custom information, all parameters are described in "Preparations" except Application which is explained below：  
* DeliveryForm: Three delivery methods of applications are available: software packaging, container image, directly running within the CVM. In this case, LOCAL indicates directly running within the CVM.  
* Command: Task startup command. Here, we run a Python script, starting with 1. Add up the first 20 numbers of Fibonacci sequence and output the sum to StdOutput.

1_SimpleStart.py is simple and can be directly executed by modifying the general parameters according to Preparations. So, no further modification is needed here.

## 3. Submit Job
The job submission process has been encapsulated in Demo in the form of Python script plus the internal trial version of Batch command line tool. So, you only need to run the Python script according to the following example.
```
$ python 1_SimpleStart.py
{
    "Response": {
        "RequestId": "d069ce2f-abfc-451f-81fd-9327dbf5cf39",
        "JobId": "job-clump52n"
    }
}
```

If JobId field is returned, the job is submitted successfully. Otherwise, check the returned value for troubleshooting, or join the chat group in [User Report](https://cloud.tencent.com/document/product/599/10806) to make a inquiry to admin.

## 4. View the Status

```
$ qcloudcli batch DescribeJob  --Version 2017-03-12 --JobId job-xxx
```
View the running status through DescribeJob. Replace --JobId with the actual JobID. Common statuses are as follows:  
* STARTING  Launching  
* RUNNING   Running  
* SUCCEED   Run successfully  
* FAILED    Failed to run

The complete returned message is as follows:

```
{
    "Response": {
        "JobState": "STARTING",
        "Zone": "ap-guangzhou-2",
        "JobName": "SimpleStart",
        "Priority": 1,
        "RequestId": "8e5ef77c-fa41-4b9f-8c80-107f2546e8ed",
        "TaskSet": [
            {
                "TaskName": "Task1",
                "TaskState": "STARTING"
            }
        ],
        "JobId": "job-n4ohivif",
        "DependenceSet": []
    }
}
```

## 5. View the Result

The result is stored in StdoutRedirectPath and StderrRedirectPath directories configured in Preparations. See below for the result.

![](https://mc.qcloudimg.com/static/img/1038bd36c2c897f7241643995757dd7f/COS_4.png)

View the standard output stdout.job-xxx.xxxx.0.log for a successful operation. The content is as below:  
```
6765
```

View the standard error stderr.job-xxx.xxxx.0.log in case of a failure. The content may be as below:
```
/bin/sh: -c: line 0: syntax error near unexpected token `('
/bin/sh: -c: line 0: ` python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" '
```




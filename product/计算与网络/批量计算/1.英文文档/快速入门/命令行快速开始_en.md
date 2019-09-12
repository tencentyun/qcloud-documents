
## A Simple Example
This example describes how to use command line to submit a simple job. Here, Fibonacci sequence summation is implemented using Python. The code is directly input in the command configuration of the task provided by Batch. Then, the result is directly output to the output address stdout of the task configuration.

## Preparation Before Start
Be prepared according to the checklist in the document [Preparation Before Start](
/doc/product/599/10807) before start. Command line tool (CLI) and cloud object storage (COS) are required in this example. Thus, you need to install and configure CLI, and create a COS bucket.

### Installing and Configuring CLI
For more information on how to configure CLI, please see [Configure Command Line Tool](/doc/product/440/6184). After installation, check whether the CLI is installed successfully.
```
qcloudcli batch help

DescribeAvailableCvmInstanceTypes       	|DescribeTask
DescribeJob                             	|SubmitJob
DescribeJobs                            	|TerminateTaskInstance
```

### Creating a COS Bucket to Store Result

In this simple example, the result is directly output to the system standard output. Then, Batch collects the data of system standard output stdout and stderr, and uploads the information to the COS Bucket you specified when the task is completed. You need to prepare a bucket and a subfolder in advance to store information.

See section 3 **"Prepare COS Directory"** in [Command Line Tool -> Preparations](/doc/product/599/10548) chapter, to create a corresponding COS bucket and a subfolder.

## Job Configuration

You can configure a Batch job that can be executed with your account by modifying the official example. Before this, you need to know the meaning of each configuration item of a job.

```
qcloudcli batch SubmitJob --Version 2017-03-12 --Job '{
    "JobName": "TestJob",       // Job name
    "JobDescription": "for test ",    // Job description
    "Priority": "1",            // Job priority
    "Tasks": [                  // Task list (this example only contains one task)
        {
            "TaskName": "Task1",   // Name of task 1
            "Application": {        // Task execution command
                "DeliveryForm": "LOCAL",    // Execute local command
                "Command": "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "   // Command content (Fibonacci summation)
            },
            "ComputeEnv": {         // Computing environment configuration
                "EnvType": "MANAGED",   // Computing environment types: MANAGED and UNMANAGED
                "EnvData": {        // Detailed configuration (the current type is MANAGED. See description of CVM instance creation)
                    "InstanceType": "S1.SMALL1",    // CVM instance type
                    "ImageId": "img-m4q71qnf",      // CVM image ID (to be replaced)
                }
            },
            "RedirectInfo": {       // Configuration of standard output redirection           
                "StdoutRedirectPath": "cos://dondonbatchv5- 1251783334.cosgz.myqcloud.com/logs/",  // Standard output (to be replaced)
                "StderrRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/"    // Standard error (to be replaced)
            },
            "Authentications": [        // Authentication information
                {
                    "Scene": "COS",     // Scenario (COS is set currently)
                    "SecretId": "***",  // SecretId (to be replaced)
                    "SecretKey": "***"  // SecretKey (to be replaced)
                }
            ]
        }
    ]
}'
--Placement'{
    "Zone": "ap-guangzhou-2"    // Availability zone (may be replaced)
}'
```

The command SubmitJob of Batch contains 3 parameters.
* **Version**: Version number. Currently, it is always entered with 2017-03-12.
* **Job**: Job configuration (in JSON format). For more information, please see the example.
* **Placement**: Availability zone where a job is executed.

``* 1. The job can be executed only when the fields marked to be replaced in it are replaced with your own information, such as custom image Id, VPC-related information, COS Bucket address and corresponding SecretId and SecretKey.``

``* 2. The above example contains annotations, thus cannot be directly executed in CLI. Copy the example below, and enter the fields to be entered before execution. Since the command is long, click the copy button at the right side of the box to prevent incomplete duplication.``

``* 3. For more information on Job configuration, please see ``[Job Configuration](https://cloud.tencent.com/document/product/599/11040)``.``

```
qcloudcli batch SubmitJob --Version 2017-03-12  --Job '{"JobName": "TestJob",  "JobDescription": "for test", "Priority": "1", "Tasks": [{"TaskName": "Task1",  "TaskInstanceNum": 1,  "Application": {"DeliveryForm": "LOCAL", "Command":  "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "},  "ComputeEnv": {"EnvType":  "MANAGED", "EnvData": {"InstanceType": "S1.SMALL1",  "ImageId": "img-m4q71qnf" }  }, "RedirectInfo": {"StdoutRedirectPath": "To be replaced", "StderrRedirectPath":   "To be replaced"}, "MaxRetryCount":  1, "Authentications": [{"Scene": "COS", "SecretId":   "To be replaced", "SecretKey":  "To be replaced"} ] } ] }' --Placement '{"Zone": "ap-guangzhou-2"}'
```

### Modify Configuration

#### 1. Enter ImageId
```"ImageId": "To be replaced"```

A configured Cloud-init service-based image is needed for internal trial. A CentOS 6.5 image (ID: img-m4q71qnf) that is officially provided can be used directly.

#### 2. Configure StdoutRedirectPath and StderrRedirectPath
```"StdoutRedirectPath": "To be replaced", "StderrRedirectPath":   "To be replaced"```

Enter the access address of the COS Bucket you created in Preparations in StdoutRedirectPath and StderrRedirectPath.

#### 3. Configure the API Key Information for Accessing COS
```"SecretId":   "To be replaced", "SecretKey":  "To be replaced"```

Replace SecretId and SecretKey under Authentications with those of the account you used to create COS Bucket in Preparations.

#### 4. Modify Availability Zone (Optional)
```
--Placement '{"Zone": "ap-guangzhou-2"}'
```

In this example, we specify Guangzhou Zone 2 as the region where you apply for resources. You can select an availability zone in the default region you configured in CLI to apply for resources. For more information on regions and availability zones, please see [Region and Availability Zone](/doc/product/213/6091).

#### 5. Enter JSON Data in Windows CLI (Optional)
To differentiate with Linux, you need to enter the JSON data in Windows CLI. For example, replace " with \". For more information, please see the section "Use JSON Data as Input Parameter" in [Get Started with Tencent Cloud Command Line Tool](/doc/product/440/6185).

## View the Result

```
{
    "Response": {
        "RequestId": "5d928636-bba2-4ab3-bef3-cf17d7c73c51",
        "JobId": "job-1rqdgnqn"
    }
}
```
If JobID is returned, the job is successfully executed.

```
$ qcloudcli batch DescribeJob  --Version 2017-03-12 --JobId job-1z4yl2bp
{
    "Response": {
        "JobState": "STARTING",
        "Zone": "ap-guangzhou-2",
        "JobName": "test job",
        "Priority": 1,
        "RequestId": "b116f9b5-410c-4a69-bbe8-b695a2d6a869",
        "TaskSet": [
            {
                "TaskName": "hello2",
                "TaskState": "STARTING"
            }
        ],
        "JobId": "job-1z4yl2bp",
        "DependenceSet": []
    }
}
```
You can view the task information you just submitted using DescribeJob.

```
$ qcloudcli batch DescribeJobs  --Version 2017-03-12
```
You can also view the job list in the current region with DescribeJobs.

## What's Next?

In this simplest example, the job only contains a single task. It does not use remote storage mapping, but only shows the most basic capabilities. You can continue to test higher level of capacities of Batch by following the API documentation.

* **Easy to use**: Batch is powerful and features many configuration items. It is fast and convenient to call Batch using script. Try this method by referring to [Preparations](/doc/product/599/10548) and [1_Simple Start](/doc/product/599/10551).

* **Execute remote code package**: Technically, Batch can fully satisfy your business needs by combining **custom image and remote code package and command line**. For more information, please see [2_Execute Remote Code Package](/doc/product/599/10552).

* **Remote storage mapping**: Batch optimizes the storage access by simplifying the access to remote storage service to an operation on local file system. For more information, please see [3_Remote Storage Mapping](/doc/product/599/10983).

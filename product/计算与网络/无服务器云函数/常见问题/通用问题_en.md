## Common Questions
### What is SCF?
Tencent Cloud Serverless Cloud Function (SCF) is a serverless execution environment provided by Tencent Cloud. You simply need to compose simple cloud functions with sole purposes, then associate them with your Tencent Cloud infrastructures and events created by other cloud services.
Users only need to focus on their own code when using cloud functions. Underlying computing resources, including server CPU, memory, network, and other configuration/resource maintenance works such as code deployment, auto scaling, load balancing, security update, resource operation status monitoring, are completely handled by Tencent Cloud. Users only need to provide their code using languages supported by the platform (currently supported language is Python). This also means that you cannot log in to or manage the servers, or customize system/environment.

Auto scaling is performed by underlying cloud function components based on the number of requests when code is executed, achieving service availability and stability under various scenarios with different request volume (from several requests per day to thousands of requests per second), without the need for any manual configuration and intervention. Cloud functions are automatically deployed in multiple availability zones in the region, providing extremely high disaster tolerance. Users only need to pay for running cloud functions. Code does not incur any service fee when not running.

You can customize when to execute your code. For example, when a file is uploaded to or deleted from a COS Bucket, when an application calls the code through SDK, or specify the code to be executed periodically. For this reason, you can use SCF as data process trigger program for COS services and realize IFTTT logic with ease. You can also construct flexible, periodical automated tasks to replace manual operations, creating a flexible and controllable software structure.

### What is serverless computing?

With serverless computing, you can build and run applications and services without the need to worry about the server. Serverless doesn't necessarily mean that there is no server. It is just that users no longer need to be concerned about these underlying resources. Of course, this also means that users cannot log in to the servers and do not need to think about server optimization. Developers only need to focus on the most important code segments, while skipping all the other complicated and boring works. The code is completely event-triggered. The platform automatically adjusts service resources in a balanced manner based on the number of requests, with almost no expansion limit. No resource is run when idle. Stateless code execution allows quick iteration and deployment. SCF is the core of Tencent Cloud serverless computing, which allows you to run code without the need to pre-configure or manage the server.
### Which events can trigger SCF?

Currently, three trigger methods are supported: manual trigger (API), timed trigger and COS trigger.

### What languages does SCF support?

Currently, SCF only supports Python 2.7.

### Can I access the infrastructure where SCF is running?

No. SCF runs and manages computing infrastructure on your behalf.

### How does SCF isolate the code?

Each function that is running in a unique environment has its own resources and file system. SCF uses the same technology as CVM to provide security and isolation at infrastructure and execution level.

## Serverless Cloud Function
### What is Serverless Cloud Function?

The code running on SCF is uploaded in the form of "serverless cloud function". Each function has corresponding configuration information, such as name, description, resource requirements, and so on. The code must be written in a "stateless" format, that is, it should be assumed that there is no close relationship with the underlying computing infrastructure. Local file system access, sub-processes are strictly controlled within the lifecycle of the cloud function. Any persistent statuses should be stored in an available external storage, such as COS or CDB. SCF can include an external library or even a local host library.

### Does SCF use function instance repeatedly?

To improve performance, SCF retains your function instance for a certain period of time and use it for subsequent requests. However, for your code, this operation is not supposed to be performed frequently.

### What is the local storage form of serverless cloud function?

Each function has `500 MB` non-persistent disk space in its own directory `/tmp`. At the end of the function's lifecycle, the files in this space are not stored.

### Why should I keep serverless cloud function stateless?

Statelessness allows the function to start as many instances as possible based on actual needs to respond to the requests rapidly.

### Can I use threads and processes in the function code?

Yes. You can use common languages and operating system features, such as creating additional threads and processes. Resources allocated to functions, including memory, execution time, disk and network, are shared through all threads/processes they use.

### Which restrictions apply to the function code?

We try not to impose restrictions on common languages and operating system activities. However, some activities are still disabled. For example: Inbound network connection is disabled

### How to create a serverless cloud function using CLI?

You can package the code (and any dependent library) into a zip file and upload it from local environment using CLI. The uploaded content must be no more than 5 MB.

### How to troubleshoot?

SCF integrates the log feature. Once the function is called, the log of this call is outputted to the log window in the console. The log records the resources resumed in each call, log in the code, call information of platform and so on, so that you can easily insert the troubleshooting-related log statement into the code.

### The function code is not displayed in the details page after the function is created by uploading zip file.
It is generally because the execution method is incorrect, or the outer folder is also compressed into the zip file. The format of execution method is `a.b`. "a" is the name of the py file, and "b" is the method name in code.
If the file named `a.py` cannot be found in the root directory that is decompressed from the zip file you uploaded, a prompt message indicating "Cannot display the function code. Cannot find the file name specified by the execution method in the code zip file" is shown.

For example: The file structure is as follows

--RootFolder
----SecondFolder
------a.py
------thirdfolder
--------sth.json

When you compress the code into a zip file, the above error occurs if the SecondFolder is compressed. You need to compress `a.py` or ` thirdfoler`.

### Why the execution time of the same code is similar regardless of memory size?
In the internal trial phase, we assign the same computing resources (i.e., the number of container cores and the memory size are fixed) for each of user's function instances, and proportionally assign the resources based on the selected memory size during public trial phase.

### How to deal with timeout?
Set a larger value to timeout (no more than 300) and test again. If timeout remains unchanged, please check whether your code log has excessive input data and a huge calculation amount, a loop that cannot be broken out of, a long time sleep, etc.

### How to expand capacity?

You don't need to worry about capacity expansion/reduction which is automatically completed by SCF platform. SCF can quickly locate the idle capacity and execute your code whenever a function request is received. Since your code is stateless, you can launch instances as many as possible when needed without lengthy deployment and configuration delay.

### How to assign function computing resources?
You can select the amount of memory allocated to the function, and the CPU and other resources are allocated proportionally. For example, when 256 MB memory is selected, the CPU allocated to the function is about twice that to 128 MB memory.

### Can I use local library?

Yes. You can include your codebase into the function code and upload it to platform in the format of zip file.
## Event Handling
### What is event source?

Event source is an application created by a certain Tencent Cloud service or developers to generate events that can trigger SCF.

### What are the event sources?

Currently, three trigger methods are supported: manual trigger (API), timed trigger and COS trigger.


### How does the application trigger a function directly?

You can call the Invoke API of SCF to trigger a function directly. Only the owner of the function can call it directly.

### What happens to the delay when function responds to an event?

Generally, SCF can process request and response within milliseconds. However, the delay increases during the creation and update of a function, or if it has not been used recently.


## Scalability and availability
### How is the availability of SCF?

SCF provides high availability through cross-region deployment, replication and redundancy.

### Can I use SCF when changing code or configuration?

Yes. There is a short window period (generally less than 1 min) when the function is updated, during which the request is implemented by the old function code or the new function code.

### Is there a limit to the number of single-run functions?

SCF supports a large number of function instances running in parallel. However, we set a default security threshold: up to 100 concurrent executions per function.

### What happens when a function fails to handle an event?
When a failure occurs, the function called synchronously returns exception information. The function called asynchronously automatically is called another 3 times at the backend automatically.

## Common Questions
### What is SCF?
Tencent Cloud Serverless Cloud Function (SCF) is a serverless execution environment provided by Tencent Cloud. You simply need to compose simple cloud functions with a sole purpose, and then associate them with your Tencent Cloud infrastructures and events created by other cloud services.
You only need to focus on the codes when using SCF. Tencent Cloud completely manages the underlying computing resources, including server CPU, memory, network, and other configuration/resource maintenance, code deployment, auto scaling, load balancing, security update, and resource operation status monitoring. You only need to provide codes using languages supported by the platform (currently supported language is Python). This also means that you cannot log in to or manage the servers, or customize system/environment.

Auto scaling is performed by underlying SCF components based on the number of requests when code is run, achieving service availability and stability under various scenarios with different request volume (from several requests per day to thousands of requests per second), without the need for any manual configuration and intervention. SCFs are automatically deployed in multiple availability zones in the region, which enables extremely high fault tolerance. You only need to pay for the running cloud functions. There is no charge when your code is not running.

You can set to run your code when a file is uploaded to or deleted from a COS Bucket, or when an application calls the code through SDK, or at regular intervals. For this reason, you can use SCF to trigger data processing for COS services and easily implement IFTTT logic. You can also construct flexible and periodical automated tasks to replace manual operations, creating a flexible and controllable software structure.

### What is serverless computing?

With serverless computing, users can build and run applications and services without thinking about servers. Serverless does not mean that there is no server involved. It just means users don't need to manage the underlying resources. This also means that users cannot log in to servers and do not need to consider optimizing them. Developers only need to focus on the most important code snippets and skip complicated and boring work. The code is completely event-triggered. The platform automatically adjusts service resources in a balanced manner based on the number of requests, with virtually unlimited capacity expansion capability. No resource is running when idle. Stateless code running allows quick iteration and deployment. SCF is the core of Tencent Cloud serverless computing, which allows you to run codes without the need to pre-configure or manage servers.

### Which events can trigger SCF?

Currently, manual trigger (API), timed trigger, COS trigger, CMQ trigger, and API gateway trigger are supported. More trigger methods will be available soon.

### What languages does SCF support?

Currently, SCF supports Python 2.7 & 3.6, Node.js 6.10 & 8.9, Java 8, and PHP 5 & 7. More languages will be supported soon.

### Can I access the infrastructure where SCF is running?

No. SCF runs and manages your computing infrastructure on your behalf.

### How does SCF isolate codes?

Each function is running in a unique environment and has its own resources and file systems. SCF uses the same technology as CVM to provide security and isolation at the infrastructure and execution level.

## Serverless Cloud Function

### What is SCF?

Codes running on SCF are uploaded in the format of "serverless cloud function". Each function contains relevant configuration information, such as name, description and resource requirements. Codes must be written in a "stateless" format. That is, it should be assumed that there is no close relationship with the underlying computing infrastructure. Local file system access and sub-processes are strictly controlled within the SCF lifecycle. Any persistent statuses should be stored in an available external storage, such as COS or CDB. SCF can include an external library or even a local host library.

### Does SCF use function instances repeatedly?

To improve performance, SCF retains your function instances for a certain period of time and uses them for subsequent requests. However, for your codes, this operation is not supposed to be performed frequently.

### What is the local storage form of SCF?

Each function has `500 MB` non-persistent disk space in its own directory `/tmp`. At the end of a function's lifecycle, the files in this space are not stored.

### Why should I keep SCF stateless?

Statelessness allows the function to start as many instances as possible based on actual needs to respond to the requests rapidly.

### Can I use threads and processes in function codes?

Yes. You can use common languages and operating system features, such as creating additional threads and processes. Resources assigned to functions, including memory, execution time, disk and network, are shared through all threads/processes they use.

### Which restrictions apply to function codes?

We try not to impose restrictions on common languages and operating system events. However, some events may still be disabled. For example, for function codes, inbound network connection is blocked.

### How can I create a serverless cloud function using CLI?

You can package the code (and any dependent library) into a zip file and upload it from local environment using CLI, or you can pull the Bucket name and file name of the zip package when creating functions after the zip file is uploaded to COS Bucket.

### How can I troubleshoot issues?

SCF integrates the log feature. Once a function is called, the log of this call is outputted to the log window in the console. The log records the resources consumed in each call, log in the codes, and calling information in the platform, so that you can easily insert the troubleshooting-related log statements into codes.

### Why is the function code not displayed in the details page after a function is created through an uploaded zip file?
This is generally because the execution method is incorrect, or the outer folder is also compressed into the zip file. The format of the execution method is `a.b`. "a" is the name of the py file, and "b" is the method name in the code.
If the file named `a.py` cannot be found in the root directory that is decompressed from the zip file you uploaded, a prompt message indicating "cannot display the function code and cannot find the file name specified by the execution method in the code zip file" is shown.

For example, the file structure is as follows:

--RootFolder
----SecondFolder
------a.py
------thirdfolder
--------sth.json

When you compress the code into a zip file, the above error may occur if the SecondFolder is compressed. You need to compress `a.py` or ` thirdfolder`.

### Why is the execution time of the same code similar regardless of the memory size?

In the public trial phase, the same computing resources (fixed number of container cores) are assigned for each function instance. After the public trial, the resources are proportionally assigned based on the selected memory size.

### How can I deal with timeout?

Set a larger value to timeout (no more than 300) and test again. If timeout still occurs, check your code log for any excessive input data, huge calculation amount, a loop that cannot be broken out of, or long sleep time.

### How can I expand capacity?

You don't need to worry about capacity expansion/reduction, which is automatically completed by the SCF platform. SCF can quickly locate the idle capacity and run your codes whenever a function request is received. Since your code is stateless, you can launch instances as many as possible when needed without any redundant deployment and configuration delay.

### How can I assign function computing resources?

You can select the memory for the function and the CPU and other resources are assigned proportionally. For example, when you select 256 MB memory, the CPU assigned to the function is about twice that to 128 MB memory.

### Can I use the local library?

Yes. You can include your code base into the function code and upload it to the platform in the format of zip file.

## Event Handling

### What is event source?

Event source is an application created by a certain Tencent Cloud service or developers to generate events that can trigger SCF.

### What are the event sources?

Currently, manual trigger (API), timed trigger, COS trigger, CMQ Topic trigger, API gateway trigger, Ckafka trigger are supported. More trigger methods will be available soon.

### How does the application trigger a function directly?

You can call the Invoke API of SCF to trigger a function directly. Only the function owner or users with the permission to call Invoke API can call the function.

### How long is the delay when a function responds to an event?

Generally, SCF can process requests and respond within milliseconds. However, the delay may increase when a function is being created or updated, or if it has not been called recently.

## Scalability and Availability

### How is the availability of SCF?

SCF provides high availability through cross-region deployment, replication and redundancy.

### Is SCF still available when I change codes or configurations?

Yes. There is a short window period (generally less than 1 min) when a function is updated, during which the request is implemented by the old function code or the new function code.

### Is there a limit to the number of functions that can be run at a time?

SCF supports a large number of function instances running concurrently. However, we set a default security threshold: up to 20 concurrent executions per function. You can submit a ticket to increase the threshold.

### What happens when a function fails to handle an event?

When a failure occurs, the function called synchronously returns exception information. The function called asynchronously is retried automatically for another 3 times at the backend.


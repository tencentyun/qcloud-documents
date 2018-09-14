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
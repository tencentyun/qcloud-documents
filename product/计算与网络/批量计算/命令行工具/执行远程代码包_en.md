Batch allows you to obtain code package from .tgz file via HTTP. You can compress the code and upload it to COS. This can help you organize the code more conveniently than using LOCAL mode.

## 1. Preparations
Complete the preparatory work as instructed in [Preparations](https://cloud.tencent.com/document/product/599/10548), and understand how to configure the general parameters of custom information.

## 2. View and Modify Demo
Open file 2_RemoteCodePkg.py with an editor.
```
 # custom (Change to your info)
imageId = "img-m4q71qnf"
Application = {
    "DeliveryForm": "PACKAGE",
    "Command": "python ./codepkg/fib.py",
    "PackagePath": "http://batchdemo-1251783334.cosgz.myqcloud.com/codepkg/codepkg.tgz"
}
secretId_COS = "your secretId"
secretKey_COS = "your secretKey"
StdoutRedirectPath = "your cos path"
StderrRedirectPath = "your cos path"
```
In custom information, all parameters are described in "Preparations" except Application which is explained below.
* DeliveryForm: Three delivery methods of applications are available: software packaging, container image, directly running within the CVM. In this case, PACKAGE indicates software packaging.  
* PackagePath: The address of software package provided via HTTP. It must be in .tgz format. Batch downloads this software package to a scheduled CVM directory, and executes command in this directory.  
* Command: Task startup command. Here, we directly call a Python script file in the software package. You can download the package, and view the file structure and content in it.

fib.py is composed as below:  
```
fib = lambda n:1 if n<=2 else fib(n-1)+fib(n-2)
print("Remote Code Package : %d"%(fib(20)))
```

2_RemoteCodePkg.py is simple and can be directly executed by modifying the general parameters according to Preparations. So, no further modification is needed here.

## 3. Submit Job
The job submission process has been encapsulated in Demo in the form of Python script plus the internal trial version of Batch command line tool. So, you only need to run the Python script according to the following example.
```
$ python 2_RemoteCodePkg.py
{
    "Response": {
        "RequestId": "d069ce2f-abfc-451f-81fd-9327dbf5cf39",
        "JobId": "job-clump52n"
    }
}
```

If JobId field is returned, the job is submitted successfully. Otherwise, check the returned value for troubleshooting, or join the chat group in [User Report](https://cloud.tencent.com/document/product/599/10806) to make a inquiry to admin.

## 4. View the Status
See chapter [Simple Start](https://cloud.tencent.com/document/product/599/10551).

## 5. View the Result
See chapter [Simple Start](https://cloud.tencent.com/document/product/599/10551).

The execution result of 2_RemoteCodePkg.py is as follows:  
```
Remote Code Package : 6765
```

Remote mapping is used as an auxiliary feature by Batch for storage services, to map remote storages, such as COS and CFS, to a local folder.

## 1. Preparations
Complete the preparatory work as instructed in [Preparations](https://cloud.tencent.com/document/product/599/10548), and understand how to configure the general parameters of custom message.

## 2. Upload the Input Data File
number.txt is composed as follows:  
```
1
2
3
4
5
6
7
8
9
```

Upload the file to the input folder created in Preparations.

![](https://mc.qcloudimg.com/static/img/02738c821f14ed132fef76c466c79d08/COS_5.png)

## 3. View and Modify Demo
Open file 3_StoreMapping.py with an editor.
```
 # custom (Change to your info)
imageId = "img-m4q71qnf"
Application = {
    "DeliveryForm": "PACKAGE",
    "Command": "python ./codepkg/countnum.py",
    "PackagePath": "http://batchdemo-1251783334.cosgz.myqcloud.com/codepkg/codepkg.tgz"
}
secretId_COS = "your secretId"
secretKey_COS = "your secretKey"
StdoutRedirectPath = "your cos path"
StderrRedirectPath = "your cos path"
InputMapping = {
    "SourcePath": "your input remote path",
    "DestinationPath": "/data/input/"
}
OutputMapping = {
    "SourcePath": "/data/output/",
    "DestinationPath": "your output remote path"
}
```
Compared to 2_RemoteCodePkg.py, some of the parameters in the custom information are modified as follows:  
* The Command of Application is changed to running countnum.py  
* InputMapping: For input mapping, SourcePath is the remote storage address (changed to the address of input folder in Preparations), and DestinationPath is the local directory (no modification required).  
* OutputMapping: For output mapping, SourcePath is the local directory (no modification required), and DestinationPath is the remote storage address (changed to the address of output folder in Preparations).

countnum.py is composed as follows:  
```
import os

inputfile = "/data/input/number.txt"
outputfile = "/data/output/result.txt"

def readFile(filename):
    total = 0
    fopen = open(filename, 'r')
    for eachLine in fopen:
        total += int(eachLine)
    fopen.close()
    print "total = ",total
    fwrite = open(outputfile, 'w')
    fwrite.write(str(total))
    fwrite.close()

print("Local input file is ",inputfile)
readFile(inputfile)
```
Open input/number.txt, add up all numbers in each row, and write the result into output/Result.txt.

## 4. Submit Job
The job submission process has been encapsulated in Demo in the form of Python script plus the internal trial version of Batch command line tool. So, you only need to run the Python script according to the following example.
```
$ python 3_StoreMapping.py
{
    "Response": {
        "RequestId": "d069ce2f-abfc-451f-81fd-9327dbf5cf39",
        "JobId": "job-clump52n"
    }
}
```

If JobId field is returned, the job is submitted successfully. Otherwise, check the returned value for troubleshooting, or join the chat group in [User Report](https://cloud.tencent.com/document/product/599/10806) to make a inquiry to admin.

## 5. View the Status
See chapter [Simple Start](https://cloud.tencent.com/document/product/599/10551).

## 6. View the Result
Batch copies the output data in the local directory to a remote storage directory. The execution result of 3_StoreMapping.py is stored in result.txt which is then automatically synced to COS.
![pic](https://mc.qcloudimg.com/static/img/aee7138e589378eea48851dd1649b711/COS_6.png)
```
45
```

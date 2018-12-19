Make sure you have installed the Python environment in your system before installing the command line tool. For more information, please see [How Can I Install Python Environment and pip Tool](
//cloud.tencent.com/document/product/440/6181).

## 1. Install Tencent Cloud Command Line Tool (CLI)	
### I. Confirm whether **the application for internal trial has been approved**
If not, you are prompted with a message indicating no access permission when you use the Batch-related commands of the command line tool.

### II. Install CLI:
* If CLI is not installed: You can quickly install Tencent Cloud CLI using pip. For more information on installation, please see [Install Command Line Tool](https://cloud.tencent.com/document/product/440/6182).
```
$ sudo pip install qcloudcli
```

* If CLI is installed: You can quickly upgrade the tool through pip by executing the following command:
```
$ sudo pip install --upgrade qcloudcli
```

### III. Check whether the CLI is successfully installed and includes Batch-related capabilities:
```
$ qcloudcli batch help
You should use the qcloudcli as follow format:
qcloudcli <module> <action> [options and parameters]
The action name you input is error! The module [batch] support the valid action as follows:

DescribeAvailableCvmInstanceTypes       	|DescribeTask
DescribeJob                             	|SubmitJob
DescribeJobs                            	|TerminateTaskInstance
```

## 2. Obtain SecretID and SecretKey.
### I. Log in to the Tencent Cloud [API Key Console](https://console.cloud.tencent.com/capi).

### II. Create a new key or use an existing cloud API key. Click the cloud API key ID to enter the details page, and obtain SecretID and SecretKey.
![Alt text](https://mc.qcloudimg.com/static/img/ab7aea426d53f31f6bb1fc84bd2ce177/1.png)

## 3. Prepare COS Directory
### I. Create a bucket and a sub-folder
![](https://mc.qcloudimg.com/static/img/ecb3282f6cf12b371925743d9efa3874/COS_1.png)
Create a bucket and name it freely. Then, create three folders in the bucket for future use and name them as shown in the above figure.

### II. Remember the COS access address
![](https://mc.qcloudimg.com/static/img/0a0a2a781ed55febaecc2531fbe4f592/COS_2.png)

View the access domain name of COS Bucket as instructed in the above figure, and create the access domain names of three folders by combining domain name and folder name. The access addresses of three folders created with the official account are as follows:

* cos://batchdemo-1251783334.cosgz.myqcloud.com/logs/
* cos://batchdemo-1251783334.cosgz.myqcloud.com/input/
* cos://batchdemo-1251783334.cosgz.myqcloud.com/output/

```Please always combine the folder access address based on the domain name you used to access the Bucket. ```

## 4. Download Batch Demo File

[Download Address](http://batchdemo-1251783334.cosgz.myqcloud.com/demo/BatchDemo.zip). After the decompression, the file directory structure is as follows. Then, use Batch and related capabilities in the following order.

* [1_SimpleStart](https://cloud.tencent.com/document/product/599/10551)
* [2_RemoteCodePkg](https://cloud.tencent.com/document/product/599/10552)
* [3_StoreMapping](https://cloud.tencent.com/document/product/599/10983)

``` Demo is provided in the form of Python plus the internal trial version of Batch command line tool. Since Batch has many capabilities and configuration items, you can work with it more conveniently using Python script.```

## 5. General Parameters in Demo Custom Information
Take the custom information of "1_SimpleStart" as an example:

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

* imageId: The image containing Cloud-init service is used during internal trial. A CentOS 6.5 image (ID: **img-m4q71qnf**) that can be used directly is officially provided in the cloud marketplace, based on which a custom image is created. [Cloud Image Marketplace Address](https://market.cloud.tencent.com/products/3081)
* secretId_COS, secretKey_COS: Enter the SecretID and SecretKey obtained in step 2.
* StdoutRedirectPath, StderrRedirectPath: Enter the complete access address of logs folders in COS directory prepared in step 3. For example, replace cos://batchdemo-1251783334.cosgz.myqcloud.com/logs/ with your access address.
* Application: Startup command line, with no modification needed.

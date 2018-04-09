## Overview

For businesses based on Windows operating system, custom image is created from the Windows Server base image provided by Tencent Cloud. [Link>>](https://market.cloud.tencent.com/products/5310)to official image with the image ID of ``img-er9shcln``.

## Steps for Creating Windows Custom Image

### 1. Create a CVM using Official Base Image

Go to the [CVM purchase page](https://buy.cloud.tencent.com/cvm).

![](https://mc.qcloudimg.com/static/img/f4c62ba416032b20e17ff9ec3ed15e39/s3.png)
[Link to Cloud Marketplace>>](https://market.cloud.tencent.com/products/5310)

When choosing image, select **Service Marketplace** first. In the search box, search **Batch**, and select Windows Server 2012 base image (image ID: img-er9shcln). For storage, network and other settings, make selections by following the instructions. Finally click **Buy Now** to create a CVM.

### 2. Install Software in CVM as Required by Businesses

View the information of the CVM you just created on the [CVM Console](https://buy.cloud.tencent.com/cvm). After remote login, install all software relied on by your businesses to this CVM and make a simple test on calling.

### 3. Create a Custom Image

![](https://mc.qcloudimg.com/static/img/270d48a5e64e7ec32e1d710f43123b47/s1.png)

You can just click **Create Image** on the console. It takes some time to finish the creation process.

![](https://mc.qcloudimg.com/static/img/e939a39dcebe0c7449c7dacdb33e52ea/s2.png)

This ID is your custom image ID and you can view it on the [Image Console](https://console.cloud.tencent.com/cvm/image) at any time.

### 4. Submit Test Job using Custom Image

```
qcloudcli batch SubmitJob --Version 2017-03-12 --Job '{
    "JobName": "TestJob",       // Job name
    "JobDescription": "for test ",    // Job description
    "Priority": "1",            // Job priority
    "Tasks": [                  // Task list (only one task in this example)
        {
            "TaskName": "Task1",   // Name of Task 1
            "Application": {        // Task execution command
                "DeliveryForm": "LOCAL",    // Execute local command
                "Command": "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "   // Command contents (Fibonacci summation)
            },
            "ComputeEnv": {         // Computing environment configuration
                "EnvType": "MANAGED",   // Computing environment type, including hosted and unhosted
                "EnvData": {        // Specific configuration (the current type is hosted. See description of CVM instance creation)
                    "InstanceType": "S1.SMALL1",    // CVM instance type
                    "ImageId": "",      // CVM image ID (which is replaced with your custom image ID)
                }
            },
            "RedirectInfo": {       // Standard output redirection configuration           
                "StdoutRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/",    // Standard output (to be replaced)
                "StderrRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/"     // Standard error (to be replaced)
            }
        }
    ]
}'
--Placement'{
    "Zone": "ap-guangzhou-2"    // Availability Zone (may be replaced)
}'
```

Compared with the example in Quick Start, you can directly replace ImageId with your custom image ID.


```
qcloudcli batch SubmitJob --Version 2017-03-12  --Job '{"JobName": "TestJob",  "JobDescription": "for test", "Priority": "1", "Tasks": [{"TaskName": "Task1",  "TaskInstanceNum": 1,  "Application": {"DeliveryForm": "LOCAL", "Command":  "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "},  "ComputeEnv": {"EnvType":  "MANAGED", "EnvData": {"InstanceType": "S1.SMALL1",  "ImageId": "To be replaced" }  }, "RedirectInfo": {"StdoutRedirectPath": "To be replaced", "StderrRedirectPath":   "To be replaced"}, "MaxRetryCount":  1 } ] }' --Placement '{"Zone": "ap-guangzhou-2"}'
```

To submit a command line in practice, copy the above command to a text and modify the "To be replaced" info (the image ID and two log addresses).






The following use case shows how to create and terminate an instance using APIs.


## 1. Query Instance Model List

Before an instance is created, you need to specify a model because it determines the number of CPU cores and memory size of an instance. Therefore, call the API [Query Instance Model List](/document/api/213/9391) or view the product documentation [Instance Type](https://intl.cloud.tencent.com/document/product/213/7153) to obtain the appropriate model parameters with specified CPU cores and memory size. In this example, the model parameters are obtained using the query API. Assume that you want to obtain a model as follows:
> The Series 2 CVM instance (Guangzhong Zone 2, two CPU cores, and 4 GB memory)

The model can be obtained using the following request. For more information on each parameter, please see [Query Instance Model List](/document/api/213/9391).

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceTypeConfigs
&Version=2017-03-12
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-2
&Filters.1.Name=instance-family
&Filters.1.Values.1=S2
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

<br>The following result is returned for the above request. The values of InstanceType corresponding to CPU and Memory are the parameters of the desired model. In this example, the model is S2.MEDIUM4.

<pre>
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "S2",
                "InstanceType": "S2.MEDIUM4",
                "CPU": 2,
                "Memory": 4
            },
            ......
        ],
        "RequestId": "2f1fd71e-95ab-4f10-8adb-895e99d33ff5"
    }
}
</pre>

## 2. Create an Instance

You can create an instance by using the API [Create an Instance](/document/api/213/9384). Assume that you want to create an instance as follows:
> Zone: Guangzhou Zone 2; billing method: postpaid by hour; image ID: img-pmqg1cw7; model: standard 1C1G (S1.SMALL1), 50 GB local common system disk with 100 GB local common data disk, basic network; public network billing method: traffic postpaid by hour; upper limit of public network bandwidth: 10 MB, assigned with public IP; instance name: QCLOUD-TEST; login password: `Qcloud@TestApi123++`; installed with Cloud Monitoring and Cloud Security; one instance is purchased.

The instance can be created using the following request. For more information on each parameter, please see [Create an Instance](/document/api/213/9384).
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=RunInstances
&Version=2017-03-12
&Placement.Zone=ap-guangzhou-2
&InstanceChargeType=POSTPAID_BY_HOUR
&ImageId=img-pmqg1cw7
&InstanceType=S1.SMALL1
&SystemDisk.DiskType=LOCAL_BASIC
&SystemDisk.DiskSize=50
&DataDisks.0.DiskType=LOCAL_BASIC
&DataDisks.0.DiskSize=100
&InternetAccessible.InternetChargeType=TRAFFIC_POSTPAID_BY_HOUR
&InternetAccessible.InternetMaxBandwidthOut=10
&InternetAccessible.PublicIpAssigned=TRUE
&InstanceName=QCLOUD-TEST
&LoginSettings.Password=Qcloud@TestApi123++
&EnhancedService.SecurityService.Enabled=TRUE
&EnhancedService.MonitorService.Enabled=TRUE
&InstanceCount=1
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

<br>The following result is returned for the above request. The InstanceId in the result is the ID of the created instance. In this example, the ID of the created instance is ins-32kcaqoa.

<pre>
{
    "Response": {
        "InstanceIdSet": [
            "ins-32kcaqoa"
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>

After creating an instance with a specified ID, you can manage it using VNC or the [remote desktop](https://intl.cloud.tencent.com/document/product/213/5435).

## 3. Return an Existing Instance

A instance that is no longer used can be returned via the API [Return Instances](/document/api/213/9395). Assume that you want to return an instance as follows:
> Instance ID: ins-32kcaqoa

The instance can be returned using the following request. For more information on each parameter, please see [Return Instances](/document/api/213/9395).
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=TerminateInstances
&Version=2017-03-12
&InstanceIds.0=ins-32kcaqoa
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

<br>The following result is returned for the above request.

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>





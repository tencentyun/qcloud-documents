## 1. API Description
 
This API (ResizeInstanceHour) is used to adjust the configuration of specified instance, including CPU, memory and data disk.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* This API only applies to pay-per-use instances for pre-paid users. To make adjustments to instances with an annual or monthly plan, please use [ResizeInstance](https://cloud.tencent.com/doc/api/229/1306) API.
* Configuration upgrade can only be performed on the instances that have been shut down.
* Upgrade is only allowed for the instances that have a Cloud Block Storage.
* An instance to which an elastic block storage has been mounted is not supported.
* Downgrade is not supported currently.



## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](/doc/api/229/831) API.
| cpu | No | Int | Number of CPU cores of the upgraded instance. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177). |
| mem | No | Int | Memory size (GB) of upgraded instance. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177). |
| storageSize | Yes | Int | Data disk size (GB). The minimum increments in which the adjustment is made is 10G. The default is 0, which means that no data disk is purchased. The type of data disk assigned to the instance is the same as specified by `storageType` when the instance was created, and cannot be changed. For information on the characteristics and capacity limitations of different types of data disks, refer to [Overview of Hard Disk Products](/doc/product/213/498). |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 
 

## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ResizeInstanceHour
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &mem=2
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
{
    "code": 0,
    "message": "ok"
}
```






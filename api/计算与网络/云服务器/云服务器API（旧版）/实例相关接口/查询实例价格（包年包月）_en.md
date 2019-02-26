## 1. API Description
 
This API (InquiryInstancePrice) is used to obtain the price of prepaid instances.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>


* This API applies only to <font color="red"> prepaid instances</font>. To query the price of a postpaid instance, please use [InquiryInstancePriceHour](https://cloud.tencent.com/doc/api/229/1346) API.



## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976).

Different products have different input parameters. Here are the details:

### 2.1. Query the price of successfully renewed prepaid instances

| Parameter Name | Required | Type | Description | Source |
|---------|---------|---------|---------|---------|
| instanceType | Yes | Int | Instance type | The system sets it to 1 for a CVM instance. |
| instanceId | Yes | String | ID of the target instance | It can be obtained from the unInstanceId in the returned field of <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8">DescribeInstances</a> API. |
| period | Yes | Int | Purchase or renewal length | User defined, in months. The maximum is 36 and the minimum is 1. |

### 2.2. Query the price of prepaid instances

* These parameters have specific range limits. For more information on the parameters, please [see　here](https://cloud.tencent.com/doc/api/229/1248).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceType | Yes | Int | Instance type. The value is 1 (for CVM instance purchase). |
| cpu | Yes | Int | Number of instance cores. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177). |
| mem | Yes | Int | Memory size (GB) of the instance. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177). |
| period | Yes | Int | Length of purchase (month). 1 - 36 months. |
| storageType | No | Int | Hard disk type. 1: Local disk, 2: Cloud Block Storage; the default is local disk. For the selection of different data disk types, refer to [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). |
| storageSize | Yes | Int | Data disk size (GB). The increment is 10. The value of 0 means that no data disk is needed. The type of data disk is the same as specified by storageType. For the maximum size of different data disks, refer to [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). |
| goodsNum | No | Int | The number of purchased instances. The default is 1 and the maximum is 100. |
| bandwidth | No | Int | Public network bandwidth (Mbps), or the peak public network bandwidth when based on the charge by traffic mode. The default is 0. |
| bandwidthType | No | String | Bandwidth type. PayByTraffic: charge by traffic; PayByBandwidth: charge by month; charge by month by default. The difference between the network billing modes can be found in [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509). |
| rootSize | No | Int | System disk size (Unit: GB). <br>The adjustment range for Linux system is 20-50G, with an increment of 1. The default size is 20G. <br>Adjustment is not supported for Windows. The default size is 50G. <br>The system disk type is the same as the data disk type. |
| imageType | Yes | Int | Image type.  1: Private Image, 2: Public Image, 3: Image form Service Marketplace, 4: Shared Image. The imageType must match the actual type of the imageid. |
| imageId | Yes | String | Image ID, which can be obtained from unImgId in the returned field of [Query Image](https://cloud.tencent.com/doc/api/229/查询可用的镜像列表) API (the link contains a list of public image names and IDs). |

### 2.3. Query the price of instance configuration upgrade

* These parameters have specific range limits. For more information on the parameters, please refer to [this API](https://cloud.tencent.com/doc/api/229/1306).


| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceType | Yes | Int | Instance type. The value is 4 (for CVM instance configuration upgrade). |
| bandwidth | No | Int | The upgraded bandwidth (Mbps). |
| bandwidthUpgradeStartTime | No | String | Start time. It should take the format such as 2014-10-30. It should not be earlier than the current time. |
| bandwidthUpgradeEndTime | No | String | End time. It should take the format such as 2014-11-30. It should not be later than the expiration date of the instance. |
| cpu | No | Int | The number of CPU cores. The number of cores after upgrade. |
| mem | No | Int | Memory.  Memory size after upgrade (GB). |
| storageType | No | Int | Data disk type. 1: Local disk 2: Cloud Block Storage |
| storageSize | No | Int | Data disk size after upgrade. The unit is GB. The value of 0 means no data disk is needed. |

### 2.4. Query the price of network during the instance upgrade

* These parameters have specific range limits. For more information on the parameters, please refer to [this API](https://cloud.tencent.com/doc/api/229/1251).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceType | Yes | Int | Instance type. The value is 5 (for CVM instance network upgrade). |
| instanceId | Yes | String | ID of the instance to be operated.  It can be obtained from the unInstanceId or instanceId in the returned field of [DescribeInstances](https://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8) API (It is recommended to use unInstanceId).
| bandwidth | Yes | Int | The upgraded bandwidth (Mbps). |
| startTime | Yes | String | Start time. It should take the format such as 2014-10-30. It should not be earlier than the current time. |
| endTime | Yes | String | End Time. It should take the format such as 2014-11-30. It cannot be later than the expiration date of the instance.
| bandwidthType | No | String | Bandwidth type. PayByTraffic: charge by traffic; PayByBandwidth: charge by month; the default is PayByBandwidth.


 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| price| Int| Discount price (unit: 0.01 CNY)|
| originalPrice| Int| Original price of the product (unit: 0.01 CNY)|


## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
NotSupport.NotPrepaidUser | Request is rejected. The API only supports pre-paid users.
OperationFail.AllResourceOpFailed | The operation performed on the resource failed.
NotSupport.SharedInstance | Renewal inquiry is not allowed for a shared core instance.
InvalidParameter.ProjectIdNotFound | The resource does not exist.
PermissionDenied | You do not have permission to adjust the size of system disk of which the type is local disk. Please contact the Customer Service.
PermissionDenied | You do not have permission to adjust the size of system disk of which the type is Cloud Block Storage. Please contact the Customer Service.
InvalidParameter.MissImageId | The imageID must be passed for adjustment of system disk.
NotSupport.InstanceConfig | Request failed. Adjustment of configuration is not allowed for a shared core instance.
NotSupport.BandwidthPackageUser | Request failed. For bandwidth package customer, adjustment of instance bandwidth with this API is not supported.
InvalidParameter.Bandwidth | Selling system interface operation failed: bandwidth parameter is incorrect, please make a check and try again. 

## 5. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=InquiryProductPrice
  &instanceType=1
  &imageId=img-1234test
  &cpu=1
  &mem=1
  &storageSize=10
  &period=1
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```
{
    "code":0,
    "message": "",
    "price": 1085
}

```






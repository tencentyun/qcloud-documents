## 1. API Description
 
This API (ResizeInstance) is used to adjust the configuration of specified instance, including CPU, memory and data disk.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Configuration adjustment can only be performed on the instances that have been shut down.
* This API only supports the instances on which the system disk is Cloud Block Storage.
* An instance to which an elastic block storage has been mounted is not supported.
* This API only applies to the instances with an annual or monthly plan. To make adjustments to charge-by-quantity instances, please refer to [ResizeInstanceHour](https://cloud.tencent.com/doc/api/229/1344).
* Downgrade of configuration is not supported currently.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description | 
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.
| cpu | No | Int | Number of CPU cores of the upgraded instance. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177). |
| mem | No | Int | Memory size (GB) of upgraded instance. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177). |
| bandwidth| No| Int| Bandwidth (Mbps). If you only need to upgrade bandwidth, you can also use [UpdateInstanceBandwidth](http://cloud.tencent.com/doc/api/229/%E8%B0%83%E6%95%B4%E5%8C%85%E5%B9%B4%E5%8C%85%E6%9C%88%E5%AE%9E%E4%BE%8B%E5%B8%A6%E5%AE%BD). If this parameter is specified, bandwidthUpgradeStartTime and bandwidthUpgradeEndTime also need to be specified. |
| bandwidthUpgradeStartTime | No | String | The date on which the bandwidth upgrade starts, for example, 2016-08-30. The upgrade takes effect at 0:00 on the same day. |
| bandwidthUpgradeEndTime | No | String | The date on which the bandwidth upgrade ends, for example, 2018-10-02. The bandwidth will return to the original value at 0:00 on the same day. |
| storageType | No | Int | Hard disk type. Hard disk types: 1: Local disk; 2: Cloud Block Storage; 3: SSD local disk; 4: SSD cloud storage. The default is 1. For the selection of hard disk types, refer to [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). The optional hard disk types are limited by the instance type (InstanceType) selected when the instance was created. In addition, the maximum capacity available for purchase varies with different types of hard disks. |
| storageSize | Yes | Int | Data disk size (GB). The minimum increments in which the adjustment is made is 10G. The default  is 0, which means that no data disk is purchased. The type of data disk assigned to the instance is the same as specified by `storageType` when the instance was created. For the characteristics and capacity limits of different types of data disks, refer to [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). |
## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://intl.cloud.tencent.com/document/product/362/4207) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://intl.cloud.tencent.com/document/product/362/4207) on Error Code page. |
| dealIds | Array | The generated order number that is used to query the information on subsequent execution. |


## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
| NotSupport.NotPrepaidUser | Request is rejected. The API only supports pre-paid users.
| OperationFail.AllResourceOpFailed | The operation performed on the resource failed.
| NotSupport.BandwidthPackageUser | Request failed. For bandwidth package customers, adjustment of instance bandwidth with this API is not supported.
| InvalidParameter.Bandwidth | Selling system interface operation failed: bandwidth parameter is incorrect, please make a check and try again.
| NotSupport.InstanceConfig | Request failed. Adjustment of configuration is not allowed for a shared core instance.
| OperationConstraints.AccountBalanceNotEnough | Your balance is insufficient. Please top up first!
| OperationFail.SystemBusy | System is busy with resource purchase.


## 5. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ResizeInstance
  &instanceId=qcvm12345
  &cpu=1
  &mem=2
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
  {
      "code" : 0,
      "message" : ""
　　  "dealIds":[
　　          121
　　      ]
  }

```






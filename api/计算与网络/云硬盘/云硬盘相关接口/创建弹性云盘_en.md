## 1. API Description

This API (CreateCbsStorages) is used to create new elastic cloud storages.

Domain for API request:<font style="color:red">cbs.api.qcloud.com</font>

Usage restrictions:<br>
1. For restrictions on the sales of HDD elastic cloud storages and SSD elastic cloud storages, refer to [Cloud Block Storage Usage Restrictions](https://cloud.tencent.com/doc/product/362/5145).


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description |
| ------- | ------- | ------- | ------- |
| storageType | Yes | String | Type of hard disk medium. <br><li> cloudBasic refers to a HDD cloud storage; <br><li>cloudSSD refers to a SSD cloud storage | 
| goodsNum | Yes | Int | Number of purchase. The maximum value refer to [Cloud Block Storage Usage Restrictions](https://cloud.tencent.com/doc/product/362/5145). | 
| payMode | Yes | String | Payment mode. Currently, only Prepaid `prePay` is supported |
| period | Yes | Int | Length of purchase (month) | 
| zoneId | Yes | Int | ID of the availability zone of the cloud disk purchased, which can be queried via the [DescribeAvailabilityZones (Query Availability Zone)](http://cloud.tencent.com/doc/api/229/1286) API |
| storageSize | No | Int | Size of the disk (GB). <br><li>If "snapshotId" is passed, "storageSize" can be unpassed. In this case, the size of the new cloud disk is the snapshot size. <br><li>If the snapshot ID and the disk size are both passed, the disk size must be greater than or equal to the snapshot size.<br><li>The value range is 10GB - 4,000GB (HDD cloud storages), 100GB - 4,000GB (SSD cloud storages). The increment is 10GB |
| projectId | No | Int | Project ID. Creation will be performed under the default project if this parameter is not passed. This can be queried via the [DescribeProject (Query Project List)](/doc/api/229/1330) API. |
| snapshotId | No | String | Snapshot ID. If it is passed, a cloud disk will be created based on this snapshot. The snapshot type must be data disk snapshot. The snapshot ID can be queried through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API | 


## 3. Output Parameters

| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| code | Int | Common error code; 0: Succeeded; other values: Failed. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81) |
| message | String | Error message. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81)|
| storageIds | Array [String] | ID list of Cloud Block Storages created |


## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |

## 5. Example

Input
<pre>
https://cbs.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
$Action=CreateCbsStorages
&storageType=cloudBasic
&storageSize=10
&goodsNum=1
&period=1
&zoneId=100002
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "storageIds":[
            "disk-jpehowjo"
        ]
}
```



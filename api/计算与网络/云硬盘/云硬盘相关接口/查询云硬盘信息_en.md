## 1. API Description

This API (DescribeCbsStorages) is used to query the details of Cloud Block Storages. You can filter the results by the ID, status, and type of Cloud Block Storage. The relationship between different filter conditions is AND. If a condition is not passed, the condition will not be used for filtering.

Domain for API request:<font style="color:red">cbs.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description |
| -------- | ----- | ----- | --------- |
| diskType | No | String | Standard values: <br><li>root, which refers to system disk; <br><li>data, which refers to data disk |
| payMode | No | String | Payment mode. <br><li>prePay means Prepaid (Annual or Monthly Plan)<br><li>postPay means Postpaid (Bill by Traffic) | 
| portable | No | Int | Indicate whether it is an elastic cloud storage. <br><li>1 means it is an elastic cloud storage<br><li>0 means it is a non-elastic cloud storage | 
| projectId | No | Int | Project ID. You can query available projects and their IDs via the DescribeProject (Query Project List) API.  | 
| storageIds | No | Array [String] | Filter by one or more Cloud Block Storage IDs.  |
| storageType | No | String | Type of hard disk medium.<br><li>cloudBasic refers to a HDD cloud storage<br><li>cloudSSD refers to a SSD cloud storage |
| storageStatus | No | Array [String] | Filter by one or more statuses. The standard values are as follows.<br><li>normal: Normal<br><li>toRecycle: To be terminated<br><li>attaching: Mounting<br><li>detaching: Unmounting<br><li>snapshotCreating: The snapshot is being created<br><li>rollback: Rollbacking<br><li>expanding: Expanding | 
| uInstanceIds | No | Array [String] | The CVM instance ID, which can be used to query the Cloud Block Storage mounted under the specified CVM |
| zoneId | No | Int | ID of the availability zone of the hard disk, which can be queried via the [DescribeAvailabilityZones (Query Availability Zone)](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%8F%AF%E7%94%A8%E5%8C%BA) API |
| offset | No | Int | Offset; default value is 0 | 
| limit | No | Int | The number of disks to be returned. The default value is 20, and the maximum value is 100 | 



## 3. Output Parameters

| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| code | Int | Common error code; 0: Succeeded; other values: Failed. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81) |
| message | String | Error message. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81)|
| storageSet | Array [Object] | Cloud Block Storage information array. See the table below |
| totalCount | Int |The returned number of Cloud Block Storages |
 
 storageSet Structure
 
| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| attached | Int | Indicate whether it is mounted. 0 means not mounted, and 1 means mounted | 
| createTime | String | Time of creation |
| deadlineTime | String | Expiry time of the Cloud Block Storage | 
| diskType | String | Hard disk type. root: System disk. data: Data disk | 
| payMode | String | Payment mode. <br>prePay means Prepaid (Annual or Monthly Plan), postPay means Postpaid (Bill by Traffic) | 
| portable | Int | Indicate whether it is an elastic cloud storage. 0 means it is not an elastic cloud storage, and 1 means it is an elastic cloud storage | 
| projectId | Int | Project ID | 
| snapshotAbility | Int | Indicate whether it has the ability to create snapshots. 0 means that it doesn't have the ability, and 1 means that it has the ability | 
| storageId | String | ID of Cloud Block Storage | 
| storageName | String | Name of Cloud Block Storage | 
| storageSize | Int | Size of Cloud Block Storage (GB) | 
| storageStatus | String | Status of Cloud Block Storage.<br><li>normal: Normal. <br><li>toRecycle: To be terminated. <br><li>attaching: Mounting.<br><li>detaching: Unmounting.<br><li>snapshotCreating: The snapshot is being created.<br><li>rollback: Rollbacking. expanding: Expanding | 
| storageType | String | Type of hard disk medium.<br><li>cloudBasic: HDD cloud storage.<br><li>cloudSSD: SSD cloud storage | 
| uInstanceId | String | ID of the CVM onto which the Cloud Block Storage is mounted |
| zoneId | Int | ID of the availability zone of the Cloud Block Storage, which can be queried via the [DescribeAvailabilityZones (Query Availability Zone)](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%8F%AF%E7%94%A8%E5%8C%BA) API | 

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
&Action=DescribeCbsStorages
&storageIds.0=disk-5h58gfba
&storageIds.1=disk-m0js2w9s
&storageStatus.0=normal
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "totalCount": 2,
    "storageSet": [
        {
            "storageId": "disk-5h58gfba",
            "uInstanceId": null,
            "storageName": "ssss",
            "projectId": 0,
            "diskType": "data",
            "storageType": "cloudBasic",
            "storageStatus": "normal",
            "zoneId": 100002,
            "createTime": "2015-04-30 10:28:28",
            "storageSize": 10,
            "snapshotAbility": 0,
            "payMode": "prePay",
            "portable": 1,
            "attached": 0,
            "deadlineTime":2017-04-30 10:28:28,
        },
        {
            "storageId": "disk-m0js2w9s",
            "uInstanceId": null,
            "storageName": "baba",
            "projectId": 0,
            "diskType": "data",
            "storageType": "cloudBasic",
            "storageStatus": "normal",
            "zoneId": 0,
            "createTime": "2015-05-02 10:19:54",
            "storageSize": 10,
            "snapshotAbility": 0,
            "payMode": "prePay",
            "portable": 0,
            "attached": 1,
            "deadlineTime":2016-05-02 10:19:54,
        }
    ]
}
```




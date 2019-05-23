## 1. API Description

This API (ApplySnapshot) is used to roll back snapshots to the original cloud disk. Rollback to other cloud disks is not supported currently. For data disk snapshots, if you need to copy snapshot data to other cloud disks, please use [CreateCbsStorages (Create Elastic Cloud Storage)](https://cloud.tencent.com/doc/api/364/2524) to create a new elastic cloud storage.

Domain for API request:<font style="color:red">snapshot.api.qcloud.com</font>

Usage restrictions:<br>
1. The snapshot must be in `normal` status. The snapshot status can be queried through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API. See the `status` field in output parameters.<br>
2. Only the rollback of snapshots to the original cloud disk is supported.<br>
3. For an elastic cloud storage, the elastic cloud storage must be unmounted. The mount status of a cloud storage can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519) API; see the `attached` field in output parameters. For a non-elastic cloud storage purchased with CVM, the CVM must be shut down. The CVM status can be queried via [View Instance List](https://cloud.tencent.com/doc/api/229/831) API; see the `status` field in output parameters.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| snapshotId | Yes | String | Snapshot ID, which can be queried through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API |
| storageId | Yes | String | ID of the original cloud disk of the snapshot. This can be queried via [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  Succeeded, other values:  Failed |
| message | String | Error message |
| detail | Array | Returned array|
| detail.requestId | Int | Task ID. Refer to [Format of Returned Results for Asynchronous Task APIs](https://cloud.tencent.com/document/product/240/8325
) | 

## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
| 16005 | IncorrectInstanceStatus.DiskBusy | The disk is busy |
| 16027 | IncorrectInstanceStatus.CbsCreatingSnapshot | The cloud disk is creating a snapshot. Please try again later |

## 5. Example

Input:
<pre>
https://snapshot.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=ApplySnapshot
&snapshotId=snap-pxxx2xmn
&storageId=disk-g7xxxs4o
</pre>

Input:
```
{
    "code":"0",
    "message":""
}
```




## 1. API Description

This API (CreateSnapshot) is used to create snapshots for the specified cloud disk. This API will return the ID of the newly created snapshot, and users can use this ID to call [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API to query the snapshot creation progress (percent). For snapshot introductions, refer to [Snapshot Features](https://cloud.tencent.com/document/product/213/502).

Domain for API request:<font style="color:red">snapshot.api.qcloud.com</font>


Usage restrictions:<br>
1. Only a cloud disk with snapshot ability can create snapshots. Whether a cloud disk has snapshot ability can be queried through [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519) API. See the `snapshotAbility` field in output parameters. <br>
2. For the number of snapshots that can be created, refer to [Product Usage Restriction](https://intl.cloud.tencent.com/doc/product/362/5145).


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://intl.cloud.tencent.com/document/api/213/6976
).


| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| storageId | Yes | String | ID of the cloud disk that needs to create snapshots, which can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519) API |
| snapshotName | No | String | Snapshot name. If not passed, the new snapshot name is "Unnamed" |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed.
| message | String | Error message |
| snapshotId | String | ID of the newly created snapshot |

## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
| 16007 | IncorrectInstanceStatus.DiskTypeInvalid | This operation is not supported by the current cloud disk |
| 16026 | IncorrectInstanceStatus.SnapshotNotSupported | Snapshot is not supported by the cloud disk |
| 16005 | IncorrectInstanceStatus.DiskBusy | The disk is busy |
| 16006 | SnapshotQuotaExceeded | Snapshot limit is exceeded |
| 16027 | IncorrectInstanceStatus.CbsCreatingSnapshot | The cloud disk is creating a snapshot. Please try again later |

## 5. Example

Input:
<pre>
https://snapshot.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CreateSnapshot
&storageId=disk-g73hhs4o
&snapshotName=mySnap
</pre>

The returned results are as below. As can be seen in the result, a snapshot has been created successfully, and the snapshot ID is snap-o7zxxxr3.

```
{
    "code":"0",
    "message":"",
    "snapshotId":"snap-o7zxxxr3"
}
```



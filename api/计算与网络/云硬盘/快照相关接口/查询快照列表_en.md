
## 1. API Description

This API (DescribeSnapshots) is used to query the details of snapshots. You can filter the results by snapshot ID, cloud disk ID creating this snapshot, and type of cloud disk creating the snapshot. The relationship between different filter conditions is AND. If a condition is not passed, the condition will not be used for filtering.

Domain for API request: <font style="color:red">snapshot.api.qcloud.com</font>



## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| diskType  | No | String | Filter by cloud disk type. Option: root (system disk), data (data disk) |
| projectId | No | Int | Filter by project ID. 0 means default project. To specify other projects, you can call <a  title="DescribeProject">DescribeProject</a> API to query |
| storageIds.n | No | Array [String] | Filter by cloud disk ID creating this snapshot. You can call <a href="http://cloud.tencent.com/doc/api/364/%E6%9F%A5%E8%AF%A2%E4%BA%91%E7%A1%AC%E7%9B%98%E4%BF%A1%E6%81%AF" title="DescribeCbsStorages">DescribeCbsStorages</a> API to query |
| snapshotIds.n  | No | Array [String] | Filter by snapshot ID. |
| offset | No | Int | Offset. The value is 0 if not passed. |
| limit | No | Int | The maximum of snapshots that can be queried at a time. The value is 20 if it is not passed, and the maximum is 100 |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Code</a>. |
| message | String | Error message |
| snapshotSet | Array [object] | Snapshot details |
| totalCount | Int | Number of snapshots that meet the condition.


snapshotSet Structure

| Parameter Name | Type | Description |
|---------|---------|---------|
| createTime | Int | Snapshot creation time|
| diskType | String | The type of cloud disk creating the snapshot. There are two types: "root" (system disk snapshot), and "data" (data disk snapshot) |
| percent | Int | The percentage of progress for snapshot creation. This field is always 100 after the snapshot is created successfully |
| projectId | Int | Project ID, adopting the project ID of the original cloud disk |
| snapshotId | String | Snapshot ID |
| snapshotName | String | Snapshot name, a user-defined snapshot alias. Call [ModifySnapshot](https://cloud.tencent.com/doc/api/364/2532) to modify this field |
| snapshotStatus | String | Snapshot status, including "normal", "creating", and "rollbacking". Only snapshots in "normal" status can perform rollback and cloud disk creation tasks |
| storageId | String | Cloud disk ID creating this snapshot |
| storageSize | Int | The size of cloud disk creating this snapshot. When using a snapshot to create an elastic cloud storage, the size of the newly created elastic cloud storage must be larger than this size |


## 4. Error Codes

The following list only provides the business logic error codes for this API. For common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
	
## 5. Example

Input:
<pre>
https://snapshot.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=DescribeSnapshots
&limit=1
</pre>

The returned results are as below. As shown in the results, the totalCount is 5, which indicates that the user has five snapshots under this region, but only the information of one snapshot is returned, because the value of the parameter "limit" entered for query is 1 (limit=1). This snapshot (snapshotId) is a data disk snapshot (diskType). The size of the cloud disk (storageId) creating this snapshot is 10 GB (storageSize), and the snapshot's current status is "normal" (snapshotStatus).

```
{
    "code": 0,
    "message": "",
    "totalCount": 5,
    "snapshotSet": [
        {
            "snapshotId": "snap-ffxxxrx",
            "storageId": "disk-8rxxyy",
            "snapshotName": "ABCDEFGHHHH",
            "snapshotStatus": "normal",
            "projectId": 0,
            "percent": 100,
            "storageSize": 10,
            "createTime": "2016-05-17 19:58:48",
            "diskType": "data"
        }
    ]
}
```



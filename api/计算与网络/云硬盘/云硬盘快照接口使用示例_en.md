Cloud Block Storage snapshot is a full backup of corresponding Cloud Block Storage. Through the snapshot, you can quickly restore your Cloud Block Storage to the status when the snapshot is created. For details, please refer to [What Is Tencent Cloud Snapshot](/doc/product/362/5754). To help you quickly use the Snapshot API, we will give you an example.

In this example, we first create a snapshot for the specified Cloud Block Storage, and then roll this snapshot back to the Cloud Block Storage.

## 1. Create Cloud Block Storage Snapshot

First, create a snapshot for the specified Cloud Block Storage using the [Create Snapshot (CreateSnapshot)](https://cloud.tencent.com/doc/api/364/2529) API. Here, we create a snapshot named `sanp_test` for a Cloud Block Storage with an ID of `disk-nmnaafrh`. The specific API request parameters are as follows:

| Parameter Name | Description |  Value |
| --- | --- | --- |
| storageId | ID of the Cloud Block Storage that needs to create snapshots |  disk-nmnaafrh |
| snapshotName | The name of the snapshot created | snap_test |

By combining [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) and API request parameters, you can get the final form of request as follows:

```txt
https://snapshot.api.qcloud.com/v2/index.php?
Action=CreateSnapshot
&snapshotName=snapshot_test
&storageId=disk-nmnaafrh
&Region=sh
&Nonce=550701091
&Signature=ZMy0vTI%2BIZi1Q3wyQexd3K5iGkA%3D
&SecretId=AKIDxxxxugEY
&Timestamp=1466076669
```

The returned result of the above request is as follows. It shows that the ID of the snapshot created is `snap-amozk0kw`. Then, you can query the progress of snapshot creation through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API.

```json
{
	"code": 0,
	"message": "",
	"snapshotId": "snap-amozk0kw"
}
```

## 2. Roll Back Snapshot

You can roll back snapshots through the [ApplySnapshot (Roll Back Snapshot)](https://cloud.tencent.com/doc/api/364/2533) API. Here, we roll back the snapshot created earlier to the original Cloud Block Storage. The specific API request parameters are as follows:

| Parameter Name | Description |  Value |
| --- | --- | --- |
| snapshotId | ID of the snapshot to be rolled back | snap-amozk0kw |
| storageId | ID of the Cloud Block Storage to which the snapshot is to be rolled back | disk-nmnaafrh |


By combining [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) and API request parameters, you can get the final form of request as follows:

```txt
https://snapshot.api.qcloud.com/v2/index.php?
Action=ApplySnapshot
&snapshotId=snap-amozk0kw
&storageId=disk-nmnaafrh
&Region=sh
&Timestamp=1466078504
&Nonce=1519922454
&SecretId=AKIDxxxxugEY
&Signature=e8NZOcYCZJniAAMgVYhqsO70wd0%3D
```

The result of the above request is as follows
```json
{
	"code": 0,
	"message": "",
}
```




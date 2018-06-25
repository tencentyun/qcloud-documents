## 1. API Description

This API (DeleteSnapshot) is used to delete snapshots that are no longer in use.

Domain for API request:<font style="color:red">snapshot.api.qcloud.com</font>

Usage restrictions:<br>
1. The snapshot must be in `normal` status. The snapshot status can be queried through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API. See the `status` field in output parameters. 

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| snapshotIds.n  | Yes | Array[String] | Snapshot ID, which can be queried through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) API |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  Deletion request is successfully initiated, other values:  Deletion request failed|
| message | String | Error message |
| detail | Array[object] | Detail value |

detail Structure

| Parameter Name | Type | Description |
|---------|---------|---------|
| snapshotId | Array | Snapshot ID | 
| snapshotId.code | Int | Error code. 0 means that the snapshot is deleted successfully | 
| snapshotId.message | String |　Error message | 

## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |


## 5. Example

Input
<pre>
https://snapshot.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=DeleteSnapshot
&snapshotIds.0=aasd
&snapshotIds.1=snap-ptqv2xmn
</pre>

The returned results are as below. As can be seen in the result, the snapshot snap-ptqv2xmn has been successfully deleted, while the deletion of snapshot aasd has failed because this snapshot does not exist.

```
{
    "code":"0",
    "message":"",
    "detail":{
        "snap-ptqv2xmn":{
            "code":"0",
            "message":"return successfully!"
        },
        "aasd":{
            "code":"16003",
            "message":"snap not exist"
        }
    }
}
```



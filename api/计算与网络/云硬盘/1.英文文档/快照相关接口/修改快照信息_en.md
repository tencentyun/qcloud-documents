## 1. API Description

This API (ModifySnapshot) is used to modify snapshot information. Only the snapshot name can be modified currently.

Domain for API request:<font style="color:red">snapshot.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| snapshotId | Yes | String | Snapshot ID, which can be queried through [DescribeSnapshots (Query Snapshot List)](https://cloud.tencent.com/doc/api/364/2530) |
| snapshotName | Yes | String | New snapshot name. Up to 60 characters in length, and both Chinese and English characters are acceptable |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0:  Succeeded, other values:  Failed |
| message | String | Error message |

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
&Action=ModifySnapshot
&snapshotId=snap-ecp37wk1
&snapshotName=mySnap
</pre>

Output
```
{
    "code":"0",
    "message":""
}
```



## 1. API Description

This API (ModifyCbsStorageAttributes) is used to modify the name or the project ID of the specified cloud disk.

Domain for API call:<font style="color:red">cbs.api.qcloud.com</font>

Usage restrictions:<br>
1. Only the project ID of elastic cloud storages can be modified; the project ID of the cloud storage created with the CVM is linked with the CVM. The cloud disk type can be queried through [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519) API. See the `portable` field in output parameters.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description | 
| ------- | ------- | ------- | ------- | 
| storageId | Yes | String | ID of the cloud storage, which can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](/doc/api/364/2519) API |
| storageName| No | String | New name of the cloud storage |
| projectId | No | Int | New project ID of the elastic cloud storage. Only the project ID of elastic cloud storages can be modified. You can query available projects and their IDs via the DescribeProject （Query Project List） API.  | 
 
 
## 3. Output Parameters

| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| code | Int | Common error code; 0: Succeeded; other values: Failed. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81) |
| message | String | Error message. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81)|

## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
| 11039 | OperationDenied.AuthFailure | Authentication failed |
 
## 5. Example

Input
<pre>
https://cbs.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=ModifyCbsStorageAttributes
&storageId=disk-3clz8g94
&storageName=nihao
</pre>

Output
```
{
    "code":"0",
    "message":""
}
```
 
 
 


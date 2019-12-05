## 1. API Description

This API (ResizeCbsStorage) is used to expand the specified elastic cloud storage.

Domain for API call:<font style="color:red">cbs.api.cloud.tencent.com</font>

Usage restrictions:
1. Only elastic cloud storages can be expanded. The cloud disk type can be queried through [DescribeCbsStorages (Query Cloud Disk Information)](https://intl.cloud.tencent.com/doc/api/364/2519) API. See the `portable` field in output parameters. The cloud disk storage created with the CVM needs to be expanded via  [ResizeInstanceHour (Adjust the Instance Configuration (Bill by Traffic)](/doc/api/229/1344) API

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://intl.cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description |
| --- | --- | --- | --- | 
| storageId | Yes | String | ID of the cloud storage, which can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/document/api/364/2519) API |
| storageSize | Yes | Int | The expanded size of data disk (GB), which must be greater than the current value. The maximum value is 4,000, and the increment is 10 | 
 
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
 
 
## 5. Example

Input
<pre>
https://cbs.api.cloud.tencent.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=ResizeCbsStorage
&storageId=disk-cw6a3g9w
&storageSize=100
</pre>

Output
```
{
    "code":"0",
    "message":""
}
```
 
 
 


## 1. API Description

This API (DescribeInstancesCbsNum) is used to query the number of elastic cloud storages that have already been mounted on the CVM and the total number of elastic cloud storages that are allowed to be mounted on the CVM.

Domain for API request:<font style="color:red">cbs.api.qcloud.com</font>

Usage restrictions:<br>

No special restrictions. For specific parameter restrictions, refer to the table below.

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description |
| ------- | ------- | ------- | ------- |
| uInstanceIds | Yes | Array [String] | CVM instance ID, which can be queried via the [DescribeInstances (View Instance List)](/doc/api/229/831) API |
 
 
## 3. Output Parameters

| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| code | Int | Common error code; 0: Succeeded; other values: Failed. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81) |
| message | String | Error message. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81)|
| detail | Array [Object] | The number of elastic cloud storages that have already been mounted on the CVM and the maximum number of elastic cloud storages that can be mounted on the CVM. See the table below |
 
detail Structure:

| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| count | Int | The number of elastic cloud storages already mounted on the current CVM |
| maxAttachNum | String | The maximum number of elastic cloud storages that can be mounted on the current CVM |
 
## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
| 9006 | InternalError | Server background error |

## 5. Example

Input
<pre>
https://cbs.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=DescribeInstancesCbsNum
&uInstanceIds.0=ins-ka40hchw
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "detail":{
        "ins-ka40hchw":{
            "count":"5",
            "maxAttachNum":"10"
        }
    }
}
```


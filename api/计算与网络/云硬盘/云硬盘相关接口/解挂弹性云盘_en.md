## 1. API Description

This API (DetachCbsStorages) is used to unmount the specified elastic cloud storage.

Domain for API call:<font style="color:red">cbs.api.qcloud.com</font>
 
Usage restrictions:<br>
1. Only elastic cloud storages are supported. The cloud disk type can be queried through [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519) API. See the `portable` field in output parameters.<br>
2. The cloud disk must be mounted and the status is `normal`. The mount status of a cloud storage can be queried through [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519) API. See the `storageStatus` and `attached` fields in output parameters. 

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, refer to [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
).

| Parameter Name | Required | Type | Description |
| ------- | ------- | ------- | ------- | 
| storageIds | Yes | Array [String] | ID of the cloud storage to be unmounted, which can be queried via [DescribeCbsStorages (Query Cloud Disk Information)](/doc/api/364/2519) API. A maximum of 10 elastic cloud storages may be operated for each request |
 
## 3. Output Parameters

| Parameter Name | Type | Description |
| ------- | ------- | ------- |
| code | Int | Common error code; 0: Succeeded; other values: Failed. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81) |
| message | String | Error message. For details, refer to the [Error Code page](https://cloud.tencent.com/doc/api/364/%E9%94%99%E8%AF%AF%E7%A0%81)|
| detail | Array [object] | Refer to [Format of Returned Results of Batch Asynchronous Task APIs](http://cloud.tencent.com/doc/api/364/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F). |

## 4. Error Code List

The following list only provides the business logic error codes for this API. For additional common error codes, refer to [Cloud Block Storage Error Codes](https://cloud.tencent.com/doc/api/364/4207).

| Error Code | English Description | Error Description |
| ------- | ------- | ------- |
| 9003 | InvalidParameter | The parameter is incorrect |
| 16007 | IncorrectInstanceStatus.DiskTypeInvalid | This operation is not supported by the current cloud disk |
| 16008 | IncorrectInstanceStatus.OnlySupportElasticCloudDisk | Only elastic cloud storages are supported |
| 9033 | InvalidInstanceId.CvmNotFound | The CVM does not exist |
| 9814 | IncorrectInstanceStatus.CvmStatusInvalid | The CVM status is not met |
| 9008 | OperationDenied.PermissionDenied | Permission denied |

## 5. Example

Input
<pre>
https://cbs.api.qcloud.com/v2/index.php?
<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=DetachCbsStorages
&storageIds.0=disk-123bdkvd
&storageIds.1=disk-a2dbffgk

</pre>

Output

```
{
    "code":"0",
    "message":"",
    "detail":{
        "disk-123bdkvd":{
            "code":"16000",
            "message":"disk not exist"
        },
        "disk-a2dbffgk":{
            "code":"0",
            "message":"ok"
        }
    }
}
```



## 1. API Description

Domain name for API request: dts.tencentcloudapi.com

When this API is called, a non-timed migration task starts immediately, while a timed task starts after the countdown.
Make sure that a data migration task is verified successfully before calling this API.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: dts.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/571/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: StartMigrateJob |
| Version | Yes |  String | Common parameter. The value used for this API: 2018-03-30 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/571/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| JobId | Yes | String | ID of a data migration task |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/571/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| FailedOperation.NotAllowOperation | Prohibits the operation. |
| FailedOperation.StartJobFailed | Failed to start a task. |
| InternalError.AddTaskError | Failed to add an async task. |
| InternalError.DatabaseError | Access to the database on the migration platform failed. |
| InternalError.DuplicateJob | Migration task conflict. |
| InternalError.LockError | Lock conflict. |
| InternalError.ProtocolError | Communication protocol error. |
| InvalidParameter | Parameter error |
| LimitExceeded.MaxUnusedJobs | The number of idle migration tasks exceeds the limit. |
| ResourceNotFound.JobNotExist | The migration task does not exist. |

## 5. Example

### Example 1 Start a data migration task

#### Input example

```
https://dts.tencentcloudapi.com/?Action=StartMigrateJob
&JobId=dts-1kl0iy0v
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "bab78b9b-ce8a-4645-bfb2-5b03397d6ea0"
  }
}
```


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)


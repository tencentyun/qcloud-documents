## 1. API Description

Domain name for API request: dts.tencentcloudapi.com

This API is used to get the verification result after a verification task is created. The current verification status and progress can be queried via this API. 
If the verification is successful, call 'StartMigrateJob' to start migration.
If it fails, query the failure reason, and modify the migration configuration or change parameters of source/destination instance according to the error message using 'ModifyMigrateJob'.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: dts.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/571/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeMigrateCheckJob |
| Version | Yes |  String | Common parameter. The value used for this API: 2018-03-30 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/571/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| JobId | Yes | String | ID of a data migration task |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Status | String | Verification task status: unavailable (unavailable), starting (starting); running (verifying); finished (verification completed) |
| ErrorCode | Integer | Error code of the task |
| ErrorMessage | String | Error message of the task |
| Progress | String | Checks the total progress of the task, for example: "30" means 30% |
| CheckFlag | Integer | Indicates whether the verification is successful or not: 0 - Successful; 1 - Failed; 3 - Not verified |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/571/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| FailedOperation.NotAllowOperation | Prohibits the operation. |
| InternalError.DatabaseError | Access to the database on the migration platform failed. |
| InternalError.ProtocolError | Communication protocol error. |
| InvalidParameter | Parameter error |
| ResourceNotFound.JobNotExist | The migration task does not exist. |

## 5. Example

### Example 1 Get migration verification result

#### Input example

```
https://dts.tencentcloudapi.com/?Action=DescribeMigrateCheckJob
&JobId=dts-1kl0iy0v
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "CheckFlag": 0,
    "ErrorCode": -1,
    "ErrorMessage": "The database table you selected does not exist. Please re-select. [The input parameter table cannot be found in the source instance]",
    "Progress": "100",
    "RequestId": "67b4cfcf-6957-48ae-b7ef-ba33209895e3",
    "Status": "finished"
  }
}
```

### Example 2 Get migration verification result

#### Input example

```
https://dts.tencentcloudapi.com/?Action=DescribeMigrateCheckJob
&JobId=dts-dau5czmd
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "CheckFlag": 1,
    "ErrorCode": 0,
    "ErrorMessage": "ok",
    "Progress": "100",
    "RequestId": "336448b0-2a45-4be4-8356-c245eab5784f",
    "Status": "finished"
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


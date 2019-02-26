## 1. API Description

Domain name for API request: dts.tencentcloudapi.com

This API is used to delete a data migration task. Any ongoing verification or migration task cannot be deleted.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: dts.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/571/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DeleteMigrateJob |
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
| InternalError.DatabaseError | Access to the database on the migration platform failed. |
| InternalError.DuplicateJob | Migration task conflict. |
| InternalError.ProtocolError | Communication protocol error. |
| InvalidParameter | Parameter error |
| ResourceNotFound.JobNotExist | The migration task does not exist. |

## 5. Example

### Example 1 Delete a data migration task

#### Input example

```
https://dts.tencentcloudapi.com/?Action=DeleteMigrateJob
&JobId=dts-1kl0iy0v
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "e15f9b4c-9841-40d2-a28b-dea284a17315"
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


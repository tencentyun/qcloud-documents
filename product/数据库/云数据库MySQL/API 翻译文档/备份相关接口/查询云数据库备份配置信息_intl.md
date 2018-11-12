## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeBackupConfig) is used to query the configuration of a database backup.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeBackupConfig |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID, such as cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| StartTimeMin | Integer | The earliest time at which the backup starts. For example, 2 indicates 2:00 am. |
| StartTimeMax | Integer | The latest time at which the backup starts. For example, 6 indicates 6:00 am. |
| BackupExpireDays | Integer | Backup expiration time (in days) |
| BackupMethod | String | Backup method. Supported values include: physical - physical backup, and logical - logical backup. |
| BinlogExpireDays | Integer | Binlog expiration time (in days) |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.CdbCgwError | System's internal error. |
| InternalError.DatabaseAccessError | Database's internal error. |
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |

## 5. Example

### Example 1 Query the configuration of a database backup

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeBackupConfig
&InstanceId=cdb-c1nl9rpv
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "BackupMethod": "logical",
    "BinlogExpireDays": 5,
    "ExpireDays": 10,
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "StartTimeMax": 6,
    "StartTimeMin": 2
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
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)


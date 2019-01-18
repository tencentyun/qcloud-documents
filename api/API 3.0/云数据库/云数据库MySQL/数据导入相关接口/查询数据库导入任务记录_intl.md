## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeDBImportRecords) is used to query the operation logs of an import task for a database.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDBImportRecords |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID, such as cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page. |
| StartTime | No | String | Start time, such as 2016-01-01 00:00:01. |
| EndTime | No | String | End time, such as 2016-01-01 23:59:59. |
| Offset | No | Integer | Offset, which is a parameter for paging. Default is 0. |
| Limit | No | Integer | Number of results returned for a single request. This is a parameter for paging. Default is 20. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of import logs that meet the condition. |
| Items | Array of [ImportRecord](/document/api/236/##ImportRecord) | List of returned import logs. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |
| InvalidParameter.InvalidAsyncRequestId | The asynchronous task does not exist. |

## 5. Example

### Example 1 Query the logs of an import task for a database

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeDBImportRecords
&InstanceId=cdb-7r8h0h61
&StartTime=2016-01-01 00:00:01
&EndTime=2017-08-24 15:03:01
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Items": [
      {
        "AsyncRequestId": "a4788d0a-df23758a-ac961e5a-af414d33",
        "Code": 1,
        "CostTime": 0,
        "CreateTime": "2017-11-09 14:26:31",
        "DbName": "test",
        "FileName": "monkey_1501490864.sql",
        "FileSize": 12,
        "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
        "JobId": 16242,
        "Message": "lock_inst.cgi: Some instance IDs have no instance logs",
        "Process": 5,
        "Status": 3,
        "WorkId": "1649290"
      },
      {
        "AsyncRequestId": "198e97de-972b1971-fb0ce76a-08ca054e",
        "Code": 1,
        "CostTime": 0,
        "CreateTime": "2017-10-18 21:18:26",
        "DbName": "",
        "FileName": "monkey_1501490864.sql",
        "FileSize": "12",
        "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
        "JobId": 16223,
        "Message": "lock_inst.cgi: Some instance IDs have no instance logs",
        "Process": 5,
        "Status": 3,
        "WorkId": "1545387"
      },
      {
        "AsyncRequestId": "9706dfbf-0d1bc6df-5f18f4e1-bb86f2f4",
        "Code": 1,
        "CostTime": 0,
        "CreateTime": "2017-10-18 20:12:07",
        "DbName": "test",
        "FileName": "monkey_1501490864.sql",
        "FileSize": "2",
        "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
        "JobId": 16222,
        "Message": "lock_inst.cgi: Some instance IDs have no instance logs",
        "Process": 5,
        "Status": 3,
        "WorkId": "1545171"
      },
      {
        "AsyncRequestId": "e8713d1e-10628d32-74682eef-d0855c1a",
        "Code": 1,
        "CostTime": 0,
        "CreateTime": "2017-10-18 17:53:54",
        "DbName": "",
        "FileName": "monkey_1501490864.sql",
        "FileSize": "12",
        "InstanceId": "e318ecb8-863f-11e7-85a5-80fb06afab26",
        "JobId": 16209,
        "Message": "lock_inst.cgi: Some instance IDs have no instance logs",
        "Process": 5,
        "Status": 3,
        "WorkId": "2228867"
      }
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "TotalCount": "4"
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


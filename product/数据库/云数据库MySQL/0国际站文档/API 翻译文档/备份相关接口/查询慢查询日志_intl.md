## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeSlowLogs) is used to obtain the slow logs of a database instance.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeSlowLogs |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page. |
| Offset | No | Integer | Offset. The minimum value is 0. |
| Limit | No | Integer | Number of results to be returned. Default is 20. Maximum is 100. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of slow logs that meet the condition |
| Items | Array of [SlowLogInfo](/document/api/236/##SlowLogInfo) | Details of the slow logs that meet the condition |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| CdbError | Backend error or process error. |
| CdbError.TaskError | Backend task error. |
| InternalError.DatabaseAccessError | Database's internal error. |
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |
| OperationDenied.WrongStatus | The backend task status is invalid. |

## 5. Example

### Example 1 Query slow logs

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeSlowLogs
&InstanceId=cdb-c1nl9rpv
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Items": [
      {
        "Date": "2017-04-26 00:00:08",
        "InternetUrl": "",
        "IntranetUrl": "",
        "Name": "ivansqwutestdr_slowlog_20170425.log",
        "Size": 0,
        "Type": "slowlog"
      },
      {
        "Date": "2017-04-27 00:00:07",
        "InternetUrl": "http://gz.xxxxxxxxxx",
        "IntranetUrl": "http://gz.xxxxxxxxxx",
        "Name": "ivansqwutestdr_slowlog_20170426.log",
        "Size": 212,
        "Type": "slowlog"
      },
      {
        "Date": "2017-04-28 00:00:09",
        "InternetUrl": "",
        "IntranetUrl": "",
        "Name": "ivansqwutestdr_slowlog_20170427.log",
        "Size": 0,
        "Type": "slowlog"
      }
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "TotalCount": 3
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


## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (InitDBInstances) is used to initialize a database instance, including its password, default character set, and instance port number.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InitDBInstances |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes | Array of String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page and can be obtained via API [Query Instance List](https://cloud.tencent.com/document/api/236/15872). Its value equals the InstanceId field value in the output parameters. |
| NewPassword | Yes | String | New password for the instance, which should be a combination of 8-64 characters comprised of at least two of the following types: letters, numbers, and special characters (!, @, #, $, %, ^, *, ()). |
| Parameters.N | Yes | Array of [ParamInfo](/document/api/236/##ParamInfo) | List of instance parameters. Parameters "character_set_server" and "lower_case_table_names" can be set. Available values for "character_set_server" are ["utf8", "latin1", "gbk", "utf8mb4"], and for "lower_case_table_names" are ["0", "1"]. |
| Vport | No | Integer | Port of the instance |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| AsyncRequestIds | Array of String | ID array of an async task request, which can be used to query the execution result of an async task. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter | Parameter error. |

## 5. Example

### Example 1 Initialize a new instance

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=InitDBInstances
&InstanceIds.0=cdb-f35wr6wj
&NewPassword=Gx18ux23F^X
&Parameters.0.name=lower_case_table_names
&Parameters.0.value=1
&Parameters.1.name=character_set_server
&Parameters.1.value=utf8
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "AsyncRequestIds": [
      "8cd119d4-61ba-11e7-aeff-018cfa1f5560"
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
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


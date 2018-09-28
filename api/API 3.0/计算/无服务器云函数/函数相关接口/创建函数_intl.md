## **1. API Description**

API request domain name: scf.tencentcloudapi.com.

This API creates a new function based on the parameters passed in.

API request frequency limit: 10 times/second.



## **2. Input Parameters**

The following list of request parameters lists only the API request parameters and some common parameters. For the complete list of common parameters, see [Common Request Parameters](/document/api/583/15692).

| Parameter name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter; the value for this API: CreateFunction |
| Version | Yes | String | Common parameter; the value for this API: 2018-04-16 |
| Region | Yes | String | Common parameters; for details, see the [Region List](/document/api/583/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| FunctionName | Yes | String | Name of the new function. It can contain 2 to 60 characters, including lower-case and upper-case English letters, numbers, dashes and underscores, must begin with a letter and cannot end with a dash or underscore |
| Code | Yes | [Code](/document/api/583/##Code) | Code of the function. Note: COS and ZipFile cannot be specified at the same time |
| Handler | No | String | Name of the function handler. This name supports the "file name.handler name" form where the file name and handler name are separated with a ".". File and handler names must be of 2-60 characters and start and end with letters, and can contain letters, numbers, underscores and dashes in the middle |
| Description | No | String | Description of the function. It can contain up to 1,000 characters including English letters, numbers, spaces, commas, line breaks, periods and Chinese characters |
| MemorySize | No | Integer | Memory size available for the function during execution between 128MB and 1,536MB in an increment of 128MB; 128MB by default |
| Timeout | No | Integer | Maximum execution duration of the function in seconds; the value can be between 1 and 300 seconds; 3 seconds by default |
| Environment | No | [Environment](/document/api/583/##Environment) | Environment variable of the function |
| Runtime | No | String | Runtime environment of the function; currently, only the following ones are supported: Python2.7, Python3.6, Nodejs6.10, PHP5, PHP7, Golang1 and Java8; Python2.7 by default |
| VpcConfig | No | [VpcConfig](/document/api/583/##VpcConfig) | VPC configuration of the function |

## **3. Output Parameters**

| Parameter name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID which is returned for each request. The RequestId for the current request needs to be provided when troubleshooting. |

## **4. Error Codes**

Only the error codes related to the API logic are listed below. For other error codes, see [Common Error Codes](/document/api/583/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error |
| InternalError.System | Internal system error. |
| InvalidParameterValue | Wrong parameter value |
| InvalidParameterValue.Code | Wrong Code parameter passed in. |
| InvalidParameterValue.Description | Wrong Description parameter passed in. |
| InvalidParameterValue.Environment | Wrong Environment parameter passed in. |
| InvalidParameterValue.FunctionName | Function does not exist. |
| InvalidParameterValue.Handler | Wrong Handler parameter passed in. |
| InvalidParameterValue.Runtime | Wrong Runtime parameter passed in. |
| LimitExceeded.Function | The number of functions exceeds the upper limit. |
| LimitExceeded.Memory | Memory exceeds the upper limit. |
| LimitExceeded.Timeout | Timeout exceeds the upper limit. |
| MissingParameter.Code | Code parameter missing. |
| ResourceInUse.FunctionName | FunctionName already exists. |
| UnauthorizedOperation.CAM | CAM authentication failed. |
| UnauthorizedOperation.Region | Error with Region. |

## **5. Examples**

### **Example 1. Creating Function**

#### **Input Example**

```
https://scf.tencentcloudapi.com/?Action=CreateFunction
&FunctionName=<FunctionName>
&Handler=<function.handler>
&Code.CosBucketName=<CosBucketName>
&Code.CosObjectName=<CosObjectName>
&<Common request parameter>
```

#### **Output Example**

```
{
  "Response": {
    "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
  }
}
```


## **6. Other Resources**

Tencent Cloud API 3.0 comes with a set of complementary development tools that make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

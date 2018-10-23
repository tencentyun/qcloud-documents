## **1. API Description**

API request domain name: scf.tencentcloudapi.com.

This API updates the function code based on the parameters passed in.

API request frequency limit: 20 times/second.



## **2. Input Parameters**

The following list of request parameters lists only the API request parameters and some common parameters. For the complete list of common parameters, see [Common Request Parameters](/document/api/583/15692).

| Parameter name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter; the value for this API: UpdateFunctionCode |
| Version | Yes | String | Common parameter; the value for this API: 2018-04-16 |
| Region | Yes | String | Common parameters; for details, see the [Region List](/document/api/583/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Handler | Yes | String | Name of the function handler. This name supports the "file name.function name" format. File and function names must be of 2-60 characters and start and end with letters, and can contain letters, numbers, underscores and dashes |
| FunctionName | Yes | String | Name of the function to be modified |
| CosBucketName | No | String | Name of the object bucket |
| CosObjectName | No | String | Path of the COS object |
| ZipFile | No | String | This contains a .zip file of the function code file and its dependencies. When using this API, the content of the .zip file needs to be encoded with Base64. It can be up to 20MB |
| CosBucketRegion | No | String | Region of the COS. For the Beijing region, you need to pass in ap-beijing; for the Beijing Zone 1, you need to pass in ap-beijing-1; for other regions, this parameter can be left blank |

## **3. Output Parameters**

| Parameter name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID which is returned for each request. The RequestId for the current request needs to be provided when troubleshooting. |

## **4. Error Codes**

Only the error codes related to the API logic are listed below. For other error codes, see [Common Error Codes](/document/api/583/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.System | Internal system error. |
| InvalidParameterValue | Wrong parameter value |
| InvalidParameterValue.Code | Wrong Code parameter passed in. |
| InvalidParameterValue.Handler | Wrong Handler parameter passed in. |
| ResourceNotFound.FunctionName | Function does not exist. |
| UnauthorizedOperation.CAM | CAM authentication failed. |

## **5. Examples**

### **Example 1. Updating Function Code**

#### **Input Example**

```
https://scf.tencentcloudapi.com/?Action=UpdateFunctionCode
&Handler=index.main
&CosBucketName=<CosBucketName>
&CosObjectName=<CosObjectName>
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

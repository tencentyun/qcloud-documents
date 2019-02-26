## **1. API Description**

API request domain name: scf.tencentcloudapi.com.

This API is used to run the function.

API request frequency limit: 20 times/second.



## **2. Input Parameters**

The following list of request parameters lists only the interface request parameters and some common parameters. For the complete list of common parameters, see [Common Request Parameters](/document/api/583/15692).

| Parameter name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter; the value for this interface: Invoke |
| Version | Yes | String | Common parameter; the value for this interface: 2018-04-16 |
| Region | Yes | String | Common parameters; for details, see the [Region List](/document/api/583/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| FunctionName | Yes | String | Name of the function |
| InvocationType | No | String | RequestResponse (sync) and Event (asynchronous); sync by default |
| Qualifier | No | String | Version number that triggers the function |
| ClientContext | No | String | Parameters when running the function; input in JSON format; the maximum supported parameter length is 1MB |
| LogType | No | String | If this field is specified when calling synchronously, the return value will contain 4K logs; possible values: None and Tail; None by default. When the value is Tail, the logMsg field in the return parameter will contain the corresponding function execution log |
| Namespace | No | String | Namespace |

## **3. Output Parameters**

| Parameter name | Type | Description |
|---------|---------|---------|
| Result | [Result](/document/api/583/##Result) | Execution result of the function|
| RequestId | String | The unique request ID which is returned for each request. The RequestId for the current request needs to be provided when troubleshooting. |

## **4. Error Codes**

Only the error codes related to the interface business logic are listed below. For other error codes, see [Common Error Codes](/document/api/583/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error |
| InternalError.System | Internal system error. |
| InvalidParameterValue | Wrong parameter value |
| InvalidParameterValue.Param | The input parameter is not in standard JSON format. |
| ResourceNotFound.FunctionName | Function does not exist. |
| ResourceUnavailable.InsufficientBalance | The balance is insufficient. Please top up first. |
| UnauthorizedOperation.CAM | CAM authentication failed. |

## **5. Examples**

### **Example 1. Running Function**

#### **Input Example**

```
https://scf.tencentcloudapi.com/?Action=Invoke
&FunctionName=xxxx
&<Common request parameter>
```

#### **Output Example**

```
{
  "Response": {
    "RequestId": "c2af8a64-c922-4d55-aee0-bd86a5c2cd12",
    "Result": {
      "BillDuration": 100,
      "Duration": 0.826,
      "ErrMsg": "",
      "FunctionRequestId": "6add56fa-58f1-11e8-89a9-5254005d5fdb",
      "InvokeResult": 0,
      "Log": "",
      "MemUsage": 3207168,
      "RetMsg": "hello from scf"
    }
  }
}
```


## **6. Other Resources**

Cloud API 3.0 comes with a set of complementary development tools that make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

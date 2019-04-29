## 1. API Description

Domain name for API request: cis.tencentcloudapi.com.

This API (InquiryPriceCreateCis) is used to query the price of a container instance.

The default limit on the requests made to the API is 20 requests per second.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/858/17764).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceCreateCis |
| Version | Yes | String | Common parameter. The value used for this API: 2018-04-08 |
| Region | Yes | String | Common parameter. For more information, see the [list of regions](/document/api/858/17764#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Zone | Yes | String | Availability zone |
| Cpu | Yes | Float | CPU (in cores) |
| Memory | Yes | Float | Memory (in Gi) |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/858/17776#Price) | Prices |
| RequestId | String | The unique request ID, which is returned for each request. The RequestId is required for troubleshooting. |

## 4. Error Codes

The following only lists the error codes related to this API. For other error codes, see [Common Error Codes](/document/api/858/17766#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError | Internal error. |
| InvalidParameter | Incorrect parameter. |

## 5. Example

### Example 1 Query the price of a container instance (with 1 core and 1 Gi) in Chengdu Zone 1

#### Input example

```
https://cis.tencentcloudapi.com/?Action=InquiryPriceCreateCis
&Zone=ap-chengdu-1
&Cpu=1.0
&Memory=1.0
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Price": {
      "DiscountPrice": 0.3,
      "OriginalPrice": 0.3
    },
    "RequestId": "12345"
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


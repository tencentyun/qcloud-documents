## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeDBPrice) is used to query the price of a database instance. Postpaid and prepaid instances are supported. You can query the price of an instance by specifying such information as instance type, purchased usage period, purchase quantity, memory size, disk size and availability zone.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDBPrice |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Zone | Yes | String | Availability zone information, such as "ap-guangzhou-1" |
| GoodsNum | Yes | Integer | Number of instances. Default is 1, minimum is 1, and maximum is 100. |
| Memory | Yes | Integer | Instance memory size (in MB) |
| Volume | Yes | Integer | Instance disk size (in GB) |
| PayType | Yes | String | Billing method. Supported values: PRE_PAID - prepaid, HOUR_PAID - postpaid |
| Period | Yes | Integer | Instance validity period (in month). The minimum is 1 and the maximum is 36. This field is not applicable to query of the prices of postpaid instances. |
| InstanceRole | No | String | Instance type. Default is master. Supported values: master - master instance, ro - read-only instance, dr - disaster recovery instance |
| ProtectMode | No | Integer | Data replication mode. Default is 0. Supported values: 0 - Async replication; 1 - Semisync replication; 2 - Strongsync replication |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | Integer | Instance price (in 0.01 CNY) |
| OriginalPrice | Integer | Instance original price (in 0.01 CNY) |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.DatabaseAccessError | Database's internal error. |
| InternalError.TradeError | Internal error with trading system. |
| InvalidParameter | Parameter error. |

## 5. Example

### Example 1 Query the price of a database instance

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeDBPrice
&Zone=ap-guangzhou-1
&GoodsNum=1
&Memory=1000
&Volume=25
&PayType=PRE_PAID
&Period=24
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "OriginalPrice": 460800,
    "Price": 48000,
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


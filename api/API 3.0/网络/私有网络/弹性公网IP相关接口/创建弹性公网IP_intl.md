## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (AllocateAddresses) is used to apply for one or more [Elastic IPs](https://cloud.tencent.com/document/product/213/1941) (EIP).
* EIP is a static IP designed for dynamic cloud computing. With EIP, you can quickly remap the EIP to another instance, shielding off the instance failures.
* Your EIP is associated with a Tencent Cloud account, instead of an instance, until you choose to explicitly release it or your payment is more than seven days overdue.
* The platform imposes quotas on number of EIPs that a user can request for each region. See [Overview of EIP products](https://cloud.tencent.com/document/product/213/5733). The above quotas can be obtained via API DescribeAddressQuota.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: AllocateAddresses |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| AddressCount | No | Integer | Number of requested EIPs. Default is 1. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| AddressSet | Array of String | List of unique IDs of the requested EIPs. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| AddressQuotaLimitExceeded | Account quota is exceeded. At most 20 EIPs can be created by each Tencent Cloud account in each region. |
| AddressQuotaLimitExceeded.DailyAllocate | The maximum number of requests is exceeded. The maximum number of requests can be made by each Tencent Cloud account in each region equals to two times the quota. |

## 5. Example

### Example 1 Create an EIP

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=AllocateAddresses
&AddressCount=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "AddressSet": [
      "eip-m44ku5d2"
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


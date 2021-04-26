## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DisassociateAddress) is used to unbind an [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP).
* You can only unbind EIPs with a status of BIND or BIND_ENI.
* Blocked EIPs cannot be unbound.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DisassociateAddress |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| AddressId | Yes | String | The unique ID of an EIP. Example of the unique ID of an EIP: `eip-11112222`. |
| ReallocateNormalPublicIp | No | Boolean | Indicates whether to allocate a public IP after unbinding an EIP. Supported values: <br><li>TRUE: Allocate a public IP after unbinding an EIP.<br><li> FALSE: Do not allocate a public IP after unbinding an EIP.<br> Default: FALSE.<br><br> The parameter can be specified only under the following conditions:<br><li> It can only be specified when you unbind an EIP from the primary private IP of the primary ENI.<br><li> After an EIP is unbound, you can assign public IPs for at most 10 times to an account per day. You can acquire more information using the API [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidAddressId.Blocked | The specified EIP is blocked. You cannot bind the EIP until it is unblocked. |
| InvalidAddressId.NotFound | The specified EIP does not exist. |
| InvalidAddressIdStatus.NotPermit | The specified EIP in the current status cannot be bound. Only EIPs in the UNBIND status can be bound. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidParameter | Invalid input parameter. |

## 5. Example

### Example 1 Unbind an EIP

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DisassociateAddress
&AddressId=eip-ek0cdz1g
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
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


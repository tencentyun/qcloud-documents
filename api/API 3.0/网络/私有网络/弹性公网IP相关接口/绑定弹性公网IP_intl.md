## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (AssociateAddress) is used to bind an [Elastic IP](https://cloud.tencent.com/document/product/213/1941) (EIP) to an instance or a specified private IP of an ENI.
* Essentially, binding an EIP to an instance means binding an EIP to the primary private IP of the primary ENI on an instance.
* When you bind an EIP to the primary private IP of the primary ENI, the previously bound public IP is automatically unbound and released.
* If the private IP of the specified ENI has been bound to an EIP, you must unbind this EIP before binding a new one.
* EIPs that are in arrears or blocked cannot be bound.
* Only EIPs in the UNBIND status can be bound.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: AssociateAddress |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| AddressId | Yes | String | The unique ID of an EIP. Example of the unique ID of an EIP: `eip-11112222`. |
| InstanceId | No | String | ID of the instance to be bound to. such as `ins-11112222`. It can be queried through the [console](https://console.cloud.tencent.com/cvm) or obtained from the `InstanceId` field value in the returned result of API [DescribeInstances](https://cloud.tencent.com/document/api/213/9389). |
| NetworkInterfaceId | No | String | ID of the ENI to be bound to. Example of an ENI ID: `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. The ENI ID can be queried through the [console](https://console.cloud.tencent.com/vpc/eni) or obtained from the `networkInterfaceId` field in the returned value by the API [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/4814). |
| PrivateIpAddress | No | String | The private IP to be bound to. If `NetworkInterfaceId` is specified, `PrivateIpAddress` must also be specified, which means binding an EIP to the specified private IP of the specified ENI. Make sure that the specified `PrivateIpAddress` is a private IP on the specified `NetworkInterfaceId`. The private IP of a specified ENI can be queried through the [console](https://console.cloud.tencent.com/vpc/eni) or obtained from the `privateIpAddress` field in the returned value by the API [DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/4814). |

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
| InvalidAddressIdState.InArrears | The specified EIP is in arrears. |
| InvalidAddressIdStatus.NotPermit | The specified EIP in the current status cannot be bound. Only EIPs in the UNBIND status can be bound. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.AlreadyBindEip | The specified instance has been bound to an EIP. You need to unbind this EIP before binding another one. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidNetworkInterfaceId.NotFound | The specified NetworkInterfaceId does not exist or the specified PrivateIpAddress is not on the NetworkInterfaceId. |
| InvalidParameterConflict | The two parameters conflict with each other, and cannot be both specified. An EIP can only be bound to an instance or a specified private IP of a specified ENI. |
| InvalidPrivateIpAddress.AlreadyBindEip | The specified private IP of the specified ENI has been bound to an EIP. A private IP cannot be bound to more than one EIP. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |
| MissingResourceId | The entity to be bound to is missing. Either InstanceId or NetworkInterfaceId and PrivateIpAddress must be specified. |

## 5. Example

### Example 1 Bind an EIP to an instance

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=AssociateAddress
&AddressId=eip-ek0cdz1g
&InstanceId=ins-1bmpb9tu
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


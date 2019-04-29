## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (ModifyVpnConnectionAttribute) is used to modify VPN tunnels.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyVpnConnectionAttribute |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpnConnectionId | Yes | String | VPN tunnel instance ID, such as vpnx-f49l6u0z. |
| VpnConnectionName | No | String | VPN tunnel name, which is limited to 60 characters. |
| PreShareKey | No | String | Pre-shared key. |
| SecurityPolicyDatabases.N | No | Array of [SecurityPolicyDatabase](/document/api/215/##SecurityPolicyDatabase) | SPD policy group, such as {"10.0.0.5/24":["172.123.10.5/16"]}, where 10.0.0.5/24 is an IP address range of the VPC and 172.123.10.5/16 is an IP address range of the IDC. You can specify which IP address ranges in the VPC can communicate with which IP address ranges in your IDC. |
| IKEOptionsSpecification | No | [IKEOptionsSpecification](/document/api/215/##IKEOptionsSpecification) | IKE (Internet Key Exchange) configuration. IKE is provided with a self-protection mechanism. The network security protocol is configured by the user. |
| IPSECOptionsSpecification | No | [IPSECOptionsSpecification](/document/api/215/##IPSECOptionsSpecification) | IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)


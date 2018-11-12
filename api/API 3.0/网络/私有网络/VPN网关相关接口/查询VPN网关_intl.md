## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeVpnGateways) is used to query the VPN gateway list.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeVpnGateways |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpnGatewayIds.N | No | Array of String | VPN gateway instance ID, such as vpngw-f49l6u0z. A maximum of 100 instances are allowed for each request. VpnGatewayIds and Filters cannot be specified at the same time. |
| Filters.N | No | Array of [FilterObject](/document/api/215/##FilterObject) | Filter object attributes |
| Offset | No | Integer | Offset |
| Limit | No | Integer | Number of requested objects |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| VpnGatewaySet | Array of [VpnGateway](/document/api/215/##VpnGateway) | Details of VPN gateway instances. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidVpnGatewayId.Malformed | Invalid VPN gateway. The VPN instance ID is invalid. |
| InvalidVpnGatewayId.NotFound | Invalid VPN gateway. The VPN instance does not exist. Verify whether the resource information you entered is correct. |

## 5. Example

### Example 1 Query VPN gateways

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeVpnGateways
&Version=2017-03-12
&Offset=0
&Limit=2
&Filters.0.Name=vpn-gateway-name
&Filters.0.Values.0=TEST
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
    "TotalCount": 10,
    "VpnGatewaySet": [
      {
        "CreatedTime": "2018-03-25 16:05:22",
        "ExpiredTime": "0000-00-00 00:00:00",
        "InstanceChargeType": "POSTPAID_BY_HOUR",
        "InternetMaxBandwidthOut": 5,
        "IsAddressBlocked": false,
        "PublicIpAddress": "",
        "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
        "State": "PENDING",
        "Type": "IPSEC",
        "VpcId": "vpc-ngenl4az",
        "VpnGatewayId": "vpngw-rn2yn85v",
        "VpnGatewayName": "TEST_POSTPAID"
      },
      {
        "CreatedTime": "2017-02-08 12:55:00",
        "ExpiredTime": "0000-00-00 00:00:00",
        "InstanceChargeType": "PREPAID",
        "InternetMaxBandwidthOut": 5,
        "IsAddressBlocked": false,
        "PublicIpAddress": "",
        "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
        "State": "PENDING",
        "Type": "IPSEC",
        "VpcId": "vpc-lzwkkgyz",
        "VpnGatewayId": "vpngw-fa4hsbed",
        "VpnGatewayName": "leo-test-3"
      }
    ]
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


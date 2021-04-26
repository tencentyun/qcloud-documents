## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (CreateVpnGateways) is used to create VPN gateways.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateVpnGateway |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpcId | Yes | String | VPC instance ID. You can obtain the parameter value from the VpcId field value in the returned result of API DescribeVpcs. |
| VpnGatewayName | Yes | String | VPN gateway name, which is limited to 60 bytes. |
| InternetMaxBandwidthOut | Yes | Integer | Public network bandwidth setting. Available bandwidth specifications: 5, 10, 20, 50, and 100 (in Mbps) |
| InstanceChargeType | No | String | Billing method of the VPN gateway. PREPAID: Prepaid; POSTPAID_BY_HOUR: Postpaid. Default is POSTPAID_BY_HOUR. If the prepaid mode is specified, the parameter InstanceChargePrepaid is required. |
| InstanceChargePrepaid | No | [InstanceChargePrepaid](/document/api/215/##InstanceChargePrepaid) | Indicates the relevant parameter setting for the prepaid mode. This parameter can specify the purchased usage period, whether to set automatic renewal, and other attributes of the instance purchased on a prepaid basis. This parameter is required if the billing method for the specified instance is prepaid. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| VpnGateway | [VpnGateway](/document/api/215/##VpnGateway) | VPN gateway object |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. |
| InvalidVpcId.Malformed | Invalid VPC. The VPC instance ID is invalid. |
| InvalidVpcId.NotFound | Invalid VPC. The VPC resource does not exist. |

## 5. Example

### Example 1 Create a postpaid gateway

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateVpnGateway
&Version=2017-03-12
&VpcId=vpc-ngenl4az
&VpnGatewayName=TEST_POSTPAID_VPNGW
&InstanceChargeType=POSTPAID_BY_HOUR
&InternetMaxBandwidthOut=5
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "1dede54a-bbad-4d7b-9110-c7cb1ed7c152",
    "VpnGateway": {
      "InstanceChargeType": "POSTPAID_BY_HOUR",
      "State": "Pending",
      "Type": "IPSEC",
      "VpcId": "vpc-ngenl4az",
      "VpnGatewayId": "vpngw-rn2yn85v",
      "VpnGatewayName": "TEST_POSTPAID_VPNGW"
    }
  }
}
```

### Example 2 Create a prepaid gateway

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateVpnGateway
&Version=2017-03-12
&VpcId=vpc-5rkcp0wb
&VpnGatewayName=TEST_PREPAID_VPNGW
&InstanceChargeType=PREPAID
&InternetMaxBandwidthOut=5
&InstanceChargePrepaid.Period=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "7e553bb7-5603-4b79-a9f5-ecfe37d9eb27",
    "VpnGateway": {
      "InstanceChargeType": "PREPAID",
      "State": "Pending",
      "Type": "IPSEC",
      "VpcId": "vpc-5rkcp0wb",
      "VpnGatewayId": "vpngw-97yhzme3",
      "VpnGatewayName": "TEST_PREPAID_VPNGW"
    }
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


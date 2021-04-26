## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

 This API (DescribeVpnConnections) is used to query the VPN tunnel list.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeVpnConnections |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpnConnectionIds.N | No | Array of String | VPN tunnel instance ID, such as vpnx-f49l6u0z. A maximum of 100 instances are allowed for each request. VpnConnectionIds and Filters cannot be specified at the same time. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter condition. For more information, see the Table of Instance Filter Conditions below. The maximum number of Filters for each request is 10, and the maximum number of Filter.Values is 5. VpnConnectionIds and Filters cannot be specified at the same time. |
| Offset | No | Integer | Offset. Default is 0. For more information about Offset, see the relevant section in API Introduction. |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| VpnConnectionSet | Array of [VpnConnection](/document/api/215/##VpnConnection) | VPN tunnel instance. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter.Coexist | Parameters specified conflict with each other. |
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Query the VPN tunnel list

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeVpnConnections
&Version=2017-03-12
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
    "TotalCount": 1,
    "VpnConnectionSet": [
      {
        "CreatedTime": "2017-08-0510: 27: 32",
        "CustomerGatewayId": "cgw-l4rblw63",
        "EncryptProto": "IKE",
        "IKEOptionsSpecification": {
          "DhGroupName": "GROUP1",
          "ExchangeMode": "MAIN",
          "IKESaLifetimeSeconds": "86400",
          "IKEVersion": "IKEV1",
          "LocalAddress": "183.60.249.17",
          "LocalFqdnName": "",
          "LocalIdentity": "ADDRESS",
          "PropoAuthenAlgorithm": "MD5",
          "PropoEncryAlgorithm": "3DES-CBC",
          "RemoteAddress": "183.60.249.126",
          "RemoteFqdnName": "",
          "RemoteIdentity": "ADDRESS"
        },
        "IPSECOptionsSpecification": {
          "EncapMode": "TUNNEL",
          "EncryptAlgorithm": "3DES-CBC",
          "IPSECSaLifetimeSeconds": "3600",
          "IPSECSaLifetimeTraffic": "1843200",
          "IntegrityAlgorith": "MD5",
          "PfsDhGroup": "NULL",
          "SecurityProto": "ESP"
        },
        "NetStatus": "UNAVAILABLE",
        "PreShareKey": "123456",
        "RouteType": "STATIC",
        "SecurityPolicyDatabaseSet": [
          {
            "LocalCidrBlock": "172.16.0.0/16",
            "RemoteCidrBlock": [
              "10.10.0.0/16"
            ]
          }
        ],
        "State": "AVAILABLE",
        "VpcId": "vpc-0a36uwkr",
        "VpnConnectionId": "vpnx-5p7vkch8",
        "VpnConnectionName": "testjoan",
        "VpnGatewayId": "vpngw-p4lmqawn",
        "VpnProto": "IPSEC"
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


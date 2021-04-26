## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

 This API (DescribeRouteTables) is used to query route tables.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeRouteTables |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| RouteTableIds.N | Yes | Array of String | Route table instance ID, such as rtb-azd4dt1c. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | Filter condition. This parameter does not support specifying both RouteTableIds and Filters.<br/><li> route-table-id - String - (Filter condition) Route table instance ID.</li><li> route-table-name - String - (Filter condition) Route table name.</li><li> vpc-id - String - (Filter condition) VPC instance ID, such as vpc-f49l6u0z.</li><li> association.main - String - (Filter condition) Indicates whether it is the main route table.</li> |
| Offset | No | String | Offset. |
| Limit | No | String | Number of request objects. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances matching the filter condition. |
| RouteTableSet | Array of [RouteTable](/document/api/215/##RouteTable) | Route table object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter.Coexist | Parameters specified conflict with each other. |
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Query the list of route table objects

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeRouteTables
&Version=2017-03-12
&Offset=0
&Limit=1
&Filters.0.Name=route-table-id
&Filters.0.Values.0=rtb-l2h8d7c2
&Filters.1.Name=vpc-id
&Filters.1.Values.0=vpc-2at5y1pn
&Filters.2.Name=route-table-name
&Filters.2.Values.0=TestRouteTable
&Filters.3.Name=association.main
&Filters.3.Values.0=true
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
    "RouteTableSet": [
      {
        "AssociationSet": [],
        "CreatedTime": "2017-06-30 19:52:03",
        "Main": false,
        "RouteSet": [
          {
            "DestinationCidrBlock": "169.254.64.0/23",
            "GatewayId": "172.16.0.25",
            "GatewayType": "NORMAL_CVM",
            "RouteDescription": "",
            "RouteId": 14915
          },
          {
            "DestinationCidrBlock": "10.254.64.0/24",
            "GatewayId": "172.16.0.26",
            "GatewayType": "NORMAL_CVM",
            "RouteDescription": "",
            "RouteId": 14916
          },
          {
            "DestinationCidrBlock": "10.254.100.0/24",
            "GatewayId": "172.16.0.26",
            "GatewayType": "NORMAL_CVM",
            "RouteDescription": "whoIam",
            "RouteId": 14917
          },
          {
            "DestinationCidrBlock": "10.200.0.0/18",
            "GatewayId": "pcx-4n2m594s",
            "GatewayType": "PEERCONNECTION",
            "RouteDescription": "bb",
            "RouteId": 16642
          }
        ],
        "RouteTableId": "=rtb-l2h8d7c2",
        "RouteTableName": "TestRouteTable",
        "VpcId": "vpc-2at5y1pn"
      }
    ],
    "TotalCount": 16
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


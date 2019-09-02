## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (CreateRouteTable) is used to create a route table.
* When a VPC is created, the system will create a default route table with which all new subnets will be associated. By default, you can use the default route table to manage your routing policies. It you have many routing policies, you can call the API "Create Route Table" to create more route tables to manage your routing policies.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateRouteTable |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| VpcId | Yes | String | ID of the VPC instance you are working with. You can obtain the parameter value from the VpcId field value in the returned result of API DescribeVpcs. |
| RouteTableName | Yes | String | Route table name, which is limited to 60 characters. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RouteTable | [RouteTable](/document/api/215/##RouteTable) | Route table object. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Malformed | Invalid input parameter format. |
| ResourceNotFound | Resource does not exist. |

## 5. Example

### Example 1 Create a route table

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=CreateRouteTable
&Version=2017-03-12
&RouteTableName=TestRouteTable
&VpcId=vpc-2at5y1pn
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
    "RouteTable": {
      "AssociationSet": [],
      "Main": false,
      "RouteSet": [],
      "RouteTableId": "rtb-azd4dt1c",
      "RouteTableName": "TestRouteTable",
      "VpcId": "vpc-2at5y1pn"
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


## 1. API Description

Domain name for API request: vpc.tencentcloudapi.com.

This API (DescribeAddresses) is used to query the details of one or more [Elastic IPs](https://cloud.tencent.com/document/product/213/1941) (EIP).
* If the parameter is empty, a certain number (specified by Limit, the default is 20) of EIPs are returned to the current user.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: vpc.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/215/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeAddresses |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/215/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| AddressIds.N | No | Array of String | List of unique IDs of EIPs. Example of the unique ID of an EIP: `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time. |
| Filters.N | No | Array of [Filter](/document/api/215/##Filter) | The maximum number of `Filters` for each request is 10, and the maximum number of `Filter.Values` is 5. `AddressIds` and `Filters` cannot be specified at the same time. Specific filter conditions are described as follows:<br/><li> address-id - String - Required: No - (Filter condition) Filter by the unique ID of EIP. Example of the unique ID of an EIP: eip-11112222.</li><li> address-name - String - Required: No - (Filter condition) Filter by EIP name. Fuzzy filtering is not supported.</li><li> address-ip - String - Required: No - (Filter condition) Filter by the IP address of EIP.</li><li> address-status - String - Required: No - (Filter condition) Filter by EIP status. Value range: See the [EIP status list](https://cloud.tencent.com/document/api/213/9452#eip_state).</li><li> instance-id - String - Required: No - (Filter condition) Filter by ID of instance bound with EIP. Example of an instance ID: ins-11112222.</li><li> private-ip-address - String - Required: No - (Filter condition) Filter by the private IP bound with EIP.</li><li> network-interface-id - String - Required: No - (Filter condition) Filter by ID of ENI bound with EIP. Example of an ENI ID: eni-11112222.</li><li> is-arrears - String - Required: No - (Filter condition) Filter by whether the EIP is in arrears. (TRUE: EIP is in arrears&#124;FALSE: EIP is paid normally.)</li> |
| Offset | No | Integer | Offset. Default is 0. For more information about `Offset`, see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/11646). |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. For more information about `Limit`, see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/11646). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of EIPs that meet the condition. |
| AddressSet | Array of [Address](/document/api/215/##Address) | List of details of EIPs. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/215/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameter | Invalid input parameter. |

## 5. Example

### Example 1 Query EIPs using AddressIds

#### Input example

```
https://vpc.tencentcloudapi.com/?Action=DescribeAddresses
&AddressIds.0=eip-hxlqja90
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "AddressSet": [
      {
        "AddressId": "eip-hxlqja90",
        "AddressIp": "123.121.34.33",
        "AddressName": "test",
        "AddressStatus": "BINDED",
        "CreatedTime": "2017-09-12T07:52:00Z",
        "InstanceId": "ins-m2j0thu6",
        "IsArrears": false,
        "IsBlocked": false,
        "NetworkInterfaceId": null,
        "PrivateAddressIp": null
      }
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
    "TotalCount": 1
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


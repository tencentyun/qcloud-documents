## 1. API Description

This API (DescribeAddresses) is used to query the details of one or more [Elastic IPs](https://intl.cloud.tencent.com/document/product/213/5733) (EIPs).

Domain name for API request: eip.api.qcloud.com

* If the parameter is empty, a certain number (specified by Limit, the default is 20) of EIPs are returned to the current user.

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter  | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| AddressIds.N | Array of String | No | List of unique IDs of EIPs, such as `eip-11112222`. `AddressIds` and `Filters` cannot be specified at the same time. |
| Filters.N | Array of [Filter](https://cloud.tencent.com/document/api/213/9451#filter) objects | No | Filter criteria can be found in Table of EIP Filter Criteria. The maximum number of `Filters` of each request is 10, and the maximum number of `Filter.Values` is 5. `AddressIds` and `Filters` cannot be specified at the same time. |
| Offset | Integer | No | Offset. Default is 0. For more information on `offset`, please see relevant sections in API [Introduction](/document/api/213/11646). |
| Limit | Integer | No | Number of results to be returned. Default is 20. Maximum is 100. For more information on `limit`, please see relevant sections in API [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |


Table of EIP Filter Criteria

| Parameter| Type | Required | Description |
|---------|---------|---------|---------|
| address-id | String | No | (Filter criteria) Filter by the unique EIP ID, such as `eip-11112222`. |
| address-name | String | No | (Filter criteria) Filter by EIP name. Fuzzy filter is not supported. |
| address-ip | String | No | (Filter criteria) Filter by EIP address.|
| address-status | String | No | Filter by the EIP status. Value range: Please see [EIP Status List](/document/api/213/9452#eip_state). |
| instance-id | String | No | (Filter criteria) Filter by the ID of the instance to which the EIP is bound, such as `ins-11112222`. |
| private-ip-address | String | No | (Filter criteria) Filter by the private IP to which the EIP is bound. |
| network-interface-id | String | No | (Filter criteria) Filter by the ID of the ENI to which the EIP is bound, such as `eni-11112222`. |
| is-arrears | String | No | (Filter criteria) Filter by whether the EIP is in arrears. Value range:<br><li>TRUE: EIP is in arrears<br><li>FALSE: EIP is paid normally. |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| TotalCount | Integer | Number of EIPs that meet the condition. |
| AddressSet | Array of [Address](/document/api/213/9451#address) objects | List of EIP details.|


## 4. Sample Codes
### Example 1

> **Using `AddressIds` to query EIPs:**<br>

### Request Parameters
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddresses
&Version=2017-03-12
&AddressIds.1=eip-hxlqja90
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
  "Response": {
    "TotalCount": 1,
    "AddressSet": [
      {
        "AddressId": "eip-hxlqja90",
        "AddressName": "test",
        "AddressIp": "123.121.34.33",
        "AddressStatus": "BINDED",
        "InstanceId": "ins-m2j0thu6",
        "NetworkInterfaceId": null,
        "PrivateAddressIp": null,
        "IsArrears": False,
        "IsBlocked": False,
        "CreatedTime": "2017-09-12T07:52:00Z"
      }
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
</pre>

### Example 2

> ** Use `Filters` to query the EIP:**<br>

### Request Parameters
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=DescribeAddresses
&Version=2017-03-12
&Filters.1.Name=address-id
&Filters.1.Values.1=eip-hxlqja90
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
  "Response": {
    "TotalCount": 1,
    "AddressSet": [
      {
        "AddressId": "eip-hxlqja90",
        "AddressName": "test",
        "AddressIp": "123.121.34.33",
        "AddressStatus": "BINDED",
        "InstanceId": "ins-m2j0thu6",
        "NetworkInterfaceId": null,
        "PrivateAddressIp": null,
        "IsArrears": False,
        "IsBlocked": False,
        "CreatedTime": "2017-09-12T07:52:00Z"
      }
    ],
    "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
</pre>


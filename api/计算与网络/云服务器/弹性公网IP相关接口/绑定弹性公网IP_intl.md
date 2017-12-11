## 1. API Description

This API (AssociateAddress) is used to bind an [Elastic IP](/document/product/213/1941) (EIP) to a specified private IP of an instance or ENI.

Domain name for API request: eip.api.qcloud.com


* Essentially, binding an EIP to an instance means binding the EIP to the primary private IP of the primary ENI on the instance.
* When you bind an EIP to the primary private IP of a primary ENI, the previously bound public IP is automatically unbound and released.
* If the private IP of the specified ENI has bound an EIP, unbind the EIP before binding a new one.
* EIP that is in arrears or blocked cannot be bound.
* Only the EIP with a status of UNBIND is allowed to be bound.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| AddressId | String| Yes | The unique ID of an EIP, such as `eip-11112222`. |
| InstanceId | String | No | The ID of the instance to bind, such as `ins-11112222`. You can obtain the instance ID by either of the following ways: query the instance ID via [Console](https://console.cloud.tencent.com/cvm); obtain the instance ID from the `InstanceId` field of the returned values of API [DescribeInstances](/document/api/213/9389).
| NetworkInterfaceId | String | No| The ID of the ENI to bind, such as `eni-11112222`. `NetworkInterfaceId` and `InstanceId` cannot be specified at the same time. You can obtain the ENI ID by either of the following ways: query the ENI ID via [Console](https://console.cloud.tencent.com/vpc/eni); obtain the ENI ID from the `networkInterfaceId` field of the returned values of API [DescribeNetworkInterfaces](/document/api/215/4814). |
| PrivateIpAddress | String | No | The private IP to bind. If `NetworkInterfaceId` is specified, `PrivateIpAddress` must also be specified, which means binding an EIP to the specified private IP of the specified ENI. Make sure that the specified `PrivateIpAddress` is a private IP of the specified `NetworkInterfaceId`. You can obtain the private IP of a specified ENI by either of the following ways: query the private IP via [Console](https://console.cloud.tencent.com/vpc/eni); obtain the private IP from the `privateIpAddress` field of the returned values of API [DescribeNetworkInterfaces](/document/api/215/4814). |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidAddressId.NotFound | The specified EIP does not exist. |
| InvalidAddressId.Blocked | The specified EIP is blocked. You cannot bind the EIP until it is unblocked. |
| InvalidAddressIdState.InArrears | The specified EIP is in arrears. |
| InvalidAddressIdStatus.NotPermit | The EIP in the current status cannot be bound. You can only bind the EIP with a status of UNBIND. |
| InvalidInstanceId.NotFound | The specified instance ID does not exist. |
| InvalidInstanceId.AlreadyBindEip | The instance has bound an EIP. You need to unbind the EIP before binding another one. |
| InvalidInstance.NotSupported | The EIP cannot be bound to the instance in the current status. |
| InvalidNetworkInterfaceId.NotFound | The specified `NetworkInterfaceId` does not exist or the specified `PrivateIpAddress` is not on `NetworkInterfaceId`. |
| InvalidPrivateIpAddress.AlreadyBindEip | The specified private IP of the specified ENI has bound an EIP. You cannot bind another EIP for the private IP. |
| InvalidParameterConflict | The specified two parameters conflict. The EIP can only be bound to the instance or the specified private IP of the specified ENI. |
| MissingParameter | The required parameter is missing. `NetworkInterfaceId` and `PrivateIpAddress` must be specified at the same time, indicating that binding the EIP to the specified private IP of the specified ENI. |
| MissingResourceId | The instance to bind is missing. Either `InstanceId` or `NetworkInterfaceId` and `PrivateIpAddress` must be specified. |



## 5. Sample Codes


### Example 1

> **Bind an EIP to an instance:**<br>


### Request Parameters
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &InstanceId=ins-1bmpb9tu
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


### Example 2

> **Bind an EIP to the specified private IP of the specified ENI:**<br>


### Request Parameters
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=AssociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &NetworkInterfaceId=eni-8x55qvrh
  &PrivateIpAddress=10.0.0.2
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


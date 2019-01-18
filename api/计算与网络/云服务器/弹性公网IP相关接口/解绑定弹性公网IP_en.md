## 1. API Description

This API (DisassociateAddress) is used to unbind an [Elastic IP](/document/product/213/1941) (EIP).

Domain name for API request: eip.api.qcloud.com

* You can only unbind the EIP with a status of BIND or BIND_ENI.
* The blocked EIP cannot be unbound.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| AddressId | String| Yes | The unique ID of an EIP, such as `eip-11112222`. |
| ReallocateNormalPublicIp | String| No | Whether to assign an ordinary public IP after the EIP is unbound. Value range:<br><li>TRUE: assign an ordinary public IP after the EIP is unbound.<br><li>FALSE: not assign an ordinary public IP after the EIP is unbound.<br>Default: FALSE.<br><br>The parameter can be specified only under the following conditions:<br><li>The EIP is unbound from the primary private IP of the primary ENI.<br><li>After the EIP is unbound, you can assign at most ten ordinary public IPs to an account per day. Details can be found in [DescribeAddressQuota](/document/api/213/1378). |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidAddressId.NotFound | The specified EIP does not exist. |
| InvalidAddressId.Blocked | The specified EIP is blocked. You cannot unbind the EIP until it is unblocked. |
| InvalidAddressIdStatus.NotPermit | The EIP in the current status cannot be unbound. You can only unbind the EIP with a status of BIND or BIND_ENI. |
| InvalidInstanceId.NotFound | The specified instance ID does not exist. |
| InvalidInstance.NotSupported | The EIP cannot be unbound from the instance in the current status. |
| InvalidParameter | The parameter value is invalid. |
| AddressQuotaLimitExceeded.DailyAllocate | The maximum number of ordinary public IPs that can be re-assigned to the account per day is exceeded. More information on the quota can be found in [DescribeAddressQuota](/document/api/213/1378). |


## 5. Sample Codes


### Example 1

> **Unbind an EIP:**<br>


### Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DisassociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Output
<pre>
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


### Example 2

> **Unbind an EIP and assign an ordinary public IP:**<br>
> This operation is supported only when the EIP is bound to the primary private IP of the primary ENI.


### Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DisassociateAddress
  &Version=2017-03-12
  &AddressId=eip-ek0cdz1g
  &ReallocateNormalPublicIp=TRUE
  &<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Output
<pre>
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
</pre>


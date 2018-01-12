## 1. API Description

This API (ModifyAddressAttribute) is used to modify the name of an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/5733) (EIP).

Domain name for API request: eip.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| AddressId | String| Yes| The unique ID of an EIP, such as `eip-11112222`. |
| AddressName | String | Yes | New name of the EIP, up to 20 characters. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidAddressId.NotFound | The specified EIP does not exist. |
| InvalidParameterValue.TooLong | The EIP name you set is too long. The EIP name cannot exceed 20 characters.|
| InvalidParameterValue | The parameter value is invalid. |



## 5. Example

### Input
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=ModifyAddressAttribute
&Version=2017-03-12
&AddressId=eip-p2x6wxc0
&AddressName=test_eip
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Output
<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>


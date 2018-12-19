## 1. API Description

This API (ReleaseAddresses) is used to release one or more [Elastic IPs](/document/product/213/1941) (EIP).

Domain name for API request: eip.api.qcloud.com

* This operation cannot be undone. Once you release an EIP, the IP associated with the EIP no longer belong to your account.
* Only the EIP with a status of UNBIND is allowed to be released.

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| AddressIds.N | Array of String | No | List of unique IDs of EIPs, such as `eip-11112222`. |


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidAddressId.NotFound | The specified EIP does not exist. |
| InvalidAddressState | The EIP in the current status cannot be released. You can only release the EIP with a status of UNBIND. |

## 5. Example

### Input
<pre>
https://eip.api.qcloud.com/v2/index.php?Action=ReleaseAddresses
&Version=2017-03-12
&AddressIds.1=eip-gzc5rgr2
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


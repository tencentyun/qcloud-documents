## 1. API Description

This API (DeleteKeyPairs) is used to delete the key pairs hosted in Tencent Cloud.

Domain name for API request: cvm.api.qcloud.com

* You can delete multiple key pairs at the same time.
* The key pair referenced by an instance or image cannot be deleted. You need to verify whether all the key pairs have been deleted successfully. 


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter| Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
|KeyIds.N | Array of Strings | Yes | ID(s) of one or more key pairs you are working with. The maximum number of key pairs for each request for batch operations is 100. <br><br>You can obtain the available key pair IDs by either of the following ways: <br><li>Log in to [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; <br><li>Obtain the key pair ID from the `KeyId` field in the returned values of API [DescribeKeyPairs](/document/api/213/9403). |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error Code | Description |
|---------|---------|
| MissingParameter | A required parameter is missing in the request. |
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InternalServerError | Internal operation error. |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DeleteKeyPairs
&Version=2017-03-12
&KeyIds.1=skey-mv9yzyjj
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>


## 1. API Description

This API (ModifyKeyPairAttribute) is used to modify the attributes of key pairs.

Domain name for API request: cvm.api.qcloud.com

* Modify the name and description of the key pair specified with the key pair ID.
* The name of key pair must be unique.
* Key pair ID is the unique identifier of key pair and cannot be modified.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
| ----------- | ------ | ---- | ---------------------------------------- |
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| KeyId       | String | Yes   | Key pair ID, such as `skey-11112222`. <br><br>You can obtain the available key pair IDs by either of the following ways: <br><li>Log in to [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; <br><li>Obtain the key pair ID from the `KeyId` field in the returned values of API [DescribeKeyPairs](/document/api/213/9403). |
| KeyName     | String | No   | Modified name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters.      |
| Description | String | No    | Modified description of key pair. This can be arbitrarily specified, but cannot exceed 60 characters.            |


## 3. Output Parameters

| Parameter | Type | Description |
| --------- | ------ | ---------------------------------------- |
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error Code | Description |
| -------------------------------- | ---------------------------------------- |
| MissingParameter |  A required parameter is missing in the request. |
| InvalidParameter                 | Parameter does not meet the requirement or is not supported.                    |
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| InvalidKeyPairId.Malformed       | The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidKeyPairId.NotFound        | The specified key pair ID does not exist.                     |
| InvalidKeyPairName.Duplicate     | Duplicate key pair name exists.                                 |
| InvalidKeyPairDescriptionTooLong | The key pair description exceeds 60 characters.                             |
| InternalServerError | Internal operation error. |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ModifyKeyPairAttribute
&Version=2017-03-12
&KeyId=skey-mv9yzyjj
&KeyName=Tencent
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


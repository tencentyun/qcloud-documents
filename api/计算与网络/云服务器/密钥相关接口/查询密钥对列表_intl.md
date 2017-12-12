## 1. API Description

This API (DescribeKeyPairs) is used to query key pair information.

Domain name for API request: cvm.api.qcloud.com

* [Key Pair](/document/product/213/6092) is a pair of keys generated with an algorithm. In the generated key pair, one key is open to the public and called public key, and the other key is kept by user and called private key. The public key content of the key can be queried through this API, but the private key content is not retained by system.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| KeyIds.N  | Array of Strings | No | ID of key pair, such as `skey-11112222`. (This API supports filtering multiple IDs at the same time. For the format of this parameter, please see the `id.N` section in API [Introduction](/document/api/213/11646)). This parameter does not support specifying both `KeyIds` and `Filters`.<br> The key pair ID can be queried by logging in to the [console](https://console.cloud.tencent.com/cvm/sshkey). |
| Filters.N | Array of [Filter](/document/api/213/9451#filter) objects| No | Filter condition. For more information, please see the Key Pair Filter Condition Table. This parameter does not support specifying both `KeyIds` and `Filters`. |
| Offset | Integer | No | Offset. Default is 0. For more information, please see the relevant section in API [Introduction](/document/api/213/11646#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |
| Limit | Integer | No | Number of results to be returned. Default is 20. Maximum is 100. For more information, please see the relevant section in API [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |

Key Pair Filter Condition Table

| Parameter  | Type | Required | Description |
|---------|---------|---------|---------|
|project-id| Integer| No | (Filter condition). Filter by project ID.<br><br> You can obtain the project ID by either of the following ways: <br><li>Query the project ID via [Project List](https://console.cloud.tencent.com/project);<br><li>Obtain the project ID from the `projectId` field in the returned values of API [DescribeProject](/document/api/378/4400).|
| key-name| String| No| (Filter condition). Filter by key pair name.|


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| TotalCount | Integer | The number of key pairs matching the filter condition. |
| KeyPairSet| array of [KeyPair](/document/api/213/9451#keypair) objects| List of details of key pairs. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error Code | Description |
|---------|---------|
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidParameterValueOffset | Invalid parameter value. The specified `Offset` is invalid.
| InvalidFilterValue.LimitExceeded | The number of parameter values of [`Filter`](/document/api/213/9451#filter) exceeds the limit. |
| InvalidFilter | The specified [`Filter`](/document/api/213/9451#filter) is not supported. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InternalServerError | Internal operation error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeKeyPairs
&Version=2017-03-12
&Filters.1.Name=key-name
&Filters.1.Values.1=Tencent
&Offset=0
&Limit=20
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "TotalCount": 1,
        "KeyPairSet": [
            {
                "KeyId": "skey-mv9yzyjj",
                "KeyName": "Tencent",
                "Description": "",
                "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168",
                "AssociatedInstanceIds": [
                ],
                "CreateTime": "2016-12-02T00:22:40Z"
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>


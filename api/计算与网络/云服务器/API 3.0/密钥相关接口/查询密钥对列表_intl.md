## 1. API Description

This API (DescribeKeyPairs) is used to query key pair information.

* A key pair is a pair of keys generated with an algorithm. In the generated key pair, one key is open to the public and called public key, and the other key is kept by users and called private key. The public key content of the key can be queried through this API, but the private key content is not retained by system.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeKeyPairs |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| KeyIds.N | No | Array of String | ID of the key pair, such as `skey-11112222`. (This API supports filtering multiple IDs at the same time. For the format of this parameter, please see the `id.N` section in API [Introduction](https://cloud.tencent.com/document/api/213/15688)). This parameter does not support specifying both `KeyIds` and `Filters`. The key pair ID can be queried by logging in to the [console](https://console.cloud.tencent.com/cvm/index). |
| Filters.N | No | Array of [Filter](/document/api/213/15753#Filter) | Filter conditions. <li> project-id - Integer - Required or not: No - (Filter condition) Filter by project ID. You can query the project ID via [Project List](https://console.cloud.tencent.com/project), or obtain the project ID from the projectId field in the returned values of API [DescribeProject](https://cloud.tencent.com/document/api/378/4400). </li><li> key-name - String - Required or not: No - (Filter condition) Filter by key pair name. </li> This parameter does not support specifying both `KeyIds` and `Filters`. |
| Offset | No | Integer | Offset. Default is 0. For more information, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |[AD1]
| Limit | No | Integer | Number of the results to be returned. The default is 20, and the maximum is 100. For more information, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | The number of key pairs matching the filter condition. |
| KeyPairSet | Array of [KeyPair](/document/api/213/15753#KeyPair) | List of details of key pairs. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidFilter | Invalid filter. |
| InvalidFilterValue.LimitExceeded | The number of parameter values of [`Filter`](/document/api/213/9451#filter) exceeds the limit. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValueLimit | The number of parameter values exceeds the limit. |
| InvalidParameterValueOffset | Invalid parameter value. The specified `Offset` is invalid. |

## 5. Example

## Example 1 Example

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeKeyPairs
&Filters.0.Name=key-name
&Filters.0.Values.0=Tencent
&Offset=0
&Limit=20
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "KeyPairSet": [
      {
        "AssociatedInstanceIds": [],
        "CreateTime": "2016-12-02T00:22:40Z",
        "Description": "",
        "KeyId": "skey-mv9yzyjj",
        "KeyName": "Tencent",
        "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168"
      }
    ],
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
    "TotalCount": 1
  }
}
```


        
[AD1]原文与下一句段有重复，已经提query

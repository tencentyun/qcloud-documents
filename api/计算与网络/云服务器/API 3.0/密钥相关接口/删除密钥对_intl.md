## 1. API Description

This API (DeleteKeyPairs) is used to delete the key pairs hosted in Tencent Cloud.

* You can delete multiple key pairs at the same time.
* The key pair referenced by an instance or image cannot be deleted. You need to verify whether all the key pairs have been deleted successfully.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DeleteKeyPairs |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| KeyIds.N | Yes | Array of String | ID(s) of one or more key pairs you are working with. The maximum number of key pairs in a batch for each request is 100. You can obtain the available key pair IDs by either of the following ways: <li>log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; </li><li>obtain the key pair ID from the `KeyId` parameter of the returned values of API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699). |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Delete a key pair

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DeleteKeyPairs
&KeyIds.0=skey-mv9yzyjj
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```


        

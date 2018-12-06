## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DeleteKeyPairs) is used to delete the key pairs hosted in Tencent Cloud.

* You can delete multiple key pairs at a time.
* The key pair referenced by an instance or image cannot be deleted. You need to verify whether all the key pairs have been deleted successfully.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DeleteKeyPairs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| KeyIds.N | Yes | Array of String | ID(s) of one or more key pair IDs you are working with. A maximum of 100 key pairs are allowed in a batch for each request.<br> You can obtain the available key ID by either of the following ways: <br><li>Query the key ID by logging in to the [Console](https://console.cloud.tencent.com/cvm/sshkey).<br><li> Call the API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) to obtain the key pair ID from the `KeyId` field value in the returned result. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidKeyPair.LimitExceeded | Number of key pairs exceeds the limit. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` has an invalid `ID` length. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Delete a key pair

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DeleteKeyPairs
&KeyIds.0=skey-mv9yzyjj
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```



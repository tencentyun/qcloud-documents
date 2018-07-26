## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ModifyKeyPairAttribute) is used to modify the attributes of key pairs.

* This API modifies the name and description of the key pair identified by the key pair ID.
* The name of key pair must be unique.
* Key pair ID is the unique identifier of key pair and cannot be modified.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyKeyPairAttribute |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| KeyId | Yes | String | Key pair ID, such as `skey-xxxxxxxx`.<br><br> You can obtain the available key ID by either of the following ways: <br><li>Query the key ID by logging in to the [Console](https://console.cloud.tencent.com/cvm/sshkey).<br><li> Call the API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/9403) to obtain the key pair ID from the `KeyId` field value in the returned result. |
| KeyName | No | String | Modified name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters. |
| Description | No | String | Modified description of key pair. It is limited to 60 characters. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` has an invalid `ID` length. |
| InvalidKeyPairId.NotFound | Invalid key pair ID. The specified key pair ID does not exist. |
| InvalidKeyPairName.Duplicate | Duplicate key pair name. |
| InvalidParameter | Invalid parameter. The parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Modify the key pair name

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyKeyPairAttribute
&KeyId=skey-mv9yzyjj
&KeyName=Tencent
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

### Example 2 Modify the key pair description

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyKeyPairAttribute
&KeyId=skey-mv9yzyjj
&Description=Tencent
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "aea2227b-fbb7-4cc7-bf29-d49b2b6db97c"
  }
}
```



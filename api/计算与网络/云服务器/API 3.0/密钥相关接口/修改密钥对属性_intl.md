
## 1. API Description

This API (ModifyKeyPairAttribute) is used to modify the attributes of key pairs.

* Modify the name and description of the key pair specified with the key pair ID.
* The name of key pair must be unique.
* Key pair ID is the unique identifier of key pair and cannot be modified.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyKeyPairAttribute |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| KeyId | Yes | String | Key pair ID, such as `skey-xxxxxxxx`. <br><br>You can obtain the available key pair IDs by either of the following ways: <li>log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; </li><li>obtain the key pair ID from the `KeyId` parameter of the returned values of API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/9403). |
| KeyName | No | String | Modified name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters. |
| Description | No | String | Modified description of key pair. This can be arbitrarily specified, but cannot exceed 60 characters. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidKeyPairId.NotFound | Invalid key pair ID. The specified key pair ID does not exist. |
| InvalidKeyPairName.Duplicate | Duplicate key pair name exists. |
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Modify the key pair name

### Scenario description

This example shows how to modify the key pair name.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyKeyPairAttribute
&KeyId=skey-mv9yzyjj
&KeyName=Tencent
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

## Example 2 Modify the key pair description

### Scenario description

This example shows how to modify the key pair description.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyKeyPairAttribute
&KeyId=skey-mv9yzyjj
&Description=Tencent
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "aea2227b-fbb7-4cc7-bf29-d49b2b6db97c"
  }
}
```


        

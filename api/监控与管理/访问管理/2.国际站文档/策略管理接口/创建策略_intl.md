## API Description

This API (CreatePolicy) is used to create a policy.

Request domain name:

```
cam.api.qcloud.com
```

> **Note:**
>
> For the policy created via this API (CreatePolicy), createMode is 2 by default.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------------- | ------ | ---- | -------- |
| policyName | string | Yes | Policy name |
| description | string | No | Policy description |
| policyDocument | string | Yes | Policy document |

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ---- | ------- |
| policyId | int | Policy ID |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyName=testpppName323
&policyDocument=%7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22action%22%3A%22cvm%3A%2A%22%2C%22effect%22%3A%22allow%22%2C%22resource%22%3A%22%2A%22%7D%5D%7D
&SignatureMethod=HmacSHA256
&Action=CreatePolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=19057
&Timestamp=1508489703
&RequestClient=SDK_PHP_1.1
&Signature=7mTuDFCaxt8Ki%2FtnEpvws%2BvoWcMPi1zESHpPXMElSQc%3D
```

### Output

```
 {
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "policyId": 524497
    }
}xxxxxxxxxx {    "code": 0,    "message": "",    "codeDesc": "Success",    "data": {        "policyId": 524497    }}

```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).


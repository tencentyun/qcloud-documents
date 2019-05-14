## API Description

This API (DetachUserPolicy) is used to unbind a policy from a user.

Request domain name:

```
cam.api.qcloud.com 
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | ---- | ---------- |
| policyId | int | Yes | Policy ID |
| uin | int | Yes | Sub-account uin |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyId=524497
&uin=3449203261
&SignatureMethod=HmacSHA256
&Action=DetachUserPolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=23226
&Timestamp=1508491185
&RequestClient=SDK_PHP_1.1
&Signature=wcplGgmw%2FGsggtSKSTx4nqVhZ15jJ3QOG7a%2Bp%2Btviug%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).


## API Description

This API (AddUserToGroup) is used to add a user to a user group.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ----- | ---- | ------------------------------------------------------------ |
| info | array | Yes | Index array. Array members are associative arrays, including uid (user ID) and groupId (user group ID). |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?info.0.uid=1133398
&info.0.groupId=26705
&SignatureMethod=HmacSHA256
&Action=AddUserToGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=12209
&Timestamp=1522668642
&RequestClient=SDK_PHP_1.1
&Signature=hSAeZcyfCaGxEmS2J50BBfpHAIMC9qyN5d31BmT0XNc%3D
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

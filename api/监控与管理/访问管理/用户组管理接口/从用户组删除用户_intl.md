## API Description

This API (RemoveUserFromGroup) is used to remove a user from a user group.

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
&Action=RemoveUserFromGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=36266
&Timestamp=1522668876
&RequestClient=SDK_PHP_1.1
&Signature=nu3X4yjkc%2F8CrRb72ewqKP1tB%2Bb26Cnge8lNvHhvUSE%3D
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

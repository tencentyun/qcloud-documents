## API Description

This API (UpdateGroup) is used to update a user group.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| --------- | ------ | ---- | ---------- |
| groupId | int | Yes | User group ID |
| groupName | string | No | User group name |
| remark | string | No | User group description |

## Output Parameters
None.
## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?groupId=28791
&groupName=testgrname
&remark=tee123
&SignatureMethod=HmacSHA256
&Action=UpdateGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=52700
&Timestamp=1512703514
&RequestClient=SDK_PHP_1.1
&Signature=K0vw4YiIN%2B%2FZzl7bBVZzOm7CqIvuuOlx0ZkHMQUcnUk%3D
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


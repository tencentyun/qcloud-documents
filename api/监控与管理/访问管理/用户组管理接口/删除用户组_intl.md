## API Description

This API (DeleteGroup) is used to delete a user group.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | ---- | --------- |
| groupId | int | Yes | User group ID |

## Output Parameters
None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?groupId=28791
&SignatureMethod=HmacSHA256
&Action=DeleteGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=59745
&Timestamp=1512716474
&RequestClient=SDK_PHP_1.1
&Signature=A2IYDCP1SGf%2BDoxLDerfWxKC4XEGxAigvo0HgSZr67o%3D
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


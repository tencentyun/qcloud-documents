## API Description

This API (DeleteUser) is used to delete sub-users.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ------ | ---- | ------------ |
| name | string | Yes | Sub-user name |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?name=testName
&SignatureMethod=HmacSHA256
&action=DeleteUser
&region=gz
&secretid=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=23207
&Timestamp=1506398326
&RequestClient=SDK_PHP_1.1
&Signature=VuPUIgv4nQG6h83dECMIMzuiRAr2rnNwSOzvuD0wb4Q%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

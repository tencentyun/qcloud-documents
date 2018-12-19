## API Description

This API (ListUsers) is used to pull a sub-user.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

No input parameter is needed for this API. For common parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

## Output Parameters

| Parameter Name | Type | Description |
| ------------ | ------ | -------------------- |
| uin | string | Sub-user ID |
| name | string | Sub-user name |
| uid | string | Sub-user UID |
| remark | string | Remarks for a sub-user |
| consoleLogin | int | Whether a sub-user is allowed to log in to console |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?SignatureMethod=HmacSHA256
&Action=ListUsers
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
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
        [
            "uin": "90881234151",
            "name": "testName",
            "password": "juhawe@f112",
            "secretId": "AKIDWwGVed95Zu693ltdoopjcKrDct20DKky15215",
            "secretKey": "AKIDWwGVed95Zu693ltdoopjcKrDct20DKky12562",
        ]
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

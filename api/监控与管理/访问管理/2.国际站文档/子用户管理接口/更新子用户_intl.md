## API Description

This API (UpdateUser) is used to update a sub-user.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| ----------------- | ------ | ---- | ------------------------------------------------ |
| name | string | Yes | Sub-user name |
| remark | string | No | Remarks for a sub-user |
| consoleLogin | int | No | Whether a sub-user is allowed to log in to console |
| password | string | No | Login password for the console (valid only when the sub-user is allowed to log in to the console) |
| needResetPassword | int | No | Whether a sub-user needs to reset the password when logging in the next time |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?name=testName
&remark=testRemark
&consoleLogin=1
&password=topSecret
&needResetPassword=1
&SignatureMethod=HmacSHA256
&Action=UpdateUser
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
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

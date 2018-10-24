## API Description

This API (AddUser) is used to add sub-users.

Request domain name:
```
cam.api.qcloud.com
```

## Input Parameters
The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).


| Parameter Name | Type | Required | Description |
| ----------------- | ------ | ---- | ------------------------------------------------------------ |
| name | string | Yes | Sub-user name |
| remark | string | No | Remarks for sub-user |
| consoleLogin | int | No | Whether a sub-user is allowed to log in to console |
| useApi | int | No | Whether to generate sub-user key |
| password | string | No | Login password for the console (valid only when the sub-user is allowed to log in to the console). For a user allowed to log in to console, a random password will be automatically generated if the parameter is left empty. |
| needResetPassword | int | No | Whether a sub-user needs to reset the password when logging in the next time |

## Output Parameters

| Parameter Name | Type | Description |
| --------- | ------ | ---------------------------------------------------- |
| uin | string | Sub-user ID |
| name | string | Sub-user name |
| password | string | If a random password is automatically generated based on the input parameter, the password will be returned. |
| secretId | string | Sub-user key ID |
| secretKey | string | Sub-user key |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?name=testName
&remark=testRemark
&consoleLogin=1
&useApi=1
&password=topSecret
&needResetPassword=1
&SignatureMethod=HmacSHA256
&Action=AddUser
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
        "uin": "90881234151",
        "name": "testName",
        "password": "topSecret",
        "secretId": "AKIDWwGVed95Zu693ltdoopjcKrDct20DKky15215",
        "secretKey": "AKIDWwGVed95Zu693ltdoopjcKrDct20DKky12562",
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

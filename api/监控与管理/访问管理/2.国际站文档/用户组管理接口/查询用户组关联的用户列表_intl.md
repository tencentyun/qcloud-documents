## API Description

This API (ListUsersForGroup) is used to query the list of users associated with a user group.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | ---- | ------------------------------------- |
| page | int | Yes | Page number, which starts from 1 and cannot be greater than 200 |
| rp | int | Yes | Number of items on each page, which must be greater than 0 and less than or equal to 200 |
| groupId | int | Yes | User group ID |

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ----- | ------------------------------------------------------------ |
| totalNum | int | The total number of users associated with a user group |
| userInfo | array | Array of users, where each member includes the following fields: uid (user ID), uin (user uin), name (user name), createTime (creation time), isReceiverOwner (whether the main account is used) |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?rp=10
&page=1
&groupId=23742
&SignatureMethod=HmacSHA256
&Action=ListUsersForGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=53463
&Timestamp=1510737439
&RequestClient=SDK_PHP_1.1
&Signature=43rnmIrGF64te4WuPdWgBDdHPRAU1CsuF19WUR8dxVc%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "groupInfo": [],
        "totalNum": "1",
        "userInfo": [
            {
                "uid": 1133398,
                "uin": 3449203261,
                "name": "test1",
                "phoneNum": "13631422209",
                "countryCode": "86",
                "phoneFlag": 0,
                "email": "2385420691@qq.com",
                "emailFlag": 0,
                "userType": 3,
                "createTime": "2017-09-04 16:40:15",
                "isReceiverOwner": 0
            }
        ]
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

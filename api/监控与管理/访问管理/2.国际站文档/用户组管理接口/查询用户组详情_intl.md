## API Description

This API (GetGroup) is used to list the details of a user group.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | -------- | --------- |
| groupId | int | Yes | User group ID |

## Output Parameters

| Parameter Name | Type | Description |
| ---------- | ------ | ------------------------------------------------------------ |
| groupId | int | User group ID |
| groupName | string | User group name |
| groupNum | int | Number of members in a user group |
| remark | string | User group description |
| createTime | String | Time when a user group is created |
| userInfo | array | Array of indexes, where a member is an associative array, indicating a user who joins the user group. Member fields include uid (user group), uin (sub-account uin), name (sub-account nickname) |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?groupId=28791
&SignatureMethod=HmacSHA256
&Action=GetGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=64065
&Timestamp=1512715507
&RequestClient=SDK_PHP_1.1
&Signature=cmXkOx7XeFtmhmaCJTUTUmKYPZ5vT4S6LjIGBnRiTL4%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "groupId": 28791,
        "groupName": "testgrname",
        "groupNum": 1,
        "channel": 3,
        "remark": "tee123",
        "createTime": "2017-12-08 11:15:56",
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

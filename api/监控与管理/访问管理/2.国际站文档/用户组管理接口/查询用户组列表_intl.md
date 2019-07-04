## API Description

This API (ListGroups) is used to query the list of user groups.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ------ | ---- | ------------------------------------- |
| page | int | Yes | Page number, which starts from 1 and cannot be greater than 200 |
| rp | int | Yes | Number of items on each page, which must be greater than 0 and less than or equal to 200 |
| keyword | string | No | Match based on user group name |

## Output Parameters

| Parameter Name | Type | Description |
| --------- | ----- | ------------------------------------------------------------ |
| totalNum | int | Total number of user groups |
| groupInfo | array | Array of user groups, where each member has the following fields: groupId (user group ID), groupName (user group name), createTime (time when a user group is created), remark (user group description). |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?rp=10
&page=1
&SignatureMethod=HmacSHA256
&Action=ListGroups
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=21810
&Timestamp=1510736488
&RequestClient=SDK_PHP_1.1
&Signature=d8ZMD4byKJB0vBVqLqj0NJoyMa3c5DtFsZcbw1oLCEk%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "groupInfo": [
            {
                "groupId": 26705,
                "groupName": "ckwmwsllx",
                "channel": 3,
                "remark": "Zhehenxiyou 5",
                "createTime": "2017-10-23 20:49:49"
            },
            {
                "groupId": 23742,
                "groupName": "gtdx",
                "channel": 3,
                "remark": null,
                "createTime": "2017-07-24 19:42:39"
            }
        ],
        "totalNum": "2"
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

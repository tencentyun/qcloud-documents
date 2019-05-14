## API Description

This API (CreateGroup) is used to create a user group.

Request domain name:

```
cam.api.qcloud.com
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| --------- | ------ | ---- | ---------- |
| groupName | string | No | User group name |
| remark | string | No | User group description |

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ---- | ---- |
| groupId | int | User group ID |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?groupName=testgroupname
&remark=testre123
&SignatureMethod=HmacSHA256
&Action=CreateGroup
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=38803
&Timestamp=1512702940
&RequestClient=SDK_PHP_1.1
&Signature=p4APCiYw5pHhjVk9Fwjk6U9n2%2FuTTaVGzSehd2G4YZc%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "groupId": 28791
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).

## API Description

This API (AttachGroupPolicy) is used to associate a policy to a user group.

Request domain name:

```
cam.api.qcloud.com 
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | ---- | --------- |
| policyId | int | Yes | Policy ID |
| groupId | int | Yes | User group ID |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyId=1
&groupId=34444
&SignatureMethod=HmacSHA256
&Action=AttachGroupPolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=28335
&Timestamp=1523261970
&RequestClient=SDK_PHP_1.1
&Signature=QeBOuhSP6G5NLgzkkY3At6I9hjGxxfLO1PkDhsGwnsc%3D
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


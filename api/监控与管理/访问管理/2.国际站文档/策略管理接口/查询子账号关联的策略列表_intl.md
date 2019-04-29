## API Description

This API (ListAttachedUserPolicies) is used to query the list of policies associated with a sub-account.

Request domain name:

```
cam.api.qcloud.com 
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | ---- | --------------------------- |
| uin | int | Yes | Sub-account uin |
| page | int | No | Page number, which starts from 1. Default is 1. |
| rp | int | No | Page size. Default is 20. |

## Output Parameters

For more information on API description, please see [ListPolicies](https://cloud.tencent.com/document/product/598/15426).

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?uin=3449203261
&page=1
&rp=20
&SignatureMethod=HmacSHA256
&Action=ListAttachedUserPolicies
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=33994
&Timestamp=1508492653
&RequestClient=SDK_PHP_1.1
&Signature=YQflvL9ZCPDfTJNum84oXRQex6iKKTNi2fwgLUh2qZE%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalNum": 5,
        "list": [
            {
                "policyId": 524497,
                "policyName": "testpppName323",
                "addTime": "2017-10-20 17:26:16",
                "createMode": 2
            },
            {
                "policyId": 296232,
                "policyName": "QcloudCCSInnerFullAccess",
                "addTime": "2017-10-20 17:11:19",
                "createMode": 2
            },
            {
                "policyId": 514581,
                "policyName": "dsc35trc56",
                "addTime": "2017-10-16 16:33:28",
                "createMode": 1
            },
            {
                "policyId": 419082,
                "policyName": "QcloudCCRFullAccess",
                "addTime": "2017-09-15 16:35:03",
                "createMode": 2
            },
            {
                "policyId": 219851,
                "policyName": "QcloudCLBReadOnlyAccess",
                "addTime": "2017-09-04 16:40:15",
                "createMode": 2
            }
        ]
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).


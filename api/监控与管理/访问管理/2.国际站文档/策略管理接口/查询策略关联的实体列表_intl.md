## API Description

This API (ListEntitiesForPolicy) is used to query the list of instances associated with a policy.

Request domain name:

```
cam.api.qcloud.com 
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| ------------ | ------ | ------| ------------------------------------------------------------ |
| policyId | int | Yes | Policy ID |
| page | int | No | Page number, which starts from 1. Default is 1. |
| rp | int | No | Page size. Default is 20 |
| entityFilter | string | No | Available values: 'All', 'User', 'Group' and 'Role'. 'All': All types of instances; 'User': Only sub-accounts; 'Group': Only user groups; 'Role': Only roles. Default is 'All'. |

## Output Parameters

| Parameter Name | Type | Description |
| ----------- | ------ | -------------------------------------- |
| id | string | ID of a sub-account, role, or user group |
| relatedType | int | 1: Sub-account; 2: User group: 3: Role |
| name | string | Name of sub-account, role, or user group |
| uin | int | Sub-account uin (optional) |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyId=524497
&page=1
&rp=20
&SignatureMethod=HmacSHA256
&Action=ListEntitiesForPolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=2216
&Timestamp=1508491800
&RequestClient=SDK_PHP_1.1
&Signature=B1tsiw%2Bo0OJKF4YCAFncte%2BnjU1Sc4bmU9KVx4sCxjo%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalNum": 2,
        "list": [
            {
                "id": "23742",
                "relatedType": 2,
                "name": "gtdx"
            },
            {
                "id": "1133398",
                "relatedType": 1,
                "uin": 3449203261,
                "name": "test1"
            }
        ]
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).


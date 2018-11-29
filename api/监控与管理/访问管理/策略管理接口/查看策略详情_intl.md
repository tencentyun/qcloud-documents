## API Description

This API (GetPolicy) is used to query the details of a policy.

Request domain name:

  ```
cam.api.qcloud.com
  ```

> **Note:**
>
>This API (GetPolicy) can only be used to query the details of a policy with createMode not equal to 1.

## Input Parameters 

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ---- | ---- | ------- |
| policyId | int | Yes | Policy ID |

## Output Parameters

| Parameter Name | Type | Description |
| -------------- | ------ | ------------------------ |
| policyName | string | Policy name |
| description | string | Policy description |
| type | int | 1: Custom policy; 2: Preset policy |
| addTime | string | Time when a policy is created |
| updateTime | string | Latest update time of a policy |
| policyDocument | array | Policy document |

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyId=1
&SignatureMethod=HmacSHA256
&Action=GetPolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=38353
&Timestamp=1508487969
&RequestClient=SDK_PHP_1.1
&Signature=hYDq3kqcJUDft%2Fc7AvBqAL1OkK1ZpZCPkZ9LcwTiXXk%3D
```

### Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "policyDocument": {
            "version": "2.0",
            "statement": [
                {
                    "effect": "allow",
                    "action": "*",
                    "resource": "*"
                }
            ]
        },
        "updateTime": "2017-09-04 11:50:19",
        "addTime": "2016-06-02 19:40:09",
        "policyName": "AdministratorAccess",
        "description": "This policy allows you to manage all users under your account and their permissions, financial information and Cloud assets.",
        "type": 2
    }
}
```

## Error Codes

For more information, please see [Error Codes](https://cloud.tencent.com/document/product/598/13884).


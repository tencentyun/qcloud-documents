## API Description

This API (UpdatePolicy) is used to update a policy.

Request domain name:

```
cam.api.qcloud.com 
```

> **Note:**
>
> This API (UpdatePolicy) can only be used to update policies with createMode=2.

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------------- | ------ | ---- | -------- |
| policyId | int | Yes | Policy ID |
| policyName | string | No | Policy name |
| description | string | No | Policy description |
| policyDocument | string | No | Policy document |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyId=524497
&policyName=testpppName1827
&policyDocument=%7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22action%22%3A%22clb%3A%2A%22%2C%22effect%22%3A%22allow%22%2C%22resource%22%3A%22%2A%22%7D%5D%7D
&SignatureMethod=HmacSHA256
&Action=UpdatePolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=51231
&Timestamp=1508493076
&RequestClient=SDK_PHP_1.1
&Signature=vYb7gUVyg2POAj8Bgfc7SqgJ%2FB5ob9YFjRcdVH78M8U%3D
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


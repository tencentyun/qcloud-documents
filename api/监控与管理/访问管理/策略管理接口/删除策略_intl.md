## API Description

This API (DeletePolicy) is used to delete a policy.

Request domain name:

```
cam.api.qcloud.com 
```

## Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Type | Required | Description |
| -------- | ----- | ---- | ----------------------------------------- |
| policyId | array | Yes | Array, whose members are policy IDs. Deleting policies in batches is supported. |

## Output Parameters

None.

## Example

### Input

```
https://cam.api.qcloud.com/v2/index.php
?policyId.0=699602
&SignatureMethod=HmacSHA256
&Action=DeletePolicy
&Region=gz
&SecretId=AKIDWwGVed95Zu693ltdoopjcKrDct20DKky
&Nonce=29348
&Timestamp=1512717279
&RequestClient=SDK_PHP_1.1
&Signature=pdDVUvsGxLLsjnK3JHZYW2lGLi1FE%2BGqkUq57Nf%2Bp4c%3D
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


## 1. API Description
 

This API (DeleteKeyPair) is used to delete keys hosted on Tencent Cloud.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Multiple keys can be deleted at a time.
* A key that has been referenced by an instance or image cannot be deleted; for this reason, maybe not all keys can be successfully deleted, and whether a key is deletable needs to be determined individually.
 
## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| keyIds.n | Yes | String | ID of key (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)). |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| deleteKeySet | Array | Result of deletion of keys. * For some reasons such as binding of key, maybe not all keys can be successfully deleted, and whether a key is deletable needs to be determined individually. |

deleteKeySet contains the information of multiple deleted keys. The detailed data structure for each key is as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| keyId | String | ID of key. |
| message | String | Message returned after the deletion. |
| code | Int | Result code. 0 indicates success. |

## 4. Example
 
Input

```
  https://cvm.api.qcloud.com/v2/index.php?Action=DeleteKeyPair
  &keyIds.0=skey-mv9yzyjj
  &<Public request parameters>
```

 Output

```
{
    "codeDesc": "Success",
    "message": "",
    "code": 0,
    "detail": {
        "deleteKeySet": [
            {
                "code": 0,
                "message": "success",
                "keyId": "skey-mv9yzyjj"
            }
        ]
    }
}
```






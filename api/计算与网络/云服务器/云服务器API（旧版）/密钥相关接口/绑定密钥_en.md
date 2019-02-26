## 1. API Description


This API (BindInstanceKey) is used to bind a key to a CVM instance.
Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>


* When the system has written the public key of a key to the SSH configuration of the instance, user can log in to CVM through the private key of the key.
* If the instance has been bound to a key before, then the original key will become invalid.
* If the instance was originally logged in through a password, the password cannot be used after the key is bound to the instance.
* Keys can only be bound to a sub-machine that has been shut down.
* **<font color="red">Note: On Windows, key-binding is not allowed.</font>**
 

## 2. Input Parameters


The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceIds.n | Yes | String | Instance ID (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)). |
| keyId | Yes | String | Key ID. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |





## 4. Example

Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=BindInstanceKey
  &instanceIds.0=ins-xxxxx
  &instanceIds.1=ins-xxxxx
  &keyId=skey-xxxxx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
```
{
    "code": 0,
    "message": "",
}

```






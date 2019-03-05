## 1. API Description
 
This API (UnBindInstanceKey) is used to unbind a key from a CVM instance.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Key-unbinding only applies to Linux sub-machine that has been shut down.
* After the key is unbound, the instance can be logged in with the password that was set previously.
* If the password was not set, you cannot log in to the instance using SSH after unbinding. You can call [ResetInstancePassword](https://cloud.tencent.com/doc/api/229/1245) to add a login password.
 
## 2. Input Parameters


The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| keyId | Yes | String | Key ID. |
| instanceIds.n | Yes | String | Instance ID (This API allows passing multiple instance IDs for unbinding at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |


## 4. Example

Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=unBindInstanceKey
  &instanceIds.0=ins-xxxxx
  &instanceIds.1=ins-xxxxx
  &keyId=skey-xxxxx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output
```
{
    "code": 0,
    "message": "",
}

```






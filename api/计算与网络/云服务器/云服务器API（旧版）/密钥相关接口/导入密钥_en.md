## 1. API Description
 

This API (ImportKeyPair) is used to import keys.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>


* This API only imports a key to user's account and does not automatically bind the key to an instance. If you want to bind the key to an instance using API, refer to [BindInstanceKey](https://cloud.tencent.com/doc/api/229/1947) API.
* The key name and the public key text of the key need to be specified.
* If you have only the private key, you can convert the private key to a public key using SSL tool and then import the converted key.
 

## 2. Input Parameters


The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| keyName | Yes | String | Name of key. |
| pubKey | Yes | String | The Public key content of the key (in OpenSSH format). |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| keyId | String | ID of key. |


## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ImportKeyPair
  &keyName=operation_key
  &pubKey=ssh-rsa XXXXXXXXXXXX== skey_45071
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>

</pre>

Output

```
{
    "code": 0,
    "message": "",
    "keyId":"skey-xxxx"
}
```






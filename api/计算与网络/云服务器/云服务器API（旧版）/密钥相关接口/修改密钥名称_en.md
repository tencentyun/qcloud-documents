## 1. API Description
 

This API (ModifyKeyPair) is used to modify the key name.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* You can change the key name based on the key ID. The key ID is the unique identifier of the key and can not be modified.

## 2. Input Parameters


The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| keyId | Yes | String | Used to specify the key ID.
| keyName | Yes | String | The modified key name. It can only contain numbers, letters and "_".

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |




 

## 4. Example
 
Input

```
  https://cvm.api.qcloud.com/v2/index.php?Action=ModifyKeyPair
  &keyId=skey-mv9yzyjj
  &keyName=Tencent
  &<Common request parameters>

```

Output

```
{
    "codeDesc": "Success",
    "message": "",
    "code": 0,
    "data": []
}

```







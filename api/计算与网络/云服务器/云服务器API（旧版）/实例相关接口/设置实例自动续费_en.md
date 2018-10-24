## 1. API Description

This API (SetAutoRenew) is used to set automatic renewal for instances.

Domain name for API request: <font style="color:red">trade.api.qcloud.com</font>

* Any instance marked "Auto Renewal" will be automatically renewed for one month whenever it expires.
* Before using this API, please make ensure that there is sufficient balance in user's account.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceType | Yes | Int | Instance type. Set it to 1 if you want to set auto renewal for a CVM instance. |
| instanceIds.n | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API. This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568). |
| autoRenew | Yes | Int | Indicator for auto renewal. 0 indicates that the instance is not automatically renewed, 1 indicates that the instance is automatically renewed, and 2 indicates that the instance is no longer renewed. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 


## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=SetAutoRenew
  &instanceType=1&instanceId.0=ins-cvm1234&autoRenew=1
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>


Output

```
{
    "code" : 0,
    "message" : "ok"
}

```





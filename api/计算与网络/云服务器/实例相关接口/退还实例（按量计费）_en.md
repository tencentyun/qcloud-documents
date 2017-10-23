## 1. API Description
 
This API (ReturnInstance) is used to return instances.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Postpaid instances will keep running if they are not terminated. When an instance is not used, it need to be returned.
* This API only supports return of postpaid instances. To return prepaid instances, please [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7).

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |

## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
OperationConstraints.InvaildInstanceStatus | Instance status is incorrect or the attempt to obtain the instance status failed

## 5. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ReturnInstance
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
{
    "code": 0,
    "message": "ok"
}
```





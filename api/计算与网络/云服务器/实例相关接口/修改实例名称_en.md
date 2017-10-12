## 1. API Description
 
This API (ModifyInstanceAttributes) is used to modify the attributes of an instance (currently only the modification to instance name is supported).

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* "Instance name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or instance management.
* This API only supports modification to a single instance.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.
| instanceName| Yes| String | Instance name; you can specify any name you like, but its length should be limited to 60 characters. |

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |

## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
| OperationConstraints.InvaildInstanceStatus | Instance status is incorrect or the attempt to obtain the instance status failed (EC_CVM_STATUS_ERROR) | 
## 5. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ModifyInstanceAttributes
  &instanceId=ins-12345678
  &instancesName=Tencent
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
{
    "code" : 0,
    "message" : "ok"
}

```



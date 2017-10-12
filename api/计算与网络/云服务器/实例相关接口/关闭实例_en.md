## 1. API Description
 
This API (StopInstances) is used to shut down one or more instances.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Only instances that are in a running status can be stopped. Shutdown of an instance in any other status will cause an error message.
* Some applications running in an instance can cause a failure of normal shutdown. In this case, you can add forceStop parameter to allow the API to use a forced shutdown policy after a shutdown failure. Forced shutdown will not be performed by default.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceIds.n | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)). |
| forceStop | No | Int | Indicate whether a forced shutdown is performed. A value of 0 indicates a normal shutdown, and a value of 1 indicates a forced shutdown. The default value is 0. |



## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| detail| Array | Refer to [Format of Returned Results of Batch Asynchronous Task API](https://cloud.tencent.com/doc/api/229/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F#2.-.E6.89.B9.E9.87.8F.E5.BC.82.E6.AD.A5.E4.BB.BB.E5.8A.A1.E6.8E.A5.E5.8F.A3.E8.BF.94.E5.9B.9E.E6.A0.BC.E5.BC.8F). |

 
## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
| OperationConstraints.InvaildInstanceStatus | Instance status is incorrect or the attempt to obtain the instance status failed | 
## 5. Example
 
Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=StopInstances
  &instanceIds.0=qcvm12345
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output
Refer to [Format of Returned Results of Batch Asynchronous Task API](http://cloud.tencent.com/doc/api/229/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F#2.-批量异步任务接口返回格式)






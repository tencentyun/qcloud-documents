## 1. API Description
 
This API (ModifyInstanceProject) is used to modify the project to which an instance belongs. A project is a virtual concept. A user can create multiple projects under an account, with different resources managed in each project.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API.
| projectId | Yes | Int | Project ID. A project can be created using [AddProject](https://cloud.tencent.com/doc/api/403/4398). During the query of instance using [DescribeInstances](https://cloud.tencent.com/doc/api/229/831), the project ID can be used to filter the results.



## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 
## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
OperationConstraints.InstanceInAs | For an instance in auto-scale mode, its project is not allowed to be updated.
InvalidParameter.UuidOrUuidList | The uuid or uuidList parameter is missing
InvalidParameter.ProjectIdNotFound | ProjectID does not exist
OperationConstraints.InstanceBindWithLoadBalance | For an instance bound with Cloud Load Balance, this operation is not allowed.

## 5. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?
  Action=ModifyInstanceProject
  &instanceId=qcvm882eae196692549cc581015c495d312421
  &projectId=0
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
{
    "code": 0,
    "message": "ok"
}
```






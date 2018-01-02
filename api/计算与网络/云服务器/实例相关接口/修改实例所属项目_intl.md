## 1. API Description

This API (ModifyInstancesProject) is used to modify the project to which an instance belongs.

Domain name for API request: cvm.api.qcloud.com

* A project is a virtual concept. A user can create multiple projects under an account, with different resources managed in each project. You can allocate different instances to different projects, and then use the API [`DescribeInstances`](/document/api/213/9388) to query instances. The project ID can be used to filter the results.
* The project of the instances bound with load balancers cannot be modified until the load balancers are unbound using the API [`DeregisterInstancesFromLoadBalancer`](/document/api/214/1258).
* The security groups originally associated with the instances are automatically disassociated when the project of the instances is modified. You can use the API [`ModifySecurityGroupsOfInstance`](/document/api/213/1367) to associate security groups after modification.
* Batch operations are supported. The maximum number of instances for each request for batch operations is 100. For the instances that do not allow batch operations, an Error Code is returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | Array of Strings | Yes | ID(s) of one or more instances you want to modify. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
| ProjectId | Integer | Yes | Project ID. A project can be created using the API [AddProject](https://intl.cloud.tencent.com/document/product/378/4398). During the query of instance using the API [DescribeInstances](/document/api/213/9388), the project ID can be used to filter the results.


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Internal operation error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ModifyInstancesProject
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&ProjectId=1045
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>


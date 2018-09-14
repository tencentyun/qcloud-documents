## 1. API Description

This API (ModifyInstancesProject) is used to modify the project to which an instance belongs.

* The project is a virtual concept. Users can create multiple projects under one account to manage different resources in each project, and assign the different instances to different projects. The API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388) can be used to query instances and the project ID can be used to filter the results.
* The project of the instances bound with load balancers cannot be modified until the load balancers are unbound using the API [`DeregisterInstancesFromLoadBalancer`](https://cloud.tencent.com/document/api/214/1258).
The security groups associated with the instances are automatically disassociated when the project of the instances is modified. You can use the API [`ModifySecurityGroupsOfInstance`](https://cloud.tencent.com/document/api/213/1367) to associate security groups after modification.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyInstancesProject |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated. It can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
| ProjectId | Yes | Integer | Project ID. A project can be created using the API [AddProject](https://cloud.tencent.com/doc/api/403/4398). During the query of instance using the API [DescribeInstances](https://cloud.tencent.com/document/api/213/9388), the project ID can be used to filter the results.

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Instance not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Modify the Project to Which Two Instances belong

### Scenario description

This example is used to modify the project to which two instances belong as a specified one.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyInstancesProject
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&ProjectId=1045
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```


        

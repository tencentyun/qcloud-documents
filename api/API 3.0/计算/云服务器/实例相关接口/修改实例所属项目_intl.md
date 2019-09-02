## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ModifyInstancesProject) is used to modify the project to which an instance belongs.

* Project is a virtual concept. Users can create multiple projects under one account to manage different resources in each project, and assign different instances to different projects. The API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388) can be used to query instances and the project ID can be used to filter the results.
* The project of the instances bound with load balancers cannot be modified until the load balancers are unbound using the API [`DeregisterInstancesFromLoadBalancer`](https://cloud.tencent.com/document/api/214/1258).
* The security groups associated with the instances are automatically disassociated when the project of the instances is modified. You can use the API [`ModifySecurityGroupsOfInstance`](https://cloud.tencent.com/document/api/213/1367) to associate security groups after modification.
* Batch operations are supported. A maximum of 100 instances are allowed in a batch for each request.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyInstancesProject |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). A maximum of 100 instances are allowed for each request. |
| ProjectId | Yes | Integer | Project ID. A project can be created using the API [AddProject](https://cloud.tencent.com/doc/api/403/4398). During the query of instances using the API [DescribeInstances](https://cloud.tencent.com/document/api/213/9388), the project ID can be used to filter the results. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Modify the project to which two instances belong

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ModifyInstancesProject
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&ProjectId=1045
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```



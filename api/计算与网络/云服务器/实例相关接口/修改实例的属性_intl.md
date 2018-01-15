## 1. API Description

This API (ModifyInstancesAttribute) is used to modify the attributes of an instance (only the instance name can be modified now).

Domain name for API request: cvm.api.qcloud.com

* "Instance name" is only used by users for easy management. This name is not used in ticket system or for instance operations.
* Batch operations are supported. The maximum number of instances for each request for batch operations is 100. For the instances that do not allow batch operations, an error code is returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | String | Yes | IDs of one or more instances to be operated. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). Up to 100 instances can be modified each time. |
| InstanceName | String | Yes | Instance name. This can be arbitrarily specified, but can not exceed 60 characters. |


## 3. Output Parameters

| Parameter| Type | Description |
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
| InvalidInstanceName.TooLong | Invalid instance name. The length of instance name exceeds the limit. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Internal service error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ModifyInstancesAttribute
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&InstanceName=Mysql_Server
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


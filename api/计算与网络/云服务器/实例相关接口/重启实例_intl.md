## 1. API Description

This API (RebootInstances) is used to restart an instance.

Domain name for API request: cvm.api.qcloud.com

* This operation is only allowed for the instances with a status of `RUNNING`.
* When the API is called successfully, the instance goes into the `REBOOTING` status. When restarted, it goes into the `RUNNING` status.
* Forced restart is supported. Just like restarting a physical PC after a power-off, forced restart may cause data loss or the corruption of file system. Be sure to perform forced restart only when the server cannot be restarted normally.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100. If any instance that does not allow batch operations exists in the batch, an error code is returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances you are working with. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
| ForceReboot | Boolean | No | Whether to perform a forced restart on the instance in case of a failure of normal restart. Values: <br><li>TRUE: Perform a forced restart ;<br><li>FALSE: Do not. <br><br>Default: FALSE. |


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | Invalid instance ID. The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Tencent Cloud server error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=RebootInstances
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&ForceReboot=FALSE
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


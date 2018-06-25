## 1. API Description

This API (StopInstances) is used to shut down one or more instances.

Domain name for API request: cvm.api.qcloud.com

* This operation is only allowed for the instances with a status of `RUNNING`.
* When the API is called, the instance will go into the `STOPPING` status. When the instance is shut down, it will go into the `STOPPED` status.
* Forced shutdown is supported. Just like powering off a physical PC, forced restart may cause data loss or the corruption of file system. Be sure to perform forced restart only when the server cannot be shut down normally.
* Batch operations are supported. The maximum number of instances for each request for batch operations is 100. Before instances are started in batches, an Error Code is returned for those that do not allow batch operations.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances to be operated. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances for each request for batch operation is 100. |
| ForceStop | Boolean | No | Whether to perform a forced shutdown on the instance in case of a failure of normal shutdown. Values: <br><li>TRUE: Perform a forced shutdown;<br><li>FALSE: Do not. <br><br>Default: FALSE.


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
https://cvm.api.qcloud.com/v2/index.php?Action=StopInstances
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&ForceStop=FALSE
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


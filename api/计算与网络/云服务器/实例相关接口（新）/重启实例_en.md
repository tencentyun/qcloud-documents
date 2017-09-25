## 1. API Description

Note: This API is the updated API. For information on the old API, please see [Restart Instance](https://www.qcloud.com/document/api/213/1247)

This API (RebootInstances) is used to restart the instance.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Only instances with the status of `RUNNING` can perform this action.
* When the API is called, the instance will go into the `REBOOTING` status. When the instance is restarted, it will go into the `RUNNING` status.
* Forced restart is supported. Just like traditional restart after a power cut, forced restart may also cause data loss due to data in the instance operating system not written to the disk. For more information, please see [Forced Restart]().
* Batch operations are supported. The maximum number of instances for batch request is 100 each time. If some instances in the batch of instances cannot be operated, a specific [error code]() will be returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | Indicates API version No., used for identifying the API version of the request. To indicate the first version of this API, you can input the value "2017-03-12" to the parameter. |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instance to be operated, which can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances for batch request is 100 each time. |
| ForceReboot | Boolean | No | Whether to force restart the instance after a normal restart failed. Value range: <br><li>TRUE: force restart the instance after a normal restart failed <br><li>FALSE: not force restart the instance after a normal restart failed.<br><br>Default: FALSE. For more information, please see: Forced Restart Risks. |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request `ID`. `RequestId` is returned for each request. `RequestId` should be provided to the backend developer for a help when the user fails to call the API. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://www.qcloud.com/document/api/213/10146).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. The request does not have the required parameters. |
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` indicates an instance `ID` length error. |
| InvalidParameterValue | Invalid parameter value. Parameter value is not in a correct format or not supported, etc. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | Instance does not support this operation. |
| InternalServerError | Internal operation error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=RebootInstances
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&ForceReboot=FALSE
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>



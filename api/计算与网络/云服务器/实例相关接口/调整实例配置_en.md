## 1. API Description

This API (ResetInstancesType) is used to adjust instance model.

Domain name for API request: cvm.api.qcloud.com

* Currently, using this API for adjusting models is only supported for the instances with a [system disk type](/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.
* Currently, this API cannot be used to adjust the models of [CDH](/document/product/416) instances.
* Currently, model adjustment is not supported for different models and systems. That is, the `InstanceType` specified when you use this API and the original instance model need to be of the same series.
* For prepaid instances, using this API will charge a fee. Please ensure that the user account has sufficient balance. The balance can be queried using the API [`DescribeAccountBalance`](/document/product/378/4397).


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances to be operated. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances for each request for batch operation is 1 for now. |
| InstanceType | String | Yes | Instance model. Different resource specifications are specified for different instance models. For specific values, please see Table of Resource Specifications. You can also obtain the latest specification list using the API "Query List of Instance Resource Specifications". |
|ForceStop| Boolean| No | Whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password for it. Values: <br><li>TRUE: Perform a forced shutdown in case of a failure of normal shutdown; <br><li>FALSE: Do not.<br><br> Default: FALSE. <br><br>Just like shutting down a physical PC, forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally.|


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique "requestId" is returned for each request. In case of a failed call to the API, "requestId" needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InvalidPermission | This operation is not supported for the account. |
| InvalidAccount.InsufficientBalance | The account balance is sufficient. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InternalServerError | Internal service error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ResetInstancesType
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceType=S1.LARGE4
&DryRun=FALSE
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
</pre>


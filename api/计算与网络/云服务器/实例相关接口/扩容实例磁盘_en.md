## 1. API Description

This API (ResizeInstanceDisks) is used to scale up instance data disks.

Domain name for API request: cvm.api.qcloud.com

* This API can only be used to expand disks purchased along with instances, and the [data disk type](/document/api/213/9452#block_device) must be: `CLOUD_BASIC`, `CLOUD_PREMIUM` or `CLOUD_SSD`.
* This API is not available to [CDH](/document/product/416) instances.
* For prepaid instances, using this API will charge a fee. Please ensure that the user account has sufficient balance. You can query your account balance via the API [`DescribeAccountBalance`](/document/product/378/4397).
* You can scale up ONLY ONE data disk each time.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceId | String | Yes | ID(s) of one or more instances to be operated. It can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). |
| DataDisks.N | [Array of DataDisk objects](https://cloud.tencent.com/document/api/213/9451#datadisk) | Yes | Configuration information of the data disk to be scaled up. Only data disks purchased along with the instances can be scaled up, and the following [Data Disk Types](/document/api/213/9452#block_device) are supported: `CLOUD_BASIC`, `CLOUD_PREMIUM`, `CLOUD_SSD`. Unit: GB. Minimum increments: 10 GB. For more information on how to choose data disk type, please see Overview of Data Disk Products. Supported data disks are subject to `InstanceType`. In addition, the maximum capacity available for expansion varies with different types of data disks. |
|ForceStop| Boolean| No | Whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password for it. Values: <br><li>TRUE: Perform a forced shutdown in case of a failure of normal shutdown; <br><li>FALSE: Do not.<br><br> Default: FALSE. <br><br>Just like shutting down a physical PC, forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally.|


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique "requestId" is returned for each request. In case of a failed call to the API, "requestId" needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InvalidAccount.InsufficientBalance | The account balance is sufficient. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InternalServerError | Internal operation error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ResizeInstanceDisks
&Version=2017-03-12
&InstanceId=ins-r8hr2upy
&DataDisks.0.DiskSize=100
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


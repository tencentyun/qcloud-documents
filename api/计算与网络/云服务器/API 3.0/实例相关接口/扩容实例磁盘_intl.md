## 1. API Description

This API (ResizeInstanceDisks) is used to expand the capacity of the data disk of instance.

* Only the data disk purchased with the instance is supported, and the [data disk type](/document/api/213/9452#block_device) is: `CLOUD_BASIC`, `CLOUD_PREMIUM`, `CLOUD_SSD`. * The [CDH](https://cloud.tencent.com/document/product/416) instance is not supported to use this API to expand the capacity of data disk.
* For the prepaid instances, using this API will deduct involved fee from the account balance. Make sure the account balance is sufficient. You can query the account balance via the [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397) API.
* Now, only capacity expansion for one data disk is supported.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: ResizeInstanceDisks |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceId | Yes | String | ID of instance to work with. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). |
| DataDisks.N | Yes | Array of [DataDisk](/document/api/213/15753#DataDisk) | Configuration information of the data disk to be expanded. Only the data disk purchased with the instance is supported, and the [data disk type](/document/api/213/9452#block_device) is: `CLOUD_BASIC`, `CLOUD_PREMIUM`, `CLOUD_SSD`. Data disk capacity unit: GB. Minimum capacity expansion increment: 10G. For the selection of the data disk type, please see Overview of Hard Disk Products. The available data disk types are limited by the instance type `InstanceType`. In addition, the maximum capacity allowed for expansion varies depending on the type of data disk. |
| ForceStop | No | Boolean | Indicate whether a forced shutdown is performed to running instances. It is recommended that you manually shut down the running instance before resetting the user password. Value range: <li>TRUE: indicates the forced shutdown will be performed after a normal shutdown failure. </li><li>FALSE: indicates that the forced shutdown is not performed after a normal shutdown failure. </li><br>Default value: FALSE.<br><br> The result of forced shutdown is the same as turning off the power switch of the physical computer. Forced shutdown may lead to data loss or damage to file system, so use it only when the server cannot be shut down properly. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidAccount.InsufficientBalance | Insufficient balance. |
| InvalidAccount.UnpaidOrder | There is an unpaid order in the account. |
| InvalidInstance.NotSupported | The instance is not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` format is incorrect. For example, `ins-1122` indicates an ID length error. |
| InvalidInstanceId.NotFound | The corresponding instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| MissingParameter | Missing parameters. The request does not have the required parameters. |

## 5. Example

## Example 1 Reset the Size of a Disk with a Specified ID

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ResizeInstanceDisks
&InstanceId=ins-r8hr2upy
&DataDisks.0.DiskSize=100
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
  }
}
```


        

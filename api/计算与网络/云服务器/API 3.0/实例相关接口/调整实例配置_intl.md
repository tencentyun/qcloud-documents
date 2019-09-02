
## 1. API Description

This API (ResetInstancesType) is used to adjust the model of an instance.
* Currently, using this API for adjusting models is only supported for the instances with a [system disk type](/document/api/213/9452#block_device) of `CLOUD_BASIC`, `CLOUD_PREMIUM` and `CLOUD_SSD`.
* Currently, using this API for adjusting models is not supported for the [CDH](https://cloud.tencent.com/document/product/416) instances. * Model adjustment is not supported for different models and systems, which means that the `InstanceType` specified when you use this API and the original instance model must be in the same series. * For prepaid instances, fee deduction will be involved in using this API, so make sure to keep sufficient balance in your account. You can query the balance via the API [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397).

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ResetInstancesType |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with, which can be obtained from `InstanceId` in the returned value of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances in a batch for each request is 1. |
| InstanceType | Yes | String | Instance model. Different resource specifications are specified for different instance models. For specific values, please see the table of instance resource specifications. You can also obtain the latest specification list using the API for querying the list of instance resource specifications. |
| ForceStop | No | Boolean | Indicate whether a forced shutdown is performed on running instances. It is recommended that you manually shut down a running instance before resetting the user password. Values: <li>TRUE: indicates the forced shutdown will be performed after a normal shutdown failure. </li><li>FALSE: indicates that the forced shutdown is not performed after a normal shutdown failure. </li>Default value: FALSE.<br><br> The result of forced shutdown is the same as turning off the power switch of the physical computer. Forced shutdown may lead to data loss or damage to file systems. Use this only when the server cannot be shut down properly. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidAccount.InsufficientBalance | Insufficient account balance. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidPermission | This operation is not supported for the account. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Reset the instance model

### Scenario description

If the current model configuration does not meet the business needs, you can adjust the specifications.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ResetInstancesType
&InstanceIds.0=ins-r8hr2upy
&InstanceType=S1.LARGE4
&DryRun=FALSE
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



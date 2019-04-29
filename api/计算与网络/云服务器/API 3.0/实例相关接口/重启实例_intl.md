## 1. API Description

This API (RebootInstances) is used to restart an instance.

* This operation is only allowed for the instances with a status of `RUNNING`.
* When the API is called successfully, the instance goes into the `REBOOTING` status. When restarted, it goes into the `RUNNING` status.
* Forced restart is supported. Just like restarting a physical PC after a power-off, forced restart may cause data loss or the corruption of file system. Be sure to perform forced restart only when the server cannot be restarted normally.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: RebootInstances |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with, which can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). The maximum number of instances in a batch for each request is 100.
| ForceReboot | No | Boolean | Whether to perform a forced restart on the instance in case of a failure of normal restart. Values: <li>TRUE: Perform a forced restart ;</li><li>FALSE: Do not. </li>Default: FALSE. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Restart instances

### Scenario description

Two instances will be restarted in this example.


### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RebootInstances
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&ForceReboot=FALSE
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


## 1. API Description

This API (StopInstances) is used to shut down one or more instances.

* This operation is only allowed for the instances with a status of `RUNNING`.
* When the API is called successfully, the instance goes into the `STOPPING` status. When the instance is shut down, it goes into the `STOPPED` status.
* Forced shutdown is supported. Just like powering off a physical PC, forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: StopInstances |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated, which can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances for batch request is 100 each time. |
| ForceStop | No | Boolean | Whether to perform a forced shutdown on the instance in case of a failure of normal shutdown. Values: <li>TRUE: Perform a forced shutdown</li><li>FALSE: Do not</li><br>Default value: FALSE. |
| StopType | No | String | Instance shutdown mode. Value range: <li>SOFT_FIRST: Perform a forced shutdown in case of a failure of the normal shutdown</li><li>HARD: Perform a forced shutdown directly</li><li>SOFT: Soft shutdown</li><br>Default value: SOFT. |
| StoppedMode | No | String | Shutdown billing mode<li>KEEP_CHARGING: Keep charging after shutdown</li><li>STOP_CHARGING: Stop charging after shutdown</li><br>Default value: KEEP_CHARGING. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Instance not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Shut Down Instances

### Scenario description

This example is used to shut down two instances.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=StopInstances
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&ForceStop=FALSE
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


        

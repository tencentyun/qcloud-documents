
## 1. API Description

This API (TerminateInstances) is used to return instances.

* The instances that are no longer used can be returned via this API.
* Postpaid instances can be directly returned via this API. Prepaid instances that conform to the [rules for return](https://cloud.tencent.com/document/product/213/9711) can also be returned via this API.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: TerminateInstances |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with, which can be obtained from `InstanceId` in the returned value of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances in a batch for each request is 100. |
| DryRun | No | Boolean | Dry run. |

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
| InvalidInstanceNotSupportedPrepaidInstance | This instance does not conform to the [rules for return](https://cloud.tencent.com/document/product/213/9711) of prepaid instances. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Terminate the instance with the specified ID

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=TerminateInstances
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
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


## 1. API Description

This API (StartInstances) is used to start one or more instances.

* This operation is only allowed for the instances with a status of `STOPPED`.
* When the API is called, the instance will go into the `STARTING` status. When the instance is started, it will go into the `RUNNING` status.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: StartInstances |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated, which can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances for batch request is 100 each time. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Instance not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` format is incorrect. For example, instance `ID` length error `ins-1122`. |
| InvalidInstanceId.NotFound | The corresponding instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameters. The request does not have the required parameters. |

## 5. Example

## Example 1 Start an Instance with a Specified ID

### Scenario description

You can also start one or more instances of shutdown status

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=StartInstances
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
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


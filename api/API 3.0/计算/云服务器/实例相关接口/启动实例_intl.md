## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (StartInstances) is used to start one or more instances.

* This operation is only allowed for the instances with a status of `STOPPED`.
* When the API is called successfully, the instance goes into the `STARTING` status. When started, it goes into the `RUNNING` status.
* Batch operations are supported. A maximum of 100 instances are allowed in a batch for each request.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: StartInstances |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). A maximum of 100 instances are allowed in a batch for each request. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Start an instance with a specified ID

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=StartInstances
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
  }
}
```



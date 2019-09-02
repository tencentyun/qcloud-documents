## 1. API Description

This API (ModifyInstancesAttribute) is used to modify the attributes of an instance (currently only the modification to instance name is supported).

* "Instance name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or instance management.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyInstancesAttribute |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instance to be operated. It can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
| InstanceName | No | String | Instance name; you can specify any name you like, but its length should be limited to 60 characters.

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
| InvalidInstanceName.TooLong | The specified InstanceName exceeds the maximum length of 60 bytes.|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Modify Instance Name

### Scenario description

This example is used to modify the names of two instances.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ModifyInstancesAttribute
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&InstanceName=Mysql_Server
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


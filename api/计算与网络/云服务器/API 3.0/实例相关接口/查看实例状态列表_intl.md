## 1. API Description

This API (DescribeInstancesStatus) is used to query the status of one or more instances.

* You can query the status of an instance according to its `ID`.
* If the parameter is empty, the status of a certain number (specified by Limit, the default is 20) of instances is returned to the current user.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeInstancesStatus |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| InstanceIds.N | No | Array of String | To query according to one or more instance IDs, such as `ins-11112222`. For the format of this parameter, please see `id.N` section of API [Introduction](https://cloud.tencent.com/document/api/213/15688). The maximum number of instances of each request is 100. |
| Offset | No | Integer | Offset. Default is 0. For more information on `offset`, please see relevant sections of API [Introduction](https://cloud.tencent.com/document/api/213/15688). |
| Limit | No | Integer | Number of returned results. The default is 20, and the maximum is 100. For more information on `limit`, please see relevant sections of API [Introduction](https://cloud.tencent.com/document/api/213/15688). |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instance statuses that meet the condition. |
| InstanceStatusSet | Array of [InstanceStatus](/document/api/213/15753#InstanceStatus) | [Instance Status](https://cloud.tencent.com/document/api/213/15738) list. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` format is incorrect. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |

## 5. Example

## Example 1 View the List of Instance Statuses

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstancesStatus
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&Offset=0
&Limit=2
&<Common request parameters>
```
### Response Parameters

```
{
  "Response": {
    "InstanceStatusSet": [
      {
        "InstanceId": "ins-r8hr2upy",
        "InstanceState": "RUNNING"
      },
      {
        "InstanceId": "ins-5d8a23rs",
        "InstanceState": "STOPPED"
      }
    ],
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
    "TotalCount": 2
  }
}
```


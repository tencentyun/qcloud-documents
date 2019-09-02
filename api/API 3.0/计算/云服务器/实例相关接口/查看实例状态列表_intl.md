## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInstancesStatus) is used to query the status of one or more instances.

* You can query the status of an instance according to its `ID`.
* If the parameter is empty, the status of a certain number (specified by Limit, the default is 20) of instances is returned to the current user.

A maximum of 40 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstancesStatus |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | No | Array of String | Query by one or more instance IDs, such as `ins-11112222`. For the format of this parameter, please see the `id.N` section in the API [Introduction](https://cloud.tencent.com/document/api/213/15688). A maximum of 100 instances are allowed for each request. |
| Offset | No | Integer | Offset. Default is 0. For more information about `Offset`, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. For more information about `Limit`, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instance statues matching the filter condition. |
| InstanceStatusSet | Array of [InstanceStatus](/document/api/213/##InstanceStatus) | [Instance status](https://cloud.tencent.com/document/api/213/15738) list. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |

## 5. Example

### Example 1 View the instance status list

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstancesStatus
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&Offset=0
&Limit=2
&<Common request parameters>
```

#### Output example

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



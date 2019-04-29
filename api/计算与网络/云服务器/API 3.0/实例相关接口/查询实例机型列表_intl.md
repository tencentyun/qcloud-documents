## 1. API Description

This API (DescribeInstanceTypeConfigs) is used to query the instance model configuration.

* You can query the instance model configuration using `zone` or `instance-family`. For more information on filtering conditions, please see `Filter`.
* If the parameter is empty, model configuration of all instances under the specified region are returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeInstanceTypeConfigs |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| Filters.N | No | Array of [Filter](/document/api/213/15753#Filter) | Filter criteria.
 zone - String - Required: No - (Filter criteria) Filter by [availability zone](https://cloud.tencent.com/document/api/213/9452#zone).
 instance-family - String - Required: No - (Filter criteria) Filter by instance model series, such as: `S1`, `I1`, `M1`.

The maximum number of `Filters ' of each request is 10, and the maximum number of` Filter.Values`' is 1. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceTypeConfigSet | Array of [InstanceTypeConfig](/document/api/213/15753#InstanceTypeConfig) | List of instance model configuration. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidFilter | Invalid filter. |
| InvalidFilterValue.LimitExceeded | The number of values of parameter [`Filter`](/document/api/213/9451#filter) exceeds the limit. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

## Example 1 Query the Instance Model List

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceTypeConfigs
&Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-2
&Filters.1.Name=instance-family
&Filters.1.Values.0=I1
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "InstanceTypeConfigSet": [
      {
        "CPU": 2,
        "FPGA": 0,
        "GPU": 0,
        "InstanceFamily": "I1",
        "InstanceType": "I1.MEDIUM4",
        "Memory": 4,
        "Zone": "ap-guangzhou-2"
      },
      {
        "CPU": 2,
        "FPGA": 0,
        "GPU": 0,
        "InstanceFamily": "I1",
        "InstanceType": "I1.MEDIUM8",
        "Memory": 8,
        "Zone": "ap-guangzhou-2"
      },
      {
        "CPU": 2,
        "FPGA": 0,
        "GPU": 0,
        "InstanceFamily": "I1",
        "InstanceType": "I1.MEDIUM16",
        "Memory": 16,
        "Zone": "ap-guangzhou-2"
      },
      {
        "CPU": 4,
        "FPGA": 0,
        "GPU": 0,
        "InstanceFamily": "I1",
        "InstanceType": "I1.LARGE8",
        "Memory": 8,
        "Zone": "ap-guangzhou-2"
      }
    ],
    "RequestId": "2f1fd71e-95ab-4f10-8adb-895e99d33ff5"
  }
}
```

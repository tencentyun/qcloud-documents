## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInstanceTypeConfigs) is used to query the instance model configuration.

* You can query the instance model configuration via `zone` and `instance-family`. Filter criteria can be found in `Filter`.
* If the parameter is empty, model configuration of all instances under the specified region are returned.

A maximum of 40 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstanceTypeConfigs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Filters.N | No | Array of [Filter](/document/api/213/##Filter) | Filter conditions.<br/><li> zone - String - Required: No - (Filter condition) Filter by [availability zone](https://cloud.tencent.com/document/api/213/9452#zone).</li><li> instance-family - String - Required: No - (Filter condition) Filter by instance model series, such as S1, I1, and M1.</li><br/> The maximum number of `Filters ' of each request is 10, and the maximum number of` Filter.Values`' is 1. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceTypeConfigSet | Array of [InstanceTypeConfig](/document/api/213/##InstanceTypeConfig) | List of instance model configurations. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidFilter | Invalid filter. |
| InvalidFilterValue.LimitExceeded | [`Filter`](/document/api/213/9451#filter)Number of parameter values exceeds the limit. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

### Example 1 Query the instance model list

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceTypeConfigs
&Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-2
&Filters.1.Name=instance-family
&Filters.1.Values.0=I1
&<Common request parameters>
```

#### Output example

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



## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInstanceFamilyConfigs) is used to query the list of model families supported by the current user and region.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstanceFamilyConfigs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceFamilyConfigSet | Array of [InstanceFamilyConfig](/document/api/213/##InstanceFamilyConfig) | List of instance model family configurations |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidRegion.NotFound | The region cannot be found. |

## 5. Example

### Example 1 Query the information on supported instance model families

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceFamilyConfigs
&Region=ap-guangzhou
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "InstanceFamilyConfigSet": [
      {
        "InstanceFamily": "S1",
        "InstanceFamilyName": "Standard S1"
      },
      {
        "InstanceFamily": "N1",
        "InstanceFamilyName": "Network optimized N1"
      },
      {
        "InstanceFamily": "I1",
        "InstanceFamilyName": "High IO I1"
      },
      {
        "InstanceFamily": "M1",
        "InstanceFamilyName": "MEM optimized M1"
      },
      {
        "InstanceFamily": "S2",
        "InstanceFamilyName": "Standard S2"
      },
      {
        "InstanceFamily": "SN2",
        "InstanceFamilyName": "Standard SN2"
      },
      {
        "InstanceFamily": "I2",
        "InstanceFamilyName": "High IO I2"
      },
      {
        "InstanceFamily": "M2",
        "InstanceFamilyName": "MEM optimized M2"
      },
      {
        "InstanceFamily": "C2",
        "InstanceFamilyName": "Computing C2"
      },
      {
        "InstanceFamily": "CN2",
        "InstanceFamilyName": "Computing CN2"
      },
      {
        "InstanceFamily": "S3",
        "InstanceFamilyName": "Standard S3"
      },
      {
        "InstanceFamily": "C3",
        "InstanceFamilyName": "Computing C3"
      },
      {
        "InstanceFamily": "FX2",
        "InstanceFamilyName": "FPGA FX2"
      },
      {
        "InstanceFamily": "GN2",
        "InstanceFamilyName": "GPU computing GN2"
      },
      {
        "InstanceFamily": "GA2",
        "InstanceFamilyName": "GPU rendering GA2"
      },
      {
        "InstanceFamily": "GN8",
        "InstanceFamilyName": "GPU computing GN8"
      },
      {
        "InstanceFamily": "CDH",
        "InstanceFamilyName": "Exclusive"
      },
      {
        "InstanceFamily": "SHARED",
        "InstanceFamilyName": "Shared core"
      },
      {
        "InstanceFamily": "SPECIAL",
        "InstanceFamilyName": "Special model"
      },
      {
        "InstanceFamily": "OTHER",
        "InstanceFamilyName": "Other"
      }
    ],
    "RequestId": "b061782b-934a-4e53-b1eb-d5f2fed8130e"
  }
}
```



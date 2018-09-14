## 1. API Description

This API (DescribeInstanceFamilyConfigs) is used to query the list of model families supported by the current user and region.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeInstanceFamilyConfigs |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceFamilyConfigSet | Array of [InstanceFamilyConfig](/document/api/213/15753#InstanceFamilyConfig) | List of instance model group configuration. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidParameterValue | Invalid parameter value. The format of the parameter value is incorrect or the parameter value is not supported. |
| InvalidRegion.NotFound | The region was not found. |

## 5. Example

## Example 1 Query the Information on Supported Instance Model Families

### Scenario description

Query the information on the instance model group in Guangzhou region.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceFamilyConfigs
&Region=ap-guangzhou
&<Common request parameters>
```
### Response parameters

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

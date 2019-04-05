## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeRegions) is used to query regions.

A maximum of 20 requests can be initiated per second for this API.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeRegions |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | No | String | Common parameter. This parameter is not required for this API. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of regions |
| RegionSet | Array of [RegionInfo](/document/api/213/15753#RegionInfo) | Region details |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, please see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Request example

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeRegions
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RegionSet": [
      {
        "Region": "ap-beijing",
        "RegionName": "North China (Beijing)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-guangzhou",
        "RegionName": "South China (Guangzhou)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-guangzhou-open",
        "RegionName": "South China (Guangzhou Open)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-hongkong",
        "RegionName": "Southeast Asia (Hong Kong)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-shanghai",
        "RegionName": "East China (Shanghai)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-shanghai-fsi",
        "RegionName": "East China (Shanghai Finance)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-shenzhen-fsi",
        "RegionName": "South China (Shenzhen Finance)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "ap-singapore",
        "RegionName": "Southeast Asia (Singapore)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "na-siliconvalley",
        "RegionName": "Western U.S. (Silicon Valley)",
        "RegionState": "AVAILABLE"
      },
      {
        "Region": "na-toronto",
        "RegionName": "North America (Toronto)",
        "RegionState": "AVAILABLE"
      }
    ],
    "RequestId": "C563943B-3BEA-FE92-29FE-591EAEB7871F",
    "TotalCount": 10
  }
}
```



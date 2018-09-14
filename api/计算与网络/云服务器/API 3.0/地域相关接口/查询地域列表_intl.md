## 1. API Description

This API (DescribeRegions) is used to query regions.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeRegions |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of regions |
| RegionSet | Array of [RegionInfo](/document/api/213/15753#RegionInfo) | Region list information |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



## 5. Example

## Example 1 Request Example

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeRegions
&<Common request parameters>
```
### Response parameters

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
        "RegionName": "Western America (Silicon Valley)",
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

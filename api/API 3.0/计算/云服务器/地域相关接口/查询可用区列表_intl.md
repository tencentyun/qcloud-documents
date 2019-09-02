## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeZones) is used to query availability zones.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeZones |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of availability zones |
| ZoneSet | Array of [ZoneInfo](/document/api/213/##ZoneInfo) | Availability zone details |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, please see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Request example

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeZones
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A",
    "TotalCount": 3,
    "ZoneSet": [
      {
        "Zone": "ap-guangzhou-1",
        "ZoneId": "100001",
        "ZoneName": "Guangzhou Zone 1",
        "ZoneState": "UNAVAILABLE"
      },
      {
        "Zone": "ap-guangzhou-2",
        "ZoneId": "100002",
        "ZoneName": "Guangzhou Zone 2",
        "ZoneState": "AVAILABLE"
      },
      {
        "Zone": "ap-guangzhou-3",
        "ZoneId": "100003",
        "ZoneName": "Guangzhou Zone 3",
        "ZoneState": "AVAILABLE"
      }
    ]
  }
}
```



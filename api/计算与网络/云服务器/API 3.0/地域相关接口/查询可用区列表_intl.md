## 1. API Description

This API (DescribeZones) is used to query availability zones.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeZones |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of availability zones |
| ZoneSet | Array of [ZoneInfo](/document/api/213/15753#ZoneInfo) | Availability zone list information |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



## 5. Example

## Example 1 Request Example

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeZones
&<Common request parameters>
```
### Response parameters

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


        

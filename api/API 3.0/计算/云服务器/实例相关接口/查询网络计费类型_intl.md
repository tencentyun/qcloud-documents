## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInternetChargeTypeConfigs) is used to query the network billing type.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInternetChargeTypeConfigs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InternetChargeTypeConfigSet | Array of [InternetChargeTypeConfig](/document/api/213/##InternetChargeTypeConfig) | Network billing type configuration. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, please see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Query the network billing type

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInternetChargeTypeConfigs
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "InternetChargeTypeConfigSet": [
      {
        "Description": "Postpaid by month",
        "InternetChargeType": "BANDWIDTH_POSTPAID_BY_MONTH"
      },
      {
        "Description": "Bill by bandwidth",
        "InternetChargeType": "BANDWIDTH_PREPAID"
      },
      {
        "Description": "Bill by traffic",
        "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR"
      },
      {
        "Description": "Bill by bandwidth usage time",
        "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR"
      },
      {
        "Description": "Bill by bandwidth package",
        "InternetChargeType": "BANDWIDTH_PACKAGE"
      }
    ],
    "RequestId": "c2abdac4-ea7b-4653-b07c-87cc303fabf0"
  }
}
```



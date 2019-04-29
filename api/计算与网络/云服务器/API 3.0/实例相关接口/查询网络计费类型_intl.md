## 1. API Description

This API (DescribeInternetChargeTypeConfigs) is used to query the network billing type.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DescribeInternetChargeTypeConfigs |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| InternetChargeTypeConfigSet | Array of [InternetChargeTypeConfig](/document/api/213/15753#InternetChargeTypeConfig) | Network billing type configuration |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



## 5. Example

## Example 1 Query the Network Billing Type

### Scenario description

When creating a server by calling API, you need to enter the network billing type. Using this API, you can query all network billing types and select an appropriate parameter.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=DescribeInternetChargeTypeConfigs
&<Common request parameters>
```
### Response parameters

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


        

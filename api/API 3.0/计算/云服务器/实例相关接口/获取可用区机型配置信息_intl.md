## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeZoneInstanceConfigInfos) is used to obtain the model information in an availability zone.

A maximum of 40 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeZoneInstanceConfigInfos |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Filters.N | No | Array of [Filter](/document/api/213/##Filter) | Filter conditions.<br/><br/><li> zone - String - Required: No - (Filter condition) Filter by availability zone.</li><br/><br/><li> instance-family - String - Required: No - (Filter condition) Filter by instance model series, such as S1, I1, and M1.</li><br/><br/><li> instance-type - String - Required: No - (Filter condition) Filter by instance model. Different instance models specify different resource specifications. Specific values can be found in the latest Specifications by calling the API DescribeInstanceTypeConfigs or in the instance type description. If this parameter is not specified, S1.SMALL1 is used by default.</li><br/><br/><li> instance-charge-type - String - Required: No - (Filter condition) Filter by instance billing method. (PREPAID: prepaid (by year/month) &#124; POSTPAID_BY_HOUR: postpaid (by traffic) &#124; CDHPAID: CDH paid, i.e., only pay for CDH, excluding instances on the CDH. )  </li> |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InstanceTypeQuotaSet | Array of [InstanceTypeQuotaItem](/document/api/213/##InstanceTypeQuotaItem) | List of model configuration in an availability zone. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidInstanceType.Malformed | The format of the specified parameter InstanceType is invalid. |
| InvalidRegion.NotFound | The region cannot be found. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

### Example 1 Obtain the list of model configuration in an availability zone

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeZoneInstanceConfigInfos
&Filters.0.Name=zone
&Filters.0.Values.0=ap-guangzhou-2
&Filters.1.Name=instance-charge-type
&Filters.1.Values.0=POSTPAID_BY_HOUR
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "InstanceTypeQuotaSet": [
      {
        "Cpu": 2,
        "Externals": {},
        "InstanceChargeType": "POSTPAID_BY_HOUR",
        "InstanceFamily": "S2",
        "InstanceType": "S2.MEDIUM4",
        "LocalDiskTypeList": [
          {
            "MaxSize": 50,
            "MinSize": 50,
            "PartitionType": "ROOT",
            "Type": "LOCAL_BASIC"
          },
          {
            "MaxSize": 500,
            "MinSize": 0,
            "PartitionType": "DATA",
            "Type": "LOCAL_BASIC"
          }
        ],
        "Memory": 4,
        "NetworkCard": 0,
        "Price": {
          "ChargeUnit": "HOUR",
          "UnitPrice": 0.64
        },
        "Status": "SELL",
        "TypeName": "Standard S2",
        "Zone": "ap-guangzhou-2"
      }
    ],
    "RequestId": "c28559ca-d3cf-40f0-9664-2ab303484efa"
  }
}
```



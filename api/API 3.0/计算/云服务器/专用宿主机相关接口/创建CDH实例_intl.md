## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (AllocateHosts) is used to create one or more CDH instances with specified configuration.
* When HostChargeType is PREPAID, the HostChargePrepaid parameter must be specified.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: AllocateHosts |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Placement | Yes | [Placement](/document/api/213/##Placement) | Location of the instance. This parameter is used to specify the availability zone and project to which the instance belongs. |
| ClientToken | No |  String | A string to ensure the idempotency of the request. |
| HostChargePrepaid | No | [ChargePrepaid](/document/api/213/##ChargePrepaid) | Indicates the relevant parameter setting for the prepaid mode. This parameter can specify the usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is required if the billing method for the specified instance is prepaid. |
| HostChargeType | No | String | Billing type of the instance. Only PREPAID (the prepaid mode) is supported. |
| HostType | No | String | CDH instance model, which defaults to 'HS1'. | |
| HostCount | No | Integer | Number of CDH instances to be purchased. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| HostIdSet | Array of String | List of IDs of CDH instances on which new cloud servers are created. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidPeriod | Invalid period. Supported period values are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36 (in month). |
| InvalidProjectId.NotFound | Invalid project ID. The specified project ID does not exist. |
| InvalidRegion.NotFound | The region cannot be found. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

### Example 1 Purchase a prepaid CDH instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=AllocateHosts
&Placement.Zone=ap-guangzhou-2
&HostChargeType=PREPAID
&HostChargePrepaid.Period=1
&HostChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&HostType=HS1
&HostCount=1
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "HostIdSet": [
      "host-lan4lb2k"
    ],
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```



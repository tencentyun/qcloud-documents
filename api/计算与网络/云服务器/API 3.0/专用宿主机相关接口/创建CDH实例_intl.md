## 1. API Description

This API (AllocateHosts) is used to create one or more CDH instances with specified configuration.
* When HostChargeType is PREPAID, the HostChargePrepaid parameter must be specified.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
| ----------------- | -------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| Action | Yes | String | Common parameter. Value​used in this API: AllocateHosts |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| ClientToken | No | String | A string to ensure the idempotency of the request. |
| Placement | Yes | [Placement](/document/api/213/15753#Placement) | Location of the instance. This parameter is used to specify the availability zone and project to which the instance belongs, etc. |
| HostChargePrepaid | No | [ChargePrepaid](/document/api/213/15753#ChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the purchased usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. If the payment mode of the specified instance is prepaid, this parameter must be submitted. |
| HostChargeType | No | String | Billing type of instance. Only PREPAID (prepaid, that is prepaid mode) is supported for now. |
| HostType | No | String | CDH instance model, default is: 'HS1'. |
| HostCount | No | Integer | Number of CDH instances purchased. |

## 3. Output Parameters



| Parameter Name | Type | Description |
| --------- | --------------- | ------------------------------------------------------------ |
| HostIdSet | Array of String | List of instance IDs for newly created cloud server. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
| -------------------------- | ------------------------------------------------------------ |
| InvalidPeriod | Invalid period. The periods supported are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] (in month). |
| InvalidProjectId.NotFound | Invalid project ID. The specified project ID does not exist. |
| InvalidRegion.NotFound | The region is not found. |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |

## 5. Example

## Example 1 Purchase Prepaid CDH Instances

### Scenario description

Purchase prepaid CDH instances


### Request parameters

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
### Response parameters

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

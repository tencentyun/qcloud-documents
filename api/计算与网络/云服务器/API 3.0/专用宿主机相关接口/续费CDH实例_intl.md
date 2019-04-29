## 1. API Description

This API (RenewHosts) is used to renew the prepaid CDH instances.

* Only the prepaid instances are supported, otherwise a specific [error code](#4.-.E9.94.99.E8.AF.AF.E7.A0.81) will be returned.
* Make sure the account balance is sufficient when renewing. You can query the account balance via the [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397) API.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: RenewHosts |
| Version | Yes | String | Common parameter. Value​used in this API: 2017-03-12 |
| HostIds.N | Yes | Array of String | ID(s) of one or more CDH instance to be operated. |
| HostChargePrepaid | Yes | [ChargePrepaid](/document/api/213/15753#ChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the purchased usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. If the payment mode of the specified instance is prepaid, this parameter must be submitted. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidHost.NotSupported | This host instance is not supported for performing the specified operation. |
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID`format is incorrect. For example, `ID` length error `host-1122`. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |

## 5. Example

## Example 1 Renew CDH Instances

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=RenewHosts
&HostChargePrepaid.Period=1
&HostChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&HostIds.1=host-ey16rkyg
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```


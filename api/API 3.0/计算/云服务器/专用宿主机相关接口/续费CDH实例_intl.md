## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (RenewHosts) is used to renew the prepaid CDH instances.

* Only the prepaid instances are supported, otherwise a specific [error code](#4.-.E9.94.99.E8.AF.AF.E7.A0.81) will be returned.
* Make sure your account balance is sufficient for renewals. You can query the account balance via API [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397).

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: RenewHosts |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| HostIds.N | Yes | Array of String | ID(s) of one or more CDH instances you are working with. |
| HostChargePrepaid | Yes | [ChargePrepaid](/document/api/213/##ChargePrepaid) | Indicates the relevant parameter setting for the prepaid mode. This parameter can specify the usage period, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. This parameter is required if the billing method for the specified instance is prepaid. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidHost.NotSupported | This host instance is not supported for performing the specified operation. |
| InvalidHostId.Malformed | Invalid [CDH](https://cloud.tencent.com/document/product/416) `ID`. The specified [CDH](https://cloud.tencent.com/document/product/416) `ID` is in an incorrect format. For example, `host-1122` has an invalid `ID` length. |
| InvalidHostId.NotFound | The specified HostId does not exist, or does not belong to the request account. |

## 5. Example

### Example 1 Renew a CDH instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=RenewHosts
&HostChargePrepaid.Period=1
&HostChargePrepaid.RenewFlag=NOTIFY_AND_AUTO_RENEW
&HostIds.0=host-ey16rkyg
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
  }
}
```



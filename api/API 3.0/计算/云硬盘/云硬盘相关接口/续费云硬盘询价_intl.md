## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (InquiryPriceRenewDisks) is used to inquire the prices for renewing cloud disks.

* Only the prices of renewed prepaid elastic cloud disks can be queried.
* The mounted cloud disk can be renewed together with the instance. The CurInstanceDeadline in the [DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid) parameter must be specified. In such case, you can inquire the price for renewing the cloud disk to the expiration time of the instance.
* You can specify different renewal lengths for multiple cloud disks. The price returned in such case is the total price for renewal of multiple cloud disks.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceRenewDisks |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskIds.N | Yes | Array of String | Cloud disk ID, which can be queried via the API [DescribeDisks](/document/product/362/16315). |
| DiskChargePrepaids.N | No | Array of [DiskChargePrepaid](/document/api/362/##DiskChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter can specify the usage period of a prepaid instance. If CurInstanceDeadline is specified in this parameter, the cloud disk is renewed to the expiration time of the server. If the price for batch renewal is inquired, this parameter corresponds to the Disks parameter and the number of elements must be the same. |
| NewDeadline | No | String | Specifies the new expiration time of the cloud disk, in such format as 2017-12-17 00:00:00. The parameters `NewDeadline` and `DiskChargePrepaids` are two options to specify the inquiry length, and you must specify at least one. |
| ProjectId | No | Integer | ID of the project to which the cloud disk belongs. This parameter is only used for authentication. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskPrice | [Price](/document/api/362/##Price) | Indicates the price for the renewal of the cloud disk. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.NotPortable | Non-elastic cloud disk is not supported. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Inquire the price for renewing the cloud disk for 1 month

#### Input Example

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceRenewDisks
&DiskIds.0=disk-jwk0zvrg
&DiskChargePrepaids.0.Period=1
&<Common request parameters>
```

#### Output Example

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 33.26,
      "OriginalPrice": 37.8
    },
    "RequestId": "7269a7c9-daa0-48aa-372a-5a1f8029a4f4"
  }
}
```

### Example 2 When renewing an instance, you need to renew the mounted prepaid cloud disk to make its expiration time the same as that of the instance.

#### Input Example

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceRenewDisks
&DiskIds.0=disk-jwk0zvrg
&DiskChargePrepaids.0.Period=1
&DiskChargePrepaids.0.CurInstanceDeadline=2018-03-17 15:15:03
&<Common request parameters>
```

#### Output Example

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 6.0,
      "OriginalPrice": 6.0
    },
    "RequestId": "f31302ca-7e60-412c-9d84-0675e09db295"
  }
}
```



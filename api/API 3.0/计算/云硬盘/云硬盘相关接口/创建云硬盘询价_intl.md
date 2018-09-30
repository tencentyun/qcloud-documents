## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (InquiryPriceCreateDisks) is used to inquire the price for cloud disk creation.

* It supports inquiring the price for the creation of multiple cloud disks. The total price for the creation is returned.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceCreateDisks |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskType | Yes | String | Cloud disk type. Value range: <br><li>HDD cloud disk: CLOUD_BASIC <br><li>Premium cloud disk: CLOUD_PREMIUM <br><li>SSD cloud disk: CLOUD_SSD. |
| DiskSize | Yes | Integer | Cloud disk size (in GB). For the value range of cloud disks, please see CBS [Product Category](/document/product/362/2353). |
| DiskChargeType | Yes | String | Billing type of the cloud disk.<br><li> PREPAID: prepaid (by year/month) <br><li>POSTPAID_BY_HOUR: postpaid by hour |
| DiskChargePrepaid | No | [DiskChargePrepaid](/document/api/362/##DiskChargePrepaid) | Prepaid mode, which is the relevant parameter setting for prepaid mode. This parameter is used to specify the purchased usage period, whether to set automatic renewal and other attributes of the cloud disk purchased on a prepaid basis. <br> This parameter is required to create a prepaid cloud disk, while it is not required for a postpaid cloud disk on an hourly basis. |
| DiskCount | No | Integer | The number of cloud disks to be purchased. It defaults to 1 if left empty. |
| ProjectId | No | Integer | ID of the project to which the cloud disk belongs. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskPrice | [Price](/document/api/362/##Price) | Describes the price of the cloud disk to be purchased. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Inquire the price for purchasing a HDD cloud disk (50 GB) for 6 months

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceCreateDisks
&DiskType=CLOUD_BASIC
&DiskSize=50
&DiskChargeType=PREPAID
&DiskChargePrepaid.Period=6
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 92.4,
      "OriginalPrice": 105.0
    },
    "RequestId": "c438f713-64a8-4d66-b924-5a1f80cf74e8"
  }
}
```

### Example 2 Inquire the price for purchasing a postpaid cloud disk on an hourly basis.

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceCreateDisks
&DiskType=CLOUD_PREMIUM
&DiskSize=100
&DiskCount=1
&DiskChargeType=POSTPAID_BY_HOUR
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DiskPrice": {
      "ChargeUnit": "HOUR",
      "UnitPrice": 0.09
    },
    "RequestId": "dbf177bd-21f5-4e79-93f2-099e529382b8"
  }
}
```



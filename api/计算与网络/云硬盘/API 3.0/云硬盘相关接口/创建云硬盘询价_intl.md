## 1. API Description

This API (InquiryPriceCreateDisks) is used to inquire the price for cloud disk creation.

* It supports inquiring the price for the creation of multiple cloud disks. The total price for the creation is returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: InquiryPriceCreateDisks |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskType | Yes | String | Cloud disk type. Value range: <li>HDD cloud disk: CLOUD_BASIC </li><li>Premium cloud disk: CLOUD_PREMIUM </li><li>SSD SSD cloud disk: CLOUD_SSD. |
| DiskSize | Yes | Integer | Cloud disk size. Value range: HDD cloud disk: 10 GB - 4,000 GB; Premium cloud disk: 50 GB - 4,000 GB; SSD cloud disk: 100 GB - 4,000 GB. The step width is 10 GB. |
| DiskChargeType | Yes | String | Billing method (Prepaid). Currently, the value can only be PREPAID. |
| DiskChargePrepaid | No | [DiskChargePrepaid](/document/api/362/15669#DiskChargePrepaid) | It is the relevant parameter setting for prepaid mode. This parameter is used to specify the purchased usage period of a prepaid cloud disk. It is required to create a prepaid cloud disk. |
| DiskCount | No | Integer | The number of purchased cloud disks. If it is left empty, the default is 1. |
| ProjectId | No | Integer | ID of the project to which the cloud disk belongs |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskPrice | [Price](/document/api/362/15669#Price) | This parameter indicates the price of the purchased cloud disk |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Inquire the Price for Purchasing an HDD Cloud Disk (50 GB) for 6 months

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceCreateDisks
&DiskType=CLOUD_BASIC
&DiskSize=50
&DiskChargeType=PREPAID
&DiskChargePrepaid.Period=6
&<Common request parameters>
```
### Return parameters

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


        

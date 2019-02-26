## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (InquiryPriceResizeDisk) is used to inquire the price for the capacity expansion of cloud disks.

* Only the price for the capacity expansion of prepaid cloud disks can be queried.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: InquiryPriceResizeDisk |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskId | Yes | String | Cloud disk ID, which can be queried via the API [DescribeDisks](/document/product/362/16315). |
| DiskSize | Yes | Integer | The capacity of the expanded cloud disk (in GB), which must be greater than or equal to the original cloud disk size. For the value range of cloud disks, please see CBS [Product Category](/document/product/362/2353). |
| ProjectId | No | Integer | ID of the project to which the cloud disk belongs. This parameter is only used for authentication. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskPrice | [Price](/document/api/362/##Price) | Describes the price of a cloud disk. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.Expire | The cloud disk has expired. |
| InvalidDisk.NotPortable | Non-elastic cloud disk is not supported. |
| InvalidInstanceId.NotFound | The `InstanceId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Query the price for expanding the cloud disk capacity to 200 GB

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceResizeDisk
&DiskId=disk-dw0bbzws
&DiskSize=200
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DiskPrice": {
      "DiscountPrice": 210.09,
      "OriginalPrice": 210.09
    },
    "RequestId": "2ba7b520-ddb4-f5ea-34d1-5a1f80434911"
  }
}
```



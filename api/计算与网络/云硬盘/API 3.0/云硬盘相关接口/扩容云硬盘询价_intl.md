## 1. API Description

This API (InquiryPriceResizeDisk) is used to inquire the price for the capacity expansion of cloud disks.

* Only the price for the capacity expansion of prepaid cloud disks can be queried.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: InquiryPriceResizeDisk |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskId | Yes | String | ID of the cloud disk, which can be queried via the API [DescribeDisks](/document/product/362/16315). |
| DiskSize | Yes | Integer | The capacity of the expanded cloud disk (in GB), which must be greater than or equal to the original cloud disk size. Value range: HDD cloud disk: 10 GB - 4,000 GB; Premium cloud disk: 50 GB - 4,000 GB; SSD cloud disk: 100 GB - 4,000 GB. The step width is 10 GB. |
| ProjectId | No | Integer | ID of the project to which the cloud disk belongs. This parameter is only used for authentication. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| DiskPrice | [Price](/document/api/362/15669#Price) | This parameter indicates the price for the capacity expansion of cloud disks. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidDisk.Expire | The cloud disk has expired. |
| InvalidDisk.NotPortable | Non-elastic cloud disks cannot be mounted. |
| InvalidInstanceId.NotFound | The `InstanceId` of the instance does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Query the Price for Expanding the Cloud Disk Capacity to 200 GB

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=InquiryPriceResizeDisk
&DiskId=disk-dw0bbzws
&DiskSize=200
&<Common request parameters>
```
### Return parameters

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


        

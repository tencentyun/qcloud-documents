## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (ResizeDisk) is used to expand the capacity of the cloud disk.

* Only elastic cloud disks can be expanded. Cloud disk type can be queried in Portable field in the output parameters returned by the API [DescribeDisks](/document/product/362/16315). For the cloud disk created along with a CVM, the capacity can only be expanded via the API [ResizeInstanceDisks](/document/product/213/15731).
* This API is an asynchronous API. The cloud disk is not immediately expanded to the specified size as the API successfully returns results. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. The cloud disk in the status of "EXPANDING" is in the process of capacity expansion. When the status changes to "UNATTACHED", the capacity expansion is completed. 

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ResizeDisk |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskId | Yes | String | Cloud disk ID, which can be queried via the API [DescribeDisks](/document/product/362/16315). |
| DiskSize | Yes | Integer | The capacity of the expanded cloud disk (in GB), which must be greater than the original cloud disk size. For the value range of cloud disks, please see CBS [Product Category](/document/product/362/2353). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.Busy | The cloud disk is busy. Try again later. |
| InvalidDisk.Expire | The cloud disk has expired. |
| InvalidDisk.NotSupported | Indicates that the operation is not supported for the cloud disk. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Expand the capacity of the cloud disk to 200 GB

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=ResizeDisk
&DiskId=disk-lzrg2pwi
&DiskSize=200
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "adefc06d-2cf1-29f6-24a6-5a1f81b5c0ac"
  }
}
```



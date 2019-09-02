## 1. API Description

This API (ResizeDisk) is used to expand the capacity of the cloud disk.

* Only elastic cloud disks can be expanded. The cloud disk type can be queried in the Portable field in the output parameters through the API [DescribeDisks](/document/product/362/16315). For the cloud disk created along with the CVM, the capacity can only be expanded via the API [ResizeInstanceDisks](/document/product/213/15731).
* This API is an asynchronous API. The cloud disk is not immediately expanded to the specified size as the API successfully returns results. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. The cloud disk in the status of "EXPANDING" is in the process of capacity expansion. When the status changes to "UNATTACHED", the capacity expansion is completed. 

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ResizeDisk |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskId | Yes | String | ID of the cloud disk, which can be queried via the API [DescribeDisks](/document/product/362/16315). |
| DiskSize | Yes | Integer | The capacity of the expanded cloud disk (in GB), which must be greater than the original cloud disk size. Value range: HDD cloud disk: 10 GB - 4,000 GB; Premium cloud disk: 50 GB - 4,000 GB; SSD cloud disk: 100 GB - 4,000 GB. The step width is 10 GB. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidDisk.Busy | The cloud disk is busy. Try again later. |
| InvalidDisk.Expire | The cloud disk has expired. |
| InvalidDisk.NotSupported | This operation is not supported for cloud disks. |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Expand the Capacity of the Cloud Disk to 200 GB

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=ResizeDisk
&DiskId=disk-lzrg2pwi
&DiskSize=200
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "adefc06d-2cf1-29f6-24a6-5a1f81b5c0ac"
  }
}
```



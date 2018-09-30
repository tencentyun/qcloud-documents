Location: CBS -> API Documentation -> CBS-related APIs -> Unmount Cloud Disk Change Log (Latest version: 2017.4.5)
     Operation
Basic Information Content Extended Configuration
  
 URL for documentation (Chinese)

master/
 
Content  

## 1. API Description

This API (DetachDisks) is used to unmount cloud disks.

* Batch operations are supported. Multiple cloud disks mounted to the same CVM can be unmounted in batch. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.
* This API is an asynchronous API. When the request successfully returns results, the cloud disk is not unmounted from the CVM immediately. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. If the status changes from "ATTACHED" to "UNATTACHED", the cloud disk is unmounted.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DetachDisks |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskIds.N | Yes | Array of String | ID of the cloud disk to be unmounted, which can be queried through the API [DescribeDisks](/document/product/362/16315). A maximum of 10 elastic cloud disks can be unmounted in a single request. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalError.ResourceOpFailed | The operation performed on the resource failed. For the specific error information, please see the Message field in the error description. Try again later or contact the customer service for help. |
| InvalidDisk.NotPortable | Non-elastic cloud disks cannot be mounted. |
| InvalidDisk.NotSupported | This operation is not supported for cloud disks. |
| InvalidDisk.TypeError | Invalid cloud disk type |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Unmount a Cloud Disk

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=DetachDisks
&DiskIds.0=disk-lzrg2pwi
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "aafa71a0-ed62-0fac-3ebf-5a1f808d1085"
  }
}
```



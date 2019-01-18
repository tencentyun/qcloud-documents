
## 1. API Description

This API (AttachDisks) is used to mount cloud disks.

* Batch operations are supported. Multiple cloud disks can be mounted to a CVM. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.
* This API is an asynchronous API. If the request for mounting the cloud disk successfully returns results, the operation of mounting cloud disk has been initiated at the background. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. If the status changes from "ATTACHING" to "ATTACHED", the cloud disk is mounted.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: AttachDisks |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskIds.N | Yes | Array of String | ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](/document/product/362/16315). A maximum of 10 elastic cloud disks can be mounted in a single request. |
| InstanceId | Yes | String | ID of the CVM instance, which can be queried via the API [DescribeInstances](/document/product/213/15728). The cloud disk will be mounted to this CVM. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalError.ResourceOpFailed | The operation performed on the resource failed. For the specific error information, please see the Message field in the error description. Try again later or contact the customer service for help. |
| InvalidDisk.Attached | The cloud disk has been mounted. |
| InvalidDisk.NotPortable | Non-elastic cloud disks cannot be mounted. |
| InvalidDisk.NotSupported | This operation is not supported for cloud disks. |
| InvalidDisk.TypeError | Invalid cloud disk type |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidInstance.NotSupported | cloud disks cannot be mounted to the CVM. |
| InvalidInstanceId.NotFound | The `InstanceId` of the instance does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| ZoneNotMatch | The cloud disk and the instance are not in the same availability zone. |

## 5. Example

## Example 1 Mount Cloud Disk

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=AttachDisks
&DiskIds.0=disk-lzrg2pwi
&InstanceId=ins-dyzmimrw
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "e0f140e5-14d6-c4a1-91e0-5a1f7f05a68a"
  }
}
```


        

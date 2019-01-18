## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (AttachDisks) is used to mount cloud disks.

* Batch operations are supported. Multiple cloud disks can be mounted to a CVM. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.
* This API is an asynchronous API. If the request for mounting the cloud disk successfully returns results, the operation of mounting cloud disk has been initiated at the background. You can use the API [DescribeDisks](/document/product/362/16315) to query the cloud disk status. If the status changes from "ATTACHING" to "ATTACHED", the cloud disk is mounted.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: AttachDisks |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskIds.N | Yes | Array of String | ID of the elastic cloud disk to be mounted, which can be queried through the API [DescribeDisks](/document/product/362/16315). A maximum of 10 elastic cloud disks can be mounted in a single request. |
| InstanceId | Yes | String | CVM instance ID, which can be queried via the API [DescribeInstances](/document/product/213/15728). |
| DeleteWithInstance | No | Boolean | Optional parameter. Only mounting is performed if no parameter is passed. If `True` is passed in, the cloud disk is configured to "deleted with CVM" mode (only for postpaid cloud disks). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.ResourceOpFailed | The operation performed on the resource failed. For error message, please see the "Message" field in error description. Try again later or contact customer service. |
| InvalidDisk.Attached | The cloud disk has been mounted. |
| InvalidDisk.NotPortable | Non-elastic cloud disk is not supported. |
| InvalidDisk.NotSupported | Indicates that the operation is not supported for the cloud disk. |
| InvalidDisk.TypeError | Invalid cloud disk type |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidInstance.NotSupported | The cloud disk cannot be mounted to the CVM |
| InvalidInstanceId.NotFound | The `InstanceId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeded the limit. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |
| ZoneNotMatch | The cloud disk and the instance are not in the same availability zone. |

## 5. Example

## Example 1 Mount cloud disk

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=AttachDisks
&DiskIds.0=disk-lzrg2pwi
&InstanceId=ins-dyzmimrw
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "e0f140e5-14d6-c4a1-91e0-5a1f7f05a68a"
  }
}
```



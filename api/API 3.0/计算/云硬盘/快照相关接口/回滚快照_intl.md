## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (ApplySnapshot) is used to roll back a snapshot to the original cloud disk.

* A snapshot can only be rolled back to the original cloud disk. For data disk snapshots, if you need to copy the snapshot data to other cloud disks, use the API [CreateDisks](/document/product/362/16312) to create an elastic cloud disk and then copy the snapshot data to the created cloud disk. 
* The snapshot for rollback must be in NORMAL status. The snapshot status can be queried in the SnapshotState field returned by the API [DescribeSnapshots](/document/product/362/15647).
* For elastic cloud disks, the cloud disk must be unmounted. The mounting status of a cloud disk can be obtained from the Attached field returned via the API [DescribeDisks](/document/product/362/16315). For non-elastic cloud disks purchased together with instances, the instance must be shut down. The instance status can be queried through the API [DescribeInstancesStatus](/document/product/213/15738).

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ApplySnapshot |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SnapshotId | Yes | String | Snapshot ID, which can be queried using [DescribeSnapshots](/document/product/362/15647). |
| DiskId | Yes | String | ID of the original cloud disk of the snapshot, which can be queried via the API [DescribeDisks](/document/product/362/16315). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.Busy | The cloud disk is busy. Try again later. |
| InvalidDisk.NotSupported | Indicates that the operation is not supported for the cloud disk. |
| InvalidDisk.SnapshotCreating | A snapshot is being created for the cloud disk. Try again later. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidInstanceId.NotFound | The `InstanceId` entered does not exist. |
| InvalidParameter.DiskSizeNotMatch | The size of the cloud disk does not match the snapshot size. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidSnapshot.NotSupported | Indicates that the operation is not supported for the snapshot. |
| InvalidSnapshotId.NotFound | The `SnapshotId` entered does not exist. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |
| ResourceBusy | The resource is busy. Try again later. |

## 5. Example

### Example 1 Create a snapshot

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=ApplySnapshot
&DiskId=disk-lzrg2pwi
&SnapshotId=snap-gybrif0z
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "cc96242e-566c-ae6a-b74a-5a1f823683b2"
  }
}
```



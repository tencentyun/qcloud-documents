## 1. API Description

This API (ApplySnapshot) is used to roll back a snapshot to the original cloud disk.

* The snapshot can only be rolled back to the original cloud disk. For data disk snapshots, if you need to copy the snapshot data to other cloud disks, use the API [CreateDisks](/document/product/362/16312) to create an elastic cloud disk and then copy the snapshot data to the created cloud disk. 
* The snapshot for rollback must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](/document/product/362/15647).
* For elastic cloud disks, the cloud disk must be in UNMOUNTED status. The cloud disk status can be queried in the Attached field returned by the API [DescribeDisks](/document/product/362/16315). For non-elastic cloud disks purchased together with CVMs, the CVM must be in SHUTDOWN status. The CVM status can be queried through the API [DescribeInstancesStatus](/document/product/213/15738).

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ApplySnapshot |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| SnapshotId | Yes | String | Snapshot ID, which can be queried via [DescribeSnapshots](/document/product/362/15647). |
| DiskId | Yes | String | ID of the original cloud disk corresponding to the snapshot, which can be queried via the API [DescribeDisks](/document/product/362/16315). |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidDisk.Busy | The cloud disk is busy. Try again later. |
| InvalidDisk.NotSupported | This operation is not supported for cloud disks. |
| InvalidDisk.SnapshotCreating | A snapshot is being created for the cloud disk. Try again later. |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidInstanceId.NotFound | The `InstanceId` of the instance does not exist. |
| InvalidParameter.DiskSizeNotMatch | The size of the cloud disk does not match the snapshot size. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidSnapshot.NotSupported | This operation is not supported for the snapshot. |
| InvalidSnapshotId.NotFound | The `SnapshotId` does not exist. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| ResourceBusy | The resource is busy. Try again later. |

## 5. Example

## Example 1 Create a Snapshot

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=ApplySnapshot
&DiskId=disk-lzrg2pwi
&SnapshotId=snap-gybrif0z
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "cc96242e-566c-ae6a-b74a-5a1f823683b2"
  }
}
```


        

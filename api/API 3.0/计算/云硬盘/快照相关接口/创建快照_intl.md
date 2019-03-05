## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (CreateSnapshot) is used to create a snapshot of a specified cloud disk.

* Snapshots can only be created for cloud disks with the snapshot capability. To check whether a cloud disk has the snapshot capability, please see the SnapshotAbility field returned by the API [DescribeDisks](/document/product/362/16315).
* For the number of snapshots that can be created, please see [Product Usage Restriction](https://cloud.tencent.com/doc/product/362/5145).

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateSnapshot |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskId | Yes | String | ID of the cloud disk for which a snapshot needs to be created. It can be queried via the API [DescribeDisks](/document/product/362/16315). |
| SnapshotName | No | String | Snapshot name. If it is left empty, the new snapshot name is "Not named" by default. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| SnapshotId | String | ID of the new snapshot. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InsufficientSnapshotQuota | Insufficient snapshot quota. |
| InvalidAccount.InsufficientBalance | Insufficient account balance. |
| InvalidDisk.NotSupportSnapshot | The cloud disk does not have the snapshot capability. |
| InvalidDisk.NotSupported | Indicates that the operation is not supported for the cloud disk. |
| InvalidDisk.SnapshotCreating | A snapshot is being created for the cloud disk. Try again later. |
| InvalidDisk.TypeError | Invalid cloud disk type. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Create a snapshot

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=CreateSnapshot
&DiskId=disk-lzrg2pwi
&SnapshotName=snap_201711301015
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "1bd35eca-0c9a-6e0b-938a-5a1f80511c19",
    "SnapshotId": "snap-gybrif0z"
  }
}
```



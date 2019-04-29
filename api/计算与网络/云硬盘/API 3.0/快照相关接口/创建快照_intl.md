## 1. API Description

This API (CreateSnapshot) is used to create a snapshot of a specified cloud disk.

* Snapshots can only be created for cloud disks with the snapshot capability. To check whether a cloud disk has the snapshot capability, see the SnapshotAbility field returned by the API [DescribeDisks](/document/product/362/16315).
* For the number of snapshots that can be created, please see [Product Usage Restriction](https://cloud.tencent.com/doc/product/362/5145).

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: CreateSnapshot |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskId | Yes | String | ID of the cloud disk, for which a snapshot needs to be created. It can be queried via the API [DescribeDisks](/document/product/362/16315). |
| SnapshotName | No | String | Snapshot name. If it is left empty, the default is "not named". |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| SnapshotId | String | ID of the created snapshot |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InsufficientSnapshotQuota | The snapshot quota is insufficient. |
| InvalidAccount.InsufficientBalance | Insufficient account balance. |
| InvalidDisk.NotSupportSnapshot | The cloud disk does not have the snapshot capability. |
| InvalidDisk.NotSupported | This operation is not supported for cloud disks. |
| InvalidDisk.SnapshotCreating | A snapshot is being created for the cloud disk. Try again later. |
| InvalidDisk.TypeError | Invalid cloud disk type |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Create a Snapshot

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=CreateSnapshot
&DiskId=disk-lzrg2pwi
&SnapshotName=snap_201711301015
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "1bd35eca-0c9a-6e0b-938a-5a1f80511c19",
    "SnapshotId": "snap-gybrif0z"
  }
}
```


        

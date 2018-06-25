## 1. API Description

This API (DescribeSnapshots) is used to query the details of snapshots.

* Filter the results by the snapshot ID, the ID of cloud disk, for which the snapshot is created, and the type of cloud disk, for which the snapshot is created. The relationship between different conditions is AND. For more information about filtering, please see `Filter`.
* If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of snapshot lists are returned to the current user.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeSnapshots |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| SnapshotIds.N | No | Array of String | List of IDs of the snapshots to be queried. This parameter does not support specifying both `SnapshotIds` and `Filters`. |
| Filters.N | No | Array of [Filter](/document/api/362/15669#Filter) | Filter conditions. This parameter does not support specifying both `SnapshotIds` and `Filters`. <li>snapshot-id - Array of String - Required or not: No - (Filter condition) Filter by the snapshot ID in such format as `snap-11112222`. </li><li>snapshot-name - Array of String - Required or not: No - (Filter condition) Filter by the snapshot name. </li><li>snapshot-state - Array of String - Required or not: No - (Filter condition) Filter by the snapshot status (NORMAL: normal &#124; CREATING: creating &#124; ROLLBACKING: rolling back). </li><li>disk-usage - Array of String - Required or not: No - (Filter condition) Filter by the type of the cloud disk for which the snapshot is created (SYSTEM_DISK: system disk &#124; DATA_DISK: data disk). </li><li>project-id - Array of String - Required or not: No - (Filter condition) Filter by ID of the project to which the cloud disk belongs. </li><li>disk-id - Array of String - Required or not: No - (Filter condition) Filter by the ID of the cloud disk for which the snapshot is created. </li><li>zone - Array of String - Required or not: No - (Filter condition) Filter by [availability zone](/document/api/213/9452#zone). |
| Offset | No | Integer | Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](/document/product/362/15633). |
| Limit | No | Integer | Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](/document/product/362/15633). |
| Order | No | String | The order of the output cloud disk list. Value range: <li>ASC: sort in an ascending order </li><li>DESC: sort in a descending order.</li> |
| OrderField | No | String | The field by which the snapshot list is sorted. Value range: <li>CREATETIME: sorted by the creation time of snapshots </li>By default, the snapshot list is sorted by the creation time of snapshots. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of snapshots. |
| SnapshotSet | Array of [Snapshot](/document/api/362/15669#Snapshot) | List of snapshot details |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidFilter | The specified Filter is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Query the Snapshots in NORMAL Status in Guangzhou Zone 2

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=DescribeSnapshots
&Filters.0.Name=snapshot-state
&Filters.0.Values.0=NORMAL
&Filters.1.Name=zone
&Filters.1.Values.0=ap-guangzhou-2
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "3a823099-86f1-6887-6273-5a1f8043d8a3",
    "SnapshotSet": [
      {
        "CreateTime": "2018-04-12 17:34:45",
        "DeadlineTime": null,
        "DiskId": "disk-22rkwrvw",
        "DiskSize": 10,
        "DiskUsage": "DATA_DISK",
        "Encrypt": false,
        "IsPermanent": true,
        "Percent": 100,
        "Placement": {
          "ProjectId": 0,
          "Zone": "ap-guangzhou-2"
        },
        "SnapshotId": "snap-1i97mf6d",
        "SnapshotName": "test_snap_count",
        "SnapshotState": "NORMAL"
      }
    ],
    "TotalCount": 1
  }
}
```



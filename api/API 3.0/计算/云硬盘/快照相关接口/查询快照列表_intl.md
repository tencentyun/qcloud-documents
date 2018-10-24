## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (DescribeSnapshots) is used to query the details of snapshots.

* Filter the results by the snapshot ID, the ID of cloud disk, for which the snapshot is created, and the type of cloud disk, for which the snapshot is created. The relationship between different conditions is AND. For more information about filtering, please see `Filter`.
* If the parameter is empty, a certain number (specified by `Limit`; the default is 20) of snapshot lists are returned to the current user.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeSnapshots |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SnapshotIds.N | No | Array of String | List of IDs of the snapshots to be queried. The parameter does not support specifying both `SnapshotIds` and `Filters`. |
| Filters.N | No | Array of [Filter](/document/api/362/##Filter) | Filter conditions. The parameter does not support specifying both `SnapshotIds` and `Filters`.<br><li> snapshot-id - Array of String - Required: No - (Filter condition) Filter by the snapshot ID in the format of `snap-11112222`.<br><li> snapshot-name - Array of String - Required: No - (Filter condition) Filter by the snapshot name.<br><li> snapshot-state - Array of String - Required: No - (Filter condition) Filter by the snapshot status. (NORMAL: Normal &#124; CREATING: Creating &#124; ROLLBACKING: Rolling back)<br><li> disk-usage - Array of String - Required: No - (Filter condition) Filter by the type of the cloud disk for which the snapshot is created. (SYSTEM_DISK: System disk &#124; DATA_DISK: Data disk)<br><li> project-id - Array of String - Required: No - (Filter condition) Filter by the ID of the project to which the cloud disk belongs.<br><li> disk-id - Array of String - Required: No - (Filter condition) Filter by the ID of the cloud disk for which the snapshot is created.<br><li> zone - Array of String - Required: No - (Filter condition) Filter by the [availability zone](/document/api/213/9452#zone).<br><li> encrypt - Array of String - Required: No - (Filter condition) Filter by whether the snapshot is created from an encrypted disk. (TRUE: Encrypted disk &#124; FALSE: Non-encrypted disk) |
| Offset | No | Integer | Offset. Default is 0. For more information on `Offset`, please see relevant sections in API [Introduction](/document/product/362/15633). |
| Limit | No | Integer | Number of results to be returned. Default is 20. Maximum is 100. For more information on `Limit`, please see relevant sections in API [Introduction](/document/product/362/15633). |
| Order | No | String | The order of the output cloud disk list. Value: <br><li>ASC: Sort in an ascending order<br><li>DESC: Sort in a descending order. |
| OrderField | No | String | The field by which the snapshot list is sorted. Value:<br><li>CREATE_TIME: Sorted by the creation time of snapshots<br>By default, the snapshot list is sorted by the creation time of snapshots. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of snapshots. |
| SnapshotSet | Array of [Snapshot](/document/api/362/##Snapshot) | List of snapshot details. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidFilter | The specified Filter is not supported. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Query the snapshots in NORMAL status in Guangzhou Zone 2

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=DescribeSnapshots
&Filters.0.Name=snapshot-state
&Filters.0.Values.0=NORMAL
&Filters.1.Name=zone
&Filters.1.Values.0=ap-guangzhou-2
&<Common request parameters>
```

#### Output example

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



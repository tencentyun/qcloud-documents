## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (ModifySnapshotAttribute) is used to modify the attributes of a specified snapshot.

* Currently, you can only modify snapshot name and change non-permanent snapshots into permanent snapshots.
* "Snapshot name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or snapshot management.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifySnapshotAttribute |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| SnapshotId | Yes | String | Snapshot ID, which can be queried using [DescribeSnapshots](/document/product/362/15647). |
| SnapshotName | No | String | New snapshot name with a maximum length of 60 characters. |
|| IsPermanent | No | Boolean | The retention time of the snapshot. FALSE: non-permanent retention; TRUE: permanent retention. You can only modify non-permanent snapshots to permanent snapshots. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidSnapshot.NotSupported | Indicates that the operation is not supported for the snapshot. |
| InvalidSnapshotId.NotFound | The `SnapshotId` entered does not exist. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Modify snapshot name

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=ModifySnapshotAttribute
&SnapshotId=snap-gybrif0z
&SnapshotName=snap_201711301143
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
  }
}
```



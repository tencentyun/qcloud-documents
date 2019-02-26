
## 1. API Description

This API (ModifySnapshotAttribute) is used to modify the attributes of a specified snapshot.

* Currently, you can only modify snapshot name and change non-permanent snapshots into permanent snapshots.
* "Snapshot name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or snapshot management.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifySnapshotAttribute |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| SnapshotId | Yes | String | Snapshot ID, which can be queried via [DescribeSnapshots](/document/product/362/15647). |
| SnapshotName | No | String | New snapshot name with a maximum of 60 characters. |
| IsPermanent | No | Boolean | The retention time of the snapshot. FALSE: non-permanent retention; TRUE: permanent retention. You can only modify non-permanent snapshots to permanent snapshots. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidSnapshot.NotSupported | This operation is not supported for the snapshot. |
| InvalidSnapshotId.NotFound | The `SnapshotId` does not exist. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Modify Snapshot Name

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=ModifySnapshotAttribute
&SnapshotId=snap-gybrif0z
&SnapshotName=snap_201711301143
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
  }
}
```



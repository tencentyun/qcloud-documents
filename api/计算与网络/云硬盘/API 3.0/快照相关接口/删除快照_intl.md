
## 1. API Description

This API (DeleteSnapshots) is used to delete snapshots.

* The snapshot must be in NORMAL status. The snapshot status can be queried in the SnapshotState field in the output parameters through the API [DescribeSnapshots](/document/product/362/15647).
* Batch operations are supported. If one of the snapshots in a batch cannot be deleted, the operation is not performed and a specific error code is returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DeleteSnapshots |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| SnapshotIds.N | Yes | Array of String | List of IDs of snapshots to be deleted, which can be queried via [DescribeSnapshots](/document/product/362/15647). |

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

## Example 1 Delete a Snapshot

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=DeleteSnapshots
&SnapshotIds.0=snap-gybrif0z
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "b4770576-d9eb-4689-0866-5a1f8200a722"
  }
}
```


        

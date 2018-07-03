
## 1. API Description

This API (ModifyDiskAttributes) is used to modify cloud disk attributes.

* Only the project ID of elastic cloud disk can be modified. The project ID of the cloud disk created with the CVM is linked with the CVM. The project ID can be can be queried in the Portable field in the output parameters through the API [DescribeDisks](/document/product/362/16315).
* "Cloud disk name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or cloud disk management.
* Batch operations are supported. If multiple cloud disk IDs are specified, all the specified cloud disks must have the same attribute. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ModifyDiskAttributes |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskIds.N | Yes | Array of String | ID(s) of one or more cloud disks to be operated. If multiple cloud disk IDs are specified, all the specified cloud disks can only have the same attribute. |
| ProjectId | No | Integer | The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](/document/api/378/4400). |
| DiskName | No | String | The new cloud disk name. |
| Portable | No | Boolean | Whether it is an elastic cloud disk. FALSE: non-elastic cloud disk; TRUE: elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidDisk.NotSupported | This operation is not supported for cloud disks. |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Modify the Cloud Disk Name

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=ModifyDiskAttributes
&DiskIds.0=disk-fyctkqsf
&DiskName=test_data_disk
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "bf84fb00-6949-c0f6-aea8-5a1f806401c2"
  }
}
```


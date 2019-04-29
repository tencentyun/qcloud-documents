## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (ModifyDiskAttributes) is used to modify cloud disk attributes.

* Only the project ID of elastic cloud disk can be modified. The project ID of the cloud disk created with the CVM is linked with the CVM. Cloud disk attributes can be queried in the Portable field in the output parameters through the API [DescribeDisks](/document/product/362/16315).
* "Cloud disk name" is only used by users for their management. Tencent Cloud does not use the name as the basis for ticket submission or cloud disk management.
* Batch operations are supported. If multiple cloud disk IDs are passed in, attributes of all the cloud disks are modified to the same attribute. If there is a cloud disk that does not allow this operation, the operation is not performed and a specific error code is returned.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ModifyDiskAttributes |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskIds.N | Yes |  Array of String | ID(s) of one or more cloud disks to be operated. * If multiple cloud disk IDs are passed in, attributes of all the cloud disks are modified to the same attribute. |
| ProjectId | No | Integer | The new project ID of the cloud disk. Only the project ID of elastic cloud disk can be modified. The available projects and their IDs can be queried via the API [DescribeProject](/document/api/378/4400) |
| DiskName | No | String | The new cloud disk name. |
| Portable | No | Boolean | Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk. You can only modify non-elastic cloud disks to elastic cloud disks. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.NotSupported | Indicates that the operation is not supported for the cloud disk. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Modify the cloud disk name

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=ModifyDiskAttributes
&DiskIds.0=disk-fyctkqsf
&DiskName=test_data_disk
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "bf84fb00-6949-c0f6-aea8-5a1f806401c2"
  }
}
```



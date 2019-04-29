## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.

* Batch operations are supported. If multiple CVM instance IDs are specified, the returned results will list the number of cloud disks mounted on each CVM.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstancesDiskNum |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes | Array of String | CVM instance ID, which can be queried via the API [DescribeInstances](/document/product/213/15728). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| AttachedDiskCount | Integer | The number of elastic cloud disks mounted on the current CVM. |
| MaxAttachCount | Integer | The maximum number of elastic cloud disks that can be mounted on the current CVM. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidDisk.NotPortable | Non-elastic cloud disk is not supported. |
| InvalidDiskId.NotFound | The `DiskId` entered does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Query the number of cloud disks mounted on multiple instances

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=DescribeInstancesDiskNum
&InstanceIds.0=ins-9w5d2buw
&InstanceIds.1=ins-jw0vit58
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca",
    "ins-9w5d2buw": {
      "AttachedDiskCount": 0,
      "MaxAttachCount": 10
    },
    "ins-jw0vit58": {
      "AttachedDiskCount": 0,
      "MaxAttachCount": 10
    }
  }
}
```



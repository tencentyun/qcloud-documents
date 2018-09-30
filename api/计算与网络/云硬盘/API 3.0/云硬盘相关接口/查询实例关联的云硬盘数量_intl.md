## 1. API Description

This API (DescribeInstancesDiskNum) is used to query the number of cloud disks mounted in the instance.

* Batch operations are supported. If multiple CVM instance IDs are specified, the returned results will list the number of cloud disks mounted on each CVM.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: DescribeInstancesDiskNum |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | CVM instance ID, which can be queried via the API [DescribeInstances](/document/product/213/15728) |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| AttachedDiskCount | Integer | The number of elastic cloud disks mounted on the current CVM. |
| MaxAttachCount | Integer | The maximum number of elastic cloud disks that can be mounted on the current CVM |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InvalidDisk.NotPortable | Non-elastic cloud disks cannot be mounted. |
| InvalidDiskId.NotFound | The `DiskId` does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Query the Number of Cloud Disks Mounted on Multiple Instances

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=DescribeInstancesDiskNum
&InstanceIds.0=ins-9w5d2buw
&InstanceIds.1=ins-jw0vit58
&<Common request parameters>
```
### Return parameters

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


        

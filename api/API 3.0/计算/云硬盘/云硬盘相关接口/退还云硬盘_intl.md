## 1. API Description

Domain name for API request: cbs.tencentcloudapi.com

This API (TerminateDisks) is used to return cloud disks.

* The cloud disks that are no longer used can be returned via this API.
* This API supports returning prepaid cloud disks and postpaid cloud disks on an hourly basis. Postpaid cloud disks on an hourly basis can be directly returned via this API; prepaid cloud disks that meet the rules for returning cloud disks can also be returned via this API.
* Batch operations are supported. The maximum number of cloud disks in a batch for each request is 50. If some cloud disks in this batch cannot be operated, a specific error code will be returned.

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cbs.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: TerminateDisks |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/362/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DiskIds.N | Yes | Array of String | The list of IDs of cloud disks to be returned. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/362/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InsufficientRefundQuota | Number of returned cloud disks has reached the limit and no more cloud disks can be returned. |
| InternalError.FailQueryResource | Failed to query the resource. |
| InvalidDisk.Expire | The cloud disk has expired. |
| InvalidDisk.NotSupportRefund | The cloud disk cannot be returned. |
| InvalidDisk.RepeatRefund | The cloud disk has been returned and cannot be returned again. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Return cloud disks in batch

#### Input example

```
https://cbs.tencentcloudapi.com/?Action=TerminateDisks
DiskIds.0=disk-lzrg2pwi
DiskIds.1=disk-g27hqeo2
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "52c965d2-5deb-459a-8b5a-b3b9a1376544"
  }
}
```



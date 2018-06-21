
## 1. API Description

This API (TerminateDisks) is used to return cloud disks.

* Currently, only prepaid cloud disks can be returned.
* Batch operations are supported. The maximum number of cloud disks in a batch for each request is 50. If any cloud disk that does not allow batch operations exists in the batch, an error code is returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/362/15637).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: TerminateDisks |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| DiskIds.N | Yes | Array of String | The list of IDs of cloud disks to be returned. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InsufficientRefundQuota | Number of returned cloud disks has reached the limit and no more cloud disks can be returned. |
| InternalError.FailQueryResource | Failed to query the resource. |
| InvalidDisk.Expire | The cloud disk has expired. |
| InvalidDisk.NotSupportRefund | The cloud disk cannot be returned. |
| InvalidDisk.RepeatRefund | The cloud disk has been returned and cannot be returned again. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Return Cloud Disks in Batch

### Request parameters

```
https://cbs.tencentcloudapi.com/?Action=TerminateDisks
DiskIds.0=disk-lzrg2pwi
DiskIds.1=disk-g27hqeo2
&<Common request parameters>
```
### Return parameters

```
{
  "Response": {
    "RequestId": "52c965d2-5deb-459a-8b5a-b3b9a1376544"
  }
}
```



## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DeleteDisasterRecoverGroups) is used to delete [spread placement groups](https://cloud.tencent.com/document/product/213/15486). Only empty placement groups can be deleted. A place group with CVMs in it cannot be deleted until all the CVMs are terminated, otherwise the deletion may fail.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DeleteDisasterRecoverGroups |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DisasterRecoverGroupIds.N | Yes | Array of String | List of spread placement group IDs which can be obtained via API [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/api/213/17810). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| FailedOperation.PlacementSetNotEmpty | The specified placement group is not empty. |
| ResourceNotFound.InvalidPlacementSet | The specified placement group does not exist. |

## 5. Example

### Example 1 Deletes a spread placement group

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DeleteDisasterRecoverGroups
&DisasterRecoverGroupIds.0=ps-58l1hu01
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
  }
}
```



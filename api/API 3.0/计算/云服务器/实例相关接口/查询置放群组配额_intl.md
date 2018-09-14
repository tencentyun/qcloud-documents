## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeDisasterRecoverGroupQuota) is used to query the quota of [spread placement groups](https://cloud.tencent.com/document/product/213/15486).

A maximum of 20 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDisasterRecoverGroupQuota |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| GroupQuota | Integer | The maximum number of placement groups that can be created. |
| CurrentNum | Integer | The number of placement groups that have been created by the current user. |
| CvmInHostGroupQuota | Integer | Quota of instances in a physical-machine-type disaster recovery group. |
| CvmInSwGroupQuota | Integer | Quota of instances in an exchange-type disaster recovery group. |
| CvmInRackGroupQuota | Integer | Quota of instances in a rack-type disaster recovery group. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, please see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Query the quota of placement groups of an user

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeDisasterRecoverGroupQuota
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "CurrentNum": 25,
    "CvmInHostGroupQuota": 50,
    "CvmInRackGroupQuota": 30,
    "CvmInSwGroupQuota": 20,
    "GroupQuota": 10,
    "RequestId": "a13da94a-1cbc-42ca-ac6c-e14ef0c76a7c"
  }
}
```



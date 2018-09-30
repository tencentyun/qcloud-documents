## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeDisasterRecoverGroups) is used to query the information on a [spread placement group](https://cloud.tencent.com/document/product/213/15486).

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeDisasterRecoverGroups |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| DisasterRecoverGroupIds.N | No | Array of String | List of spread placement group IDs. |
| Name | No | String | Spread placement group name. Fuzzy match is supported. |
| Offset | No | Integer | Offset. Default is 0. For more information about `Offset`, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |
| Limit | No | Integer | Number of values to be returned. Default is 20. Maximum is 100. For more information about `Limit`, please see the relevant section in API [Introduction](https://cloud.tencent.com/document/api/213/15688). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DisasterRecoverGroupSet | Array of [DisasterRecoverGroup](/document/api/213/##DisasterRecoverGroup) | List of information on a spread placement group | |
| TotalCount | Integer | Total number of placement groups of an user. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

There is no error code related to the API business logic. For other error codes, please see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

## 5. Example

### Example 1 Query the information of a spread placement group

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeDisasterRecoverGroups
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "DisasterRecoverGroupSet": [
      {
        "CreateTime": "2018-04-19T02:47:12Z",
        "CurrentNum": 0,
        "CvmQuotaTotal": 30,
        "DisasterRecoverGroupId": "ps-21q9ibvr",
        "InstanceIds": [],
        "Name": "alexpant_test",
        "Type": "RACK"
      }
    ],
    "RequestId": "c68ce193-be41-4d13-9a9b-2dc031db6477",
    "TotalCount": 1
  }
}
```



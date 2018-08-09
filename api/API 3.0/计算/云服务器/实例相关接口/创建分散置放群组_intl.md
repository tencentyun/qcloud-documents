## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (CreateDisasterRecoverGroup) is used to create [Spread Placement Groups](https://cloud.tencent.com/document/product/213/15486). Once a spread placement group is created, you can specify it when [creating an instance](https://cloud.tencent.com/document/api/213/15730).

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateDisasterRecoverGroup |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| Name | Yes | String | Name of a spread placement group with a length of 1-60 characters. |
| Type | Yes | String | Type of a spread placement group. Value range: <br><li>HOST: Physical machine<br><li>SW: Exchange<br><li>RACK: Rack |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| DisasterRecoverGroupId | String | List of spread placement group IDs. |
| Type | String | Type of a spread placement group. Value range: <br><li>HOST: Physical machine<br><li>SW: Exchange<br><li>RACK: Rack |
| Name | String | Name of a spread placement group with a length of 1-60 characters. |
| CvmQuotaTotal | Integer | Number of CVMs that a placement group can have. |
| CurrentNum | Integer | Number of CVMs that a placement group contains. |
| CreateTime | Timestamp | Creation time of a placement group |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InvalidParameterValue.Range | Invalid parameter value. The parameter value range is invalid. |
| InvalidParameterValue.TooLong | Invalid parameter value. The parameter value is too long. |

## 5. Example

### Example 1 Create a spread placement group

#### Input Example

```
https://cvm.tencentcloudapi.com/?Action=CreateDisasterRecoverGroup
&Name=Physical-machine-type disaster recovery group
&Type=HOST
&<Common request parameters>
```

#### Output Example

```
{
  "Response": {
    "CreateTime": "2018-06-08T07:26:38Z",
    "CurrentNum": 0,
    "CvmQuotaTotal": 50,
    "DisasterRecoverGroupId": "ps-qajfd25h",
    "Name": "Physical Machine Disaster Recovery Group",
    "RequestId": "21387009-9b9c-4b57-8fa2-8228f702ff6c",
    "Type": "HOST"
  }
}
```



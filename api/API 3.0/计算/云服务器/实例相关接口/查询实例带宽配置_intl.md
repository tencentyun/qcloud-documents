## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (DescribeInstanceInternetBandwidthConfigs) is used to query the instance bandwidth configuration.

* Only query for the bandwidth configuration of instances with `BANDWIDTH_PREPAID` billing method is supported.
* All bandwidth configuration information (including historical bandwidth configuration information) of an instance is returned via the API.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeInstanceInternetBandwidthConfigs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | IDs of instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| InternetBandwidthConfigSet | Array of [InternetBandwidthConfig](/document/api/213/##InternetBandwidthConfig) | List of bandwidth configurations. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Query instance bandwidth configuration

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=DescribeInstanceInternetBandwidthConfigs
&InstanceId=ins-6lafsaz0
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "InternetBandwidthConfigSet": [
      {
        "EndTime": "2017-04-12T16:00:00Z",
        "InternetAccessible": {
          "InternetChargeType": "BANDWIDTH_PREPAID",
          "InternetMaxBandwidthOut": 50
        },
        "StartTime": "2017-03-12T16:00:00Z"
      }
    ],
    "RequestId": "314161cd-ee40-4c37-921e-b10c4ed5607c"
  }
}
```



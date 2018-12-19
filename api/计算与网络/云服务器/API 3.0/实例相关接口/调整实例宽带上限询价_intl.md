## 1. API Description

This API (InquiryPriceResetInstancesInternetMaxBandwidth) is used to inquire the price of adjusting the public network bandwidth cap of an instance.

* The bandwidth cap varies with different models. For details, please see [Purchase Network Bandwidth](https://cloud.tencent.com/document/product/213/509).
* For a bandwidth with the `BANDWIDTH_PREPAID` billing method, the parameters `StartTime` and `EndTime` need to be input to specify the validity period of the adjusted bandwidth. Bandwidth downgrade is not supported currently in this scenario. Since fee deduction is involved, make sure to keep sufficient balance in your account. You can query the balance via the API [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397).
* For a bandwidth with the `TRAFFIC_POSTPAID_BY_HOUR`, the `BANDWIDTH_POSTPAID_BY_HOUR`, or the `BANDWIDTH_PACKAGE` billing method, the adjustment of the bandwidth cap using this API takes effect in real time. Bandwidth upgrade and downgrade in the permitted range are supported, and the input of parameters `StartTime` and `EndTime` is not supported.
* This API does not support adjusting a bandwidth with the `BANDWIDTH_POSTPAID_BY_MONTH` billing method.
* This API does not support batch adjustment of bandwidths with the `BANDWIDTH_PREPAID` or the `BANDWIDTH_POSTPAID_BY_HOUR` billing method.
* This API does not support batch adjustment of bandwidths with hybrid billing methods. For instance, it does not support adjusting bandwidths with the `TRAFFIC_POSTPAID_BY_HOUR` and the `BANDWIDTH_PACKAGE` billing methods at the same time.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: InquiryPriceResetInstancesInternetMaxBandwidth |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with, which can be obtained from `InstanceId` in the returned value of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances in a batch for each request is 100. |
| InternetAccessible | Yes | [InternetAccessible](/document/api/213/15753#InternetAccessible) | The outbound bandwidth configuration of the public network. The bandwidth cap varies with different models. For details, see the bandwidth limit reconciliation. Only the parameter `InternetMaxBandwidthOut` is supported currently. |
| StartTime | No | String | The date from which the bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The start date cannot be earlier than the current date. If the start date is today, the newly set bandwidth takes effect immediately. This parameter is only valid for the prepaid bandwidth. Corresponding error code will be returned by this API if a bandwidth with other billing methods is selected. |
| EndTime | No | String | The date until which the bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the newly set bandwidth includes the end date. The end date cannot be later than the expiry date of the prepaid instance. The expiry date of an instance can be obtained from `ExpiredTime` in the returned value of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). This parameter is only valid for the prepaid bandwidth. Corresponding error code will be returned by this API if a bandwidth with other billing methods is selected. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/15753#Price) | The price of the adjusted bandwidth. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidAccount.InsufficientBalance | Insufficient account balance. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.Range | Invalid parameter value. Invalid parameter value range. |
| InvalidPermission | This operation is not supported for the account. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Adjust the bandwidth cap of a postpaid instance

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=InquiryPriceResetInstancesInternetMaxBandwidth
&InstanceIds.0=ins-fd8spnmq
InternetAccessible.InternetMaxBandwidthOut=20
&DryRun=FALSE
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "Price": {
      "BandwidthPrice": {
        "ChargeUnit": "GB",
        "UnitPrice": 0.8
      }
    },
    "RequestId": "700864b9-85da-4cb9-bc80-d99eaf9fa047"
  }
}
```


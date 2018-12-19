## 1. API Description

This API (InquiryPriceResetInstancesInternetMaxBandwidth) is used to inquire the prices of public network bandwidth with adjusted upper limit.

Domain name for API request: cvm.api.qcloud.com

* Upper limit of bandwidth varies among different models. For details, please see [Purchase Network Bandwidth](https://cloud.tencent.com/document/product/213/509).
* For the bandwidth of `BANDWIDTH_PREPAID` billing method, you need to enter the parameters `StartTime` and `EndTime`, and to specify the time when the adjusted bandwidth takes effect. In this scenario, the bandwidth adjusted to a value lower than the current value will be charged a fee. Please ensure that the user account has sufficient balance. The balance can be queried using the API [`DescribeAccountBalance`](/document/product/378/4397).
* For the bandwidth of `TRAFFIC_POSTPAID_BY_HOUR`, `BANDWIDTH_POSTPAID_BY_HOUR`, or `BANDWIDTH_PACKAGE` billing method, the bandwidth whose upper limit is adjusted using this API takes effect in real time. The bandwidth can be adjusted to a value higher or lower than the current value within an allowable range. The input of parameters `StartTime` and `EndTime` is not supported.
* The adjustment of bandwidth of `BANDWIDTH_POSTPAID_BY_MONTH` billing method is not supported for this API.
* Batch adjustment of bandwidth of `BANDWIDTH_PREPAID` and `BANDWIDTH_POSTPAID_BY_HOUR` billing methods is not supported for this API.
* Batch adjustment of bandwidth of mixed billing methods is not supported for this API. For example, the bandwidth of `TRAFFIC_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE` billing methods cannot be adjusted at the same time.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | Array of Strings | Yes | ID(s) of one or more instances to be operated. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances for each request for batch operation is 100. |
| InternetAccessible | [InternetAccessible object](/document/api/213/9451#internetaccessible) | Yes | Configuration for the outbound bandwidth of public network. The upper limit of bandwidth varies among different models. For more information, please see Table of Bandwidth Limits. Currently, only the parameter `InternetMaxBandwidthOut` is supported. |
| StartTime | String | No | Start time of updated bandwidth. It should take the format of `YYYY-MM-DD`, such as `2016-10-30`. It should not be earlier than the current time. If it is today, the updated bandwidth takes effect immediately. This parameter is only applies to prepaid bandwidth. Error code is returned via this API for the bandwidth of unsupported billing methods. |
| EndTime | String | No | End time of bandwidth. It should take the format of `YYYY-MM-DD`, such as `2016-10-30`. It should not later than the expiry date of prepaid instances. The expiry date is obtained from `ExpiredTime` in the returned values of API [`DescribeInstances`](/document/api/213/9388). This parameter is only applies to prepaid bandwidth. Error code is returned via this API for the bandwidth of unsupported billing methods. |


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/9451#price) object | The price of the adjusted bandwidth. |
| RequestId | String | Unique request ID. A unique "requestId" is returned for each request. In case of a failed call to the API, "requestId" needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameter | Invalid parameter. Parameter does not meet the requirement or is not supported. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.Range | Invalid parameter value. Invalid parameter value range. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InvalidPermission | This operation is not supported for the account. |
| InvalidAccount.InsufficientBalance | The account balance is sufficient. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InternalServerError | Internal service error. |


## 5. Examples

### Example 1

> **Adjusting the upper limit of bandwidth for an prepaid instance:**<br>


### Request Parameters
```
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResetInstancesInternetMaxBandwidth
&Version=2017-03-12
&InstanceIds.1=ins-2zvpghhc
&InternetAccessible.InternetMaxBandwidthOut=20&StartTime=2017-05-15
&EndTime=2017-05-16
&<<a href="/document/api/213/11650">Common request parameters</a>>
```

#### Response Parameters
```
{
    "Response": {
        "Price": {
            "BandwidthPrice": {
                "OriginalPrice": "96.33",
                "DiscountPrice": "96.33"
            }
        },
        "RequestId": "d4603747-86b9-4108-b42f-f623e7cc2538"
    }
}
```

### Example 2

> **Adjusting the upper limit of bandwidth for an postpaid instance:**<br>


### Request Parameters
```
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceResetInstancesInternetMaxBandwidth
&InstanceIds.1=ins-fd8spnmq
InternetAccessible.InternetMaxBandwidthOut=20
&DryRun=FALSE
&<<a href="/document/api/213/11650">Common request parameters</a>>
```

#### Response Parameters
```
{
    "Response": {
        "Price": {
            "BandwidthPrice": {
                "UnitPrice": 0.8,
                "ChargeUnit": "GB"
            }
        },
        "RequestId": "700864b9-85da-4cb9-bc80-d99eaf9fa047"
    }
}
```


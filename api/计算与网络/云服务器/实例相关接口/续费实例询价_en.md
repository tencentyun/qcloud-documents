## 1. API Description

This API (RenewInstance) is used to inquire the prices of renewed prepaid instances.

Domain name for API request: cvm.api.qcloud.com


* Only inquiry for renewal prices of prepaid instances is supported for this API.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | Array of Strings | Yes | ID(s) of one or more instances to be operated. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances for each request for batch operation is 100. |
| InstanceChargePrepaid | [InstanceChargePrepaid object](https://cloud.tencent.com/document/api/213/9451#instancechargeprepaid) | Yes | Prepaid mode, parameter configuration of prepaid by year/month. This parameter can specify the renewal length, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| Price | [Price](/document/api/213/9451#price) object | The price of the instance with corresponding configuration. |
| RequestId | String | Unique request ID. A unique "requestId" is returned for each request. In case of a failed call to the API, "requestId" needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | Invalid instance ID. The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
| InvalidPeriod | Invalid period. Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] (in month) |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InvalidAccount.InsufficientBalance | The account balance is sufficient. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InternalServerError | Tencent Cloud server error. |


## 5. Example

### Example 1

> **Price inquiry for renewed prepaid instances**<br>

### Request Parameters
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=InquiryPriceRenewInstances
&Version=2017-03-12
&InstanceIds.1=ins-2zvpghhc
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_MANUAL_RENEW
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

#### Response Parameters
<pre>
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": "120.00",
                "DiscountPrice": "1.20"
            }
        },
        "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
    }
}
</pre>


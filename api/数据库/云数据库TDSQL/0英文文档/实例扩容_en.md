## 1. API Description
This API (CdbTdsqlExpandInstance) is used to expand instance capacity.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlExpandInstance.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceUuid | Yes | String | Instance UUID (string), which can be obtained via API [View Instance List](/doc/api/309/5447). |
| dbType | Yes | Int | Old product type. The pid field can be obtained via API [View Instance List](/doc/api/309/5447) |
| newDbType | Yes | Int | New product type after expansion. Destination pid can be selected via API [Query Instance Specifications](/doc/api/309/5537) |
| curDeadline | Yes | datetime | Current expiration time, such as 2015-09-26 16:28:02, which can be obtained via API [View Instance List](/doc/api/309/5447) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data | Array | Returned data, mainly including order information |
| data.dealNames | Array | Long order ID, which is used to report order-related problems to customer service | 
| data.dealIds | Array | Order ID, which is used to call cloud APIs, such as [Query Order Information](/doc/api/309/5690) | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| PriceParamError | Billing API parameter error |
| GetPriceError | Failed to acquire price |
| PriceDBError | Billing DB operation failed |
| InvalidCoupon | Invalid coupon |
| GetGoodsConfigFailed | Failed to obtain goods configuration |
| IllegalGoodsID | Invalid goods ID |
| IllegalGoodsOperation | The operation is not allowed for the goods |
| FailedToPay | Payment failed |
| SomeBillsFailed | Payment is successful, but delivery for some orders failed |
| PayError | Error occurred during payment |
| BalanceIsNotEnough | Insufficient balance |
| ReachTheAmounLimit | Purchase quantity exceeds the limit |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlExpandInstance
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&cdbInstanceUuid=tdsql-rmtg9lj2
&dbType=10551
&newDbType=10552
&curDeadline=2016-07-25 16:28:02
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "dealNames":[
            "20160726110061"
        ],
        "dealIds":[
            "454043"
        ]
    }
}
```



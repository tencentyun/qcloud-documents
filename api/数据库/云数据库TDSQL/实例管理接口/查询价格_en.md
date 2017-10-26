## 1. API Description
This API (CdbTdsqlGetPrice) is used to query the price.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlGetPrice.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| costType | No | Int | Billing type. 0: Prepaid; 1: Pay per Use. Only "Prepaid" is supported currently |
| dbType | Yes | Int | Product type. For more information, please see pid field in [Query Instance Specifications](/doc/api/309/5537) |
| goodsNum | No | Int | Number of goods |
| period | No | Int | Length of period (in month), which is applicable to "Prepaid" mode |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| originalPrice | Int | Original price (in 0.01 CNY) |
| price | Int | Actual price (in 0.01 CNY). This may be different from original price for reasons such as discount |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| GetPriceError | Failed to acquire price |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetPrice
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&dbType=10552
&period=24
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "originalPrice":"7680000",
    "price":"6400000"
}
```



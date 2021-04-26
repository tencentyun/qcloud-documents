## 1. API Description
This API (CdbTdsqlGetOrderInfo) is used to query order information.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlGetOrderInfo.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| dealIds.n (dealIds is an array. The input parameters here are the array elements) | Yes | String | List of orders to be queried, with n starting with 0 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data | Array | Results of query |
| data.deals | Array | Array of order details | 
| data.totalNum | Int | Number of orders | 
| data.deals.dealId | String | Order ID, which is used to call the cloud API | 
 | data.deals.dealName | String | Long order ID, which is used to report order-related problems to customer service | 
| data.deals.zoneId | Int | ID of availability zone | 
| data.deals.ownerUin | String | UIN of creator | 
| data.deals.goodsNum | Int | Quantity of goods | 
| data.deals.payMode | Int | Payment method. 1: Prepaid; 0: Postpaid | 
| data.deals.flowId | Int | Task flow ID. Use API [Query Flow Status](/doc/api/309/5605) to query the flow status | 
| data.deals.resourceIds | Array | ID of order-related instance resource, which is used to call instance-related cloud APIs | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| PriceParamError | Billing API parameter error |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetOrderInfo
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&dealIds.0=455439
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "totalNum":"1",
        "deals":[
            {
                "dealId":"455439",
                "dealName":"20160802110001",
                "zoneId":"100002",
                "ownerUin":"909619400",
                "goodsNum":"1",
                "payMode":"1",
                "flowId":"3330",
                "resourceIds":[
                    "tdsql-e1ccp714"
                ]
            }
        ]
    }
}
```



## 1. API Description
This API (InquiryNatPrice) is used to query NAT gateway price.
Domain: vpc.api.qcloud.com


## 2. Input Parameters
| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| maxConcurrent | Yes | Int | Maximum concurrent connection of NAT gateway |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Succeeded; other values: Failed |
| message | String | Error message |
| data | Array | Returned price array |

Details of `data`

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.price | Int | Description (to be appended) | 
| data.totalCost | Int | Description (to be appended) | 
| data.realTotalCost | Int | Description (to be appended) | 
| data.timeSpan | Int | Description (to be appended) | 
| data.timeUnit | String | Description (to be appended) | 
| data.goodsNum | Int | Description (to be appended) | 
| data.policy | Int | Description (to be appended) | 
| data.unitPrice | Int | Description (to be appended) | 


## 4. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=InquiryNatPrice
&maxConcurrent=2000000
&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":[
        {
            "price":"150",
            "totalCost":"150",
            "realTotalCost":"150",
            "timeSpan":"1",
            "timeUnit":"h",
            "goodsNum":"1",
            "policy":"100",
            "unitPrice":"150"
        }
    ]
}
```



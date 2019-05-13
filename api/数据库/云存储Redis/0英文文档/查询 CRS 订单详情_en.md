## 1. API Description
This API (DescribeRedisDealDetail) is used to query the details of an order.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeRedisDealDetail.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| dealIds.n | Yes | String | An array of order numbers, with the array subscript starting from 0 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| dealDetails | Array | Returned array of orders |

**Array dealDetails is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| dealDetails.dealId | String | Order ID. Use this ID when calling the cloud API |
| dealDetails.dealName | String | Long order ID. Use this ID when reporting the order-related problems to customer service |
| dealDetails.zoneId | Int | ID of availability zone |
| dealDetails.goodsNum | Int | Number of instances associated with the order |
| dealDetails.creater | String | UIN of creator |
| dealDetails.creatTime | String | Creation time of order |
| dealDetails.overdueTime | String | Expiration time of order |
| dealDetails.endTime | String | Completion time of order |
| dealDetails.status | Int | Order status<br>1: Unpaid<br>2: Paid, Undelivered<br>3: Delivering<br>4: Delivery succeeded<br>5: Delivery failed<br>6: Refunded<br>7: Order closed<br>8: Order expired<br>9: Order invalidated<br>10: Product invalidated<br>11: Payment by agent rejected<br>12: Payment is in progress |
| dealDetails.description | String | Description of order status |
| dealDetails.price | Int | Actual total price of order (in 0.01 CNY) |
| dealDetails.goodsDetail | Array | Returned array. goodsDetail varies with different orders |

**goodsDetail array of created instance:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| memSize| int | Capacity of instance (in MB) |
| timeSpan | int | Purchased usage period. The unit is subject to timeUnit |
| timeUnit | String | Unit of purchased usage period. m - month, d - day |
| redisIds | Array | List of associated redisIds |

**goodsDetail array of renewed instance:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| curDeadline | String | Expiration time of instance before renewal |
| memSize| int | Capacity of instance (in MB) |
| timeSpan | int | Purchased usage period. The unit is subject to timeUnit |
| timeUnit | String | Unit of purchased usage period. m - month, d - day |
| redisIds | Array | List of associated redisIds |

**goodsDetail array of upgraded instance:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| oldMemSize | int | Capacity of instance before upgrade (in MB) |
| newMemsize | int | Capacity of instance after upgrade (in MB) |
| redisIds | Array | List of associated redisIds |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11059 | DealIdNotFound | Order ID does not exist |

## 5. Example
Input
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeRedisDealDetail
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&dealIds.0=432583
&dealIds.1=432586
&dealIds.2=432587
</pre>
Output
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
    "dealDetails": [
        {
            "dealId": "432583",
            "dealName": "20160712110021",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-12 21:10:11",
            "overdueTime": "2016-07-27 21:10:11",
            "endTime": "2016-07-12 21:11:17",
            "status": 4,
            "description": "Delivery succeeded",
            "price": 16000,
            "goodsDetail": {
                "memSize": 1024,
                "timeSpan": 2,
                "timeUnit": "m",
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        },
        {
            "dealId": "432586",
            "dealName": "20160712110027",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-12 22:05:43",
            "overdueTime": "2016-07-27 22:05:43",
            "endTime": "2016-07-12 22:05:45",
            "status": 4,
            "description": "Delivery succeeded",
            "price": 8000,
            "goodsDetail": {
                "curDeadline": "2016-09-12 21:10:13",
                "memSize": 1024,
                "timeSpan": 1,
                "timeUnit": "m",
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        },
        {
            "dealId": "432587",
            "dealName": "20160712110029",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3227991405",
            "creatTime": "2016-07-12 22:15:55",
            "overdueTime": "2016-07-27 22:15:55",
            "endTime": "2016-07-12 22:16:59",
            "status": 4,
            "description": "Delivery succeeded",
            "price": 24460,
            "goodsDetail": {
                "oldMemSize": 1024,
                "newMemsize": 2048,
                "redisIds": [
                    "crs-ifmymj41"
                ]
            }
        }
    ]
}
```

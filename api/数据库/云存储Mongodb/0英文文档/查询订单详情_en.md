## 1. API Description
This API (DescribeMongodbDealDetail) is used to query order details.
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is DescribeMongodbDealDetail.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| dealIds.n | Yes | String | An array of order IDs, with the array subscript starting from 0 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| details | Array | Array of returned order details |

Parameter details indicates an array of order details and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| details.dealId | String | Short order ID. Use this ID when calling the cloud API |
| details.dealName | String | Long order ID. Use this ID when reporting the order-related problems to customer service |
| details.zoneId | Int | Availability zone ID |
| details.goodsNum | Int | Number of instances associated with the order |
| details.creater | String | UIN of creator of order |
| details.creatTime | String | Creation time of order |
| details.overdueTime | String | Expiration time of order |
| details.endTime | String | Completion time of order |
| details.status | Int | Order status<br>1: Unpaid<br>2: Paid, Undelivered<br>3: Delivering<br>4: Delivery succeeded<br>5: Delivery failed<br>6: Refunded<br>7: Order closed<br>8: Order expired<br>9: Order invalidated<br>10: Product invalidated<br>11: Payment by agent rejected<br>12: Payment is in progress |
| details.price | Int | Actual total price of order (in 0.01 CNY) |
| details.goodsDetail | Object | Details of the commodity associated with the order |

**goodsDetail returned for the creation of an instance:**

| Parameter Name | Type | Description |
|:---------|---------|---------|
| memSize| int | Memory size of instance (in MB) |
| disksize | int | Disk capacity of instance (in GB) |
| typeId | String | Name of instance type |  GIO: High IO; TGIO: High IO (10 GB) |
| clusterType | Array | Instance cluster type. 0: replica set |
| secondaryNum | Array | Number of slave nodes of replica set instance. Only 1 and 2 are supported currently |
| zoneId | Array | Availability zone ID |
| mongoVersion | Array | Database version number, for example: MONGO_3_MMAP, MONGO_3_WT |
| timeSpan | Array | Validity period of instance, with the unit being subject to the returned value of timeUnit |
| timeUnit | Array | Unit of validity period of instance (m: month; d: day) |
| SerialIds | Array | An array of instance IDs |

**goodsDetail returned for the renewal of instance:**

| Parameter Name | Type | Description |
|:---------|---------|---------|
| curDeadline | String | Expiration time of instance before renewal |
| timeSpan | int | Renewed period, with the unit being subject to the returned value of timeUnit |
| timeUnit | String | Unit of renewed period (m: month; d: day) |
| SerialIds | Array | An array of instance IDs |

**goodsDetail returned for the upgrade of instance:**

| Parameter Name | Type | Description |
|:---------|---------|---------|
| curDeadline | String | Expiration time of instance |
| newMemsize | int | Memory size of upgraded instance (in MB) |
| newDisksize | int | Disk capacity of upgraded instance (in GB) |
| oldMemsize | int | Memory size of instance before upgrade (in MB)|
| oldDisksize | int | Disk capacity of instance before upgrade (in GB)|
| SerialIds | Array | An array of instance IDs |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |

## 5. Example
Input
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=DescribeMongodbDealDetail
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&dealIds.0=3373037
&dealIds.1=3374462
&dealIds.2=3374558
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "details": [
        {
            "dealId": "3373037",
            "dealName": "20170206121420",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3374998458",
            "creatTime": "2017-02-06 14:07:46",
            "overdueTime": "2017-02-21 14:07:46",
            "endTime": "2017-02-06 14:11:54",
            "status": 4,
            "price": 72200,
            "goodsDetail": {
                "memSize": 4096,
                "disksize": 30,
                "typeId": "GIO",
                "clusterType": "ReplSet",
                "secondaryNum": 2,
                "zoneId": 100002,
                "mongoVersion": "MONGO_3_MMAP",
                "timeSpan": 1,
                "timeUnit": "m",
                "SerialIds": [
                    "cmgo-6ozqe0uh"
                ]
            }
        },
        {
            "dealId": "3374462",
            "dealName": "20170206124372",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3374998458",
            "creatTime": "2017-02-06 16:32:45",
            "overdueTime": "2017-02-21 16:32:45",
            "endTime": "2017-02-06 16:32:46",
            "status": 4,
            "price": 72200,
            "goodsDetail": {
                "curDeadline": "2017-03-06 14:07:46",
                "timeSpan": 1,
                "timeUnit": "m",
                "SerialIds": [
                    "cmgo-6ozqe0uh"
                ]
            }
        },
        {
            "dealId": "3374558",
            "dealName": "20170206124575",
            "zoneId": 100002,
            "goodsNum": 1,
            "creater": "3374998458",
            "creatTime": "2017-02-06 16:43:17",
            "overdueTime": "2017-02-21 16:43:17",
            "endTime": "2017-02-06 16:45:49",
            "status": 4,
            "price": 142421,
            "goodsDetail": {
                "curDeadline": "2017-04-06 14:07:46",
                "newMemsize": 8192,
                "newDisksize": 60,
                "oldMemsize": 4096,
                "oldDisksize": 30,
                "SerialIds": [
                    "cmgo-6ozqe0uh"
                ]
            }
        }
    ]
}

```


## 1. API Description
This API (InquiryRedisPrice) is used to query the prices for purchasing and renewing an instance. To query the price for upgrading an instance, please see [Query Price for Instance Upgrade](http://cloud.tencent.com/doc/api/260/5327).
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/239/7200' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is InquiryRedisPrice.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId | Yes | UInt | The availability zone to which the instance belongs. This value is subject to the returned values of API [Query Supported Availability Zones](http://cloud.tencent.com/doc/api/260/4951) |
| typeId | Yes | UInt | Instance type. 1 - Cluster; 2 - Standalone |
| memSize | Yes | UInt | Capacity of instance, which is an integral multiple of 1024 (in MB). This value is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) |
| goodsNum | Yes | UInt | Number of instances. This value is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) |
| period | Yes | UInt | Purchased or renewed usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Array | Returned array of prices |

**Array data is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.price | Int | The total price for purchasing or renewing an instance (in 0.01 CNY) | 

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11052 | UserNotInWhiteList |The user is not in the whitelist |
| 10000 | NoRedisService | The Redis service is not available in the requested zone |
| 11062 | NoTypeIdRedisService | The Redis service of the requested type is not available in the requested zone |
| 11053 | InvalidInstanceTypeId | The type of the instance to purchase is incorrect (TypeId 1: Cluster; 2: Master-Slave (the former Standalone version) |
| 10703 | InvalidMemSize | The requested capacity is not included in the supported specifications (memSize (in MB) should be an integral multiple of 1024) |
| 11063 | MemSizeNotInRange | The requested capacity is not within the range of supported capacities (please use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the limits on the capacity) |
| 11065 | PeriodExceedMaxLimit | The purchased usage period exceeds the maximum usage period |
| 11066 | PeriodLessThanMinLimit |The purchased usage period is less than the minimum usage period |
| 11064 | GoodsNumNotInRange | The number of instances purchased at a time exceeds the maximum number of instances allowed to be purchased (please use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the limits on the number of instances allowed to be purchased) |


## 5. Example
Input
```
https://redis.api.qcloud.com/v2/index.php?Action=InquiryRedisPrice
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&zoneId=100002
&typeId=1
&memSize=1024
&goodsNum=1
&period=2
```
Output
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
    "data":{
        "price": 16000
    }
}
```

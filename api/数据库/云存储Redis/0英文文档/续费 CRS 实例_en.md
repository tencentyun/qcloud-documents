## 1. API Description
This API (RenewRedis) is used to renew an instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is RenewRedis.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| redisId | Yes | String | Instance ID. It can be queried with the API [Query CRS Instance List](http://cloud.tencent.com/doc/api/260/1384) |
| period | Yes | Int | Purchased usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Array | Returned array of orders |

**Array data is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.dealId | String | Unique order ID. You can use the API [DescribeRedisDealDetail](https://cloud.tencent.com/doc/api/260/5329) to query order details |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 10701 | InstanceNotExists | No instance can be found for the serialId |
| 11055 | InstanceDeleted | The instance has been reclaimed upon expiration |
| 11056 | InstanceBeenLocked | The operation is impossible because the instance is locked by another process |
| 11065 | PeriodExceedMaxLimit | The purchased usage period exceeds the maximum usage period |
| 11066 | PeriodLessThanMinLimit |The purchased usage period is less than the minimum usage period |
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient account balance. Please top it up. |

## 5. Example
Input
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=RenewRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&redisId=crs-ifmymj41
&period=1
</pre>
Output
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data":{
		"dealId":"432586"
	}
}
```

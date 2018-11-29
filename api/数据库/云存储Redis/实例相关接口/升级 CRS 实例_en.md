## 1. API Description
This API (UpgradeRedis) is used to upgrade an instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is UpgradeRedis.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| redisId | Yes | String | Instance ID. It can be queried with the API [Query CRS Instance List](http://cloud.tencent.com/doc/api/260/1384) |
| memSize | Yes | UInt | The capacity of upgraded instance, which should be an integral multiple of 1024 (in MB) |  This value must be greater than the current instance specification, and is subject to the returned values of API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Array | Returned array |

**Array data is composed as follows:**

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.dealId | String | Unique order ID. You can use the API [DescribeRedisDealDetail](https://cloud.tencent.com/doc/api/260/5329) to query order details |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 10701 | InstanceNotExists | No instance can be found for the serialId |
| 10703 | InvalidMemSize | The requested capacity is not included in the supported specifications (memSize (in MB) should be an integral multiple of 1024) |
| 11063 | MemSizeNotInRange | The requested capacity is not within the range of supported capacities (please use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the limits on the capacity) |
| 10702 | InstanceStatusAbnormal | The operation is impossible due to an abnormal instance status. For example, the instance has a status of "in process" or "isolated" or "deleted" |
| 11057 | ReduceCapacityNotAllowed | The requested capacity is less than the actual capacity of the instance. Reduction of capacity is not supported currently |
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient account balance. Please top it up. |


## 5. Example
Input
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=UpgradeRedis
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&redisId=crs-ifmymj41
&memSize=2048
</pre>
Output
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data":{
		"dealId":"432587"
	}
}
```

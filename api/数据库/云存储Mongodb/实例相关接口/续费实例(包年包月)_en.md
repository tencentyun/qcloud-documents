## 1. API Description
This API (RenewMongoDB) is used to renew a replica set instance (annual or monthly plan). Please make sure your account balance is sufficient.
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is RenewMongoDB.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of instance to work with. This can be obtained from instanceId in the returned values of API [DescribeMongoDBInstances](/document/product/240/8312). |
| period | Yes | Int | Renewed usage period (in month). Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Returned order ID |

Parameter data indicates the order ID, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.dealId | String | Order ID. You can use API [DescribeMongodbDealDetail](/document/product/240/8313) to query order details |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter |Incorrect business parameter |
| 11056 | InstanceNotExists | Instance does not exist |
| 11051 | InstanceDeleted | The instance has been reclaimed upon expiration |
| 11067 | PeriodNotInRange | The requested period is not in the supported range |
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient account balance. Please top it up |

## 5. Example
Input
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=RenewMongoDB
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&instanceId=cmgo-6ozqe0uh
&period=1
</pre>
Output
```
{
    "code":"0",
    "message":"",
	"codeDesc": "Success",
	"data":{
		"dealId":"3374462"
	}
}
```

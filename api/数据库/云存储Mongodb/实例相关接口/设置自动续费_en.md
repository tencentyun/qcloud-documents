## 1. API Description
This API (SetMongoDBAutoRenew) is used to set auto renewal for an instance.
Domain for API request: <font style='color:red'>mongodb.api.qcloud.com </font>



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is SetMongoDBAutoRenew.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| instanceIds.n | Yes | String | One or more instance IDs (n represents array subscript starting with 0).  This can be obtained from instanceId in the returned values of API [DescribeMongoDBInstances](/document/product/240/8312). |
| isAutoRenew | Yes | Int | Set auto renewal flag: 0 - Do not set auto renewal; a notification will be given upon expiration of instance; 1 - Set auto renewal; instance will be automatically renewed upon expiration; 2 - Neither renewal nor notification will be made upon the expiration of instance |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter | Incorrect business parameter |
| 10716 |NoInstanceIds| Array of requested instance IDs is empty |
| 11056 | InstanceNotExists | Instance does not exist |
| 11051 | InstanceDeleted | The instance has been reclaimed upon expiration |

## 5. Example
Input
<pre>
https://mongodb.api.qcloud.com/v2/index.php?Action=SetMongoDBAutoRenew
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&instanceIds.0=cmgo-6ozqe0uh
&isAutoRenew=1
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

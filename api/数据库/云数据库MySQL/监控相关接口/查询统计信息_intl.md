## 1. API Description
This API (QueryCdbStatisticsInfo) is used to query the cloud database instance's statistical information. The statistical data within the last minute will be queried.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is QueryCdbStatisticsInfo.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| cdbStatInfo | Object | Status information |
cdbStatInfo is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| allStorageSize | Int | Total amount of space occupied, including logs. Unit: Byte | 
| dbStorageSize | Int | Space occupied by database, excluding logs. Unit: Byte | 
| queryCount | Int | Access frequency. Unit: times/minute | 
| slowQueryCount | Int | Slow query access frequency. Unit: times/minute | 
| charset | String | Character set, possible return value: latin1, utf8, gbk, utf8mb4 | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError | System internal error |
| 9016 | InternalError | DES system internal error |
| 9544 | OperationDenied | Instance does not exist |
| 9572 | InstanceNotExists | Instance does not exist |
| 9593 | IncorrectInstanceStatus | Abnormal instance status|


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=QueryCdbStatisticsInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "cdbStatInfo": {
        "charset": "utf8",
        "allStorageSize": 4173332480,
        "dbStorageSize": 3088056320,
        "queryCount": 0,
        "slowQueryCount": 0
    }
}
```



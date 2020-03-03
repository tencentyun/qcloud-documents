## 1. API Description
 
This API (GetMongoDBSlowLog) is used to obtain the slow log of an instance.
Domain name for API request: mongodb.api.cloud.tencent.com.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/api/240/8320' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is GetMongoDBSlowLog.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| Limit | Yes | Int | Length of a page. Maximum is 100 |
| Offset | Yes | Int | Current page number. A maximum of 10,000 query results are supported, that is, Limit multiplied by Offset does not exceed 10,000. For query APIs, a default maximum number of returned records is generally set for a single query. To traverse all the resources, you need to use "limit" and "offset" for paging queries. For example, to query the 40 records between 110 and 149, you can set offset = 110 and limit = 40. |
| QueryMaxTime | Yes | Int | Slow log threshold in milliseconds, and the minimum value is 100 milliseconds. |
| MongodbId | Yes | String | The ID of instance to be operated. It can be obtained from the instanceId in the returned value of API [DescribeMongoDBInstances](https://cloud.tencent.com/document/api/240/8312). |
| BeginTime | Yes | String | Start time in the format like 2017-02-08 16:46:34. The slow logs initiated within the time period of [beginTime, endTime] are queried. |
| EndTime | Yes | String | End time in the format like 2017-02-08 19:09:26. The slow logs initiated within the time period of [beginTime, endTime] are queried. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|:---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://www.cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> in the Error Codes page.|
| message | String | Error message description. A null value indicates a success. |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned. |
| totalCount | Int | Total number of instances. |
| slowLogs | Array | Slow logs. |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11050 | InvalidParameter | Incorrect business parameter. |
| 11056 | InstanceNotExists | Instance does not exist. |
| 11077 | TimeFormatError | Wrong format of beginTime or endTime. The correct format is 2006-01-02 15:04:05. |
| 11078 | QueryTimeRangeError | beginTime is later than endTime. |
| 11081 | StartTimeTooOld | Only the data within the last 7 days can be queried. |
| 11082 | QueryNumExcessive | Only 10,000 slow logs can be queried. |
| 11083 | QueryTimeRangeMoreThan1day | The query time range must be within 1 day. |
| 11084 | LimitExcessive | A maximum of 100 records can be returned for a single query. |
| 11085 | QueryMaxTimeTooSmall | Slow log threshold must be greater than or equal to 100 milliseconds. |

## 5. Example
```
https://mongodb.api.cloud.tencent.com/v2/index.php?Action=GetMongoDBSlowLog
&<<a href="https://cloud.tencent.com/document/api/240/8320">Common request parameters</a>>
&Offset=0
&Limit=5
&QueryMaxTime=100
&BeginTime=2017-10-20 19:16:59
&EndTime=2017-10-20 20:16:00
&MongodbId=cmgo-a1234567
```
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 221,
    "slowLogs": [
        "Fri Oct 20 19:28:21.748 I COMMAND  [conn64407066] command admin.$cmd command: serverStatus { serverStatus: 1 } keyUpdates:0 writeConflicts:0 numYields:0 reslen:21178 locks:{} protocol:op_query 490ms",
        "Fri Oct 20 19:30:23.076 I COMMAND  [conn64407817] command admin.$cmd command: serverStatus { serverStatus: 1 } keyUpdates:0 writeConflicts:0 numYields:0 reslen:21178 locks:{} protocol:op_query 479ms",
        "Fri Oct 20 19:36:27.095 I COMMAND  [conn64410069] command admin.$cmd command: serverStatus { serverStatus: 1 } keyUpdates:0 writeConflicts:0 numYields:0 reslen:21178 locks:{} protocol:op_query 473ms",
        "Fri Oct 20 20:13:51.758 I COMMAND  [conn64423918] command admin.$cmd command: serverStatus { serverStatus: 1 } keyUpdates:0 writeConflicts:0 numYields:0 reslen:21182 locks:{} protocol:op_query 466ms",
        "Fri Oct 20 19:25:19.744 I COMMAND  [conn64405942] command admin.$cmd command: serverStatus { serverStatus: 1 } keyUpdates:0 writeConflicts:0 numYields:0 reslen:21178 locks:{} protocol:op_query 460ms"
    ]
}
```


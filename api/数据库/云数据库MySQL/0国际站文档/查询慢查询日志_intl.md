## 1. API Description
This API (DescribeCdbSlowQueryLog) is used to obtain the slow query log of a cloud database instance.  <font style="color:red">It was deprecated, and you are recommended to use </font>[Query Backups and Logs](/document/product/236/4691) API to download slow query logs.

Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>

1. Slow query logs are obtained according to cloud database instance IDs;
2. The API only returns log information of a single day;
3. A single request returns a maximum of 100 log records.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/253/1739' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DescribeCdbSlowQueryLog.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](https://intl.cloud.tencent.com/document/product/236/6921). Its value equals to the uInstanceId field value in the output parameter.  |
| date | No | String | Date; data of only recent seven days (including that very day, default to be today ) is saved; records of a single day is returned. Format: yyyy-mm-dd |
| offset | No | Int | Offset; default value is 0 |
| limit | No | Int | Number of returned records; default value is 20 and the maximum value is 100 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| totalCount | Int | Return the total number of logs that meet query conditions|
| slowLogSet | Array | Log of slow query; sorting is conducted by default according to the time log is created |


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
| 9590 | InternalFailure | Task database access error |
| 9593 | IncorrectInstanceStatus | Abnormal database status |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=DescribeCdbSlowQueryLog
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
</pre>

Output
```
{
  "code":0,
  "message":"",
  "codeDesc":"Success",
  "totalCount":1,
  "slowLogSet":["SEL﻿﻿﻿ECT_ * FROM table"]
}

```



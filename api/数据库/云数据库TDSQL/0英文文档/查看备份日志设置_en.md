## 1. API Description
This API (CdbTdsqlQueryLogConfig) is used to view the configurations for database backup logs.

Domain for API request: <tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlQueryLogConfig.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976). The following only provides the formats of returned values for the "data" field.

| Parameter Name | Type | Description |
|---------|---------|---------|
| id | String | Instance ID (string) |
| groupid | String | Group ID (applicable to distributed databases) |
| days | Int | Number of days the logs are kept |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| EINSTANCEDELETED | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| OssOpertaionFailed | OSS internal failure|
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&Action=CdbTdsqlQueryLogConfig
&cdbInstanceId=40732
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": "set_1468578840_203059",
        "groupid": "",
        "days": 30
    }
}
```



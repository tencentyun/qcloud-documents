## 1. API Description
This API (CdbTdsqlGetUserList) is used to view the account list of a database.
Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetUserList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976).
The following only provides the format of returned values for "data" field.

| Parameter Name | Type | Description |
|---------|---------|---------|
| id | Int | Instance ID |
| users | Array | User list. For description of the field, please see input parameters in [Create Account](/doc/api/309/5394) |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| InstanceAlreadyDeleted | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| GetUserListFailed | Failed to acquire user list |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlGetUserList
&cdbInstanceId=40732
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": 40732,
        "users": [
            {
                "user": "testuser1",
                "host": "172.17.%.%",
                "description": "Test account",
                "createTime": "2016-07-15 18:39:47",
                "updateTime": "2016-07-18 12:42:31",
                "readonly": 0,
                "delay_thresh": 0
            },
            {
                "user": "testuser2",
                "host": "%",
                "description": "Test account",
                "createTime": "2016-07-18 11:51:33",
                "updateTime": "2016-07-18 12:42:44",
                "readonly": 0,
                "delay_thresh": 0
            }
        ]
    }
}
```



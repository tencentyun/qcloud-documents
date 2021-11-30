## 1. API Description
This API (CdbTdsqlAddUser) is used to create account for a TDSQL database.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlAddUser.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| userName | Yes | String | User name |
| host | Yes | String | Accessing host allowed for the user |
| password | Yes | String | New password |
| description | No | String | User description |
| readOnly | No | Int | 0: Default value; 1: Slave is preferred for the SQL request of the account. Master is used when slave is not available; 2: Slave is preferred. The operation fails if the slave is not available. |
| delayThresh | No | Int | Threshold of delay before the salve responses to an SQL query request (in sec). When the threshold is exceeded, the slave is considered unavailable. This field is applicable when readOnly is not 0. Default value is used if you enter 0 or left it empty. |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Logic error code description |
| data.id | Int | ID of affected instance |
| data.user | String | User name |
| data.host | String | Allowed accessing host |
| data.readonly | Int | Transparently transmit the value in the input parameter |
| data.delaythresh | Int | Transparently transmit the value in the input parameter |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| InstanceHasBeenLocked | TDSQL is locked by another flow |
| CharacterError | Invalid character |
| DbOperationFailed | DB internal failure |
| InstanceAlreadyDeleted | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| OssOpertaionFailed | OSS internal failure |
| ProxyNeedsUpgrade | Current PROXY version is too low and needs an upgrade |
| SuperUserForbidden | Operation on TDSQL of super user is not allowed |
| GetUserListFailed | Failed to acquire user list |
| UserHostExistsAlready | User already exists |
| CreateUserFailed | Failed to create user |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlAddUser
&cdbInstanceId=40732
&userName=testuser1
&host=172.17.%.%
&password=1234qweri#
&description=Test account
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": 40732,
        "user": "testuser1",
        "host": "172.17.%.%",
        "readonly": 0,
        "delaythresh": 0,
    }
}
```



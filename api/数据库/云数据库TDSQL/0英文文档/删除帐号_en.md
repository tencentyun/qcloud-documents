## 1. API Description
This API (CdbTdsqlDeleteUser) is used to delete the account of a TDSQL database.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlDeleteUser.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| userName | Yes | String | User name |
| host | Yes | String | Accessing host allowed for the user |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976).
The following only provides the format of returned values for "data" field.

Message indicating success or failure is returned.
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| InstanceHasBeenLocked | TDSQL is locked by another flow |
| CharacterError | Invalid character |
| DbOperationFailed | DB internal failure |
| InstanceAlreadyDeleted | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| ResetPasswordFailed | Failed to reset password |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlDeleteUser
&cdbInstanceId=40732
&userName=testuser1
&host=172.17.%.%
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```



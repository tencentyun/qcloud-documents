## 1. API Description
This API (CdbTdsqlCopyRight) is used to copy the permissions between accounts.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976). The Action field for this API is CdbTdsqlCopyRight.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| srcUserName | Yes | String | Source user name |
| srcHost | Yes | String | Source host |
| srcReadOnly | No | Int | 0: Default value; 1: Slave is preferred for the operation of the account. Master is used when slave is not available; 2: Slave is preferred. The operation fails if the slave is not available. |
| dstUserName | Yes | String | Destination user name |
| dstHost | Yes | String | Destination host |
| dstReadOnly | No | Int | 0: Default value; 1: Slave is preferred for the operation of the account. Master is used when slave is not available; 2: Slave is preferred. The operation fails if the slave is not available. The permissions of read-only accounts can only be copied from read-only accounts. |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976). The following only provides the formats of returned values for the "data" field.

If successful, ID of affected instance is returned.
Otherwise the reason for failure is returned.
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| BadUserType | Invalid user type |
| InstanceHasBeenLocked | TDSQL is locked by another flow |
| DbOperationFailed | DB internal failure |
| InstanceAlreadyDeleted | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| CopyRightError | Error occurred while copying permissions |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlCopyRight
&dstUserName=testuser2
&dstHost=%
&srcUserName=testuser1
&srcHost=172.17.%.%
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": 40732
    }
}
```



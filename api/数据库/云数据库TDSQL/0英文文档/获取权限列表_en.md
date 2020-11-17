## 1. API Description
This API (CdbTdsqlGetRightList) is used to set the permission of a database account.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetRightList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| userName | Yes | String | User name |
| host | Yes | String | Accessing host allowed for the user |
| dbName | Yes | String | Database name. If it is \*, global permission (i.e. \*.\*) is set, and parameters "type" and "object" are ignored |
| type | Yes | String | Type (table, view, proc, func or \*). If DbName is a specific database name and type is \*, the database permissions (i.e. db.*) are set and parameter "object" is ignored |
| object | No | String | Name of type. For example, if type is table, this is a table name. If both DbName and Type are specific names, Object refers to a specific object name, and cannot be \* or be left empty |
| colName | No | String | When type=table, if it is \*, table permissions are granted; if it is a field name, field permissions are granted |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters
The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976).
The following only provides the format of returned values for "data" field.

If successful, the list of permissions for the request object is returned. Otherwise the reason for failure is returned.
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| InstanceAlreadyDeleted | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| GetRightFailed | Failed to acquire permissions |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlGetRightList
&cdbInstanceId=40732
&userName=testuser1
&host=172.17.%.%
&dbName=*
&type=*
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
        "db": "*",
        "type": "",
        "object": "",
        "col": "",
        "rights": [
            "SELECT",
            "UPDATE"
        ]
    }
}
```



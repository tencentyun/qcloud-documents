## 1. API Description
This API (RollbackCdbDatabaseTables) is used to batch roll back database tables of CDB instances.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is RollbackCdbDatabaseTables.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| instances.n.cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| instances.n.para | Yes | String | JSON string, containing rollback database table information (this can be obtained using API [Query Database](/doc/api/253/7167) and API [Query Database Table](/doc/api/253/7176)) and rollback time (this can be obtained using API [Query Time Available for Rollback](/doc/api/253/7168)). Please encapsulate input parameters following the example. Batch rollback of multiple databases and multiple tables is supported |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobId | String | Task ID. You can use API [Query Task Status](/document/product/238/6878) to query task details. |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9570 | OperationDenied | Task execution is not allowed |
| 9590 | OperationDenied | Task database access error |
| 9592 | OperationDenied | Task is running |
| 11041 | InternalError.CDBNotExist | CDB instance does not exist |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=RollbackCdbDatabaseTables
&<<a href="/document/product/236/6921">Common request parameters</a>>
&instances.0.cdbInstanceId=cdb-mo64xu70
&instances.0.para={"rollbacktime":"2016-10-31 12:00:00","dbs": [{"dbname": "db1","newname": "db1_bak"}],"tables":[{"db":"db1","table":[{"tablename":"table1","newname":"table1_bak"}]}]}
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "jobId":"111"
    }
}
```



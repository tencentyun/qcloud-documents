## 1. API Description
This API (QueryCdbDatabases) is used to query the database information of Cloud Database instance.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is QueryCdbDatabases.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n | Yes | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter.  |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Instance's database data|
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code returned for database query |
| message | String | Error message returned for database query |
| CdbInstanceId | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.   |
| databaseList | Array | Database information list | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error code | Error Message | Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=QueryCdbDatabases
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceIds.0=cdb-f35wr6wj
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "code": 0,
            "message": "ok",
			"cdbInstanceId": "cdb-f35wr6wj",
            "databaseList": [
                "information_schema",
                "mysql",
                "performance_schema",
                "test"
            ],
        }
    ]
}
```



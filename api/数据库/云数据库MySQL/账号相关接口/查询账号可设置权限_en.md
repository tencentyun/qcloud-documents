## 1. API Description
This API (GetCdbInstanceAccountAvailablePrivileges) is used to query the available permissions of the account of a Cloud Database instance.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/253/1739' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbInstanceAccountAvailablePrivileges.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using the [Query List of Instances](/doc/api/253/1266) API.  |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Data |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9572 | InstanceNotExists | Instance does not exist |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbInstanceAccountAvailablePrivileges
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-rharyuir
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc":"Success",
    "data": {
        "global_support_priv": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE",
            "CREATE",
            "DROP",
            "REFERENCES",
            "INDEX",
            "ALTER",
            "SHOW DATABASES"
        ],
        "db_support_priv": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE",
            "CREATE",
            "DROP"
        ],
        "tb_support_priv": [
            "SELECT",
            "INSERT",
            "UPDATE"
        ],
        "col_support_priv": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "REFERENCES"
        ]
    }
}
```



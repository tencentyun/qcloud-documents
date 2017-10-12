## 1. API Description
This API (ModifyCdbInstanceAccountPrivileges) is used to modify the access permission of the account of a Cloud Database instance.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/253/1739' title='Common Request Parameters>Common Request Parameters</a>. The Action field for this API is ModifyCdbInstanceAccountPrivileges.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using the [Query List of Instances](/doc/api/253/1266) API.  |
| user | Yes | String | Account name. Rules: the name should contain 1-16 characters, including upper/lowercase letters, numbers, or underscores; the first character cannot be an underscore |
| host | Yes | String | CVM name. Rules: the name should contain 1-32 characters, including upper/lowercase letters, numbers, or special characters (%. :) |
| cdbInstanceIds.n | No | String | One or more instance IDs (n represents array subscript starting with 0). |
| dbPriv | No | Array | Database permission parameter |
| tbPriv | No | Array | Database table permission parameter |
| colPriv | No | Array | Column permission parameter |
Parameter dbPriv is composed of the following elements:

| Parameter Name | Type | Description |
|---------|---------|---------|
| db | String | Database name |
| priv.n | String | One or more database permissions (n represents array subscript starting with 0).  |
Parameter tbPriv is composed of the following elements:

| Parameter Name | Type | Description |
|---------|---------|---------|
| db | String | Database name |
| db | String | Data table name |
| priv.n | String | One or more data table permissions (n represents array subscript starting with 0).  |
Parameter colPriv is composed of the following elements:

| Parameter Name | Type | Description |
|---------|---------|---------|
| db | String | Database name |
| db | String | Data table name |
| col | String | Column name |
| priv.n | String | One or more column permissions (n represents array subscript starting with 0).  |

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
| 9587 | InvalidParameter | Wrong password format|
| 9572 | InstanceNotExists | Instance does not exist |
| 9537 | ConnectRefusedRootPassword  | Instance connection is refused due to incorrect root password |
| 9533 | SqlExecFailUnknown   | SQL execution error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=ModifyCdbInstanceAccountPrivileges
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-rharhmka
&user=root
&host=localhost
&globalPriv.0=SELECT
&globalPriv.1=INSERT
&dbPriv.0.db=test
&dbPriv.0.priv.0=SELECT
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc":"Success",
    "data": []
}
```



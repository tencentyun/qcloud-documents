## 1. API Description
This API (ModifyCdbParamTemplate) is used to modify the parameter template of the Cloud Database instance.
You can also use API [Query List of Parameter Templates](/doc/api/253/7185) to query the details of the list of parameter templates.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is ModifyCdbParamTemplate.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| templateId | Yes | Int | Template ID, you can use API [Query List of Parameter Templates](/doc/api/253/7185) to query the parameter template ID |
| name | No |String |Template name, which must be unique.
| desc |No | String | Template description |
| paramList.n | No | String | Parameter list. Format: paramList.0.name=auto_increment_increment&paramList.0.value=1 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9613 | InternalError | Database query error |
| 20002 | InvalidParameter.DuplicateName | A duplicate parameter template name exists |

## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=ModifyCdbParamTemplate
&<<a href="/document/product/236/6921">Common request parameters</a>>
&templateId=1005
&amp;paramList.0.name=connect_timeout
&amp;paramList.0.value=10
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        
    ]
}
```



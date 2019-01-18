## 1. API Description
This API (GetCdbParamsModifyHistory) is used to query the parameter modification record.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='https://intl.cloud.tencent.com/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbParamsModifyHistory.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| page | No | Int | Page to be pulled out, default value is 1 |
| pageSize | No | Int | number on each page; default value is 20; maximum is 100 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Total number of modification records |
| paramList | Array | List of modification records |

paramList contains a lot of parameter information, and the data structure for each parameter information is as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| paramName | String | Parameter name | 
| oldValue | String | Old value | 
| newValue | String | New value | 
| isSucess | Int | Whether Modification succeeds. Possible returned values include: 1-Succeeded; 0-Failed | 
| modifyTime | String | Modification time. Format: yyyy-mm-dd hh:mm:ss | 
| cdbInstanceId | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |

## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9543 | NameNotExists | Rename the instance; the old instance name does not exist |
| 9613 | InternalError | Database query error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbParamsModifyHistory
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-jcti2cuw
&page=1
&pageSize=10
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "paramList": [
            {
                "paramName": "back_log",
                "oldValue": "211",
                "newValue": "212",
                "isSucess": 1,
                "modifyTime": "2017-02-13 16:36:25",
                "cdbInstanceId": "qcdb6bfd419f2e054beb210b8fa12b68fc15"
            }
        ]
    }
}
```



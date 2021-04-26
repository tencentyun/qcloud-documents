## 1. API Description
This API (GetCdbInstanceAccountList) is used to query the account list of a database.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbInstanceAccountList.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| offset | No | Int | Record offset; default is 0|
| limit | No | Int | Number of records returned for a single request; default is 20; maximum is 100 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| total | Int | The total number of records |
| rows | Array | Account list |
Parameter rows is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| user | String | Account name |
| host | String | CVM name |
| create_time | String | Creation time |
| modify_time | String | Last modification time |
| remarks | String | Notes |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9531 | ConnectRefused | Instance connection is refused |
| 9532 | ConnectErrorUnknown | Instance connection error |
| 9533 | SqlExecFailUnknown   | Database operation failed |
| 9572 | InstanceNotExists | Instance does not exist |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbInstanceAccountList
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-mjrgnlng
&offset=0
&limit=10
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "total": 6,
        "rows": [
            {
                "host": "localhost",
                "user": "root",
                "create_time": "2016-12-25 10:15:55",
                "modify_time": "2016-12-25 10:15:55",
                "remarks": ""
            },
            {
                "host": "127.0.0.1",
                "user": "root",
                "create_time": "2016-12-25 10:15:55",
                "modify_time": "2016-12-25 10:15:55",
                "remarks": ""
            },
            {
                "host": "::1",
                "user": "root",
                "create_time": "2016-12-25 10:15:55",
                "modify_time": "2016-12-25 10:15:55",
                "remarks": ""
            },
            {
                "host": "%",
                "user": "root",
                "create_time": "2016-12-25 10:15:55",
                "modify_time": "2016-12-25 10:15:55",
                "remarks": ""
            },
            {
                "host": "%",
                "user": "test",
                "create_time": "2016-12-27 15:37:32",
                "modify_time": "2016-12-27 15:38:03",
                "remarks": "hehehe, hahaha"
            }
        ]
    }
}
```



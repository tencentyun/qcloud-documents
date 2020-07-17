## 1. API Description
This API (OpenCdbHour) is used to recover the isolated instance with pay by usage mode. Please make sure that the account is topped up.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is OpenCdbHour.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n | Yes | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| instanceRole | No | String | Instance type. Default is master. Possible values include: master - master instance/disaster recovery instance; ro - read-only instance.


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
| instanceRole | String | Instance type. Default is master. Possible values include: master - master instance/disaster recovery instance; ro - read-only instance.
| cdbInstanceIds | Array | List of the result of recovering instances |
Parameter cdbInstanceIds is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Result, possibly return values: 0 - Succeeded; other values - Failed |
| message | String | Error description. Valid only if code is not 0 |
| oldStatus | String | Status value of instance before change, possible values include: 1 - running; 5 - isolated |
| cdbInstanceId | String | Instance ID |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient balance |
| 9003 | InvalidParameter | Incorrect parameter |
| 9640 | InternalFailure | Account balance query failed|
| 9572 | InstanceNotExists | Instance does not exist |
| 9548 | IncorrectInstanceStatus | Database is not isolated |
| 9592 | OperationDenied | Task is running|


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=OpenCdbHour
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceIds.0=cdb-41lrk52w
&instanceRole=master
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "cdbInstanceIds":[
            {
                "oldStatus":"5",
                "code":"0",
                "message":"",
                "cdbInstanceId":"cdb-41lrk52w"
            }
        ],
        "instanceRole":"master"
    }
}
```



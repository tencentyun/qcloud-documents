## 1. API Description
This API (UpgradeCdbEngineVersion) is used to upgrade the engine version of a Cloud Database instance.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is UpgradeCdbEngineVersion.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| engineVersion | Yes | String | MySQL version. Values include: 5.5, 5.6 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |

If the billing model of an instance is annual or monthly plan, parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dealIds | Array | Short order ID, which is used to call the Cloud API-related APIs, such as [Acquire Order Information](http://intl.cloud.tencent.com/document/product/378/4403) |
| dealNames | Array | Long order ID, which is used to report the order-related problems to Tencent Cloud customer service |
| cdbInstanceIds | Array | Instance ID list, with long order ID as the key, and instance ID as the value |

If the billing model of an instance is pay by usage mode, parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dealIds | Array | Pay-by-usage order ID, which is used to report the order-related problems to Tencent Cloud customer service |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9301 | InvalidParameter | Incorrect transaction parameter |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=UpgradeCdbEngineVersion
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-8qrg9t04
&engineVersion=5.6
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "dealIds": [
            "20161123160000035193343514402319"
        ]
    }
}
```



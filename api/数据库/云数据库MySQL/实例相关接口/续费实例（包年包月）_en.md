## 1. API Description
This API (RenewCdb) is used to renew the Cloud Database instances (master instances and read-only instances) with the billing model of annual or monthly plan. Renewal is not applicable to instances with pay by usage mode.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is RenewCdb.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| period | Yes | Int | Renewal period (Unit: month). The minimum and maximum values are 1 and 36 respectively. You can use API [Query Supported Specifications](/doc/api/253/1333) to acquire the validity period of an instance that can be renewed. The returned field "timeSpan" represents the available period |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| dealIds | Array | Short order ID, which is used to call the Cloud API-related APIs, such as [Acquire Order Information](/doc/api/403/4392) |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dealIds | Array | Short order ID, which is used to call the Cloud API-related APIs, such as [Acquire Order Information](/doc/api/403/4392) |
| dealNames | Array | Long order ID, which is used to report the order-related problems to Tencent Cloud customer service |
| cdbInstanceIds | Array | Instance ID list, with long order ID as the key, and instance ID as the value |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient balance |
| 9650 | InvalidParameter | The instance is not the renewable instance with annual or monthly plan |
| 9572 | InstanceNotExists | Instance does not exist |
| 9301 | InvalidParameter | Incorrect transaction parameter |
| 9006 | InternalError | Database internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=RenewCdb
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&period=1
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "dealIds": [
        "458936"
    ],
    "data": {
        "dealNames": [
            "20161222110059"
        ],
        "dealIds": [
            "458936"
        ],
        "cdbInstanceIds": {
            "20161222110059": [
                "cdb-0pzitle8"
            ]
        }
    }
}
```



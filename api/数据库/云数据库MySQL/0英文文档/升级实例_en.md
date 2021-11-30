## 1. API Description
This API (UpgradeCdb) is used to upgrade Cloud Database instances. Master instances, disaster recovery instances and read-only instances can be upgraded via this API.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is UpsgradeCdb.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| memory | Yes | Int | Size of upgraded memory (unit: MB). To ensure the validity of specified memory value, you can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire the available memory specifications.  |
| volume | Yes | Int | Size of upgraded disk (unit: GB). To ensure the validity of specified volume value, you can use API [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) to acquire the available disk range.  |
| instanceRole | No | String | Instance type. Default is master. Possible values include: master - master instance/disaster recovery instance, ro - read-only instance.  |
| protectMode | No | Int | Data copy method. Default is 0. Possible values include: 0 - indicates asynchronous copy, 1 - indicates semi-synchronized copy, 2 - indicates strong synchronized copy. You can specify this parameter when upgrading master instances, while this parameter will be ignored when upgrading read-only instances or disaster recovery instances |
| deployMode | No | Int | Multiple availability zones. Default is 0. Possible values include: 0 - single availability zone, 1 - multiple availability zones. You can specify this parameter when upgrading master instances, while this parameter will be ignored when upgrading read-only instances or disaster recovery instances |
| slaveZoneFirst | No | Int | Availability zone ID of slave 1. Default is the value of zoneId. You can specify this parameter when upgrading master instances, while this parameter will be ignored when upgrading read-only instances or disaster recovery instances |
| slaveZoneSecond | No | Int | Availability zone ID of slave 2. Default is 0. You can specify this parameter when upgrading master instances, while this parameter will be ignored when upgrading read-only instances or disaster recovery instances |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |

If the billing model of an instance is annual or monthly plan, parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dealIds | Array | Short order ID, which is used to call the Cloud API-related APIs, such as [Acquire Order Information](/doc/api/403/4392) |
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
| 100207 | OperationConstraints.AccountBalanceNotEnough | Insufficient balance |
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9301 | InvalidParameter | Incorrect transaction parameter |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=UpgradeCdb
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-8qrg9t04
&memory=4000
&volume=25
&instanceRole=master
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



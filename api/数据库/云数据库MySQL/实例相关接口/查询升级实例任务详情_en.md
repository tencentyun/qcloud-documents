## 1. API Description
This API (GetCdbUpgradeJobInfo) is used to query task details of instance upgrade. The queries for update details of master instances, disaster recovery instances and read-only instances are supported.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbUpgradeJobInfo.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | ID of instance upgrade task, which will be returned when performing [Instance Update](/document/product/236/7164) task. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Task details |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Task error code; 0: Succeeded; other values: Failed.  |
| message | String | Task message. An error message will be returned if the task fails.  |
| jobId | Int | Task ID |
| type | Int | Task type. Possible returned values include: 9 - read-only instance upgrade; 11 - master instance upgrade; |
| status | Int | Task status. Possible returned values: 0 - running; 2 - execution succeeded; 3 - execution failed; 4 - terminated; 5 - deleted; 6- terminating |
| progress | Int | Task progress. Value range: [0-100], where 0 means the task starts and 100 means that the task is completed.  |
| startTime | String | Start time of task. Format: 2017-02-05 18:19:08 |
| endTime | String | End time of task. Format: 2017-02-05 18:19:08 |
| detail | Object | Task details |
Parameter detail is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbInstanceId | String | Instance ID |
| dealName | String | Long order ID, which is used to report order-related problems to Tencent Cloud customer service |
| before | Object | Instance information before upgrade |
| after | Object | Instance information after upgrade |
Parameter before is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbType | String | Instance specifications before upgrade |
| memory | Int | Memory size before upgrade (in MB) |
| volume | Int | Disk size before upgrade (in GB) |
| engineVersion | String | MySQL version before upgrade |
| protectMode | String | Data copy method before upgrade |
| deployMode | String | Multiple availability zones before upgrade. Possible values include: 0 - Single availability zone deployment, 1 - Multiple availability zones deployment |
| masterZone | String | Zone ID of master database before upgrade |
| slaveZoneFirst | Int | Zone ID of slave database_1 before upgrade |
| slaveZoneSecond | Int | Zone ID of slave database_2 before upgrade |
Parameter after is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbType | String | Instance specifications after upgrade |
| memory | Int | Memory size after upgrade (in MB) |
| volume | Int | Disk size after upgrade (in GB) |
| engineVersion | String | MySQL version after upgrade |
| protectMode | String | Data copy method after upgrade |
| deployMode | String | Multiple availability zones after upgrade. Possible values include: 0 - Single availability zone deployment, 1 - Multiple availability zones deployment |
| masterZone | String | Zone ID of master database after upgrade |
| slaveZoneFirst | Int | Zone ID of slave database_1 after upgrade |
| slaveZoneSecond | Int | Zone ID of slave database_2 after upgrade |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9590 | InternalFailure | Task database access error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbUpgradeJobInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&jobId=12944
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "code": "0",
        "message": "success",
        "jobId": "47258",
        "type": "11",
        "status": "2",
        "progress": "100",
        "startTime": "2017-02-13 15:14:31",
        "endTime": "2017-02-13 15:18:32",
        "detail": [
            {
                "cdbInstanceId": "cdb-pdn63pw5",
                "dealName": "",
                "before": {
                    "memory": 1000,
                    "volume": 35,
                    "engineVersion": "5.5",
                    "protectMode": "",
                    "deployMode": "",
                    "masterZone": 100003,
                    "slaveZoneFirst": 100003,
                    "slaveZoneSecond": "",
                    "cdbType": ""
                },
                "after": {
                    "memory": 1000,
                    "volume": 40,
                    "engineVersion": "5.5",
                    "protectMode": "",
                    "deployMode": "",
                    "masterZone": 100003,
                    "slaveZoneFirst": 100003,
                    "slaveZoneSecond": 100003,
                    "cdbType": ""
                }
            }
        ]
    }
}
```



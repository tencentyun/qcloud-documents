## 1. API Description

This API (GetPushLogs) is used to query the status of submitted prefetch tasks.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

**Note:**

+ Specifying date, task ID, task status and keyword is supported;
+ Paged query is supported;
+ The status query is limited to the prefetch tasks submitted in the last 30 days.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is GetPushLogs.

| Parameter Name     | Required | Type     | Description                                       |
| -------- | ---- | ------ | ---------------------------------------- |
| date     | Yes    | String | Query the prefetch tasks submitted on specified date. The data format is yyyy-mm-dd. For example, 2016-07-03             |
| taskId   | No    | Int    | The ID returned upon the submission of prefetch task; It is used to query a specific task submitted on specified date               |
| status.n | No    | String | Status of prefetch task. The value of "init" means the task is in queue and has not been started; "process" means the prefetch task is in the process of execution; "done" means the task has been completed. You may query one or more tasks with one of the above statuses. |
| keyword  | No    | String | Query by keyword. Make a query through filtering by a part of a URL string              |
| offset   | No    | Int    | Query by offset. This is used for paging .                              |
| limit    | No    | Int    | The number of returned logs. This is used for paging.                              |

## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page |
| message  | String | Module error message description depending on API                           |
| codeDesc | String | Error message or error code at business side                           |
| data     | Object | Returned data result; For details, refer to the description later.                           |

#### data Field Description

| Parameter Name  | Type     | Description             |
| ----- | ------ | -------------- |
| logs  | Object | Details about prefetch tasks; For details, refer to the description later.|
| total | Int    | Total number of URL prefetch tasks returned for the query   |

#### logs Field Description

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| log_id   | Int    | The ID of the operation log                              |
| task_id  | Int    | The ID returned upon submission of prefetch task                             |
| host     | String | Domain for the prefetched URL                             |
| datetime | String | Submission date and time of prefetch task                                |
| status   | String | Current status of prefetch task. "Inprocess" means the task is in the process of execution; "Done" means the task has been completed; "Fail" means the prefetch task has failed. |
| url      | String | Prefetched URL                                   |


## 4. Example

### 4.1 Input Example

> date: 2016-09-30

### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetPushLogs
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462422547
&Nonce=12345678
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
&date=2016-09-30
```

### 4.3 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetPushLogs',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-09-30'
)
```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "logs": [
            {
                "log_id": 10736,
                "task_id": 9214,
                "host": "www.test.com",
                "datetime": "2016-09-30 11:31:34",
                "status": "fail",
                "url": "http://www.test.com/2.jpg"
            },
            {
                "log_id": 10735,
                "task_id": 9214,
                "host": "www.test.com",
                "datetime": "2016-09-30 11:31:34",
                "status": "fail",
                "url": "http://www.test.com/1.jpg"
            }
        ],
        "total": 2
    }
}
```



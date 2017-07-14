## 1. API Description

This API (GetCdnOverseaPushLogs) is used to query the operation status of submitted overseas prefetch tasks.

Domain name for API request: cdn.api.qcloud.com

**API Instruction**

+ You may query by specifying date, task and/or URL;
+ Currently you can only query the operation status of a prefetch task that was submitted within 30 days.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473) page for details. The Action field for this API is GetCdnOverseaPushLogs.

| Parameter Name    | Required | Type     | Description                                       |
| ------- | ---- | ------ | ---------------------------------------- |
| date    | Yes    | String | Query for prefetch tasks that were submitted on specified date. Format is yyyy-mm-dd, for example: 2016-07-03             |
| type    | Yes    | String | Query type. url means query based on URL; task means query based on task        |
| keyword | Yes    | String | Query keyword. When type is task, keyword refers to the task ID; when type is url, keyword refers to a part of the string in a URL for filtered query |

## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page |
| message  | String | Module error message description depending on API                           |
| codeDesc | String | English error message or error code at business side                           |
| data     | Array  | Returned data result; details are described below                           |

#### data Field Description

When type is "task" and a user queries based on prefetch task:

| Parameter Name             | Type     | Description                                       |
| ---------------- | ------ | ---------------------------------------- |
| task_id          | String | taskid of the prefetch task to be queried                            |
| app_id           | Int    | User APP ID                                 |
| urls             | Array  | The URL list in the prefetch task                              |
| status           | String | Status of the prefetch task. If query is based on tasks, pending means prefetch task is waiting to be processed, in-process means the task is being processed and done means prefetch task has been finished |
| task_create_time | String | Time when the prefetch task was created                                 |

When type is "url" and a user queries based on URL

| Parameter Name             | Type     | Description                                       |
| ---------------- | ------ | ---------------------------------------- |
| task_id          | String | taskid of the prefetch task to which the queried prefetch URL belongs                            |
| app_id           | Int    | User APP ID                                 |
| url              | String | Prefetched URL                                    |
| status           | String | Status of the prefetched URL. When query is based on URL, in-process means prefetching, done means prefetch completed |
| task_create_time | String | Time when the prefetch task to which the prefetched URL belongs was created                         |

****Note:**** When querying based on URL, the return will be empty if the task to which the url belongs is pending.



## 4. Example

### 4.1 Example of Input

> date: 2016-10-27
>
> type=task
>
> keyword=20161027-5811b70c7cbff

### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnOverseaPushLogs
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462422547
&Nonce=12345678
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
&date=2016-10-27
&type=task
&keyword=20161027-5811b70c7cbff
```

### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnOverseaPushLogs',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-10-27',
  'type' => 'task',
  'keyword' => '20161027-5811b70c7cbff'
)
```

### 4.4 Example of Response Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "app_id": 12345678,
            "urls": [
                "http://www.test.com/1.jpg"
            ],
            "status": "done",
            "task_id": "20161027-5811b70c7cbff",
            "task_create_time": "2016-10-27 16:13:00"
        }
    ]
}
```



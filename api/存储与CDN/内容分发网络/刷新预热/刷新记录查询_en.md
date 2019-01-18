## 1. API Description

This API (GetCdnRefreshLog) is used to query purge logs and the number of purge operations within the specified time range. You may query by specifying URL.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is GetCdnRefreshLog.

| Parameter Name      | Required | Type     | Description            |
| --------- | ---- | ------ | ------------- |
| startDate | No   | String | Start time of the query  |
| endDate   | No    | String | End time of the query  |
| taskId | No | Int | You may query by the task_id returned by the submitted purge URL task 
| url       | No    | String | URL to be queried (can be blank) |

**Note:**

+ Support query for the purge history within 30 days;
+ Support query for time range accurate to seconds. The time format should be: 2017-02-09 00:00:00;
+ If startDate&endDate and taskId are both empty, the query will fail. Either startDate&endDate or taskId should be filled in;
+ If startDate&endDate and taskId are both filled in, when the taskId is not submitted within this time range, "The date is invalid" will appear;


## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |
| data     | Array  | Returned data result                                   |

#### data Field Description

| Parameter Name  | Type    | Description   |
| ----- | ----- | ---- |
| logs  | Array | Log details |
| total | Int   | Number of purges |

#### logs Field Description

| Parameter Name       | Type     | Description                             |
| ---------- | ------ | ------------------------------ |
| id         | Int    | Code                             |
| app_id     | Int    | User APP ID                       |
| project_id | Int    | Project ID                           |
| host       | String | Domain                             |
| type       | Int    | Purge type. There are two types: 0 refers to URL purge, and 1 refers to directory purge; |
| status     | Int    | Purge result. 1 means the purge is successful, 0 means the purge is in progress, and a negative number means the purge failed               |
| url_list   | Array  | The URL list submitted for this purge operation                  |
| datetime   | String | Time of submission                           |



## 4. Example

### 4.1 Input Example

> startDate: 2017-02-06 19:00:00
> endDate:  2017-02-06 19:40:00



### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnRefreshLog
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462422547
&Nonce=12345678
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
&startDate=2017-02-06+19%3A00%3A00
&endDate=2017-02-06+19%3A40%3A00
```



### 4.3 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnRefreshLog',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'startDate' => '2017-02-06 19:00:00',
  "endDate" => '2017-02-06 19:40:00'
)
```





### 4.4 Example of Returned Result

```json
{
    "retcode": 0,
    "errmsg": "ok",
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "logs": [
            {
                "id": 6182538,
                "app_id": 123456,
                "project_id": 0,
                "host": "www.test.com",
                "type": 0,
                "status": 1,
                "url_list": [
                    "http://www.test.com/Content/image/test.png"
                ],
                "datetime": "2017-02-06 19:39:59"
            }
        "total": 1
    }
}
```



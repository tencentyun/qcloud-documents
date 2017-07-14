## 1. API Description

This API (GetCdnOverseaRefreshLog) is used to query purge logs and the number of purge operations of an overseas CDN for the specified time. You may query by specifying URL and/or domain.

Domain name for API request: cdn.api.qcloud.com

**API Instruction**

- You may query by specifying date, URL and/or domain;
- Currently you can only query the operation status of a purge task that was submitted within 30 days.

[Call Demo](https://www.qcloud.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473) page for details. The Action field for this API is GetCdnOverseaRefreshLog.

| Parameter Name | Required | Type     | Description              |
| ---- | ---- | ------ | --------------- |
| Date | Yes    | String | Query date (day)         |
| url  | No    | String | Purged URL to be queried (can be blank) |
| host | No    | String | Purged domain to be queried (can be blank)  |



## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |
| data     | Array  | Returned data result                                   |

#### data Field Description

| Parameter Name  | Type    | Description   |
| ----- | ----- | ---- |
| logs  | Array | Log details |
| total | Int   | Number of purges |

#### logs Field Description

| Parameter Name       | Type     | Description                           |
| ---------- | ------ | ---------------------------- |
| id         | Int    | Code                           |
| app_id     | Int    | User APP ID                     |
| project_id | Int    | Project ID                         |
| host       | String | Domain                           |
| url        | String | URL submitted for purge                    |
| datetime   | String | Time of submission                         |
| status     | Int    | Result of purge task. 1 means purging, 2 means purge succeeded, -1 means purge failed |



## 4. Example

### 4.1 Example of Input

> date: 20161027



### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnOverseaRefreshLog
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462422547
&Nonce=12345678
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
&date=20161027
```



### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnOverseaRefreshLog',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '20161027',
)
```



### 4.4 Example of Response Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
      	"total":1,
        "logs": [
            {
                "id": 7,
                "app_id": 1251007194,
                "project_id": 0,
                "host": "www.test.com",
                "url": "http://www.test.com/1.jpg",
                "datetime": "2016-10-27 19:30:29",
                "status": 2
            },
        ]
    }
}
```




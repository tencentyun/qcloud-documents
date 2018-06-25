## 1. API Description

This API (RefreshCdnUrl) is used to set specified resources on a node as expired.

Domain for API request:<font style="color:red">cdn.api.cloud.tencent.com</font>

1) Each user is allowed to purge up to 10,000 URLs each day;
2) A maximum of 1,000 URLs can be submitted for each purge.

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is RefreshCdnUrl.

| Parameter Name | Required | Type   | Description                              |
| -------------- | -------- | ------ | ---------------------------------------- |
| urls.n         | Yes      | String | URL to be purged. You may purge multiple URLs |


#### Note

+ You may purge one or multiple URLs. When purging multiple URLs, you can pass parameters like this:
    ```
    urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg
    ```
+ Note that URLs must start with "http://" or "https://", otherwise errors will occur;

+ The domain in the submitted purge URL must be a domain that has already been connected to CDN by the user, and whose status is **Deploying** or *Activated*; otherwise errors will occur.
+ If there is a parameter in a purge URL, for example:
```
   > https://www.abc.com/index.php?name=1
   > https://www.abc.com/index.php?name=2
```
   The parameter will be ignored, and the URL `https://www.abc.com/index.php` will be purged.




## 3. Output Parameters

| Parameter Name | Type   | Description                              |
| -------------- | ------ | ---------------------------------------- |
| code           | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message        | String | Module error message description depending on API |
| codeDesc       | String | English error message or error code at business side. |
| data           | Array  | Details will be described below          |

**data Field Description:**

| Parameter Name | Type   | Description                              |
| -------------- | ------ | ---------------------------------------- |
| count          | Int    | Number of URLs submitted for this purge operation |
| task_id        | String | ID of the purge task                     |




## 4. Example

### 4.1 Input Example

`> urls.0: https://www.test.com/1.jpg`


### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.cloud.tencent.com/v2/index.php?
Action=RefreshCdnUrl
&SecretId=XXXXXXXXXXXXXXXXXX
&Timestamp=1462521223
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&urls.0=https%3A%2F%2www.test.com%2F1.jpg
```



### 4.3 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.cloud.tencent.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'RefreshCdnUrl',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462864833,
  'Nonce' => 1149033341,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'urls.0' => 'https://www.test.com/1.jpg'
)
```
<font color="red">When there are too many URLs to be purged, in order to avoid overlength of GET request, it is recommended to use POST method to call this API.</font>

### 4.4 Example of Returned Result

#### Purge submission succeeded 

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "count": 1,
        "task_id": "1480069888795584532"
    }
}
```

#### Purge submission failed

```json
{
    "code": 4000,
    "message": "(9110) Information for this domain does not exist. cdn no such host",
    "codeDesc": "9110"
}
```



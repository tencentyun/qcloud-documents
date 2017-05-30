## 1. API Description

This API (RefreshCdnOverSeaUrl) is used to set specified resources  on an overseas CDN node as expired.

Domain name for API request: cdn.api.qcloud.com

[Call Demo](https://www.qcloud.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473) page for details. The Action field for this API is RefreshCdnOverSeaUrl.

| Parameter Name   | Required | Type     | Description                     |
| ------ | ---- | ------ | ---------------------- |
| urls.n | Yes    | String | URLs to be purged. You may purge multiple URLs |

#### Note

+ To purge multiple URLs, please pass parameters like this:
  ```
  urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg
  ```

+ URLs must start with "http://" or "https://"

+ You can purge up to 10,000 URLs each day (1,000 URLs each time)




## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API                           |
| codeDesc | String |Error message                     |
| data     | Array  | Details will be described below                                  |

**data Field Description:**

| Parameter Name  | Type   | Description           |
| ----- | ---- | ------------ |
| count | Int  | Number of URLs submitted by this purge operation |




## 4. Example

### 4.1 Example of Input

> urls.0: https://www.test.com/1.jpg



### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=RefreshCdnOverSeaUrl
&SecretId=XXXXXXXXXXXXXXXXXX
&Timestamp=1462521223
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&urls.0=https%3A%2F%2www.test.com%2F1.jpg
```



### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'RefreshCdnOverSeaUrl',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462864833,
  'Nonce' => 1149033341,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'urls.0' => 'https://www.test.com/1.jpg'
)
```



### 4.4 Example of Response Result

#### Purge submission succeeded 

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "count": 1
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


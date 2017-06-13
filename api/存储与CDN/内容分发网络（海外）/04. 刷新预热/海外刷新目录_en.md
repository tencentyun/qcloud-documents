## 1. API Description

This API (RefreshCdnOverSeaDir) is used to set resources under the specified directory on a node as expired.

Domain name for API request: cdn.api.qcloud.com

1) The domain must have been connected to International CDN

2) Up to 100 directories can be purged per day.

3) Up to 20 directories can be purged at one time.

[Call Demo](https://www.qcloud.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473) page for details. The Action field for this API is RefreshCdnOverSeaDir.

| Parameter Name   | Required | Type     | Description                  |
| ------ | ---- | ------ | ------------------- |
| dirs.n | Yes    | String | Directory to be purged. You may purge multiple directories |



#### Note

+ You can purge one or multiple directories:
    ```
    dirs.0=http://www.test.com/abc/&dirs.1=http://www.test.com/def/
    ```

+ URLs must start with "http://" or "https://".


## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message|
| data     | Array  | Details will be described below                                  |

**data Field Description:**

| Parameter Name  | Type   | Description           |
| ----- | ---- | ------------ |
| count | Int  | Number of URLs submitted for this purge operation |



## 4. Example

### 4.1 Example of Input

> dirs.0: http://www.test.com/test/



### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=RefreshCdnOverSeaDir
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462521628
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&dirs.0=https%3A%2F%2Fwww.test.com%2Fabc
```



### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'RefreshCdnOverSeaDir',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462865178,
  'Nonce' => 279749933,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'dirs.0' => 'http://www.test.com/test/'
)
```





### 4.4 Example of Returned Result

#### Purge submission succeeded

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
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
    "codeDesc": 9110
}
```


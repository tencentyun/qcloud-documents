## 1. API Description

This API (RefreshCdnDir) is used to set resources under the specified directory on a node as expired.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

1) Each user is allowed to purge 100 directories per day;
2) You may submit up to 20 directories at a time.

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is RefreshCdnDir.

| Parameter Name   | Required | Type     | Description                  |
| ------ | ---- | ------ | ------------------- |
| dirs.n | Yes    | String | Directory to be purged. You may purge multiple directories |



#### Note

+ You can purge one or multiple directories:
    ```
    dirs.0=http://www.test.com/abc/&dirs.1=http://www.test.com/def/
    ```

+ Note that URLs must start with "http://" or "https://", otherwise errors will occur.


## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |




## 4. Example

### 4.1 Input Example

> dirs.0: http://www.test.com/test/



### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=RefreshCdnDir
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462521628
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&dirs.0=https%3A%2F%2Fwww.test.com%2Fabc
```



### 4.3 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'RefreshCdnDir',
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


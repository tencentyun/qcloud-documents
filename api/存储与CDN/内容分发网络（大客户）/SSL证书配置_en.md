## 1. API Description
This API (SetHttpsInfo) is used to set or delete HTTPS configuration of a domain.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473). The Action field for this API is SetHttpsInfo.

| Parameter Name | Required | Type     | Description |
| ---- | ---- | ------ | ----------------- |
| host  | Yes    | String | Domain for which a certificate is to be configured |
| httpsType |Yes | Int | Configuration type. 0: Delete https configuration, without the need to fill in the certificate and private key parameters; 1: Enable http and configure it as back-to-origin method; 2: Enable and https and configure it as back-to-origin method; When it is enabled, certificate and private key parameters need to be delivered. |
| cert | No | String | Certificate in PEM format |
| privateKey | No | String | Private key in PEM format |

**Note**

+ Currently, domains connected with COS origin or FTP origin cannot use Https as the back-to-origin method;
+ Certificate and private key transmission: Transmit the certificate and private key that are encoded with Base64

## 3. Output Parameters
| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side. |
| data     | Object | Returned data result |


## 4. Example
### 4.1 Input Example
> host: www.test.com
> httpsType: 1
> cert: 9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=
> privateKey: 9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=

### 4.2 GET Request
For GET request, all the parameters are required to be appended to URL (in the form of key=value; value is required to be URL-encoded):
```
https://cdn.api.qcloud.com/v2/index.php?
Action=SetHttpsInfo
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&httpsType=1
&cert=XXXXXXXXXXXXXXXXXXXXXXXXXX
&privateKey=XXXXXXXXXXXXXXXXXXXXXXX
```

### 4.2 POST Request
For POST request, the parameters are filled in HTTP Requestbody. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Such formats as formdata and xwwwformurlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
	'Action' => 'SetHttpsInfo',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'host' => ''www.test.com",
    'httpsType'  => 1,
    'cert' => 'XXXXXXXXXXXXXXXXXXX',
    'privateKey' => 'XXXXXXXXXXXXXXXXX'
)
```

### 4.3 Response Example

Note: IP in the example is only for reference.

```
{
  "retcode":0,
  "errmsg":'ok",
  "data":[],
  "code":0,
  "message":""
}
```




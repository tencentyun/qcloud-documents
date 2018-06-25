## API Description
This API (**SetHttpsInfo**) is used to set or delete HTTPS configuration of a domain name.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:**

+ For domain names accessing COS origin or FTP origin, the origin-pull method cannot be set to protocol following.
+ Certificate and private key transmission: Select a certificate you uploaded. Transmit the certificate and private key that are encoded based on base64.
+ Select a hosted certificate, and obtain the certificate ID using the API [Query List of Hosted Certificates](https://cloud.tencent.com/document/product/228/12543).
+ One of "httpsType" and "forceSwith" must be specified.
+ The API can be called for 100 times/min at most.

[View the example](https://cloud.tencent.com/document/product/228/1734)


## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is SetHttpsInfo.

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ---------------------------------------- |
| host | Yes | String | Domain name that requires to have a certificate configured |
| httpsType | No | Int | Configuration type<br/>"0": Delete HTTPS configuration, without the need to enter the certificate and private key parameters<br/>"1": Upload self-owned certificate and select HTTP for origin-pull<br/>"2": Upload self-owned certificate and select protocol following for origin-pull<br/>"3": Use hosted certificate and select HTTP for origin-pull<br/>"4": Use hosted certificate and select protocol following for origin-pull<br/>If domain names 1 & 2 are not configured with certificates or are configured with hosted certificates, you must upload "cert" and "privateKey"<br/>If domain names 3 & 4 are not configured with certificates or are configured with self-owned certificates, you must upload "certId" |
| cert | No | String | Certificate in PEM format |
| privateKey | No | String | Private key in PEM format |
| forceSwitch | No | Int | Forced redirect switch<br/>"1": Enable HTTP forced redirect<br/>"-1": Disable HTTP forced redirect<br/>"2": Enable HTTPS forced redirect<br/>"-2": Disable HTTPS forced redirect |
| http2 | No | String | HTTP2.0 switch<br/>"on": Enable HTTP2.0<br/>"off": Disable HTTP2.0 |
| certId | No | String | Certificate ID, which can be obtained using the API [Query List of Hosted Certificates](https://cloud.tencent.com/document/product/228/12543) |

## Output Parameters
| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Code page. |
| data | Object | Returned data result |


## Example
### Sample Parameters

Note: The private key in the example is for reference only.

```
host: www.test.com
httpsType: 1
cert: 9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=
privateKey: 9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=
```

### GET Request
For a GET request, all the parameters are required to be appended to the URL (in the form of key=value; value is required to be URL-encoded):
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

### POST Request
For a POST request, the parameters are input in HTTP Request body. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Formats of parameters such as form-data are supported. The array of parameters is as follows:

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

### Example of Returned Result

```
{
  "retcode":0,
  "errmsg":'ok",
  "data":[],
  "code":0,
  "message":""
}
```




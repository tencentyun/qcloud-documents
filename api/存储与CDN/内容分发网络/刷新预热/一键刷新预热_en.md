## API Description
This API (**FlushOrPushOverall**) is used to purge or prefetch both international and Chinese resources at a time.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:**

+ Make sure prefetch whitelist is enabled for your account before you submit a request for prefetch.
+ When you submit purge/prefetch tasks, make sure your accelerated domain name is accessed in the specified region (Chinese/international) and in the status of "Enabled" or "Deploying".
+ URLs in the submitted list must start with "http://" or "https://".
+ The number of purge/prefetch tasks performed at a time and on each day is limited. You can log in to [CDN 
+ Console](https://console.cloud.tencent.com/cdn/purge) to check your quota.
+ The frequency of calling the API is limited to 100/min.


[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is FlushOrPushOverall.

| Parameter Name | Required | Type | Description |
| -------- | ---- | ------ | ---------------------------------------- |
| command | Yes | String | Specify the operation to be performed<br/>"push" indicates prefetch<br/>"flush" indicates purge |
| urls | Yes | String | Submitted list of URLs for purge/prefetch |
| type | Yes | String | purge/prefetch type<br/>"dir" indicates directory<br/>"url" indicates full path of resource<br/>"dir" is not supported for prefetch |
| mainland | No | Int | Enter 1 for purge/prefetch in Mainland China<br/>If it is left empty, no purge/prefetch task is submitted in Mainland China |
| oversea | No | Int | Enter 1 for purge/prefetch in international regions<br/>If it is left empty, no purge/prefetch task is submitted in international regions |

#### Notes

One of the parameters for "mainland" and "international" must be set to 1 for a successful submission.

## Output Parameters
| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side.<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |


## Example
### Sample Parameters

```
command: flush
urls.0: https://www.test.com/1.jpg
type: url
mainland: 1
```

### GET Request
For a GET request, all the parameters are required to be appended to the URL (in the form of key=value; value is required to be URL-encoded):
```
https://cdn.api.qcloud.com/v2/index.php?
Action=FlushOrPushOverall
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Nonce=123456789
&Timestamp=1511794466
&command=flush
&urls.0=https%3A%2F%2Fwww.test.com%2F1.jpg
&type=url
&mainland=1
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### POST Request
For a POST request, the parameters are input in HTTP Request body. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Formats of parameters such as formdata are supported. The array of parameters is as follows:

```
array (
	'Action' => 'FlushOrPushOverall',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1511794466,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'command' => ''flush",
	'urls.0' => 'https://www.test.com/1.jpg',
	'type' => 'url',
	'mainland' => '1'
)
```

### Example of Returned Result

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```




## 1. API Description
This API (CdnOverseaPushser) is used to submit overseas CDN URL prefetch tasks.

Domain name for API request:<font style="color:red">cdn.api.qcloud.com</font>

**API Instruction**
+ Each user is allowed to submit 1000 overseas CDN resources for prefetch per day, and up to 20 resources for each submission;
+ If the default limit cannot meet your business needs, please contact us to adjust the quota;

[Call Demo](https://www.qcloud.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473) page for details. The Action field for this API is CdnOverseaPushser.

| Parameter Name   | Required | Type     | Description                        |
| ------ | ---- | ------ | ------------------------- |
| urls.n | Yes    | String | Resource URL to be prefetched. You may prefetch multiple URLs |

**Note:**

+ The submitted URLs must have "http://" or "https://" as prefix;

+ You may prefetch one or multiple URLs. When prefetching multiple URLs, you can pass parameters like this:

  ```
  urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg
  ```

+ You can submit URLs that belong to different domains, in which case CDN will split them into different prefetch tasks according to their domains;

+ Prefetch will lead to a high back-to-origin bandwidth, please split your prefetch tasks and submit them according to your origin server's bandwidth;

## 3. Output Parameters
| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |
| data     | Object | Returned data result                                   |

**data Field Description**

| Parameter Name    | Type     | Description          |
| ------- | ------ | ----------- |
| task_id | String | ID information of the submitted prefetch task |

## 4. Example
### 4.1 Example of Input
> urls.0: http://www.test.com/1.jpg

### 4.2 GET Request
All the parameters are required to be added after URL in GET request:
```
https://cdn.api.qcloud.com/v2/index.php?
Action=CdnOverseaPushser
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&urls.0=http%3A%2F%2Fwww.test.com%2F1.jpg
```

### 4.2 POST Request
In POST request, the parameters will be filled in HTTP Requestbody. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Such formats of parameters as formdata, xwwwformurlencoded are supported. The array of parameters is as follows:

```
array (
	'Action' => 'CdnOverseaPushser',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'urls.0' => 'http://www.test.com/1.jpg'
)
```

### 4.3 Example of Response
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"task_id": "20161027-5811b7bf2fac3"
	}
}
```


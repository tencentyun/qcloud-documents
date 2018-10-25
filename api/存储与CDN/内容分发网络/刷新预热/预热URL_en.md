## 1. API Description
This API (CdnPusherV2) is used to submit URL prefetch task.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

**Note:**
+ For each customer, a maximum of 1000 resources are allowed to be submitted for prefetch each day and a maximum of 20 resources are allowed to be submitted for each prefetch.
+ If the default limit cannot meet your business needs, please contact us for upscaling;
+ This API has been connected to CDN sub-user authentication system. Collaborators with permission can use their SecretId and SecretKey to call the API;
+ You can check the prefetch tasks submitted through this API and query the results in Console.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is CdnPusherV2.

| Parameter Name      | Required | Type    | Description                       |
| --------- | ---- | ----- | ------------------------ |
| urls.n    | Yes    | Array | List of resource URLs to be prefetched           |
| limitRate | No    | Int   | Prefetch rate limit (in Mbps). The minimum value is 1Mbps |

**Note:**

+ The submitted URLs must contain "http://" or "https://" as prefix;
+ You can submit URLs that belong to different domains, in which case CDN will split them into different prefetch tasks according to their domains;
+ Prefetch will lead to a high back-to-origin bandwidth. Please split your prefetch tasks and submit them according to your origin server's bandwidth;
+ If the prefetch leads to a high pressure on the origin server, you can mitigate the pressure by setting a prefetch rate limit;
+ The rate limit is set by domain dimension. If the rate is limited to 1Mbps and the resource URL to be prefetched is http://www.abc.com/1.mkv, when the resource is pulled from the origin server configured for the domain www.abc.com, the overall back-to-origin transmission rate of network-wide nodes will be limited to 1Mbps.

## 3. Output Parameters
| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | Returned data result                                   |

**data Field Description**

| Parameter Name     | Type     | Description        |
| -------- | ------ | --------- |
| task_ids | Object | IDs of submitted tasks  |

**task_ids Field Description**

| Parameter Name    | Type     | Description      |
| ------- | ------ | ------- |
| task_id | Int    | ID of submitted task |
| date    | String | Date on which the task is submitted |

## 4. Example
### 4.1 Input Example
> urls.0: http://www.test.com/1.txt
> limitRate: 1

### 4.2 GET Request
For GET request, all the parameters are required to be appended to the URL:
```
https://cdn.api.qcloud.com/v2/index.php?
Action=CdnPusherV2
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&urls.0=http://www.test.com/1.jpg
&limitRate=1
```

### 4.2 POST Request
For POST request, the parameters are filled in HTTP Requestbody. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Formats such as formdata and xwwwformurlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
	'Action' => 'CdnPusherV2',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'urls.0' => 'http://www.test.com/1.jpg',
    'limitRate'  => 1
)
```

### 4.3 Response Example
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"task_ids": [
			{
				"task_id": 20860,
				"date": "20161013"
			}
		]
	}
}
```




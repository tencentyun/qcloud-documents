## API Description
This API (GetDsaStatistics) is used to query the monitoring data for a specified time range, allowing you to observe the changes in access to domain names.   
Domain name for API request: `dsa.api.qcloud.com`  


>**Note:**  

>- A maximum of 100 calls to this API are allowed per minute. Do not call the API frequently.  
>- The monitoring data of more than one item or domain name can be queried at a time.
>- Details of more than one monitoring metric can be queried at a time.
>- The time span for query is limited to 90 days.

**The monitoring metrics allowed for query**  

| Statistical Metric | Metric Name | Metric Description |
| ------- | ------ | -------- |
| Access traffic |  flux     | Queries the monitoring data of access traffic by domain name (in byte) |
| Access bandwidth | bandwidth | Queries the monitoring data of access bandwidth by domain name (in bps) |
| Number of requests | request   | Queries the monitoring data of the number of requests for accessing domain names |
| Access latency | delay     | Queries the average access latency by domain name (in ms) |
| Status code | Status code value | Queries the monitoring data of status codes by domain name |
  
## Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/product/570/13932). The Action field for this API is `GetDsaStatistics`.   

| Parameter | Required | Type | Value Example | Description |
| ------ | ----------| ----------| ------- |
| metrics | Yes | String | ["flux","request"] | Statistical metric. More than one metric can be submitted at a time in JSON format. |
| projects | No |  Unsigned | [1001853] | Lists project IDs, [View project Ids](https://console.cloud.tencent.com/project)</br> Submitted in JSON format |
| hosts | No | String  | ["test.qcloud.com"] | List of domain names, which is used when monitoring data is queried by domain name. It is submitted in JSON format. |
| startDate | No | String  | 2018-04-19 | Start date, which is the query date by default<br/>Format: YY-MM-DD |
| endDate| No |  String   | 2018-04-20 | End date, which is the query date by default<br/>Format: YY-MM-DD |
| granularity | No | Unsigned | 15 | Query granularity (in minute). For more information, please see [Rules for query granularity](#lidu) |

> **Notes:**    
- By default, the combined statistics of all domain names under the account are queried when no query object is specified.
- When querying multiple items or domain names, you are recommended to use the POST method for submission, so as to prevent the URL length from exceeding the limit due to an overlong query parameter.

<span id="lidu"></span>
**Rules for query granularity**

| Time Span | Default Granularity | Supported Query Granularity |
| ------ | ----------| --------- |
| 1 day |  1  | 1,5,15,30,60,120,240,1440 |
| 2-3 days |  15 | 15,30,60,120,240,1440 |
| 4-7 days |  30  | 30,60,120,240,1440 |
| 8-90 days | 60 | 60,120,240,1440 |

>Data aggregation:
>1. The monitoring data queried every 1 minute is used as the basic data sampling point.
>2. The monitoring data of access traffic, number of accesses, status codes are accumulated and merged by time.
>3. Average access latencies are merged.
>4. For the bandwidth monitored at the granularity of 5 minutes, use the bandwidth generated every 1 minute as the sample value and take the average bandwidth value within 5 minutes.
>5. For the bandwidth monitored at the granularity of more than 5 minutes, use the bandwidth generated every 5 minutes as the sample value and take the maximum bandwidth value.

## Output Parameters
| Parameter | Type | Description |
|------ | ----------| ----------|
|code|Int|Common error code</br>0: Successful<br/>Other values: Failed<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/570/13937) on the Error Codes page.
|message|String|Module error message description depending on API |
|codeDesc|String|Error message or error code at business side |
|data|Array| Details on the queried data. For more information, please see [data Field Description](#data) |

> **Notes:**
- By default, the combined monitoring statistics of all domain names are returned by account when no query object is specified.
- When a domain name or an item is specified, the monitoring statistics of each domain name is returned by domain name.

<span id="data"></span>
#### data Field Description
| Parameter | Data Type | Description |
|------ | -----| -----| 
| datetime | String | Data time, for example: 2018-04-19 01:00:00 |
| bandwidth | Unsigned | This is returned when query metrics include bandwidth (in bps) |
| flux | Unsigned | This is returned when query metrics include traffic (in byte) |
| request |Unsigned | This is returned when query metrics include number of requests |
| delay | Unsigned | This is returned when query metrics include access latency (in ms) |
| Status code | Unsigned |Number of accesses to the specified status code is returned |

## Sample Code
### Query the monitoring data of bandwidth under the account 
#### Requirement 
Query the monitoring data of bandwidth for all domain names under the account on Apr. 19, 2018 at a granularity of 60 minutes.
#### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://dsa.api.qcloud.com/v2/index.php?
Action=GetDsaStatistics
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1524279600
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&metrics=["bandwidth"]
&startDate=2018-04-19
&endDate=2018-04-19
&granularity=60
```

> **Notes:**
> To prevent the URL length from exceeding the limit due to an overlong query parameter, this API is called to submit query requests using the POST method by default.

#### POST request
For a POST request, the parameters are input in HTTP Request-body. The request address is:
```
https://dsa.api.qcloud.com/v2/index.php  
```
Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows: 
```
array (
  'Action' => 'GetDsaHostLogs',
  'SecretId' => 'SecretId',
  'Timestamp' => 1524279600,
  'Nonce' => 123456789,
  'Signature' => 'Signature',
  'metrics' => '["bandwidth"]',
  'startDate' => 2018-04-19,
  'endDate' => 2018-04-19,
  'granularity' => 60
)
```
#### Example of returned result
1. Query successful
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		{
            "datetime": "2018-04-19 00:00:00",
            "bandwidth": 589746515
        },
        {
            "datetime": "2018-04-19 01:00:00",
            "bandwidth": 489746515
        },
        {
            "datetime": "2018-04-19 02:00:00",
            "bandwidth": 375489625
        },
 		......
        {
            "datetime": "2018-04-19 23:00:00",
            "bandwidth": 589746515
        }
	}
}
```
2. Query failed
```
{
    "code": 4100,
    "message": "Authentication failed. For more information, please see the Authentication section in the document.",
    "codeDesc": "AuthFailure"
}
```

### Query the monitoring data of the number of requests for accessing the specified domain name(s) and the access traffic
#### Requirement 
Query the monitoring data of the number of requests for accessing the domain names test1.dsa.qcloud.com and test2.dsa.qcloud.com as well as the access traffic on Apr. 19, 2018 at a granularity of 5 minutes.
#### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://dsa.api.qcloud.com/v2/index.php?
Action=GetDsaStatistics
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1524279600
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&metrics=["request","flux"]
&hosts=["test1.dsa.qcloud.com","test2.dsa.qcloud.com"]
&startDate=2018-04-19
&endDate=2018-04-19
&granularity=5
```

> **Notes:**
> If there are a large number of domain names, to prevent the URL length from exceeding the limit due to an overlong query parameter, this API should be called to submit query requests using the POST method.

#### POST request
For a POST request, the parameters are input in HTTP Request-body. The request address is:
```
https://dsa.api.qcloud.com/v2/index.php  
```
Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows: 
```
array (
  'Action' => 'GetDsaHostLogs',
  'SecretId' => 'SecretId',
  'Timestamp' => 1524279600,
  'Nonce' => 123456789,
  'Signature' => 'Signature',
  'metrics' => '["request","flux"]',
  'hosts' => ["test1.dsa.qcloud.com","test2.dsa.qcloud.com"],
  'startDate' => 2018-04-19,
  'endDate' => 2018-04-19,
  'granularity' => 5
)
```
#### Example of returned result
1. Query successful
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		test1.dsa.qcloud.com:[
			{
	            "datetime": "2018-04-19 00:00:00",
	            "request": 589746515,
				"flux":
	        },
	        {
	            "datetime": "2018-04-19 00:05:00",
	            "request": 489746515,
				"flux":
	        },
	        {
	            "datetime": "2018-04-19 00:10:00",
	            "request": 375489625,
				"flux":
	        },
	 		......
	        {
	            "datetime": "2018-04-19 23:55:00",
	            "request": 589746515,
				"flux":
	        }
		],
		test2.dsa.qcloud.com:[
			{
	            "datetime": "2018-04-19 00:00:00",
	            "request": 589746515,
				"flux":
	        },
	        {
	            "datetime": "2018-04-19 00:05:00",
	            "request": 489746515,
				"flux":
	        },
	        {
	            "datetime": "2018-04-19 00:10:00",
	            "request": 375489625,
				"flux":
	        },
	 		......
	        {
	            "datetime": "2018-04-19 23:55:00",
	            "request": 589746515,
				"flux":
	        }
		]
	}
}
```
2. Query failed
```
{
    "code": 4100,
    "message": "Authentication failed. For more information, please see the Authentication section in the document.",
    "codeDesc": "AuthFailure"
}
```


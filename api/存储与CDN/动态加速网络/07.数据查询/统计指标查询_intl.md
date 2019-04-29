## API Description
This API (GetDsaHostStatistics) is used to query statistical metrics for log access in a specific period of time, allowing you to get statistics on log access.
Domain name: `dsa.api.qcloud.com`


>**Note:**
>- A maximum of 100 calls to this API are allowed per minute. Do not call the API frequently.
>- More than one item or domain name can be queried at a time, and a summary of the usage data is displayed by domain name.

<span id="zhibiao"></span>
### Description of statistical metrics
| Statistical Metric | Metric Name | Metric Description |
| ------- | ------ |
| Total traffic |  flux   | Calculates the total traffic in the query period by domain name (in byte) |
| Peak bandwidth | bandwidth | Calculates the peak bandwidth in the query period by domain name (in bps) |
| Total requests | request | Calculates the total number of requests in the query period by domain name |
| Average access latency | delay | Calculates the average access latency in the query period by domain name (in ms) |

## Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/product/570/13932). The Action field for this API is `GetDsaHostStatistics`.   

| Parameter | Required | Type | Example | Description |
| ------ | ----------| ----------| ------- |
| metrics | Yes | String | flux | Statistical metric name. For more information, please see [Description of statistical metrics](#zhibiao) |
| projects | No |  Unsigned | [1001853] | Lists project IDs, [View project Ids](https://console.cloud.tencent.com/project)</br> Submitted in JSON format |
| hosts | No | String  | test.qcloud.com | Lists domain names, used to query data by domain name</br>Domain names are submitted in JSON format |
| startDate | No | String  | 2018-04-19 | Start time</br>Format: YY-MM-DD |
| endDate| No |  String   | 2018-04-20 | End time, </br>format: YY-MM-DD |
| offset | No | Unsigned | 15 | Queries the number of offsets |
| length | No | Unsigned | 10 | Length of this query |

**Parameter description:** 
- When the start time or the end time is empty, the statistics on the day of the query are returned by default.
- By default, combined statistics of all domain names are queried by account when no query object is specified.
- To prevent the URL length from exceeding the limit due to an overlong query parameter when more than one project or domain name is queried, you are recommended to submit your requests using the POST method.
- When there are a large number of accounts under an account, you can use "offset" and "length" to set fragmented queries. The queried domain names are displayed in a descending order from the first metric specified in "metrics".

## Response Parameters
| Parameter | Type | Description |
|------ | ----------| ----------|
|code|Int|Common error code</br>0: Successful</br>Other values: Failed</br>For more information, please see Common Error Codes on the [Error Codes](https://cloud.tencent.com/document/product/570/13937 ) page |
|message|String|Module error message description depending on API |
|codeDesc|String|Error message or error code at business side |
|data|Array| Details on the queried data. For more information, please see [data Field Description](#data) |

<span id="data"></span>
#### data Field Description
| Parameter Name | Type | Description |
|------ | -----| -----| 
| host | String | Domain name</br>For example: dsatest.qcloud.com |
| flux | Unsigned | Total traffic |
| bandwidth | Unsigned | Peak bandwidth |
| request | Unsigned | Total number of requests |
| delay | Unsigned | Average access latency |

## Sample Code 
### Configuration example 
Queries the statistics on traffic, bandwidth, and number of requests of all domain names under an account on 2018-04-17.
### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://dsa.api.qcloud.com/v2/index.php?
Action=GetDsaHostStatistics
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1524279600
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&metrics=[bandwidth]
&startDate=2018-04-17
&endDate=2018-04-17
```
>**Note:**
> To prevent the URL length from exceeding the limit due to an overlong query parameter, this API is called to submit query requests using the POST method by default.

### POST Request
For a POST request, the parameters are input in HTTP Request-body. The request address is:
```
https://dsa.api.qcloud.com/v2/index.php  
```
Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows: 
```
array (
  'Action' => 'GetDsaStatistics',
  'SecretId' => 'SecretId',
  'Timestamp' => 1524279600,
  'Nonce' => 123456789,
  'Signature' => 'Signature',
  'metrics' => '["flux","bandwidth","request"]',
  'startDate' => "2018-04-17"
  'endData' => "2018-04-17"
)
```
### Example of returned result
#### Query Successful
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		{
            "host": "a.dsa.qcloud.com",
			"flux":265412354,
            "bandwidth": 589746515,
			"request":123456548
        },
 		......
        {
            "host": "b.dsa.qcloud.com",
			"flux":362124545,
            "bandwidth": 749516585,
			"request":156534248
        }
	}
}
```
#### Query Failed
```
{
    "code": 4100,
    "message": "Authentication failed. For more information, please see the Authentication section in the document.",
    "codeDesc": "AuthFailure"
}
```


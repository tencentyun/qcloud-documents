## 1. API Description

This API (GetCdnLogList) is used to query the log download links of specified domain names within the specified time range. You can only query one domain at a time.

Domain name for API request:<font style="color:red">cdn.api.qcloud.com</font>

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

Log download links API_V1: [GenerateLogList](https://cloud.tencent.com/document/product/228/3950)

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is GetCdnLogList.

| Parameter Name      | Required | Type     | Description     |
| --------- | ---- | ------ | ------ |
| host   | Yes    | String    | Domain of the log to be queried |
| startDate | No    | String | Start time of the query. Format: 2016-12-30 00:00:00  |
| endDate   | No    | String | End time of the query. Format: 2016-12-30 01:00:00 |

#### Note

+ If the startDate and endDate are empty, the default query range is 30 days before the current time. One log download link is provided per hour. For more log description, refer to [Log Download](https://cloud.tencent.com/doc/product/228/6316);
+ startDate indicates the start date of the query, and endDate indicates the end date of the query. The log packets between the time range specified in startDate and endDate will be returned. Assuming startDate=2016-12-30 00:01:00 and endDate=2016-12-30 02:12:00, the packets in three hours (2016123000, 2016123001, and 2016123002) will be returned;
+ If no access log is generated for an hour, the download link will not be generated or returned accordingly.
+ The log download link is valid for 24 hours.

## 3. Output Parameters


| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |
| data     | Array  | Result data, as described below                             |


#### data Field Description

| Parameter Name | Type    | Description            |
| ---- | ----- | ------------- |
| now  | Int   | Current time, Unix timestamp |
| list | Array | List of log download links      |


#### list Field Description

| Parameter Name | Type     | Description                                       |
| ---- | ------ | ---------------------------------------- |
| date | Int    | Log date                                     |
| type | Int    | Indicate whether there is a log; 1: yes; 0: no                        |
| name | String | Log name. Format: yyyymmddhh-domain, for example: 2016050301-www.test.com |
| link | String | Download link                                     |

## 4. Example

### 4.1 Input Example

> host: www.test.com
> startDate: 2016-12-30 00:00:01
> endDate: 2016-12-30 05:12:00


### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnLogList
&SecretId=XXXXXXXXXXXXXXXXX
&Timestamp=1462430812
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&startDate=2016-12-30+00%3A00%3A01
&endDate=2016-12-30+05%3A12%3A00
```

### 4.3 POST Request



For POST request, the parameters need to be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats as form-data and x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnLogList',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462865760,
  'Nonce' => 1058191224,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => 'www.test.com',
  'startDate' => '2016-12-30 00:00:01',
  'endDate' => '2016-12-30 05:12:00'
)
```

### 4.4 Example of Returned Result

```json
{
  "code":0,
  "message":"",
  "codeDesc": "Success",
  "data":{
    "now":1483954368,
    "list":[
  		{
  	  		"date":2016-12-30,
  	  		"type":1,
  	  		"name":"2016123000-www.test.com",
  	  		"link":"http://log-download.cdn.qcloud.com/20161230/00/2016123000-www.selenawang.com.gz?st=XXXXXXXXXXXXXXXXXXXX&e=1483954368"
		},
		{
  	  		"date":2016-12-30,
  	  		"type":1,
  	  		"name":"2016123001-www.test.com",
  	  		"link":"http://log-download.cdn.qcloud.com/20161230/01/2016123001-www.test.com.gz?st=XXXXXXXXXXXXXXXXX&e=1483954368"
		},
      ...
	]
  }
}
```







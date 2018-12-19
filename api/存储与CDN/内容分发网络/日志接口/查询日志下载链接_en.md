## 1. API Description

This API (GenerateLogList) is used to query the log download links of specified domain names within the specified time range. You can only query one domain at a time.

Domain name for API request:<font style="color:red">cdn.api.qcloud.com</font>

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is GenerateLogList.

| Parameter Name      | Required | Type     | Description     |
| --------- | ---- | ------ | ------ |
| hostId    | Yes    | Int    | Domain ID |
| startDate | No    | String | Start time of the query  |
| endDate   | No    | String | End time of the query |



#### Note

+ You can use APIs [Query Domain Information by Domain Name](https://cloud.tencent.com/doc/api/231/3938) and [Query Domain Information](https://cloud.tencent.com/doc/api/231/3937) to obtain the ID of the host;
+ StartDate and endDate shall be no later than or equal to the current date;
+ If the startDate and endDate are empty, the default query range is 30 days before the current time. One log download link is provided per hour. For more log description, refer to [Log Download](https://cloud.tencent.com/doc/product/228/6316);
+ startDate indicates the start date of the query, and endDate indicates the end date of the query. Assuming startDate=20160813 and endDate=20160815, the log download links of three days (8-13, 8-14, and 8-15) are actually queried, 24 links per day;
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

> hostId: 1234



### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GenerateLogList
&SecretId=XXXXXXXXXXXXXXXXX
&Timestamp=1462430812
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&hostId=1234
```



### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GenerateLogList',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462865760,
  'Nonce' => 1058191224,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'hostId' => '1234'
)
```





### 4.4 Example of Returned Result

```json
{
  "code":0,
  "message":"",
  "codeDesc": "Success",
  "data":{
    "now":1461064041,
    "list":[
  		{
  	  		"date":2016-03-20,
  	  		"type":1,
  	  		"name":"2016032000-www.test.com",
  	  		"link":"http://log-download.cdn.qcloud.com/20160320/2016032000-www.test.com.gz?st=XXXXXXXXXXXXXXXXX&e=1461928041"
		},
		{
  	  		"date":2016-03-20,
  	  		"type":1,
  	  		"name":"2016032001-www.test.com",
  	  		"link":"http://log-download.cdn.qcloud.com/20160320/2016032001-www.test.com.gz?st=XXXXXXXXXXXXXXXXX&e=1461928042"
		},
      ...
	]
  }
}
```




### 1. API Description

- **API**
This API (**Get_BillingBandwidth**) is used to query billing bandwidth data of the account.
- **URL**
URL for calling API: ` http://fcgi.video.qcloud.com/common_access`


### 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| APPID | Customer ID | Int | LVB APPID used for identifying customers | Y | 
| interface | API name | String | Get_BillingBandwidth | Y | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | Int | UNIX time stamp (decimal) | Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | String | MD5(key+t) | Y | 
| Param.n.start_time | Start time for query | Int | Time stamp | Y |
| Param.n.end_time | End time for query | Int | Time stamp | Y |
| Param.s.domain | Domain name | String | Domain name | N |
| Param.n.home_foreign | Domestic and abroad data | Uint | 0: Query both of domestic and abroad data (default)<br /> 1: Query domestic data only<br /> 2: Query abroad data only <br /> | N |
| Param.n.get_top_bd | Obtain peak bandwidth | Uint | 0: Obtain the list rather than peak bandwidth and traffic (default) <br />1: Obtain peak bandwidth and traffic | N |


### 3. Output Parameters
| Parameter Name | Description | Type | Remarks            |
|---------|---------|---------|------------------|
| ret | Error code | Int | 0: Successful; other values: Failed |
| message | Error message | String | Error description |	
| output | Message content | Array | None |

"output" is composed as follows:

| Field Name | Description | Type | Remarks |
|---------|---------|---------|------------------|
| total_info | Statistics for total billing bandwidth | Array | The granularity is 5 minutes. |
| domain | Domain name | String | Available only after input parameters are passed |

"total_info" is composed as follows:

| Field Name | Description | Type | Remarks |
|---------|---------|---------|------------------|
| time | Statistical time | String | |	
| bandwidth | Bandwidth | Double | Mbps |
| flux | Traffic | Double | MB |


### 4. Example
To query the billing bandwidth data of the account

| Component | Example |
|-------------|------------------|
| API URL |` statcgi.video.qcloud.com/common_access?` |
| interface | Get_BillingBandwidth |
| Param.s.end_time | 2016-12-10 01:00:00 |
| Param.s.start_time | 2016-12-10 00:00:00 |
| Param.n.home_foreign | 1 |
| cmd | N |
| t | 1471850187 |
| sign | b17971b51ba0fe5916ddcd96692e9fb3 |


```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
URL = http://fcgi.video.qcloud.com/common_access?
			&interface=Get_BillingBandwidth
			&cmd=N
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
			&Param.s.start_time=2016-12-10 00:00:00
			&Param.s.end_time=2016-12-10 01:00:00
```
		


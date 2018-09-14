### 1. API Description

- **API**
  **Get_BillingBandwidth**: This API is used to query billing bandwidth data of accounts.
- **URL**
  URL for calling API: ` http://statcgi.video.qcloud.com/common_access`

- Backend configuration is required to use the API. To call the API, contact Tencent service personnel or [submit a ticket](https://console.cloud.tencent.com/workorder/category). Tel: 4009-100-100.

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
| -------------------- | ------------------------------------------------------------ | ------ | ------------------------------------------------------------ | -------- |
| cmd		       | Business appid | Enter the LVB appid, which is used to identify different customers | Y	       |
| interface                 | API name   | string |  Get_BillingBandwidth  |  Y          |
| t                    | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int    | UNIX timestamp (decimal) | Y        |
| sign                 | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y |
| Param.n.start_time   | Start time for the query                                                 | int    | Timestamp                                                       | Y        |
| Param.n.end_time     | End time for the query                                                 | int    | Timestamp                                                       | Y        |
| Param.s.domain       | Domain name                                                         | string | Domain name                                                         | N        |
| Param.n.home_foreign | Domestic and abroad data | uint   | 0: Query total data despite of domestic or abroad (default) <br /> 1: Query domestic data only <br /> 2: Query abroad data only <br /> | N        |
| Param.n.get_top_bd   | Obtain peak bandwidth | Uint   | 0: Obtain the list instead of peak bandwidth and traffic (default) <br />1: Obtain peak bandwidth and traffic	| N        |


### 3. Output Parameters
| Parameter Name | Description | Type | Note |
| ------- | -------- | ------ | ------------------------- |
| ret     | Error code | int    | 0: Successful. Other values: Failed |
| message | Error message | string | Error description |
| output  | Message content | array  | None                        |

"output" is composed as follows:

| Field Name | Description | Type | Note |
| ---------- | ------------------ | ------ | ------------ |
| total_info | Statistics information for total billing bandwidth | array  | Granularity of 5 minutes |
| domain     | Domain name               | string | Available only after input parameters are passed |

"total_info" is composed as follows:

| Field Name | Description | Type | Note |
| --------- | -------- | ------ | ---- |
| time      |Statistical time | string |      |
| bandwidth | Bandwidth     | double | Mbps |
| flux      | Traffic     | double | MB   |


### 4. Example
Purpose: To query the billing bandwidth data of accounts.

| Component | Example |
| -------------------- | ------------------------------------------ |
| API URL | ` statcgi.video.qcloud.com/common_access?` |
|cmd		       | 1251059556				    |
| interface            | Get_BillingBandwidth                       |
| Param.n.start_time     | 1481299200                       |
| Param.n.end_time   | 1481302800                      |
| Param.n.home_foreign | 1                                          |
| Param.s.domain      | 8888.liveplay.myqcloud.com                         |
| t                    | 1471850187                                 |
| sign                 | b17971b51ba0fe5916ddcd96692e9fb3           |


```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "appid is invalid".
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1251059556
			&interface=Get_BillingBandwidth
			&Param.s.domain=8888.liveplay.myqcloud.com 
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
			&Param.n.start_time=1481299200
			&Param.n.end_time=1481302800
```


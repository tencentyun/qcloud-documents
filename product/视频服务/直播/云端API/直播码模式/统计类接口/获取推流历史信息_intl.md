### 1. API Description
- **API**
This API (**Get_LivePushStatHistory**) is used to obtain the historical statistics of push.
- **URL**
URL for calling API: `http://statcgi.video.qcloud.com/common_access`
- **Note**
Used to obtain the push information for specified time period.
The push statistics is updated every 5 seconds. 
- Backend configuration is required to use the API. To call the API, contact Tencent service personnel or [submit a ticket](https://console.cloud.tencent.com/workorder/category). Tel: 4009-100-100.

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|cmd	| Business APPID |int|	To apply for a configuration, contact Tencent's service personnel or [submit a ticket](https://console.cloud.tencent.com/workorder/category). Tel: 4009-100-100 |	Y|
|interface|	API name |	string|	|	Y|
|t|	Expiration timestamp |	int|		|Y|
|sign|Signature |	string	|md5 (key+expiration timestamp) |	Y|
|Param.n.start_time|	Start time for the query |int	|Limited to the last 3 days from the timestamp |	Y|
|Param.n.end_time	|End time for the query	|int|	It is recommended to limit the time span for query between start and end times to 2 hours |	Y|
|Param.s.stream_id| Steam ID |string	||	Y|


### 3. Output Parameters
| Parameter Name | Description | Type | Remarks            | Note |
|---------|---------|---------|------------------|--------------|
| ret      | Error code |   int  | 0: Successful; other values: Failed. ||
| message | Error message |    string  | Error message ||
| output | Message content |   array  | For more information, please see the description below. | <br>|

"output" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
|stream_info|	Statistics of the time stream of push	| list	| Array (list) ||	

"stream_info" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
|time	|Time when push starts	|string	|||	
|client_ip| Push client IP |string	|||	
|server_ip	|IP of the server that receives the stream |	string|||		
|fps	| Frame rate of the push |int	|||
|speed|	Bitrate of the push |	int	|| In bps |

### 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component | Example |
|-------------|------------------|
| API URL | `http://statcgi.video.qcloud.com/common_access?` |
|cmd       | 1234 |
|interface       | Get_LivePushStatHistory |
|Param.n.start_time|1453279831|
|Param.n.end_time |1453279835 |
|Param.s.stream_id | 1234_xxx |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "cmd is invalid".
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Get_LivePushStatHistory
			&Param.n.start_time =1453279831
			&Param.n.end_time =1453279835
			&Param.s.stream_id =1234_xxx
			&t=1471850187
                        &sign=b17971b51ba0fe5916ddcd96692e9fb3

```

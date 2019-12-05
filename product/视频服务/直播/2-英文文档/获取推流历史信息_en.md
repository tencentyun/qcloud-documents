
## 1. API Description

- **API**
  - **Get_LivePushStatHistory**: This API is used to obtain the history of push.

- **URL**
  - URL for calling API: `http://statcgi.video.qcloud.com/common_access`

- **Note**
  - Can be used to obtain the push information for specified time period.
  - The push statistics is updated every 5 seconds.
  
- **Backend configuration is needed to use the API. To call the API, contact Tencent service personnel or submit a ticket. Tel: 4009-100-100**

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| cmd	| Business ID	| int |	To apply for a configuration, contact Tencent service personnel or submit a ticket. Tel: 4009-100-100 |	Y |
| interface |	API name |	string |	|	Y |
| t |	Validity period (time stamp) |	int |		| Y |
| sign |	Signature |	string | md5 (key+validity time stamp) |	Y |
| Param.n.start_time |	Start time for the query |	int	| Limited to the last 3 days |	Y |
| Param.n.end_time	| End time for the query	| int |	It is recommended to limit the time span for query between start and end times to 2 hours |	Y |
| Param.s.stream_id |	Stream ID	| string	||	Y |


## 3. Output Parameters
| Parameter Name | Description | Type | Remarks            | Note |
|---------|---------|---------|------------------|--------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed ||
| message | Error message |   string  |  Error message ||
| output | Message content |   array  |  See below ||

"output" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
| stream_info |	Statistics of the time stream of push	| list	| Array (list) ||	

"stream_info" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
| time	| Time when push starts	| string	|||	
| client_ip | Push client IP	| string	|||	
| server_ip	| Receiving server IP |	string |||		
| fps	| Frame rate of the push	| int	|||
| speed |	Bitrate of the push |	int	|| Unit: bps |

## 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component |   Example           |
|-------------|------------------|
| API URL | http://statcgi.video.qcloud.com/common_access? |
|cmd       | 1234 |
| interface       | Get_LivePushStatHistory |
|Param.n.start_time|1453279831|
| Param.n.end_time | 1453279835 |
|Param.s.stream_id | 1234_xxx |
| t | 1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "cmd is invalid".
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Get_LivePushStatHistory
			&Param.n.start_time =1453279831
			&Param.n.end_time =1453279835
			&Param.s.stream_id =1234_xxx
			&t=1471850187
                        &sign=b17971b51ba0fe5916ddcd96692e9fb3

```
			


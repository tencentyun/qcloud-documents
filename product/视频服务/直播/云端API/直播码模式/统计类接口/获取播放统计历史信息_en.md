
## 1. API Description

- **API**
  - **Get_LivePlayStatHistory**: This API is used to obtain the historical statistics of playback.

- **URL**
  - URL for calling API:` http://statcgi.video.qcloud.com/common_access`

- **Note**
  - Used to obtain the playback information for specified time period.
  - The playback statistics is updated every 1 minute.
  
- **Backend configuration is needed to use the API. To call the API, contact Tencent service personnel or submit a ticket. Tel: 4009-100-100**
   

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| cmd	| Business ID	| int |	To apply for a configuration, contact Tencent service personnel or submit a ticket. Tel: 4009-100-100 |	Y |
| interface |	API name |	string |	|	Y |
| t |	Validity period (time stamp) |	int |		| Y |
| sign |	Signature |	string | md5 (key+validity time stamp) |	Y |
| Param.n.start_time |	Start time for the query |	int	| Limited to the last 15 days from the time stamp |	Y |
| Param.n.end_time	| End time	| int |	It is recommended to limit the time stamp between start and end times to 2 hours |	Y |
| Param.s.stream_id |	Stream ID	| string |	If it is left empty, total bandwidth is obtained |	N |
| Param.s.domain	| Domain name	| String |	If it is left empty, all the data under the appid is obtained. <br>The original playback domain name before cname is required	| N |


## 3. Output Parameters
| Parameter Name | Description | Type | Remarks            | Note |
|---------|---------|---------|------------------|--------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed || 
| message | Error message |   string  |  Error message ||
| output | Message content |   array  |  See below ||

"output" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
| stat_info |	LVB stream statistics	| array		|||
| sum_info	| Traffic and summation information |	array	||	Required output parameter |
| domain	| Domain name	| string	||	Optional output parameter |
| stream_id |	Stream ID |	string ||		Optional output parameter |	

"stream_info" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
| time	| Statistical time |	string |||		
||bandwidth	| Bandwidth |	double	|| in Mbps ||
| online |	Number of online users |	int	|||	
| flux	| Traffic |	double || in MB |

"sum_info" (summation) is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
| sum_flux	| Traffic summation |	double	| Required output parameter | in MB |	

## 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component |   Example           |
|-------------|------------------|
| API URL | http://statcgi.video.qcloud.com/common_access? |
|cmd       | 1234 |
| interface       | Get_LivePlayStatHistory |
|Param.n.start_time |1453279831|
| Param.n.end_time | 1453279835 |
|Param.s.stream_id | 1234_xxx |
| Param.s.domain | www.123test.com |
|t |1471850187 |
| sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "cmd is invalid".
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Get_LivePlayStatHistory
			&Param.n.start_time =1453279831
			&Param.n.end_time =1453279835
			&Param.s.stream_id =1234_xxx
                        &Param.s.domain=www.123test.com
			&t=1471850187
      &sign=b17971b51ba0fe5916ddcd96692e9fb3

```
			


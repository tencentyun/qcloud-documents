
### 1. API Description
- **API**
This API (**Get_LivePlayStatHistory**) is used to obtain the historical statistics of playback.
- **URL**
URL for calling API: `http://statcgi.video.qcloud.com/common_access`
- **Note**
Used to obtain the playback information for specified time period.
The playback statistics is updated every 1 minute.
- Backend configuration is required to use the API. To call the API, contact Tencent service personnel or [submit a ticket](https://console.cloud.tencent.com/workorder/category). Tel: 4009-100-100.
   

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|cmd	| Business ID |int|	To apply for a configuration, contact Tencent's service personnel or [submit a ticket](https://console.cloud.tencent.com/workorder/category). Tel: 4009-100-100 |	Y|
|interface|	API name |	string|	|	Y|
|t|	Expiration timestamp |	int|		|Y|
|sign|Signature |	string	|md5 (key+expiration timestamp) |	Y|
|Param.n.start_time|Start time for the query |	int	|Limited to the last 15 days from the timestamp |	Y|
|Param.n.end_time	| End time	| int|	It is recommended to limit the timestamp between start and end times to 2 hours |	Y|
|Param.s.stream_id|	Steam ID	|string|	If it is left empty, the total bandwidth is obtained |	N|
|Param.s.domain	|Domain name	|String|	If it is left empty, all the data under the APPID is obtained. The original playback domain name before cname is required	|N|


### 3. Output Parameters
| Parameter Name | Description | Type | Remarks            | Note |
|---------|---------|---------|------------------|--------------|
| ret      | Error code |   int  | 0: Successful; other values: Failed. ||
| message | Error message |    string  | Error message ||
| output | Message content | array |  For more information, please see the description below. | - |

"output" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
|stat_info| Statistics for the LVB stream |array		|||
|sum_info	| Traffic and summation information |	array	||	Required output parameter |
|domain	| Domain Name	|string	||	Optional output parameter |
|stream_id|	Steam ID |	string||		Optional output parameter |	

"stat_info" is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
|time	|Statistical time |	string|||		
|bandwidth	|Bandwidth |	double	|| In Mbps |
|online|	Number of online users |	int	|||	
|flux	|Traffic |	double|| In MB |

"sum_info" (summary) is composed as follows:

| Parameter Name | Description | Type | Remarks                 | Note |
|---------|---------|---------|------------------|--------------|
|sum_flux	| Traffic summation |	double	|Required output parameter | In MB |	

### 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component | Example |
|-------------|------------------|
| API URL |`http://statcgi.video.qcloud.com/common_access?`|
|cmd       | 1234 |
|interface       | Get_LivePlayStatHistory |
|Param.n.start_time |1453279831|
|Param.n.end_time |1453279835 |
|Param.s.stream_id | 1234_xxx |
|Param.s.domain|www.123test.com|
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "cmd is invalid".
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Get_LivePlayStatHistory
			&Param.n.start_time =1453279831
			&Param.n.end_time =1453279835
			&Param.s.stream_id =1234_xxx
                        &Param.s.domain=www.123test.com
			&t=1471850187
      &sign=b17971b51ba0fe5916ddcd96692e9fb3

```			

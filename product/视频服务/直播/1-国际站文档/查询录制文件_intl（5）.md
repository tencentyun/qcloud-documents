### 1. API Description

- **API**
**Live_Tape_GetFilelist**: This API is used to query the recorded files generated in a certain LVB stream during a certain period of time.
- **URL**
URL for calling API: ` http://fcgi.video.qcloud.com/common_access`
- **Note**
You cannot determine when to call the API due to the uncertainty of the file generation time. Therefore, you are recommended to use [Passive Event Notification](https://cloud.tencent.com/doc/api/258/5957) (event_type = 100) mechanism.

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|APPID                       | Customer ID | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name | string | For example: Get_LivePushStat |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX timestamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | LVB Code | string | | Y|
| Param.n.page_no   | Page number | int  | Starts from 1. Default value is 1 | N |
| Param.n.page_size | Page size | int | 1-100. Default is 10 | N |
|Param.s.sort_type  | Sorting method | string| "asc" indicates ascending order, and "desc" indicates descending order. Default is "asc". |N|
|Param.s.start_time | Start time for the query | string| Format is: 2016-12-10 00:00:00 |N|
| Param.s.end_time | End time for the query | string| Format: 2016-12-10 00:00:00. The end time must be less than 24 hours later than the start time in the same day |N|
>**Note:**
> For historical reasons, the LVB Code parameter was defined as channel_id in some earlier APIs, and is defined as stream_id in new APIs.

### 3. Output Parameters
| Parameter Name | Description | Type | Note |
|---------|---------|---------|------------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed. |
| message | Error message |   string  | Error message |
| output | Message content |   array  | For more information, please see the description below. |

"output" is composed as follows:

| Field Name | Description | Type | Note |
|---------|---------|---------|------------------|
| all_count | Number of fragments |   int      |    |
| file_list    | Information of the fragment |   array  | For more information, please see the description below. |

"file_list" is composed as follows:

| Field Name | Description | Type | Note |
|---------|---------|---------|------------------|
| vid | vid of the VOD file | string | "record_file_url" is used if the field is left empty. |
| start_time   | Start time of the fragment |   string  | The time cannot be accurate to seconds due to interference of the I frame position |
| end_time    | End time of the fragment |   string  | The time cannot be accurate to seconds due to interference of the I frame position |
| file_id | ID of the VOD file | string | This parameter is required to obtain playback URL with VOD API |
| record_file_url | Playback address | string |This field is used as the address. If left empty, the address will be the vid which is assembled based on assembly format |
>**Note:**
>vid assembly format (URL format for video fragment recording requests): `http://(VODbizid).vod.myqcloud.com/(vid).f0.flv` 

### 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component |   Example           |
|-------------|------------------|
| API URL |` http://fcgi.video.qcloud.com/common_access?` |
|APPID       | 1234 |
|interface       | Live_Tape_GetFilelist |
|Param.s.channel_id | 8888_test123 |
|Param.n.page_no | 1 |
|Param.n.page_size | 20 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "appid is invalid".
URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Tape_GetFilelist
			&Param.s.channel_id=8888_test123
			&Param.n.page_no=1
			&Param.n.page_size=20
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
			&Param.s.start_time=2016-12-10 00:00:00
			&Param.s.end_time=2016-12-10 01:00:00
```
			







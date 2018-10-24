
## 1. API Description

- **API**
  - **Live_Tape_GetFilelist**: This API is used to query recording files generated in a certain LVB stream during a certain period of time.

- **URL**
  - URL for calling API:` http://fcgi.video.qcloud.com/common_access`

- **Note**
  - You are unaware of the exact file generation time so you cannot properly determine when to call such active query APIs. Therefore, it is recommended that you use [Passive Event Notification](https://cloud.tencent.com/doc/api/258/5957) (event_type = 100) mechanism.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid                        | Customer ID     | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name   | string |  such as: Get_LivePushStat  |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int  | UNIX time stamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | string | MD5 (key + t) | Y | 
| Param.s.channel_id | LVB code | string | | Y |
| Param.n.page_no   | Page number  | int  | The value starts from 1. Default value is 1 | N |
| Param.n.page_size | Page size | int   | 1-100. Default value is 10  | N |
| Param.s.sort_type  | Sorting order | string | "asc" indicates ascending, "desc" indicates descending | N |
| Param.s.start_time | Start time of the query | string | Format: 2016-12-10 00:00:00 | N |
| Param.s.end_time   | End time of the query | string | Format: 2016-12-10 00:00:00 | N |
> For historical reasons, the LVB Code parameter was defined as channel_id in some earlier APIs, and is defined as stream_id in new APIs.

## 3. Output Parameters
| Parameter Name | Description | Type | Remarks            |
|---------|---------|---------|------------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed |
| message | Error message |   string  |  Error message |
| output | Message content |   array  |  See below |

"output" is composed as follows:

| Field Name | Description | Type | Remarks                 |
|---------|---------|---------|------------------|
| all_count | Total number of parts    |   int      |    |
| file_list    | File information of the part |   array  | See below  |

"file_list" is composed as follows:

| Field Name | Description | Type | Remarks                 |
|---------|---------|---------|------------------|
| vid | vid of the VOD    |  string      | record_file_url will be used if the field is left empty |
| start_time   | Start time of the part |   string  |   The time cannot be accurate to seconds due to interference of the I frame position |
| end_time    | End time of the part |   string  |  The time cannot be accurate to seconds due to interference of the I frame position  |
| file_id        | VOD file_id     |   string  |  This parameter is required when you use the VOD API to exchange for playback URL |
| record_file_url | Playback address | string | This field is used as the address. If left empty, the address will be the vid which is assembled based on assembly format  |
**vid assembly format: URL format for video part recording requests: `http://(VOD bizid).vod.myqcloud.com/(vid).f0.flv` **

 
## 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component |   Example           |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|appid       | 1234 |
|interface       | Live_Tape_GetFilelist |
|Param.s.channel_id | 8888_test123 |
|Param.n.page_no | 1 |
|Param.n.page_size | 20 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Tape_GetFilelist
			&Param.s.channel_id=8888_test123
			&Param.n.page_no=1
			&Param.n.page_size=20
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
			&Param.s.start_time=2016-12-10 00:00:00
			&Param.s.end_time=2016-12-10 01:00:00
```
			







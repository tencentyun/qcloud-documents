
## 1. API Description

- **API**
  - **Live_Tape_Start**: This API is used to create a recording task`.

- **URL**
  - URL for calling API:` http://fcgi.video.qcloud.com/common_access`

- **Note**
  - Create a recording task. This API supports two recording modes: Scheduled Recording and Real-time Recording. In Scheduled Recording, importing start time of task is needed, which may cause the missing of wonderful moments in a video. In Real-time Recording, recording is synchronous with playback of video, making it possible to capture all of the marvelous moments in a video. Interface timeout should be greater than 3 seconds.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid                       | Customer ID     | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name   | string |  such as: Get_LivePushStat  |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int  | UNIX time stamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | string | MD5 (key + t) | Y | 
| Param.s.channel_id | Channel ID | string | | Yes |
| Param.s.start_time  | Start time of task | string  | Standard date_time which needs urlencode, such as: 2017-01-01%2010:10:01 | Y |
| Param.s.end_time | End time of task | string   | Standard date_time which needs urlencode, such as: 2017-01-01%2010:10:01. | Y |
| Param.n.task_sub_type  | Whether to enable real-time recording | int| Default is 0, and 1 means enabling real-time recording. <br>(1) If real-time recording is enabled, the video recording starts at the moment when you call this API. In this case, the input parameter of task start time is invalid. <br>(2) When real-time recording is enabled, if the end time of task is input, the recording ends at this end time. | N |


## 3. Output Parameters
| Parameter Name | Description | Type | Remarks           |
|---------|---------|---------|------------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed |
| message | Error message |   string  |  Error message |
| output | Message content |   array  |  See below |

"output" is composed as follows:

| Field Name | Description | Type | Remarks                 |
|---------|---------|---------|------------------|
| task_id | Task ID    |   int      |  64 bit unsigned integer  |

 
## 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component |   Example           |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|appid       | 1234 |
|interface       | Live_Tape_Start |
|Param.s.channel_id | 8888_test123 |
| Param.s.start_time  | Start time of task. It is a standard date_time which needs urlencode |
| Param.s.end_time| End time of task |
|t |1471850187 |
| sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Tape_Start
			&Param.s.channel_id=8888_test123
			&Param.s.start_time=2017-05-20+10%3a00%3a00
			&Param.s.end_time=2017-05-20+10%3a30%3a00
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
Note: &Param.s.start_time and &Param.s.end_time need to be encoded. After being encoded, 2017-05-20 10:00:00 is converted to 2017-05-20+10%3a00%3a00, and 2017-05-20 10:30:00 to 2017-05-20+10%3a30%3a00.
```
			


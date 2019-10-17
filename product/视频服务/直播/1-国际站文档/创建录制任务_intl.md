### 1. API Description
- **API**
**Live_Tape_Start**: This API is used to create a recording task.
- **URL**
URL for calling API: `http://fcgi.video.qcloud.com/common_access`
- **Note**
Recorded files are stored on the VOD platform. If you want to use the recording feature, you need to activate the VOD service. When recording files are stored, the charges (including charges for storage and downstream playback traffic) are calculated with VOD billing method. For more information, please see [relevant document](https://cloud.tencent.com/doc/product/266/%E4%BB%B7%E6%A0%BC%E6%80%BB%E8%A7%88).
Create a recording task. This API supports two recording modes: Scheduled Recording and Real-time Recording. In Scheduled Recording, importing the start time of a task is needed, which may cause the missing of wonderful moments in a video. In Real-time Recording, recording is synchronous with playback of a video, making it possible to capture all of the marvelous moments in a video. Note: The timeout for calling this API should be greater than 3 seconds.

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
| appid | Customer ID | int | LVB appid used for identifying customers | Y | 
| interface                 | API name |  string |  Live_Tape_Start  |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) |  int  | UNIX timestamp (decimal) |   Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | Channel ID |  string | | Y|
| Param.s.start_time  | Start time of task |  string  | Standard date_time which needs urlencode, such as: 2017-01-01%2010:10:01. |  Y|
| Param.s.end_time | End time of task | string | Standard date_time which needs urlencode, such as: 2017-01-01%2010:10:01. |  Y |
|Param.n.task_sub_type  | Whether to enable real-time recording |  int| Only real-time recording is supported. Default is 1. <br>(1) The creation of real-time video recording depends on the VJ's active pushing. The recording starts as soon as the API is called successfully. In this case, the input parameter of task start time is invalid. <br>(2) When real-time recording is enabled, if the end time of task is input, the recording ends at this end time. If no end time is input, the recording automatically ends after 30 minutes. <br>(3) If the difference between the start time of recording and the input end time of recording exceeds 30 minutes, the recording ends automatically after 30 minutes. It is recommend to limit the duration of real-time recording to 5 minutes on console. | N|
|Param.s.file_format | Format of recorded files | string| Available values include flv (default), hls, mp4, and aac | N|
|Param.s.record_type|Type of recorded files | string| Default is video<br>When record_type is "video", file_format can be "flv", "hls", or "mp4"<br>When record_type is "audio", file_format can be "aac", "flv", "hls", or "mp4" | N|


### 3. Output Parameters
| Parameter Name | Description | Type | Note |
|---------|---------|---------|------------------|
| ret      | Error code |    int  | 0: Successful; other values: Failed. |
| message | Error message |    string  | Error message |
| output | Message content |    array  | For more information, please see the description below. |

"output" is composed as follows:

| Field Name | Description | Type | Note |
|---------|---------|---------|------------------|
| task_id | Task ID | int | 64-digit unsigned integer<br> |

 
### 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component | Example |
|-------------|------------------|
| API URL |  `http://fcgi.video.qcloud.com/common_access?` |
|appid       | 1234 |
|interface       | Live_Tape_Start |
|Param.s.channel_id | 8888_test123 |
|Param.s.start_time | Start time of task. Standard date_time which needs urlencode |
|Param.s.end_time| End time of the task |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "appid is invalid".
URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Tape_Start
			&Param.s.channel_id=8888_test123
			&Param.s.start_time=2017-05-20+10%3a00%3a00
			&Param.s.end_time=2017-05-20+10%3a30%3a00
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
Note: Param.s.start_time and Param.s.end_time need to be encoded. After being encoded, 2017-05-20 10:00:00 is converted to 2017-05-20+10%3a00%3a00, and 2017-05-20 10:30:00 to 2017-05-20+10%3a30%3a00.
```
			


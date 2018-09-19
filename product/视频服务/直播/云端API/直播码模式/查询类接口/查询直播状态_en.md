
## 1. API Description
- **API**
  - **Live_Channel_GetStatus**: This API is used to query whether a stream has a status of *Broadcasting**.

- **URL**
  - URL for calling API:` http://fcgi.video.qcloud.com/common_access`

- **Use**
  - To query whether a stream has a status of **Broadcasting**. It is implemented based on Tencent Cloud's detection of audio/video stream interruption, and thus may not be as fast and accurate as the active reporting of App in terms of real-time capability. But it can serve as a good supplementary means for checking and clearing up LVB streams regularly.

- **Note**
  - If the push LVB Code to be queried is never used to push streams, the 20601 error code is returned.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid                       | Customer ID     | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name   | string |  such as: Get_LivePushStat  |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int  | UNIX time stamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | string | MD5 (key + t) | Y | 
| Param.s.channel_id | LVB Code      | string | A single LVB stream can be queried at one time      | Y           |

> For historical reasons, the LVB Code parameter was defined as channel_id in some earlier APIs, and is defined as stream_id in new APIs.

## 3. Output Parameters
| Parameter Name | Description | Type | Remarks            |
|---------|---------|---------|------------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed |
| message | Error message |   string  |  Error message |
| output | Message content |   array  |  See below |

"output" is composed as follows:

| Field name | Description | Type | Remarks            |
|---------|---------|---------|------------------|
| rate_type      | Bitrate |   int  |  0: original bitrate; 10: LD; 20: HD |
| recv_type      | Playback protocol |   int  |  1: RTMP/FLV; 2: HLS; 3: RTMP/FLV+HLS |
| status            | Status |   int  |  0: Interrupted; 1: Enabled; 3: Disabled|
 
## 4. Example

Purpose: To query whether the LVB stream with the LVB Code of 8888_test123 is in a status "Broadcasting".

| Component |   Example           |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|appid      | 1234 |
| interface       | Live_Channel_GetStatus |
|Param.s.channel_id | 8888_test123 |
| t | 1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_GetStatus
			&Param.s.channel_id=8888_test123
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```
     







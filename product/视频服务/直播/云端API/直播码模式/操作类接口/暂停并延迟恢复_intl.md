
## 1. API Description

- **API**
**channel_manager**: This API is used to stop pushing stream and delay the availability of API.
- **URL**
URL for calling API: `http://fcgi.video.qcloud.com/common_access`.
- **Purpose**
This API can be called when VJ push is not allowed for certain reasons.
- **Note**
This API is called to stop pushing a stream (which means to disable the push). To resume VJ push, you can call this API again or set a time for resuming push, and the push will be enabled at the specified time. A stream can be disabled for up to 3 months (3 months after the current time). If the suspension period is set to more than 3 months, 3 months shall prevail.

## 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
| APPID                        | Customer ID | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name | string | For example: Get_LivePushStat |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX timestamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | LVB Code | string | | Y|
| Param.n.abstime_end | The timestamp for the end time of stream suspension | int | The absolute time of stream suspension. Enter a UNIX timestamp (decimal). A stream can be disabled for up to 3 months.
| Y|
| Param.s.action|Action |string| Interrupt stream: Forbid; Resume push: Resume |Y|



## 3. Output Parameters
| Parameter Name | Description | Type | Note |
|---------|---------|---------|------------------|
| ret      | Error code |   int  | 0: Successful; other values: Failed. |
| message | Error message |   string  | Error message |
 
## 4. Example
Purpose: To ban the LVB stream with an LVB Code of 8888_test123 whose content has violated relevant regulations.

| Component | Example |
|-------------|------------------|
| API URL | `http://fcgi.video.qcloud.com/common_access?` |
|APPID       | 1234 |
|interface       | Live_Channel_SetStatus |
|Param.s.channel_id | 8888_test123 |
|Param.n.abstime_end | 1499756910 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |
|Param.s.action|resume |

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "appid is invalid".
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_SetStatus
			&Param.s.channel_id=8888_test123
			&Param.n.abstime_end=1499756910
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
                        &Param.s.actio=resume
```



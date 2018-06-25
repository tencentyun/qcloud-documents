
## 1. API Description

- **API**
  - **channel_manager**: This API is used to stop push and delay the availability of API.

- **URL**
  - URL for calling API: `http://fcgi.video.qcloud.com/common_access`

- **Use**
  - This API can be called when VJ push is not allowed for certain reasons.

- **Note**
  - This API can be called to stop pushing a stream (which means to disable the push). To resume VJ push, you can call this API again or set a time for resuming push, and the push will be enabled at the specified time.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid                        | Customer ID     | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name   | string |  such as: Get_LivePushStat  |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int  | UNIX time stamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5 (key + t) | Y | 
| Param.s.channel_id | LVB code | string | | Y |
| Param.n.abstime_end | Absolute time stamp for resuming push | int | Enter UNIX time stamp (decimal) for the absolute time for enabling the push | Y |
| Param.s.action | Action | string | Interrupt stream: Forbid; Resume push: Resume | Y |



## 3. Output Parameters
| Parameter name | Description | Type | Remarks            |
|---------|---------|---------|------------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed |
| message | Error message |   string  |  Error message |
 
## 4. Example
Purpose: To ban the LVB stream with an LVB Code of 8888_test123 whose content has violated relevant regulations.

| Component |   Example           |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|appid       | 1234 |
|interface       | Live_Channel_SetStatus |
|Param.s.channel_id | 8888_test123 |
|Param.n.abstime_end | 1000 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |
|Param.s.action|resume |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_SetStatus
			&Param.s.channel_id=8888_test123
			&Param.n.abstime_end=1000
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
                        &Param.s.actio=resume
```



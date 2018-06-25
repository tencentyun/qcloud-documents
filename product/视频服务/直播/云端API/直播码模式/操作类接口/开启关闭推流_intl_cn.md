
## 1. API Description

- **API**
  - **Live_Channel_SetStatus**: 
  This API is used to set the status of an LVB stream to: disabled, interrupted and enabled for push.** Disabled** means the stream ID is no longer available for push. During push process, the push can be interrupted and will not be restarted after interruption.** Interrupted** means the stream being pushed is interrupted and can be re-pushed after interruption. Enabled for push** means the stream ID is enabled for push.

- **URL**
  - URL for calling API: http://fcgi.video.qcloud.com/common_access

- **Use**
  - This API is used to **ban** an LVB during porn detection. For example, if a VJ is found to play porny or rebellious content, this LVB stream can be interrupted or disabled at any time.

- **Note**
  - Once an LVB stream is "disabled", Tencent Cloud actively disconnects the push linkage and rejects subsequent push requests.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid                        | Customer ID     | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name   | string |  Live_Channel_SetStatus |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int  | UNIX time stamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | string | MD5 (key + t) | Y | 
| Param.s.channel_id | LVB code | string | | Y |
| Param.n.status | Status | int | 0: Disabled; 1: Enabled for push; 2: Interrupted | Y |

> For historical reasons, the LVB Code parameter was defined as channel_id in some earlier APIs, and is defined as stream_id in new APIs.

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
|Param.n.status | 0 |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_SetStatus
			&Param.s.channel_id=8888_test123
			&Param.n.status=0
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```









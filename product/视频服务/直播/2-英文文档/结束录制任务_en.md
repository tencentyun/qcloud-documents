
## 1. API Description

- **API**
  - **Live_Tape_Stop**: This API is used to end a recording task.

- **URL**
  - URL for calling API: `http://fcgi.video.qcloud.com/common_access`

- **Note**
  - End recording task.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid                       | Customer ID     | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name   | string |  such as: Get_LivePushStat  |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int  | UNIX time stamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | string | MD5 (key + t) | Y | 
| Param.s.channel_id | Channel ID | string | | Yes |
| Param.s.task_id  | Task ID  | string  |  | Y |
| Param.n.task_sub_type  | Whether to enable real-time recording | int| Default is 0, and 1 means enabling Mini LVB recording | N |


## 3. Output Parameters
| Parameter Name | Description | Type | Remarks            |
|---------|---------|---------|------------------|
| ret      | Error code |   int  |  0: Successful; other values: Failed |
| message | Error message |   string  |  Error message |



 
## 4. Example
Purpose: To query the list of files recorded during the LVB for the LVB stream with an LVB Code of 8888_test123.

| Component |   Example           |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|appid       | 1234 |
|interface       | Live_Tape_Stop |
|Param.s.channel_id | 8888_test123 |
|Param.n.task_id  | 123|
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Tape_Stop
			&Param.s.channel_id=8888_test123
			&Param.n.task_id=123
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```
			


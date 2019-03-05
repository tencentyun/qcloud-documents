### 1. API Description
- **API**
**Live_Channel_GetLiveChannelList**: This API is used to query channel list.
- **URL**
URL for calling API: `http://fcgi.video.qcloud.com/common_access`
- **Purpose**
To query channel list for LVB in LVB Code mode.

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|APPID|Customer ID |int||Y|
|interface|API name |string | |Y|
|t|Expiration time stamp |int||Y|
|sign|Signature |string|md5(key+expiration time stamp) |Y|

### 3. Output Parameters
| Parameter Name | Description | Type | Note |
|---------|---------|---------|-----------|
| ret      | Error code |   int  | 0: Successful. Other values: Failed |
| message | Error message |   string  | Error description |
|output|Message content |  array  |     | | 

"output" is composed as follows:

| Field Name | Description | Type | Note |
|---------|---------|---------|---------|
| all_count | Total number |   int      |    |
| channel_list | List | array | | |

"channel_list" is composed as follows:

| Parameter Name | Description | Type | Note |
|---------|---------|---------|---------|
| channel_id | LVB Code ID | string | | |

### 4. Example
Purpose: To query the channel list in LVB under the account.

| Component | Example |
|-------------|------------------|
| API URL |` http://fcgi.video.qcloud.com/common_access?`|

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "appid is invalid".
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_GetChannelList
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```


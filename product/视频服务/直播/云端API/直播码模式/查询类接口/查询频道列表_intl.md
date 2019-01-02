### 1. API Description
- **API**
**Live_Channel_GetChannelList**: This API is used to query channel list.
- **URL**
URL for calling API: `http://fcgi.video.qcloud.com/common_access`
- **Purpose**
To query the current channel list in LVB Code mode.
- **Note**
You can query a list of channels with a certain status, such as channels that are active.

### 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|APPID|Customer ID |int||Y|
|interface|API name |string | |Y|
|t|Expiration time stamp |int||Y|
|sign|Signature |string|md5(key+expiration time stamp) |Y|
| Param.n.status | 0: stream interrupted; 1: enabled; 3: disabled | int  | Filter is not used by default | N | 
|Param.n.page_no| Page number | int | Starts from 1. Default value is 1 |  N   | 
| Param.n.page_size | Page size | int  | 10-100. Default is 10 |  N | 
| Param.s.order_field| Sorting field | string |Available value: create_time. Default is create_time. | N | 
| Param.n.order_type | Sorting method |  int |0 indicates ascending order. 1 indicates descending order. | N|

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
| channel_id | LVB Code ID  | string | | |

### 4. Example
Purpose: Query the list of active channels under the account

| Component | Example |
|-------------|------------------|
| API URL | `http://fcgi.video.qcloud.com/common_access?` |
|Param.n.status      | 1 |
|Param.n.page_no       | 1 |
|Param.n.page_size | 20|
|Param.s.order_field | create_time |
|Param.n.order_type |0 |


```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "appid is invalid".
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_GetChannelList
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
			&Param.n.status=1&Param.n.page_no=1&Param.n.page_size=20
			&Param.s.order_field=create_time&Param.n.order_type=0
```




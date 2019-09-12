
## 1. API Description

- **API**
  - **Live_Channel_GetChannelList**: This API is used to query channel list.

- **URL**
  - URL for calling API: `http://fcgi.video.qcloud.com/common_access`

- **Use**
  - Used to query the current channel list in LVB code mode.

- **Note**
  - You can query a list of channels with a certain status, such as channels that are currently active.

## 2. Input Parameters

| Parameter Name | Description | Type | Remarks | Required |
|---------|---------|---------|---------|---------|
| appid | Customer ID | int || Y |
| interface | API name | string | | Y |
| t | Validity period (time stamp) | int || Y |
| sign | Signature | string | md5 (key+end-of-validity period time stamp) | Y |
| Param.n.status | 0: interrupted; 1: enabled; 3: disabled   | int  | Filter is not used by default |  N   | 
| Param.n.page_no | Page number   | int |  The value starts from 1 and the default value is 1  |  N   | 
| Param.n.page_size | Page size | int  | 10-100. Default value is 10 |  N | 
| Param.s.order_field | Field used for sorting | string | Available field: create_time. Default is create_time | N | 
| Param.n.order_type | Sorting order | int | 0: ascending; 1: descending | N |


## 3. Output Parameters
| Parameter name | Description | Type | Remarks            |
|---------|---------|---------|-----------|
| ret      | Error code |   int  |  0: Successful; other values: Failed |
| message | Error message |   string  |  Error description |
| output | Message content |  array  |     | | 

"output" is composed as follows:

| Field Name | Description | Type | Note  |
|---------|---------|---------|---------|
| all_count | Total number of channels   |   int      |    |
| channel_list    | List |   array  |    |     |

"channel_list" is composed as follows:

| Parameter Name | Description | Type | Remarks |
|---------|---------|---------|---------|
| channel_id | LVB code ID  |    string |     |    |

 
## 4. Example
Purpose: To query the list of active channels under the account

| Component |   Example           |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|Param.n.status      | 1 |
| Param.n.page_no       | 1 |
|Param.n.page_size | 20|
| Param.s.order_field | create_time |
|Param.n.order_type |0 |


```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise URL construction errors may occur, such as "appid is invalid"
 URL = http://fcgi.video.qcloud.com/common_access?
			appid=1234&interface=Live_Channel_GetChannelList
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
			&Param.n.status=1&Param.n.page_no=1&Param.n.page_size=20
			&Param.s.order_field=create_time&Param.n.order_type=0
```




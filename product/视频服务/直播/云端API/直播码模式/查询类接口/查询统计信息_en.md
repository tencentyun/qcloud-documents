
## 1. API Description
- **API**
   - **Get_LiveStat**: This API is used to query the push and playback information about a specified LVB stream
   - **Get_LivePushStat**: Return only the push statistics to improve query efficiency
   - **Get_LivePlayStat**: Return only the playback statistics to improve query efficiency
- **URL**
   - URL for calling API:` http://statcgi.video.qcloud.com/common_access`
- **Use**
   - To query the statistics of an LVB stream (such as number of viewers, bandwidth, bitrate, and frame rate)
   - To query the statistics of multiple LVB streams that are currently being broadcast (paged query is recommended to avoid excessive returned data packet in each time)
- **Note**
   - The statistics are instantaneous statistics at the query time point rather than historically accumulated data.
   - If the target stream is not in LVB, the output field in the returned result is blank.
   - The push statistics are updated once every **5 seconds**, which means there's no point in querying with a interval shorter than 5 seconds.
   - The playback statistics are updated once every **1 minute**, which means there's no point in querying with a interval shorter than 60 seconds.
- **BETA**
   - The statistic API is still in Beta and is not open to all customers. If you call this API when it is not activated, you will be prompted "cmd is invalid". Contact us if there's urgent need.


## 2. Input Parameters

|        Parameter name        | Description                                     | Type     | Remarks                                       | Required |
| :---------------: | ---------------------------------------- | ------ | ---------------------------------------- | :--: |
|        cmd        | Customer ID                                     | int    | LVB APPID used for identifying customers                     |  Y   |
|     interface     | API name                                     | string | Such as: Get_LivePushStat                       |  Y   |
|         t         | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | int    | UNIX time stamp (decimal)                             |  Y   |
|       sign        | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5 ) | string | MD5 (key + t)                               |  Y   |
|  Param.n.page_no  | Page number                                     | int    | The value starts from 1 and the default value is 1                                |  N   |
| Param.n.page_size | Page size                                     | int    | 1-300. Default value is 300                             |  N   |
| Param.s.stream_id | LVB code                                      | string | If stream_id is not set, all streams that are in LVB will be queried |  N   |


## 3. Output Parameters
### Get_LiveStat
| Parameter Name | Description | Type | Remarks |
| ------- | ---- | ------ | ----------- |
| ret     | Error code  | int    | 0: Successful; other values: Failed |
| message | Error message | string | Error message        |
| output  | Message content | array  | See below        |

"output" is composed as follows:

| Field Name             | Description               | Type     | Note                 |
| --------------- | ---------------- | ------ | ------------------ |
| stream_count    | Total number of online LVB streams       | int    | 1 is returned when stream_id is specified in the request |
| stream_info     | LVB stream statistics          | array  | See below               |
| total_bandwidth | Total bandwidth for the current account upon query   | double | In Mbps            |
| total_online    | Total number of online viewers for the current account upon query | int    | Number of people               |

"stream_info" is composed as follows:

| Field Name         | Description          | Type     | Note      |
| ----------- | ----------- | ------ | ------- |
| stream_name | LVB code         | string | -       |
| bandwidth   | Instantaneous bandwidth usage of the LVB stream | double | In Mbps |
| online      | Instantaneous number of online viewers for the current LVB stream | int    | Number of people    |
| client_ip   | Push client IP    | string | -       |
| server_ip   | Receiving server IP     | string | -       |
| fps         | Instantaneous frame rate of the push       | int    | -       |
| speed       | Instantaneous bitrate of the push       | int    | bps     |

### Get_LivePushStat
The output of Get_LivePushStat is a subset of Get_LiveStat:

| Field Name         | Description         | Type    | Note                 |
| ------------ | ---------- | ----- | ------------------ |
| stream_count | Total number of online LVB streams | int    | 1 is returned when stream_id is specified in the request |
| stream_info  | LVB stream statistics    | array | See below               |

"stream_info" is composed as follows:

| Field Name         | Description         | Type    | Note                 |
| ----------- | ------- | ------ | ---- |
| stream_name | LVB code     | string | -    |
| client_ip   | Push client IP | string | -    |
| server_ip   | Receiving server IP | string | -    |
| fps         | Instantaneous frame rate of the push  | int    | -    |
| speed       | Instantaneous bitrate of the push  | int    | bps  |

### Get_LivePlayStat
The output of Get_LivePushStat is another subset of Get_LiveStat:

| Field Name             | Description               | Type     | Note                 |
| --------------- | ---------------- | ------ | ------------------ |
| stream_count    | Total number of online LVB streams       | int    | 1 is returned when stream_id is specified in the request |
| stream_info     | LVB stream statistics          | array  | See below               |
| total_bandwidth | Total bandwidth for the current account upon query   | double | In Mbps            |
| total_online    | Total number of online viewers for the current account upon query | int    | Number of people               |

"stream_info" is composed as follows:

| Field Name         | Description          | Type     | Remarks     |
| ----------- | ----------- | ------ | ------- |
| stream_name | LVB code         | string | -       |
| bandwidth   | Instantaneous bandwidth usage of the LVB stream | double | In Mbps |
| online      | Instantaneous number of online viewers for the current LVB stream | int    | Number of people    |

## 4. Example

Purpose: To query the push and playback information of all video streams that are being broadcasted under the current account

| Component              | Example                                     |
| ----------------- | ---------------------------------------- |
| API URL             | http://statcgi.video.qcloud.com/common_access? |
| cmd               | 1234                                     |
| interface         | Get_LiveStat                             |
| Param.n.page_no   | 1                                        |
| Param.n.page_size | 20                                       |
| t                 | 1471850187                               |
| sign              | b17971b51ba0fe5916ddcd96692e9fb3         |

```
// When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "cmd is invalid".
URL = http://statcgi.video.qcloud.com/common_access?
			cmd=1234&interface=Get_LiveStat
			&Param.n.page_no=1
			&Param.n.page_size=20
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```








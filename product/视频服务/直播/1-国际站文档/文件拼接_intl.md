
## 1. API Description

- **API**
  - **vod_simple_concat**: This API is used to stitch multiple recorded fragments into a complete video file.

- **URL**
  - URL for calling API: `http://<font color='red'>fcgi.</font>video.qcloud.com/common_access`


## 2. Input Parameters

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
| cmd                        | Customer ID | int       | LVB APPID used for identifying customers |  Y          | 
| interface                 | API name | string | For example: Get_LivePushStat |  Y          | 
| t | [Validity period](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | int  | UNIX timestamp (decimal) |  Y | 
| sign | [Security signature](https://cloud.tencent.com/doc/api/258/5956#.E5.AE.89.E5.85.A8.E6.A3.80.E6.9F.A5) | string | MD5(key+t) | Y | 
| Param.s.channel_id | Channel ID | string | | Y|
| Param.a.file_id_list.s.n  | ID of the files to be stitched | string  | The value of "n" starts from 1. | Y |

> For historical reasons, the LVB Code parameter was defined as channel_id in some earlier APIs, and is defined as stream_id in new APIs.

## 3. Output Parameters
| Parameter Name | Description | Type | Note |
|---------|---------|---------|------------------|
| ret      | Error code |   int  | 0: Successful; other values: Failed. |
| message | Error message |   string  | Error message |
| output | Message content |   array  | For more information, please see the description below. |

"output" is composed as follows:

| Field Name | Description | Type | Note |
|---------|---------|---------|------------------|
| all_count | Number of fragments |   int      |    |
| file_list    | Information of the fragment |   array  | For more information, please see the description below. |

"file_list" is composed as follows:

| Field Name | Description | Type | Note |
|---------|---------|---------|------------------|
| file_id | ID of the stitched VOD file | string |  |

>**Where is the stitching URL?**






*--------------------------------------------------------------------*
 
## 4. Example
Purpose: To stitch several recorded fragments with the LVB Code of 8888_test123 into a complete file.

| Component | Example |
|-------------|------------------|
| API URL | http://fcgi.video.qcloud.com/common_access? |
|cmd       | 1234 |
|interface       | vod_simple_concat |
|Param.s.channel_id | 8888_test123 |
|Param.a.file_id_list.s.n | ????? Is 9896587163648321628, 9896587163648312398 correct???? |
|t |1471850187 |
|sign | b17971b51ba0fe5916ddcd96692e9fb3 |

```
//When copying them, remove the invisible line breaks used for improving layout. Otherwise, URL construction errors may occur, such as "cmd is invalid".
URL = http://fcgi.video.qcloud.com/common_access?
			cmd=1234&interface=vod_simple_concat
			&Param.s.channel_id=8888_test123
			&Param.s.channel_id=?????1111
			&Param.a.file_id_list.s.n=?????1111
			&t=1471850187&sign=b17971b51ba0fe5916ddcd96692e9fb3
```
			








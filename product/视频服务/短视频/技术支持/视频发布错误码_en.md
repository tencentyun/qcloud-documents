
### SDK Error Codes
SDK monitors the publishing status of a short video via API TXRecordCommon.ITXVideoPublishListener. Therefore, you can check the video publishing using **retCode** in TXRecordCommon.TXPublishResult.

| Status Code | Constant in TXRecordCommon | Description |
| :--------: | :--------| :-- |
| 0 | NO_ERROR | Published successfully |
| 1001 | ERR_UGC_REQUEST_FAILED | Upload request failed |
| 1002 | ERR_UGC_PARSE_FAILED | Information resolution request failed |
| 1003 | ERR_UPLOAD_VIDEO_FAILED | Failed to upload video |
| 1004 | ERR_UPLOAD_COVER_FAILED | Failed to upload cover |
| 1005 | ERR_UGC_FINISH_REQUEST_FAILED | Failed to finish upload request |
| 1006 | ERR_UGC_FINISH_RESPONSE_FAILED | Finish upload response error |
| 1007 | ERR_USER_CANCEL | Publishing is canceled by user |
| 1007 | ERR_CLIENT_BUSY | Client is busy (object cannot process more requests) |
| 1008 | ERR_FILE_NOEXIT | The file to upload does not exist |
| 1009 | ERR_UGC_PUBLISHING | The video is being uploaded |
| 1010 | ERR_UGC_INVALID_PARAM | The upload parameter setting is incorrect |
| 1011 | ERR_UGC_INVALID_SECRETID | The secretID for video upload is invalid. It has been discarded but not thrown away|
| 1012 | ERR_UGC_INVALID_SIGNATURE | The signature for video upload is invalid |
| 1013 | ERR_UGC_INVALID_VIDOPATH | The video file path is invalid |
| 1014 | ERR_UGC_INVALID_VIDEO_FILE | The video file does not exist under the current path |
| 1015 | ERR_UGC_FILE_NAME | The video file name is too long or contains special characters |
| 1016 | ERR_UGC_INVALID_COVER_PATH | The path to the cover of the video file is invalid.  The file does not exist |



### Server Error Codes
If you cannot diagnose the video publishing result according to the SDK error codes, please see the error codes returned by servers, which can be found in the Log information.

| Error Code | Description |
| :--------: | :--------| 
| 0 | Published successfully | 
| -20001 | Instantly uploaded | 
| -20002 | Task canceled | 
| -20003 | Task suspended | 
| -20004 | File does not exist | 
| -20007 | Server response packet is empty | 
| -20008 | Request timed out | 
| -20009 | appid is empty | 
| -20010 | bucket is empty | 
| -20011 | COS remote path is empty | 
| -20012 | COS directory contains reserved characters | 
| -20013 | dest_fileId is empty | 
| -20014 | bucket_authority is empty | 
| -21001  |  Out Of Memory | 
| -22000 | IO exception | 
| -25000 | Other error codes. To solve these errors, contact Tencent commercial personnel or submit a ticket. Tel: 4009-100-100 | 



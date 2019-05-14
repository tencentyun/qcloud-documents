Tencent Cloud provides a set of LVB Code management APIs for your backend server, including status query, status management and APIs with other features.

### API List

| API | Description |
|---------------------------------|--------------------------------------------------------------|
| [Get_LiveStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the push and playback information |
| [Get_LivePushStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the push information |
| [Get_LivePlayStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the playback information |
| [Get_LivePushStatHistory](https://cloud.tencent.com/document/product/267/9579) | Obtain the history of push |
| [Get_LivePushStatHistory](https://cloud.tencent.com/document/product/267/9580) | Obtain the history of playback statistics |
| [Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958) | Query only status information of a stream (old version API) | 
| [Live_Channel_SetStatus](https://cloud.tencent.com/doc/api/258/5959) | Ban an LVB stream, mainly used in porn detection | 
| [Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960) | Query the list of videos recorded during LVB for a certain stream | 
| [Live_Queue_Get](https://cloud.tencent.com/doc/api/258/5961) | Query the list of screenshots captured during LVB for a certain stream |
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/7997) | Query channel list |
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/8862) | Query LVB channel list |
| [mix_streamv2.start_mix_stream_advanced](https://cloud.tencent.com/document/product/267/8832) | API for stream mixing on the cloud |
| [channel_manager](https://cloud.tencent.com/document/product/267/9500) | Stop pushing stream and delay the availability of API - It can disable push for a specified stream |
| [Live_Tape_Start](https://cloud.tencent.com/document/product/267/9567) | Create a recording task. It supports scheduled recording and real-time recording |
| [Live_Tape_Stop](https://cloud.tencent.com/document/product/267/9568) | End a recording task |

### Error code
1. HTTP error codes 

| Error Code | Description | Note |
|---------|---------|---------|
| 403 | Forbidden | Verification is enabled for the API to ensure security. If this error occurs when you perform verification via browser, you can check whether skey is contained in cookie. |
| 404 | Not Found | Check whether the request comes with host |

2. Returned error codes

| Error Code | Description | Note |
|---------|---------|---------|
| appid is invalid | Invalid appid, which indicates the feature is not activated | <br>|

>**Note:**
>The above error codes apply to the APIs listed in this document and do not include [Event Message Notification](https://cloud.tencent.com/document/product/267/5957).

 


Tencent Video Cloud is PAAS rather than SAAS (in another word, it only provides a platform rather than specific business to clients), which requires your business backend engineers to participate in the integration process. Backend engineers' tasks are as follows:

![](https://mc.qcloudimg.com/static/img/74a5f9784f81b6f8c597fcdffdf72887/image.png)

## Assigning URLs
For either single-session LVB or free-run LVB, assigning URLs at backend is more flexible than hardcoding URLs in your Apps.

Assigning URLs refers to the processes of returning push URLs to Apps when VJs are ready to push streams ([iOS](https://cloud.tencent.com/document/product/454/7879) | [Android](https://cloud.tencent.com/document/product/454/7885)) on Apps and returning playback URLs to Apps when viewers are ready to play back the streams ([iOS](https://cloud.tencent.com/document/product/454/7880) | [Android](https://cloud.tencent.com/document/product/454/7886)) on Apps.

For more information, please see [Assigning URLs](https://cloud.tencent.com/document/product/454/9875).

## Assigning UserSig

UserSig is a security credential for using Tencent Cloud Instant Messaging ([IM](https://cloud.tencent.com/product/im)). If you want use the chat room feature of Tencent Cloud IM service, you need to ask your backend engineer to generate a UserSig and return it to the terminal APP. If you already have an IM solution (that is, you already have your own chat room), skip this step.

For more information, please see [Assigning UserSig](https://cloud.tencent.com/document/product/454/14548).

## Controlling LVB streams
If you want to query the quantity and status of LVB streams or manage them, use the following REST APIs to perform secondary development as needed:

| API | Description |
|---------------------------------|--------------------------------------------------------------|
| [Get_LiveStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the push and playback information |
| [Get_LivePushStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the push information |
| [Get_LivePlayStat](https://cloud.tencent.com/doc/api/258/6110) | Statistics query - query the playback information |
| [Get_LivePushStatHistory](https://cloud.tencent.com/document/product/267/9579) | Obtain the history of push |
| [Get_LivePushStatHistory](https://cloud.tencent.com/document/product/267/9580) | Obtain the history of playback statistics |
| [Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958) | Query only status information of a stream (old version API) | 
| [Live_Channel_SetStatus](https://cloud.tencent.com/doc/api/258/5959) | **Ban** an LVB stream, mainly used in porn detection | 
| [Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960) | Query the list of videos **recorded** during LVB for a certain stream | 
| [Live_Queue_Get](https://cloud.tencent.com/doc/api/258/5961) | Query the list of screenshots **captured** during LVB for a certain stream |
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/7997) | Query channel list |
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/8862) | Query LVB channel list |
| [mix_streamv2.start_mix_stream_advanced](https://cloud.tencent.com/document/product/267/8832) | API for stream mixing on the cloud (used to mix screens with multiple LVB streams) |
| [channel_manager](https://cloud.tencent.com/document/product/267/9500) | Stop pushing stream and delay the availability of API - It can disable push for a specified stream |
| [Live_Tape_Start](https://cloud.tencent.com/document/product/267/9567) | Create a recording task. It supports scheduled recording and real-time recording |
| [Live_Tape_Stop](https://cloud.tencent.com/document/product/267/9568) | End a recording task |


For more information, please see [Controlling LVB Streams](https://cloud.tencent.com/document/product/454/7920).


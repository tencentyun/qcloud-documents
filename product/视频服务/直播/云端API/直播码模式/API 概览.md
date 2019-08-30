腾讯云提供了一组直播码管理 API，包括状态查询和状态管理等功能，供您的后台服务器调用。

### API 列表

| API                                | 功能介绍                                                   |
|---------------------------------|--------------------------------------------------------------|
| [Get_LiveStat](https://cloud.tencent.com/doc/api/258/6110)  | 统计信息查询 - 查询推流和播放相关信息|
| [Get_LivePushStat](https://cloud.tencent.com/doc/api/258/6110) | 统计信息查询 - 查询推流相关信息|
| [Get_LivePlayStat](https://cloud.tencent.com/doc/api/258/6110)  |  统计信息查询 - 查询播放相关信息 |
| [Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958) |  仅查询某条流的状态信息（旧版本接口） | 
| [Live_Channel_SetStatus](https://cloud.tencent.com/doc/api/258/5959) | 对某条流实行禁播操作，主要用于鉴黄场景 | 
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/7997)|查询频道列表|
| [Live_Channel_GetLiveChannelList](https://cloud.tencent.com/document/product/267/8862)|查询直播中频道列表|
| [mix_streamv2.start_mix_stream_advanced](https://cloud.tencent.com/document/product/267/8832)|云端混流操作接口|
| [channel_manager](https://cloud.tencent.com/document/product/267/9500)|暂停并延迟恢复 - 可针对某路流禁止推流|
| [Live_Tape_Start](https://cloud.tencent.com/document/product/267/9567)|创建录制任务 - 可实现定时录制任务或者实时视频录制|
| [Live_Tape_Stop](https://cloud.tencent.com/document/product/267/9568)|结束录制任务|

### 错误码
1.HTTP 错误 

| 错误码 | 含义 | 备注 |
|---------|---------|---------|
| 403 | Forbidden | 接口为了安全考虑，开启了校验；若使用浏览器验证发现该错误，可检查下 cookie 里是否含有 skey |
| 404 | Not Found | 查看请求时是否带上 host |

2.接口通用返回错误

| 错误码 | 含义 | 备注 |
|---------|---------|---------|
| appid is invalid | appid 不合法，表示未开通该功能  |  - |

>!以上错误码针对本文 API 列表中的 API，不包括 [消息事件通知](https://cloud.tencent.com/document/product/267/5957)。

 

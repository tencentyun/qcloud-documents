## 与腾讯云后台通讯
![](//mc.qcloudimg.com/static/img/bb38ba7d007910df41b2775a63c6e0d3/image.png)

您的服务器与腾讯云服务器的信息同步可以通过两种方式组合实现：
- **API 调用**：腾讯云提供了一组直播码管理 API，包括状态查询和状态管理等功能，供您的后台服务器调用。
- **消息通知**：腾讯云在直播流状态变更、录制文件生成等一系列事件发生时，能够以事件消息（JSON）的形式主动通知您的后台服务器，只需要您在腾讯云注册接收事件通知的回调 URL 即可实现。


## API 调用
腾讯云提供了一组直播码管理 API，包括状态查询和状态管理等功能，供您的后台服务器调用。

### API 列表

| API                                | 功能介绍                                                   |
|---------------------------------|--------------------------------------------------------------|
| [Get_LiveStat](https://cloud.tencent.com/doc/api/258/6110)  | 统计信息查询 - 查询推流和播放相关信息|
| [Get_LivePushStat](https://cloud.tencent.com/doc/api/258/6110) | 统计信息查询 - 查询推流相关信息|
| [Get_LivePlayStat](https://cloud.tencent.com/doc/api/258/6110)  |  统计信息查询 - 查询播放相关信息 |
| [Live_Channel_GetStatus](https://cloud.tencent.com/doc/api/258/5958) |  仅查询某条流的状态信息（旧版本接口） | 
| [Live_Channel_SetStatus](https://cloud.tencent.com/doc/api/258/5959) | 对某条流实行**禁播**操作，主要用于鉴黄场景 | 
| [Live_Tape_GetFilelist](https://cloud.tencent.com/doc/api/258/5960)| 查询某条流在直播过程中的**录制**文件列表 | 
| [Live_Queue_Get](https://cloud.tencent.com/doc/api/258/5961)| 查询某条流在直播过程中的**截图**文件列表 |
| [Live_Channel_GetChannelList](https://cloud.tencent.com/document/product/267/7997)|查询频道列表|
| [Live_Channel_GetLiveChannelList](https://cloud.tencent.com/document/product/267/8862)|查询直播中频道列表|
| [mix_streamv2.start_mix_stream_advanced](https://cloud.tencent.com/document/product/267/8832)|云端混流（用于将多条直播流的画面进行合并）操作接口|
| [channel_manager](https://cloud.tencent.com/document/product/267/9500)|暂停并延迟恢复——可针对某路流禁止推流|
| [Live_Tape_Start](https://cloud.tencent.com/document/product/267/9567)|创建录制任务——可实现定时录制任务或者实时视频录制|
| [Live_Tape_Stop](https://cloud.tencent.com/document/product/267/9568)|结束录制任务|

### 调用方法

在您的 **服务端** 采用 HTTP 协议的 GET 请求方式（即调用参数直接拼接在 URL 中）进行调用即可，详细的调用方法在每个 API 的说明文档中都有示例参考，没有任何对接难度。

<span id="anquan"></span>
### 安全机制
由于对 API 的调用采用的是普通的 HTTP 协议（出于性能考虑），这就需要一套行之有效的办法来确保您的服务器与腾讯云后台之间的通讯安全。

所有直播码相关的云端 API 都采用了同一种安全检查机制， **t + sign 校验**：
- **t（过期时间）**：如果一个 API 请求或者通知中的 t 值所规定的时间已经过期，则可以判定这个请求或者通知为无效的，这样做可以防止网络重放攻击。t 的格式为 UNIX 时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。

- **sign（安全签名）**：sign = MD5(key + t)，即把加密 key 和 t 进行字符串拼接后，计算一下 md5 值。这里的 key 即 CGI 调用 key，您在腾讯云直播管理 [控制台](https://console.cloud.tencent.com/live/livecodemanage) 中可以进行设置：

![](//mc.qcloudimg.com/static/img/e5034b47cead66be46b1f81a1fea8274/image.png)

- **安全原理**
由于 MD5 是不可逆的 HASH 算法，所以只要确保 KEY 不泄露，即使攻击者拿到很多对 t 和 sign 也无法反算出 KEY 值，进而无法进行伪装攻击。

- **计算示例**
   比如我们现在的时间是 2016-08-22 15:16:27， 我们希望有效期是1分钟，也就是 2016-08-22 15:16:27 以后再收到携带这个 t 的请求或者通知即判定为非法的：
```
	t = "2016-08-22 15:17:27" = 1471850187
```
   假设我们的 key 是 **5d41402abc4b2a76b9719d911017c592**，那么我们计算的签名结果就是：
```
	sign = MD5(5d41402abc4b2a76b9719d911017c5921471850187) = b17971b51ba0fe5916ddcd96692e9fb3
```

## 错误码
1. http 错误 

| 错误码 | 含义 | 备注 |
|---------|---------|---------|
| 403 | Forbidden | 接口为了安全考虑开启了校验，若使用浏览器验证发现该错误，可检查下 cookie 里是否含有 skey |
| 404 | Not Found | 查看请求时是否带上 host |

2. 接口通用返回错误

| 错误信息 | 含义 | 
|---------|---------|
| appid is invalid | appid 不合法，表示未开通该功能 |

3. 接口前端接入返回错误信息

| 错误信息 | 含义 | 
|---------|---------|
|cmd is invalid|cmd 不合法，表示未开通该功能|
|sign invalid|鉴权计算错误，参考 [安全机制](#anquan)|
|time expired|鉴权成功，但是超过了 url 有效期，参考 [安全机制](#anquan)|

4. 接口后端查询返回错误码

| 错误码 | 错误信息 | 含义 |
|---------|---------|---------|
|0|query data successfully|本次查询成功，并返回结果数据|
|1000|user is not registered for statapi|用户没有注册 statapi，请提工单到后台开通|
|1001|user service for statapi was stopped|用户 statapi 访问服务已经被终止|
|1201|internel/system error|内部系统错误，属于系统异常，建议通过工单反馈到服务商|
|1202|invalid request/request frequency exceeds limit|无效的请求，一般是超过了频控次数，如果频率不能满足业务需要，可申请增加次数|
|1204|invalid input param|输入参数错误，请检查下输入的参数是否符合接口规范|
|1301|has not live stream|没有活跃的流，在调用实时接口时会返回改错误码。|
|10003|query data is empty|后端查询数据成功，但是返回数据为空。例如，某时间段没有播放，此时调用接口 Get_LivePlayStatHistory 就会返回10003|

>! 以上错误码针对本文 1.API 列表中的 API，不包括 [消息事件通知](https://cloud.tencent.com/document/product/267/5957)。

## 消息通知
详情参考腾讯云事件 [消息通知](https://cloud.tencent.com/document/product/267/5957) 服务。 

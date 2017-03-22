## 与腾讯云后台通讯
![](//mc.qcloudimg.com/static/img/bb38ba7d007910df41b2775a63c6e0d3/image.png)

您的服务器与腾讯云服务器的信息同步可以通过两种方式组合实现：
- **API 调用**：腾讯云提供了一组直播码管理API，包括状态查询和状态管理等功能，供您的后台服务器调用。
- **消息通知**：腾讯云在直播流状态变更、录制文件生成等一系列事件发生时，能够以事件消息（JSON）的形式主动通知您的后台服务器，只需要您在腾讯云注册接收事件通知的回调 URL 即可实现。


## API 调用
腾讯云提供了一组直播码管理API，包括状态查询和状态管理等功能，供您的后台服务器调用。

### 1. API 列表

| API                                | 功能介绍                                                   |
|---------------------------------|--------------------------------------------------------------|
| [Get_LiveStat](https://www.qcloud.com/doc/api/258/6110)  | 统计信息查询 - 查询推流和播放相关信息|
| [Get_LivePushStat](https://www.qcloud.com/doc/api/258/6110) | 统计信息查询 - 查询推流相关信息|
| [Get_LivePlayStat](https://www.qcloud.com/doc/api/258/6110)  |  统计信息查询 - 查询播放相关信息 |
| [Live_Channel_GetStatus](https://www.qcloud.com/doc/api/258/5958) |  仅查询某条流的状态信息（旧版本接口） | 
| [Live_Channel_SetStatus](https://www.qcloud.com/doc/api/258/5959) | 对某条流实行**禁播**操作，主要用于鉴黄场景 | 
| [Live_Tape_GetFilelist](https://www.qcloud.com/doc/api/258/5960)| 查询某条流在直播过程中的**录制**文件列表 | 
| [Live_Queue_Get](https://www.qcloud.com/doc/api/258/5961)| 查询某条流在直播过程中的**截图**文件列表 |
|[Live_Channel_GetChannelList](https://www.qcloud.com/document/product/267/7997)|查询频道列表|

### 2. 调用方法

在您的 **<font color='red'>服务端</font>** 采用 HTTP 协议的 GET 请求方式（即调用参数直接拼接在 URL 中）进行调用即可，详细的调用方法在每个 API 的说明文档中都有示例参考，没有任何对接难度。

### 3. 安全机制
由于对 API 的调用采用的是普通的 HTTP 协议（出于性能考虑），这就需要一套行之有效的办法来确保您的服务器与腾讯云后台之间的通讯安全。

所有直播码相关的云端 API 都采用了同一种安全检查机制， **t + sign 校验**：
- **t（过期时间）**：如果一个API请求或者通知中的 t 值所规定的时间已经过期，则可以判定这个请求或者通知为无效的，这样做可以防止网络重放攻击。t 的格式为UNIX时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。

- **sign（安全签名）**:  <font color='blue'>sign = MD5(key + t) </font>，即把加密key 和 t 进行字符串拼接后，计算一下md5值。这里的key即CGI调用key，您在腾讯云直播管理[控制台](https://console.qcloud.com/live/livecodemanage) 中可以进行设置：

![](//mc.qcloudimg.com/static/img/e5034b47cead66be46b1f81a1fea8274/image.png)

- **安全原理**
由于MD5是不可逆的HASH算法，所以只要确保KEY不泄露，即使攻击者拿到很多对t和sign也无法反算出KEY值，进而无法进行伪装攻击。

- **计算示例**
   比如我们现在的时间是 2016-08-22 15:16:27， 我们希望有效期是1分钟，也就是 2016-08-22 15:16:27 以后再收到携带这个 t 的请求或者通知即判定为非法的：
```
	t = "2016-08-22 15:17:27" = 1471850187
```
   假设我们的key是 **5d41402abc4b2a76b9719d911017c592**，那么我们计算的签名结果就是：
```
	sign = MD5(5d41402abc4b2a76b9719d911017c5921471850187) = b17971b51ba0fe5916ddcd96692e9fb3
```

## 消息通知
详情参考腾讯云事件[消息通知](https://www.qcloud.com/document/product/267/5957)服务。 

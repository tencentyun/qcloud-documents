## 对接攻略

本节要介绍的是移动端的纯推流和纯播放功能，要借助腾讯云RTMP SDK来实现，消息、弹幕、点赞、飘星等业务逻辑在后续的文章中再做介绍。

1. 首先在 [直播控制台](https://www.qcloud.com/doc/api/258/6445) 上生成一对推流和播放地址，用来测试推流和直播观看。
2. 对接 RTMP 推流功能，一般需要0.5d - 1d 时间。
3. 对接 LIVE 在线直播功能，一般需要0.5d - 1d 时间。
4. 对接 VOD 视频点播功能（视需要而定）：先[开通点播服务](https://www.qcloud.com/doc/api/258/6208#2.1-.E5.A6.82.E4.BD.95.E5.BC.80.E9.80.9A.E8.A7.86.E9.A2.91.E7.82.B9.E6.92.AD.E6.9C.8D.E5.8A.A1)，开通之后在推流URL后面拼接 &record=flv (或者mp4) 就可以将推流的视频录制下来，之后在[点播控制台](http://console.qcloud.com/video/videolist) 可以看到相关的视频。
5. 剩下的就是等 [直播后台](https://www.qcloud.com/doc/api/258/6447) 对接好后，把测试URL换成正式的推拉流地址了。

## RTMP推流
RTMP 推流即由SDK完成音视频采集和编码，然后使用标准 rtmp 协议将音视频流推送到指定的推流URL上去。

- **摄像头直播（[iOS平台](https://www.qcloud.com/doc/product/454/6946) &  [Android 平台](https://www.qcloud.com/doc/product/454/6947)）**
摄像头直播即由SDK采集摄像头的影响和麦克风的声音，之后完成编码和推流工作，支持 iOS 7 和 Android 4.2 及更高版本的操作系统。

- **手机录屏直播（[iOS平台](https://www.qcloud.com/doc/product/454/6948) & [ Android 平台](https://www.qcloud.com/doc/product/454/6949)）**
手机录屏直播即由SDK采集手机的屏幕画面和麦克风的声音，之后完成编码和推流工作，支持 iOS 10 和 Android 5.0 及更高版本的操作系统。

- **进阶应用（[参考文档](https://www.qcloud.com/doc/product/454/6955)）**
  + 对于想要了解 RTMP SDK 内部原理的客户
  + 有音视频相关开发经验，需要结合自身场景对参数进行定制的客户
  + 想要只拿 RTMP SDK 进行推流的客户

## 在线直播(LIVE)
在线直播观看的是一个正在实时推流的视频源，相比于先预加载几分钟视频到本地，然后按部就班进行播放的VOD视频点播，在线直播要解决更加困难的几个问题：

- **低延迟**
在线直播要解决主播到观众的延迟不能太高的问题，比如 RTMP 和 FLV 两种协议的最小延迟都要控制在2-3秒以内，这就意味着 “大缓冲&稳稳播” 的思路完全不再适用。

- **低卡顿**
既然延迟不能太大，视频缓冲的就不能太多，那卡顿的规避就不能只靠大段的缓冲来抵消。而且卡顿过后随之而来的延迟不断堆加也是个必须要解决的问题。

- **秒开播**
点开一个直播间，立马就能看到视频，这是对一款合格的直播 App 的基本要求，所以播放器不支持秒开就太 Low 了。

目前腾讯云 RTMP SDK 在上述三个方面的表现均得到了客户的一致认可，对接的成本也很低，一般 1d 都能搞定。

- [iOS平台参考文档](https://www.qcloud.com/doc/product/454/6950) 
- [Android 平台参考文档](https://www.qcloud.com/doc/product/454/6952) 

## 视频点播(VOD)
VOD 视频点播的内部原理和优化方案跟 Live 在线直播有很大差异，但是接口上跟Live直播播放基本保持一致，使用上注意两点区别：
- 点播的事件通知会有 PLAY_EVT_PLAY_PROGRESS 进度通知，Live直播是不支持的。
- 点播和直播，在调用 startPlay 时一定不要把视频类型弄错了，<font color='red'>用直播播放器放VOD点播视频是会快动作的哦</font>。

RTMP SDK 的点播播放器主要面向的是视频直播客户的录制回放需求，所以在格式支持上我们并不追求大而全，仅提供了 FLV(支持分辨率切换和横竖屏切换)、 HLS 和 MP4 三种点播格式的支持。

如果已经接过直播了，分分钟就可以实现点播功能：
- [iOS平台参考文档](https://www.qcloud.com/doc/product/454/6953) 
- [Android 平台参考文档](https://www.qcloud.com/doc/product/454/6954) 

## 源码参考
下面是小直播源码中 RTMP SDK 对接部分的代码位置：


### iOS 平台

| 类名 | 模块功能 | 详细介绍 |
|---------|---------|---------|
| TCPusherMgr | 推流模块逻辑层代码 | 主要是与业务Server进行获取URL的协议通信。 |
| TCPushController | 推流模块主控制器 | 里面承载了渲染view，逻辑view，以及推流相关逻辑，同时也是SDK层事件通知的接收类。 |
| TCPushDecorateView | 推流模块界面view | 里面展示了消息列表，弹幕动画，观众列表，美颜，美白等UI，其中与SDK的逻辑交互需要交给主控制器处理。 |
| TCPlayerMgr | 播放模块逻辑层代码 | 主要是与业务Server进行获取URL的协议通信。 |
| TCPlayController | 播放模块逻辑层代码 | 里面承载了渲染view，逻辑view，以及播放相关逻辑，同时也是SDK层事件通知的接收类。 |
| TCPlayDecorateView | 播放模块界面view | 里面展示了消息列表，弹幕动画，观众列表等UI，其中与SDK的逻辑交互需要交给主控制器处理。 |

### Android 平台

| 类名 | 模块功能 | 详细介绍 |
|---------|---------|---------|
|TCPusherMgr.java|直播管理类| 和后台进行通信，拉取直播地址、通知后台退出直播。|
|TCLivePublisherActivity.java|推流模块Activity|所有的推流管理、消息管理、动画特效都在该类进行。|
|TCPlayerMgr.java|播放管理类|和后台进行通信，通知后台进入房间、退出房间、点赞事件。|
|TCLivePlayerActivity.java|播放模块Activity|包括点播和直播，所有的播放管理、消息管理、动画特效都在该类进行。|



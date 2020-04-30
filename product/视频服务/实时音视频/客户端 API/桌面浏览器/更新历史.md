
版本号`major.minor.patch`具体规则如下：
  - major：主版本号，如有重大版本重构则该字段递增，通常各主版本间接口不兼容。
  - minor：次版本号，各次版本号间接口保持兼容，如有接口新增或优化则该字段递增。
  - patch：补丁号，如有功能改善或缺陷修复则该字段递增。

>!建议您及时更新至最新版本，以便获得更好的产品稳定性及在线支持。

## 4.3.14 (2020-4-29)

**Bug Fixes**

修复小程序音频 muted unmute 事件。
  
## 4.3.13 (2020-4-16)

**Improvement**

优化可用性检测逻辑。

## 4.3.12 (2020-4-13)

**Bug Fixes**

修复一个潜在的 RTCPeerConnection 状态变化异常。
  
## 4.3.11 (2020-3-28)

**Improvement**

增加手机 QQ 浏览器检测，手机 QQ 浏览器暂时无法支持 TRTC 桌面浏览器 SDK。

**Bug Fixes**

修复 Boolean 返回值类型。

## 4.3.10 (2020-3-17)

**Improvement**

- 优化环境检测逻辑。
- RtcError 增加 name code。

## 4.3.9 (2020-3-13)

**Improvement**

- 增加部署环境自动检测。
- 优化日志。

## 4.3.8 (2020-2-24)

**Improvement**

createClient 增加 streamId userdefinerecordid 字段。

## 4.3.7 (2020-2-21)

**Improvement**

屏幕分享时切换设备抛出异常。

**Bug Fixes**

- 切换设备时释放 MediaStream，解决设备占用问题。
- 订阅接口增加处理潜在错误。

## 4.3.6 (2020-2-5)

**Bug Fixes**

调整 Stream.resume() 音视频播放顺序，修复 iOS 上微信浏览器自动播放异常问题

## 4.3.5 (2020-2-5)

**Improvement**

增加 publish 超时检查，提高信令发送成功率

## 4.3.4 (2020-1-6)

**Improvement**
 
升级 core-js 至 v3.6.1。
  
**Bug Fixes**

- unpublish 超时后向外部抛出异常事件。
- 修复第三方库引起 V8 负优化问题。

## 4.3.3 (2019-12-25)

**Improvement**

- 增加主动检测环境是否支持 webrtc 能力
- 优化 sdp 响应机制
- 优化上报逻辑

**Bug Fixes**

修复 turn URL 协议格式

## 4.3.2 (2019-12-09)

**Improvement**

- 增加下行连接 ICE 断开自动重连机制。
- 去除 STUN 打洞环节，增加内网用户连接成功率及提高连接速度。
- 日志上报时间戳统一使用服务器校正后的 UTC 时间。
- 优化 ICE 错误上报。
- 增加更多关键事件上报到 avmonitor 监控。

**Bug Fixes**

- 修复 WebSocket 信令通道1005异常重连及重连错误处理。
- 修复下行丢包率上报问题。

## 4.3.1 (2019-11-23)

**Improvement**

增加通话过程中上行链路 ICE 断开自动重连机制。

**Bug Fixes**

修复 STUN 打洞失败后 host 公网 IP 类型 ICE Candidate 不生效问题。

## 4.3.0（2019-11-15）

**Feature**

增加 Client.getTransportStats() API。

**Improvement**

- 增加更详细的上报日志。
- 事件解除绑定支持通配符。
- 增加连接超时时间至5s。
- 增加发布超时时间至5s。

**Bug Fixes**

修复因 zone.js 修改原型链导致 SDK 判断异常的问题。

## 4.2.0（2019-11-04）

**Feature**

增加 Client.off() 接口取消客户端事件绑定。

**Improvement**

- 通话状态统计优化。
- Client.publish() 增加权限检查。
- Stream.play()/resume() 增加自动播放错误提示。

**Bug Fixes**

LocalStream.switchDevice() 切换摄像头黑屏问题修复。

## 4.1.1（2019-10-24）

**Bug Fixes**

- 修复日志丢失问题。
- 修复断网重连远端用户丢失问题。

## 4.1.0（2019-10-17）

**Feature**

- Stream.play() 接口支持传入 HTMLDivElement 对象。
- 增加音频码率调控设置，开发者可通过 LocalStream.setAudioProfile() 设置音频属性，目前支持两种 Profile：standard 和 high。

**Bug Fixes**

- 修复旧版本 Chrome 上的 WebAudio Context 数量受限问题。
- 修复 replaceTrack() 未重启本地音视频播放器问题。
- 修复 LocalStream.setScreenProfile() 自定义属性设置未生效问题。
- 修复 audio/video player 重启及状态上报问题。

## 4.0.0（2019-10-11）

TRTC 桌面浏览器 SDK 重构版本，提供 Client/Stream 模式的接口，各对象职责更明确，语义更简洁明了。
重构版本与旧版本不兼容，除接口改动之外，还提供如下功能：

- 视频属性 （分辨率、帧率及码率）控制完全由 App 通过 SDK 的 LocalStream.setVideoProfile() 接口设置，不再支持老版本通过腾讯云控制台的“画面设定 （Spear Role）”。
- SDK 在 Stream 对象中封装了音视频播放器，音视频播放完全由 SDK 控制。
- 提供远端流的订阅与取消订阅功能，开发者可以通过 Client.subscribe()/unsubscribe() 接口灵活控制远端流的音频、视频或音视频数据流的接收。

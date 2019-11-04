# TRTC Web SDK 版本发布日志

- 版本号规则：[major.minor.patch]
  - major：主版本号，如有重大版本重构则该字段递增，通常各主版本间接口不兼容。
  - minor：次版本号，各次版本号间接口保持兼容，如有接口新增或优化则该字段递增。
  - patch：补丁号，如有功能改善或缺陷修复则该字段递增。
- 我们建议您及时更新到最新版本以便获得更好的产品稳定性及在线支持！

## [4.2.0](2019-11-04)

**Feature**

- 增加 Client.off() 接口取消客户端事件绑定。

**Improvement**

- 通话状态统计优化。
- Client.publish() 增加权限检查。
- Stream.play()/resume() 增加自动播放错误提示。

**Bug Fixes**

- LocalStream.switchDevice() 切换摄像头黑屏问题修复。

## [4.1.1](2019-10-24)

**Bug Fixes**

- 修复日志丢失问题。
- 修复断网重连远端用户丢失问题。

## [4.1.0](2019-10-17)

**Feature**

- Stream.play() 接口支持传入 HTMLDivElement 对象。
- 增加音频码率调控设置，开发者可通过 LocalStream.setAudioProfile() 设置音频属性，目前支持两种 Profile：standard 和 high。

**Bug Fixes**

- 修复旧版本 Chrome 上的 WebAudio Context 数量受限问题。
- 修复 replaceTrack() 未重启本地音视频播放器问题。
- 修复 LocalStream.setScreenProfile() 自定义属性设置未生效问题。
- 修复 audio/video player 重启及状态上报问题。

## [4.0.0](2019-10-11)

TRTC Web SDK (WebRTC) 重构版本，提供 Client/Stream 模式的接口，各对象职责更明确，语义更简洁明了。
重构版本与旧版本不兼容，除接口改动之外，还提供如下功能：

- 视频属性 （分辨率、帧率及码率）控制完全由 App 通过 SDK 的 LocalStream.setVideoProfile() 接口设置，不再支持老版本通过腾讯云控制台的“画面设定 （Spear Role）”。
- SDK 在 Stream 对象中封装了音视频播放器，音视频播放完全由 SDK 控制。
- 提供远端流的订阅与取消订阅功能，开发者可以通过 Client.subscribe()/unsubscribe() 接口灵活控制远端流的音频、视频或音视频数据流的接收。

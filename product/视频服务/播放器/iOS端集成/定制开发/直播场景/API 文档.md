## TXLivePlayer
 
### 视频播放器

请参见 [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html)。

主要负责将直播流的音视频画面进行解码和本地渲染，包含如下技术特点：

- 针对腾讯云的拉流地址，可使用低延时拉流，实现直播连麦等相关场景。
- 针对腾讯云的拉流地址，可使用直播时移功能，能够实现直播观看与时移观看的无缝切换。
- 支持自定义的音视频数据处理，让您可以根据项目需要处理直播流中的音视频数据后，进行渲染以及播放。

### SDK 基础函数 

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [delegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a6c78c9dda50ec1aa28a71d5548c45d71) | 设置播放回调，见`TXLivePlayListener.h`文件中的详细定义。     |
| [videoProcessDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a9eab6c2e67b2eae1bddf6fbf6978ba03) | 设置视频处理回调，见`TXVideoCustomProcessDelegate.h`文件中的详细定义。 |
| [audioRawDataDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a4d08f185792a92a087aff32b52b6b7b9) | 设置音频处理回调，见`TXAudioRawDataDelegate.h`文件中的详细定义。 |
| [enableHWAcceleration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#aa3ea979a6be5feba0da24f2b18555395) | 是否开启硬件加速，默认值：NO。                               |
| [config](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#aac73c062f0bbe5d97be40d85b68cb98a) | 设置 [TXLivePlayConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#aac73c062f0bbe5d97be40d85b68cb98a) 播放配置项，见`TXLivePlayConfig.h`文件中的详细定义。 |
| [recordDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a7a3f4c66d5019d8e8899823e04be924d) | 设置短视频录制回调，见`TXLiveRecordListener.h`文件中的详细定义。 |
| [isAutoPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a946828345d302a28708d78fa1a931763) | startPlay 后是否立即播放，默认 YES，只有点播有效。           |


### 播放基础接口

| API                                                          | 描述                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [setupVideoWidget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a9195fa66ee874328a5b48400f2a0cb14) | 创建 Video 渲染 View，该控件承载着视频内容的展示。 |
| [removeVideoWidget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#adf77d29895e70602556fdc51b931951e) | 移除 Video 渲染 Widget。                           |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a37e97416ec7a5853d217679be49cea26) | 启动从指定 URL 播放 RTMP 音视频流。                |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a7d59ca6180c4af0eb7bd63c08161f84d) | 停止播放音视频流。                                 |
| [isPlaying](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a7d3378ad416bfd00522acaedefc47dda) | 是否正在播放。                                     |
| [pause](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a7167f5c196fc5e167bfabde1a730e81d) | 暂停播放。                                         |
| [resume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a41de8150eff044a237990c271d57ea27) | 继续播放，适用于点播，直播。                       |


### 视频相关接口

| API                                                          | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#ade93023de1bcd8374b62f5a2bf4beeee) | 设置画面的方向。     |
| [setRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a3819261f776bfda7e95e3b0bf30445a4) | 设置画面的裁剪模式。 |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#aa24051e4c0271d994a5008cfc2db4775) | 截屏。               |


### 音频相关接口

| API                                                          | 描述                                   |
| ------------------------------------------------------------ | -------------------------------------- |
| [setMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a861e656ed3fbdd5522fdf8801c07ab83) | 设置静音。                             |
| [setVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a5a3bf801bad5591a3d8fe284aa6b3134) | 设置音量。                             |
| [setAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#ad56c52832a8efe45d6e0c50049406d74) | 设置声音播放模式（切换扬声器，听筒）。 |
| [setAudioVolumeEvaluationListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a87d74a7afe3f768bd9e7ca276a189533) | 设置音量大小回调接口。                 |


### 直播时移相关接口

| API                                                          | 描述                                       |
| ------------------------------------------------------------ | ------------------------------------------ |
| [prepareLiveSeek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#acf638c46e1e866ef06abda5ac938f07f) | 直播时移准备，拉取该直播流的起始播放时间。 |
| [resumeLive](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a4fa26fd4aea472d02de56d5f0bf653bf) | 停止时移播放，返回直播。                   |
| [seek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#adb8448443e6f0551eaad429d70b9f01c) | -                                          |


### 视频录制相关接口

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a7224d5a8ab5fadc1d4c0fe1feb6ac972) | 开始录制短视频。 |
| [stopRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a13313c5410c2a10a704b991f28141e6e) | 结束录制短视频。 |
| [setRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a1d79db46540e804a7bb9fc8cd87a3d99) | 设置播放速率。   |


### 更多实用接口

| API                                                          | 描述                                      |
| ------------------------------------------------------------ | ----------------------------------------- |
| [setLogViewMargin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#aa906f88b51df74ab8f3c1125d9856293) | 设置状态浮层 view 在渲染 view 上的边距。  |
| [showVideoDebugLog](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a70ec322b088ad3c38b5a41d7528467f2) | 是否显示播放状态统计及事件消息浮层 view。 |
| [switchStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a88751ad91dff45a9d6cc96dbda903b69) | FLV 直播无缝切换。                        |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#a16c53e91f9b32aaf4bf3d409a3790ef6) | 调用实验性 API 接口。                     |


### 枚举值

| 枚举                                                         | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [TX_Enum_PlayType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html#gaa164f735d1c349ce715f313c5d75892a) | 支持的直播和点播类型。 |


## TXLivePlayConfig

### 腾讯云直播播放器的参数配置模块

请参见 [TXLivePlayConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__ios.html#interfaceTXLivePlayConfig)。

主要负责 [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__ios.html) 对应的参数设置，其中绝大多数设置项在播放开始之后再设置是无效的。

## TXLivePlayListener

### 腾讯云直播播放的回调通知

请参见  [TXLivePlayListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayListener__ios.html)。

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [onPlayEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayListener__ios.html#a1e33d0cf9ed5f89ea2db32d0d7db9701) | 直播事件通知。 |
| [onNetStatus](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayListener__ios.html#aee80e62b7950c7d0a75ab97d993c10c6) | 网络状态通知。 |


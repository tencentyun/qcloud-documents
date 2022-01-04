## TXLivePlayer
 
### 视频播放器

请参见 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34762)。

主要负责将直播流的音视频画面进行解码和本地渲染，包含如下技术特点：

- 针对腾讯云的拉流地址，可使用低延时拉流，实现直播连麦等相关场景。
- 针对腾讯云的拉流地址，可使用直播时移功能，能够实现直播观看与时移观看的无缝切换。
- 支持自定义的音视频数据处理，让您可以根据项目需要处理直播流中的音视频数据后，进行渲染以及播放。

### SDK 基础函数 

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [delegate](https://cloud.tencent.com/document/product/454/34762#delegate) | 设置播放回调，见`TXLivePlayListener.h`文件中的详细定义。     |
| [videoProcessDelegate](https://cloud.tencent.com/document/product/454/34762#videoprocessdelegate) | 设置视频处理回调，见`TXVideoCustomProcessDelegate.h`文件中的详细定义。 |
| [audioRawDataDelegate](https://cloud.tencent.com/document/product/454/34762#audiorawdatadelegate) | 设置音频处理回调，见`TXAudioRawDataDelegate.h`文件中的详细定义。 |
| [enableHWAcceleration](https://cloud.tencent.com/document/product/454/34762#enablehwacceleration) | 是否开启硬件加速，默认值：NO。                               |
| [config](https://cloud.tencent.com/document/product/454/34762#config) | 设置 [TXLivePlayConfig](https://cloud.tencent.com/document/product/454/34760) 播放配置项，见`TXLivePlayConfig.h`文件中的详细定义。 |
| [recordDelegate](https://cloud.tencent.com/document/product/454/34762#recorddelegate) | 设置短视频录制回调，见`TXLiveRecordListener.h`文件中的详细定义。 |
| [isAutoPlay](https://cloud.tencent.com/document/product/454/34762#isautoplay) | startPlay 后是否立即播放，默认 YES，只有点播有效。           |


### 播放基础接口

| API                                                          | 描述                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [setupVideoWidget](https://cloud.tencent.com/document/product/454/34762#setupvideowidget) | 创建 Video 渲染 View，该控件承载着视频内容的展示。 |
| [removeVideoWidget](https://cloud.tencent.com/document/product/454/34762#removevideowidget) | 移除 Video 渲染 Widget。                           |
| [startPlay](https://cloud.tencent.com/document/product/454/34762#startplay) | 启动从指定 URL 播放 RTMP 音视频流。                |
| [stopPlay](https://cloud.tencent.com/document/product/454/34762#stopplay) | 停止播放音视频流。                                 |
| [isPlaying](https://cloud.tencent.com/document/product/454/34762#isplaying) | 是否正在播放。                                     |
| [pause](https://cloud.tencent.com/document/product/454/34762#pause) | 暂停播放。                                         |
| [resume](https://cloud.tencent.com/document/product/454/34762#resume) | 继续播放，适用于点播，直播。                       |


### 视频相关接口

| API                                                          | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| [setRenderRotation](https://cloud.tencent.com/document/product/454/34762#setrenderrotation) | 设置画面的方向。     |
| [setRenderMode](https://cloud.tencent.com/document/product/454/34762#setrendermode) | 设置画面的裁剪模式。 |
| [snapshot](https://cloud.tencent.com/document/product/454/34762#snapshot) | 截屏。               |


### 音频相关接口

| API                                                          | 描述                                   |
| ------------------------------------------------------------ | -------------------------------------- |
| [setMute](https://cloud.tencent.com/document/product/454/34762#setmute) | 设置静音。                             |
| [setVolume](https://cloud.tencent.com/document/product/454/34762#setVolume) | 设置音量。                             |
| [setAudioRoute](https://cloud.tencent.com/document/product/454/34762#setaudioroute) | 设置声音播放模式（切换扬声器，听筒）。 |
| [setAudioVolumeEvaluationListener](https://cloud.tencent.com/document/product/454/34762#setaudiovolumeevaluationlistener) | 设置音量大小回调接口。                 |


### 直播时移相关接口

| API                                                          | 描述                                       |
| ------------------------------------------------------------ | ------------------------------------------ |
| [prepareLiveSeek](https://cloud.tencent.com/document/product/454/34762#prepareliveseek) | 直播时移准备，拉取该直播流的起始播放时间。 |
| [resumeLive](https://cloud.tencent.com/document/product/454/34762#resumelive) | 停止时移播放，返回直播。                   |
| [seek](https://cloud.tencent.com/document/product/454/34762#seek) | -                                          |


### 视频录制相关接口

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [startRecord](https://cloud.tencent.com/document/product/454/34762#startrecord) | 开始录制短视频。 |
| [stopRecord](https://cloud.tencent.com/document/product/454/34762#stoprecord) | 结束录制短视频。 |
| [setRate](https://cloud.tencent.com/document/product/454/34762#setrate) | 设置播放速率。   |


### 更多实用接口

| API                                                          | 描述                                      |
| ------------------------------------------------------------ | ----------------------------------------- |
| [setLogViewMargin](https://cloud.tencent.com/document/product/454/34762#setlogviewmargin) | 设置状态浮层 view 在渲染 view 上的边距。  |
| [showVideoDebugLog](https://cloud.tencent.com/document/product/454/34762#showvideodebuglog) | 是否显示播放状态统计及事件消息浮层 view。 |
| [switchStream](https://cloud.tencent.com/document/product/454/34762#switchstream) | FLV 直播无缝切换。                        |
| [callExperimentalAPI](https://cloud.tencent.com/document/product/454/34762#callexperimentalapi) | 调用实验性 API 接口。                     |


### 枚举值

| 枚举                                                         | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [TX_Enum_PlayType](https://cloud.tencent.com/document/product/454/34762#tx_enum_playtype) | 支持的直播和点播类型。 |


## TXLivePlayConfig

### 腾讯云直播播放器的参数配置模块

请参见 [TXLivePlayConfig](https://cloud.tencent.com/document/product/454/34760)。

主要负责 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34762) 对应的参数设置，其中绝大多数设置项在播放开始之后再设置是无效的。

## TXLivePlayListener

### 腾讯云直播播放的回调通知

请参见  [TXLivePlayListener](https://cloud.tencent.com/document/product/454/34761)。

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [onPlayEvent](https://cloud.tencent.com/document/product/454/34761#onplayevent) | 直播事件通知。 |
| [onNetStatus](https://cloud.tencent.com/document/product/454/34761#onnetstatus) | 网络状态通知。 |

## TXLivePlayer

### 视频播放器

请参见 [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html)。
 
主要负责将直播流的音视频画面进行解码和本地渲染，包含如下技术特点：

- 针对腾讯云的拉流地址，可使用低延时拉流，实现直播连麦等相关场景。
- 针对腾讯云的拉流地址，可使用直播时移功能，能够实现直播观看与时移观看的无缝切换。
- 支持自定义的音视频数据处理，让您可以根据项目需要处理直播流中的音视频数据后，进行渲染以及播放。

### SDK 基础函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html) | 创建 [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html) 实例。 |
| [setConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#aec057eaad309a040e689eae94d81f6c2) | 设置 [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html) 播放配置项。 |
| [setPlayListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a0735b006fe8c56875665cb66881af144) | 设置推流回调接口。                                           |


### 播放基础接口  

| API                                                          | 描述                            |
| ------------------------------------------------------------ | ------------------------------- |
| [setPlayerView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a64eefab5bdb76cef17f609560eec5830) | 设置播放器的视频渲染 View。     |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a966517cd67d967afe969b3d275239934) | 播放器开始播放。                |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a6abf34bf566c275476b1706593cb0fe1) | 停止播放。                      |
| [isPlaying](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#ac651fc45a9f04e4db6f258f8cdd7bbcf) | 是否正在播放。                  |
| [pause](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a7167f5c196fc5e167bfabde1a730e81d) | 暂停播放。                      |
| [resume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a41de8150eff044a237990c271d57ea27) | 恢复播放。                      |
| [setSurface](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#ac06d94f1ed4ec1441c075e4ba556eb37) | 使用 Surface 模式用于本地渲染。 |
| [setSurfaceSize](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#adfa92e76bde9450b135c48f531e5434d) | 设置渲染 Surface 的大小。       |


### 播放配置接口

| API                                                          | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [setRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a6e1e1e12120b92f4884d3ea1a8e2cc94) | 设置播放渲染模式。     |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a1ae55363f74a78d935d63ea7b44130a8) | 设置图像渲染角度。     |
| [enableHardwareDecode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a33b092e7e79aab66b494e7034021b2f9) | 开启硬件加速。         |
| [setMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a85d2bb3409165c1b7b2c53f8d61a03e2) | 设置是否静音播放。     |
| [setAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a3f0305de6ccd826ab62c442408416df9) | 设置声音播放模式。     |
| [setVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a6715d5315d47c73b3838f2cb771e7b58) | 设置音量。             |
| [switchStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a53f1f75a9a06e03bbb35e2ff5368c6f9) | 多清晰度切换。         |
| [setAudioVolumeEvaluationListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#acd5e085b916732b2141ddae9ef93fc21) | 设置音量大小回调接口。 |


### 本地录制和截图

| API                                                          | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| [setVideoRecordListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#acd229e0c77d3eea61dc0762557417478) | 设置录制回调接口。   |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#aed6b1e9d26a36166ee31c0544bd95ca4) | 启动视频录制。       |
| [stopRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a13313c5410c2a10a704b991f28141e6e) | 停止视频录制。       |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a1377ad3e2678d3fef21f5037e274dd1a) | 播放过程中本地截图。 |


### 自定义数据处理

| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [addVideoRawData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a31d3d4067f5e61b80d7b750a6b5d97e2) | 设置软解码数据载体 Buffer。 |
| [setVideoRawDataListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a093d4928d038dcc1c5413e771b5f8962) | 设置软解码视频数据回调。    |
| [setAudioRawDataListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a36183b7ad026bc3e9718e82e38497e96) | 设置音频数据回调。          |


### 直播时移接口

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [prepareLiveSeek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a081d01beb281348300bd9e9689949c59) | 直播时移准备。 |
| [seek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a914c54a0122cba5ad78d84f893df8578) | 直播时移跳转。 |
| [resumeLive](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a4fa26fd4aea472d02de56d5f0bf653bf) | 恢复直播播放。 |


### 截图回调接口类

请参见 [ITXSnapshotListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#interfacecom_1_1tencent_1_1rtmp_1_1TXLivePlayer_1_1ITXSnapshotListener)。

| API                                                          | 描述       |
| ------------------------------------------------------------ | ---------- |
| [onSnapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html) | 截图回调。 |


### 软解视频数据回调接口类

请参见 [ITXVideoRawDataListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#interfacecom_1_1tencent_1_1rtmp_1_1TXLivePlayer_1_1ITXVideoRawDataListener)。

| API                                                          | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| [onVideoRawDataAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a466e71718261727174795a3cd2b95d9e/34775#onvideorawdataavailable) | 软解码器解出一帧数据回调一次。 |


### 音频原始数据接口类

请参见 [ITXAudioRawDataListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#interfacecom_1_1tencent_1_1rtmp_1_1TXLivePlayer_1_1ITXAudioRawDataListener)。

| API                                                          | 描述                               |
| ------------------------------------------------------------ | ---------------------------------- |
| [onPcmDataAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a33e835ad16580a93ae40e0723368af32) | 音频播放数据回调，数据格式 ：PCM。 |
| [onAudioInfoChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#a2aa86c3f5bd33047692b3d4dd0a59c32) | 音频播放信息回调。                 |


### 播放器音量大小接口类

请参见 [ITXAudioVolumeEvaluationListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#interfacecom_1_1tencent_1_1rtmp_1_1TXLivePlayer_1_1ITXAudioVolumeEvaluationListener)。

| API                                                          | 描述                                    |
| ------------------------------------------------------------ | --------------------------------------- |
| [onAudioVolumeEvaluationNotify](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html#ae83090684b162568b729c010acd69828) | 播放器音量大小回调, 取值范围 [0，100]。 |

## TXLivePlayConfig

### 腾讯云直播播放器的参数配置模块

请参见 [TXLivePlayConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#classcom_1_1tencent_1_1rtmp_1_1TXLivePlayConfig)。

主要负责 [TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayer__android.html) 对应的参数设置，其中绝大多数设置项在播放开始之后再设置是无效的。

### 常用设置项

| API                                                          | 描述                         |
| ------------------------------------------------------------ | ---------------------------- |
| [setAutoAdjustCacheTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#ad2b54e62edb8d9cf287ac34a0ee0bc6e) | 设置是否自动调整缓存时间。   |
| [setCacheTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#ac911ed6c1650c8723d11bb4aaa49f73f) | 设置播放器缓存时间。         |
| [setMaxAutoAdjustCacheTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#ab400433f30e53d4827b8c16c449c107c) | 设置最大的缓存时间。         |
| [setMinAutoAdjustCacheTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#af495df5fea5e42779c007c5600e7bc4a) | 设置最小的缓存时间。         |
| [setVideoBlockThreshold](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#a5d403dd5553d58ce309f26dbec61e20f) | 设置播放器视频卡顿报警阈值。 |
| [setConnectRetryCount](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#a30911117043dc5b3f559abf5eb1e9ce9) | 设置播放器重连次数。         |
| [setConnectRetryInterval](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#a5f3b8315c6276bd1c03c999ce01e4f8f) | 设置播放器重连间隔。         |


### 专业设置项

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [setEnableMessage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#a7c8e9ce786b57f2fddf921c4f336523d) | 开启消息通道。 |
| [enableAEC](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXLivePlayConfig__android.html#a2fb8e9e6f182cdd49f1260484cc484e5) | 设置回声消除。 |


## ITXLivePlayListener

### 腾讯云直播播放的回调通知

请参见 [ITXLivePlayListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITXLivePlayListener__android.html)。

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [onPlayEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITXLivePlayListener__android.html#a57e1f63dbe15f1242e3b842d0454f74f) | 播放事件通知。 |
| [onNetStatus](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITXLivePlayListener__android.html#a826de3acd9a9d2da1604a076772f2f2e) | 网络状态通知。 |

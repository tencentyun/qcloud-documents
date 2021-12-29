## TXLivePlayer

### 视频播放器

请参见 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer)。
 
主要负责将直播流的音视频画面进行解码和本地渲染，包含如下技术特点：

- 针对腾讯云的拉流地址，可使用低延时拉流，实现直播连麦等相关场景。
- 针对腾讯云的拉流地址，可使用直播时移功能，能够实现直播观看与时移观看的无缝切换。
- 支持自定义的音视频数据处理，让您可以根据项目需要处理直播流中的音视频数据后，进行渲染以及播放。

### SDK 基础函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer) | 创建 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer) 实例。 |
| [setConfig](https://cloud.tencent.com/document/product/454/34775#setconfig) | 设置 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer) 播放配置项。 |
| [setPlayListener](https://cloud.tencent.com/document/product/454/34775#setplaylistener) | 设置推流回调接口。                                           |


### 播放基础接口  

| API                                                          | 描述                            |
| ------------------------------------------------------------ | ------------------------------- |
| [setPlayerView](https://cloud.tencent.com/document/product/454/34775#setplayerview) | 设置播放器的视频渲染 View。     |
| [startPlay](https://cloud.tencent.com/document/product/454/34775#startplay) | 播放器开始播放。                |
| [stopPlay](https://cloud.tencent.com/document/product/454/34775#stopplay) | 停止播放。                      |
| [isPlaying](https://cloud.tencent.com/document/product/454/34775#isplaying) | 是否正在播放。                  |
| [pause](https://cloud.tencent.com/document/product/454/34775#pause) | 暂停播放。                      |
| [resume](https://cloud.tencent.com/document/product/454/34775#resume) | 恢复播放。                      |
| [setSurface](https://cloud.tencent.com/document/product/454/34775#setsurface) | 使用 Surface 模式用于本地渲染。 |
| [setSurfaceSize](https://cloud.tencent.com/document/product/454/34775#setsurfacesize) | 设置渲染 Surface 的大小。       |


### 播放配置接口

| API                                                          | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [setRenderMode](https://cloud.tencent.com/document/product/454/34775#setrendermode) | 设置播放渲染模式。     |
| [setRenderRotation](https://cloud.tencent.com/document/product/454/34775#setrenderrotation) | 设置图像渲染角度。     |
| [enableHardwareDecode](https://cloud.tencent.com/document/product/454/34775#enablehardwaredecode) | 开启硬件加速。         |
| [setMute](https://cloud.tencent.com/document/product/454/34775#setmute) | 设置是否静音播放。     |
| [setAudioRoute](https://cloud.tencent.com/document/product/454/34775#setaudioroute) | 设置声音播放模式。     |
| [setVolume](https://cloud.tencent.com/document/product/454/34775#setvolume) | 设置音量。             |
| [switchStream](https://cloud.tencent.com/document/product/454/34775#switchstream) | 多清晰度切换。         |
| [setAudioVolumeEvaluationListener](https://cloud.tencent.com/document/product/454/34775#setaudiovolumeevaluationlistener) | 设置音量大小回调接口。 |


### 本地录制和截图

| API                                                          | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| [setVideoRecordListener](https://cloud.tencent.com/document/product/454/34775#setvideorecordlistener) | 设置录制回调接口。   |
| [startRecord](https://cloud.tencent.com/document/product/454/34775#startrecord) | 启动视频录制。       |
| [stopRecord](https://cloud.tencent.com/document/product/454/34775#stoprecord) | 停止视频录制。       |
| [snapshot](https://cloud.tencent.com/document/product/454/34775#snapshot) | 播放过程中本地截图。 |


### 自定义数据处理

| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [addVideoRawData](https://cloud.tencent.com/document/product/454/34775#addvideorawdata) | 设置软解码数据载体 Buffer。 |
| [setVideoRawDataListener](https://cloud.tencent.com/document/product/454/34775#setvideorawdatalistener) | 设置软解码视频数据回调。    |
| [setAudioRawDataListener](https://cloud.tencent.com/document/product/454/34775#setaudiorawdatalistener) | 设置音频数据回调。          |


### 直播时移接口

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [prepareLiveSeek](https://cloud.tencent.com/document/product/454/34775#prepareliveseek) | 直播时移准备。 |
| [seek](https://cloud.tencent.com/document/product/454/34775#seek) | 直播时移跳转。 |
| [resumeLive](https://cloud.tencent.com/document/product/454/34775#resumelive) | 恢复直播播放。 |


### 截图回调接口类

请参见 [ITXSnapshotListener](https://cloud.tencent.com/document/product/454/34775#itxsnapshotlistener)。

| API                                                          | 描述       |
| ------------------------------------------------------------ | ---------- |
| [onSnapshot](https://cloud.tencent.com/document/product/454/34775#onsnapshot) | 截图回调。 |


### 软解视频数据回调接口类

请参见 [ITXVideoRawDataListener](https://cloud.tencent.com/document/product/454/34775#itxvideorawdatalistener)。

| API                                                          | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| [onVideoRawDataAvailable](https://cloud.tencent.com/document/product/454/34775#onvideorawdataavailable) | 软解码器解出一帧数据回调一次。 |


### 音频原始数据接口类

请参见 [ITXAudioRawDataListener](https://cloud.tencent.com/document/product/454/34775#itxaudiorawdatalistener)。

| API                                                          | 描述                               |
| ------------------------------------------------------------ | ---------------------------------- |
| [onPcmDataAvailable](https://cloud.tencent.com/document/product/454/34775#onpcmdataavailable) | 音频播放数据回调，数据格式 ：PCM。 |
| [onAudioInfoChanged](https://cloud.tencent.com/document/product/454/34775#onaudioinfochanged) | 音频播放信息回调。                 |


### 播放器音量大小接口类

请参见 [ITXAudioVolumeEvaluationListener](https://cloud.tencent.com/document/product/454/34775#itxaudiovolumeevaluationlistener)。

| API                                                          | 描述                                    |
| ------------------------------------------------------------ | --------------------------------------- |
| [onAudioVolumeEvaluationNotify](https://cloud.tencent.com/document/product/454/34775#onAudioVolumeEvaluationNotify) | 播放器音量大小回调, 取值范围 [0，100]。 |

## TXLivePlayConfig

### 腾讯云直播播放器的参数配置模块

请参见 [TXLivePlayConfig](https://cloud.tencent.com/document/product/454/34774)。

主要负责 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer) 对应的参数设置，其中绝大多数设置项在播放开始之后再设置是无效的。

### 常用设置项

| API                                                          | 描述                         |
| ------------------------------------------------------------ | ---------------------------- |
| [setAutoAdjustCacheTime](https://cloud.tencent.com/document/product/454/34774#setautoadjustcachetime) | 设置是否自动调整缓存时间。   |
| [setCacheTime](https://cloud.tencent.com/document/product/454/34774#setcachetime) | 设置播放器缓存时间。         |
| [setMaxAutoAdjustCacheTime](https://cloud.tencent.com/document/product/454/34774#setmaxautoadjustcachetime) | 设置最大的缓存时间。         |
| [setMinAutoAdjustCacheTime](https://cloud.tencent.com/document/product/454/34774#setminautoadjustcachetime) | 设置最小的缓存时间。         |
| [setVideoBlockThreshold](https://cloud.tencent.com/document/product/454/34774#setvideoblockthreshold) | 设置播放器视频卡顿报警阈值。 |
| [setConnectRetryCount](https://cloud.tencent.com/document/product/454/34774#setconnectretrycount) | 设置播放器重连次数。         |
| [setConnectRetryInterval](https://cloud.tencent.com/document/product/454/34774#setconnectretryinterval) | 设置播放器重连间隔。         |


### 专业设置项

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [setEnableMessage](https://cloud.tencent.com/document/product/454/34774#setenablemessage) | 开启消息通道。 |
| [enableAEC](https://cloud.tencent.com/document/product/454/34774#enableaec) | 设置回声消除。 |


## ITXLivePlayListener

### 腾讯云直播播放的回调通知

请参见 [ITXLivePlayListener](https://cloud.tencent.com/document/product/454/34773)。

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [onPlayEvent](https://cloud.tencent.com/document/product/454/34773#onplayevent) | 播放事件通知。 |
| [onNetStatus](https://cloud.tencent.com/document/product/454/34773#onnetstatus) | 网络状态通知。 |

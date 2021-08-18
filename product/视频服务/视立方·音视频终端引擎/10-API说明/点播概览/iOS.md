## TXVodPlayer

### 点播播放器

请参见 [TXVodPlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html)。
主要负责从指定的点播流地址拉取音视频数据，并进行解码和本地渲染播放。
播放器包含如下能力：

- 支持 FLV、MP4 及 HLS 多种播放格式，支持 基础播放（URL 播放） 和 点播播放（Fileid 播放）两种播放方式 。
- 屏幕截图，可以截取当前播放流的视频画面。
- 通过手势操作，调节亮度、声音、进度等。
- 可以手动切换不同的清晰度，也可根据网络带宽自适应选择清晰度。
- 可以指定不同倍速播放，并开启镜像和硬件加速。
- 完整能力，请参见 [点播超级播放器 - 能力清单](https://cloud.tencent.com/document/product/266/45539#.E8.B6.85.E7.BA.A7.E6.92.AD.E6.94.BE.E5.99.A8)。

### 播放器配置接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [config](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a3ad68ed80140f20cf3229bf344886a04) | 点播配置，配置信息请参见 [TXVodPlayConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html)。 |
| [isAutoPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a946828345d302a28708d78fa1a931763) | startPlay 后是否立即播放，默认 YES。                         |
| [token](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a946828345d302a28708d78fa1a931763) | 加密 HLS 的 token。设置此值后，播放器自动在 URL 中的文件名之前增加 `voddrm.token.TOKEN TextureView`。 |
| [loop](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a1cdc15a39387295573f41caee9a05932) | 是否循环播放 SurfaceView。                                   |
| [enableHWAcceleration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#aa3ea979a6be5feba0da24f2b18555395) | 视频渲染回调。（仅硬解支持）                                 |

### 播放基础接口  
| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#ac1af59fe9e4bc2b390661787097d2c8b) | 播放 HTTP URL 形式地址。 |
| [startPlayWithParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a0b4db90eafbc8c4d9be498e5ffefe961) | 以 fileId 形式播放。 |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a7d59ca6180c4af0eb7bd63c08161f84d) | 停止播放。 |
| [isPlaying](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a8438e3403946accc1986a05b89ee7b03) | 是否正在播放。      |
| [pause](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a7167f5c196fc5e167bfabde1a730e81d) | 暂停播放，停止获取流数据,保留最后一帧画面。 |
| [resume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a41de8150eff044a237990c271d57ea27) | 恢复播放，重新获取流数据。 |
| [seek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#adb8448443e6f0551eaad429d70b9f01c) | 跳转到视频流指定时间点，单位秒。 |
| [currentPlaybackTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a8b0ca7fda398996b355179bd9a479785) | 获取当前播放位置，单位秒。 |
| [duration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a7fd4f66e650bd1656a97d1db7fabaeda) | 获取总时长，单位秒。 |
| [playableDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a4acb1f7a723d342f7bfb9c5e540e5e77) | 获取可播放时长，单位秒。 |
| [width](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a3eeed61a3424d2f907c8a1e420fddf6d) | 获取视频宽度。 |
| [height](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a822ae85493a742654ba563619492b26a) | 获取视频高度。 |
| [setStartTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a41001e6276c4853500f78579d6bd2218) | 设置播放开始时间。 |

### 视频相关接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a9646437dc38d7dcce8c32dfec5d0bc5b) | 获取当前视频帧图像。<br>**注意：由于获取当前帧图像是比较耗时的操作，所以截图会通过异步回调出来。** |
| [setMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#aaf347826e1a9fad9998c0eea9791ed0c) | 设置镜像。                                                   |
| [setRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a1d79db46540e804a7bb9fc8cd87a3d99) | 设置点播的播放速率，默认1.0。                                |
| [bitrateIndex](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a9a325ed94acf6b545c88755855449a12) | 返回当前播放的码率索引。                                     |
| [setBitrateIndex](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a1aa8e1f3a63b46c8a1166447e2457abc) | 设置当前正在播放的码率索引，无缝切换清晰度。<br>清晰度切换可能需要等待一小段时间。 |
| [setRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a3819261f776bfda7e95e3b0bf30445a4) | 设置 [图像平铺模式](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#a0645160ad90c67581f7f226a6c0c46ae)。 |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#ade93023de1bcd8374b62f5a2bf4beeee) | 设置 [图像渲染角度](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#ad00f3ee125e574cab63d955e03f5f23f)。 |

### 音频相关接口

| API                                                          | 描述                          |
| ------------------------------------------------------------ | ----------------------------- |
| [setMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a861e656ed3fbdd5522fdf8801c07ab83) | 设置是否静音播放。            |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#ac92633d1cdfff1f93f48b7aec1d35b98) | 设置音量大小，范围：0 - 100。 |

### 事件通知接口

| API                    | 描述                   |
| ---------------------- | ---------------------- |
| [delegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a6c78c9dda50ec1aa28a71d5548c45d71) | 事件回调，建议使用 [vodDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a609f883ff450c123d75b04a902aabe79)。 |
| [vodDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a609f883ff450c123d75b04a902aabe79) | 设置播放器的回调。                                 |
| [videoProcessDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a9eab6c2e67b2eae1bddf6fbf6978ba03) | 视频渲染回调（仅硬解支持）。                  |

### TRTC 相关接口

通过以下接口，可以把点播播放器的音视频流通过 TRTC 进行推送，更多 TRTC 服务请参见 [TRTC  产品概述](https://cloud.tencent.com/document/product/647/16788)。

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [attachTRTC](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#affcfcba7937a7ef88a918afb0b3d73bc) | 点播绑定到 [TRTC](https://cloud.tencent.com/document/product/647/16788) 服务。 |
| [detachTRTC](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a5b947acf9f4fc992f0f02f8d87de3334) | 点播解绑 [TRTC](https://cloud.tencent.com/document/product/647/16788) 服务。 |
| [publishVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a8298f704cb659c725da28a27e08afbed) | 开始推送视频流。                                             |
| [unpublishVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#aaa6ecf72bfa9e35078561dd98d62be0c) | 取消推送视频流。                                             |
| [publishAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a7f1b46c4ae27f86188dc29f0f5d64b95) | 开始推送音频流。                                             |
| [unpublishAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__ios.html#a206d786a74ae3b71766755135161773e) | 取消推送音频流。                                             |

## TXVodPlayListener

腾讯云点播回调通知。
### SDK 基础回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onPlayEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayListener__ios.html#a6330db18bb40862fc2d66474fc34166b) | 点播播放事件通知，请参见 [播放事件列表](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#a3c3fa833bb8585df2f362da5b70c610a)、[事件参数](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#a5cb5e37938b510270847d4f5c751a594)。 |
| [onNetStatus](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayListener__ios.html#a08721fef1ba130fd182de4bed3b4430e) | 点播播放器 [网络状态通知](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#aa7190fc964cf23a567b56d9793ad5737)。 |

## TXVodPlayConfig

点播播放器配置类。

### 基础配置接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [connectRetryCount](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#ad89d728973fb42eced3ac18be873af1b) | 设置播放器重连次数。                                         |
| [connectRetryInterval](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#a07fde7cd21980c096b5bbd93aed137d5) | 设置播放器重连间隔，单位秒。                                 |
| [timeout](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#a39233eb85b4cbae04411577510e7c5e6) | 设置播放器连接超时时间，单位秒。                             |
| [cacheFolderPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#aec1a8f0064562368fe3c2df4f7fb72eb) | 设置点播缓存目录，点播 MP4、HLS 有效。                       |
| [maxCacheItems](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#aedbc9cc868baa2c44e3badbe6fdf4a43) | 设置缓存文件个数。                                           |
| [playerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#a4595fb5853016c5e5919324e71ad6f4c) | 设置播放器类型。                                             |
| [headers](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#ad69aaf8885027863ea19657425ef1974) | 设置自定义 HTTP headers。                                    |
| [enableAccurateSeek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#ada91e71bad4df942e6190650915a7728) | 设置是否精确 seek，默认 true。                               |
| [autoRotate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#aa1a372684aaaf95b9b17abf0c7a4e6c6) | 播放 MP4 文件时，若设为 YES 则根据文件中的旋转角度自动旋转。<br>旋转角度可在 PLAY_EVT_CHANGE_ROTATION 事件中获得。默认 YES。 |
| [smoothSwitchBitrate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#aa1caeddde1f950ec7965dcc721109928) | 平滑切换多码率 HLS，默认 false。                             |
| [progressInterval](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#a943e212cbd5e3d89de0529ab7c6042fb) | 设置进度回调间隔，单位毫秒。                                 |
| [maxBufferSize](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__ios.html#aa4934cef81784d3a195a5d95a43953f5) | 最大预加载大小，单位 MB。                                    |



## 错误码表

### 常规事件

| code | 事件定义                   | 含义说明                                                    |
| ---- | -------------------------- | ----------------------------------------------------------- |
| 2004 | PLAY_EVT_PLAY_BEGIN        | 视频播放开始（若有转菊花效果，此时将停止）。                |
| 2005 | PLAY_EVT_PLAY_PROGRESS     | 视频播放进度，会通知当前播放进度、加载进度和总体时长。      |
| 2007 | PLAY_EVT_PLAY_LOADING      | 视频播放 loading，如果能够恢复，之后会有 LOADING_END 事件。 |
| 2014 | PLAY_EVT_VOD_LOADING_END   | 视频播放 loading 结束，视频继续播放。                       |
| 2006 | PLAY_EVT_PLAY_END          | 视频播放结束。                                              |
| 2013 | PLAY_EVT_VOD_PLAY_PREPARED | 播放器已准备完成，可以播放。                                |
| 2003 | PLAY_EVT_RCV_FIRST_I_FRAME | 网络接收到首个可渲染的视频数据包（IDR）。                   |
| 2009 | PLAY_EVT_CHANGE_RESOLUTION | 视频分辨率改变。                                            |
| 2011 | PLAY_EVT_CHANGE_ROTATION   | MP4 视频旋转角度。                                          |



### 警告事件

| code  | 事件定义                          | 含义说明                                                     |
| ----- | --------------------------------- | ------------------------------------------------------------ |
| -2301 | PLAY_ERR_NET_DISCONNECT           | 网络断连，且经多次重连亦不能恢复,更多重试请自行重启播放。    |
| -2305 | PLAY_ERR_HLS_KEY                  | HLS 解密 key 获取失败。                                      |
| 2101  | PLAY_WARNING_VIDEO_DECODE_FAIL    | 当前视频帧解码失败。                                         |
| 2102  | PLAY_WARNING_AUDIO_DECODE_FAIL    | 当前音频帧解码失败。                                         |
| 2103  | PLAY_WARNING_RECONNECT            | 网络断连, 已启动自动重连（重连超过三次就直接抛送 PLAY_ERR_NET_DISCONNECT）。 |
| 2106  | PLAY_WARNING_HW_ACCELERATION_FAIL | 硬解启动失败，采用软解。                                     |
| -2304 | PLAY_ERR_HEVC_DECODE_FAIL         | H265 解码失败。                                              |
| -2303 | PLAY_ERR_FILE_NOT_FOUND           | 播放的文件不存在。                                           |

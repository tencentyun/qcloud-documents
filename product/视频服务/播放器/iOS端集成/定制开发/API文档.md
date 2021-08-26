## 直播（V2TXLivePlayer）

### 视频播放器

请参见 [V2TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html)。
主要负责从指定的直播流地址拉取音视频数据，并进行解码和本地渲染播放。
播放器包含如下能力：
- 支持 RTMP、HTTP-FLV、TRTC 以及 WebRTC 协议。
- 屏幕截图，可以截取当前直播流的视频画面。
- 延时调节，可以设置播放器缓存自动调整的最小和最大时间。
- 自定义的视频数据处理，您可以根据项目需要处理直播流中的视频数据后，再进行渲染以及播放。

### SDK 基础函数

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [setObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#aabeb99813cc5848e3106b64d8de11287) | 设置播放器回调。 |


### 播放基础接口  

| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [setRenderView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a5bf0688f150c9b724a7237e2bcff96cd) | 设置播放器的视频渲染 View。 |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a5c186e91db27840ec1ff4c9605248359) | 播放器开始播放。            |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a768b1c3893d15ae73d76d1a4c3b29aa6) | 停止播放。                  |
| [isPlaying](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a0bdbaa951f2110e5f7af91be5dfd7c67) | 是否正在播放。              |

### 视频相关接口

| API                   | 描述                       |
| --------------------- | -------------------------- |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a953256f3f232eb24e18c54f0d5ef0eaa)     | 设置播放器画面的旋转角度。 |
| [setRenderFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#ad1674b2b37e210af8a53f3684ac57a28)     | 设置画面的填充模式。       |
| [pauseVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#af0bf373d9d4c4509aedfd8814e537333)            | 暂停播放器的视频流。       |
| [resumeVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a1fc6989bb7eb53c6d6953554ceb9e418)           | 恢复播放器的视频流。       |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a7d6e28ab61e78b8185e5ea9713adad59)              | 截取播放过程中的视频画面。 |
| [enableCustomRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#abe456bc3437418e7b250e3ea173eb850) | 设置视频自定义渲染回调。   |

### 音频相关接口

| API                    | 描述                   |
| ---------------------- | ---------------------- |
| [pauseAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a8bb9976e8a0d9711a9e17f8888b2aa80)             | 暂停播放器的音频流。   |
| [resumeAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a6c34ddc58f1715d905b9864afee7c4b7)            | 恢复播放器的音频流。   |
| [setPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a88a48339b54a168c403a22f0b0bd2704)       | 设置音量。             |
| [enableVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#aeed74080dd72e52b15475a54ca5fd86b) | 启用播放音量大小提示。 |

### 更多实用接口

| API                    | 描述                   |
| ---------------------- | ---------------------- |
| [setCacheParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#ae439fa2774477dc54b8c27e994d0d42c)             | 设置播放器缓存自动调整的最小和最大时间 ( 单位：秒 )。   |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__ios.html#a94005f62b788b1030636b51bb5a0210a)            | 是否显示播放器状态信息的调试浮层。  |

## V2TXLivePlayerObserver
腾讯云直播播放的回调通知。
### SDK 基础回调

| API       | 描述                                                 |
| --------- | ---------------------------------------------------- |
| [onError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#aeba95a71e4698ea19780de253d3a0099)   | 直播播放器错误通知，播放器出现错误时，会回调该通知。 |
| [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a6e977d51482a006ad0ce2adc507510a2) | 直播播放器警告通知。                                 |

### 视频相关回调
| API       | 描述                                                 |
| --------- | ---------------------------------------------------- |
| [onVideoPlayStatusUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a3b0ae3081c30cb1a920d09333813df89)   | 直播播放器视频状态变化通知。|
| [onSnapshotComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a5754eb816b91fd0d0ac1559dd7884dad) | 截图回调。                                 |
| [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a1ee10f163275f3b9316ce387573fcbe1) | 自定义视频渲染回调。|

### 音频相关回调
| API       | 描述                                                 |
| --------- | ---------------------------------------------------- |
| [onAudioPlayStatusUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a7a467cced525d22cf1c0e7aeeee90acb)   | 直播播放器音频状态变化通知。|
| [onPlayoutVolumeUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a5439ba0397be3943c6ebfb6083c27664) | 播放器音量大小回调。                       |

### 统计回调
| API       | 描述                                                 |
| --------- | ---------------------------------------------------- |
| [onStatisticsUpdate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayerObserver__ios.html#a4cdfa0b36d4b9e910c1e0d1b5dc44cde)   | 直播播放器统计数据回调。|

## V2TXLivePusher

### 直播推流类

请参见 [V2TXLivePusher](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html)。

主要负责将本地的音频和视频画面进行编码，并推送到指定的推流地址，支持任意的推流服务端。
推流器包含如下能力：
- 自定义的视频采集，让您可以根据项目需要定制自己的音视频数据源。
- 美颜、滤镜、贴纸，包含多套美颜磨皮算法（自然&光滑）和多款色彩空间滤镜（支持自定义滤镜）。
- Qos 流量控制技术，具备上行网络自适应能力，可以根据主播端网络的具体情况实时调节音视频数据量。
- 脸形调整、动效挂件，支持基于优图 AI 人脸识别技术的大眼、瘦脸、隆鼻等脸形微调以及动效挂件效果，只需要购买 **优图 License** 就可以轻松实现丰富的直播效果。

### SDK 基础函数

| API         | 描述             |
| ----------- | ---------------- |
| [setObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#aa523f8cd2bab159e3723819ab1fe4fe2) | 设置推流器回调。 |

### 推流基础接口

| API                | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| [setRenderView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a5bf0688f150c9b724a7237e2bcff96cd)      | 设置本地摄像头预览 View。 |
| [startPush](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a33b38f236a439e7d848606acb68cc087)          | 开始音视频数据推流。                                         |
| [stopPush](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a7332411d6264bc743b0b2bae0b8a73ae)           | 停止推送音视频数据。                                         |
| [isPushing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a59ba29c9ce1f9dec5c63e6e06b861820)          | 当前推流器是否正在推流中。                                   |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a9db6d67c2e8dc94c6d9d658366b2dbb2) | 开启屏幕采集。                                               |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#ad2fe97c868e0187d82cb44a1204f7f89)  | 关闭屏幕采集。                                               |

### 视频相关接口

| API                                                          | 描述                                                |
| ------------------------------------------------------------ | --------------------------------------------------- |
| [setVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a0b08436c1e14a8d7d9875fae59ac6d84) | 设置推流视频分辨率，以及宽高比模式（横屏 / 竖屏）。 |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a953256f3f232eb24e18c54f0d5ef0eaa) | 设置本地摄像头预览画面的旋转角度。                  |
| [setRenderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#adf4cd57c705a1022d6730fd722f8dab5) | 设置本地摄像头预览镜像。                            |
| [startCamera](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#aa0b3bda940078de28d0350e9f57910a4)                                                  | 打开本地摄像头。                                    |
| [stopCamera](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a082890fe66c00c9b97277a4351c62027) | 关闭本地摄像头。                                    |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a7d6e28ab61e78b8185e5ea9713adad59) | 截取推流过程中的本地画面。                          |
| [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#ad48aacbfad38b8f5389c159283fae859)                                                 | 设置推流器水印。默认情况下，水印不开启。            |
| [setEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#ae4464d33567ce1a31d92530e02a48dd7) | 设置视频编码镜像。                                  |

### 美颜相关接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a4fb05ae6b5face276ace62558731280a) | 获取美颜管理对象 [TXBeautyManager](https://cloud.tencent.com/document/product/454/39382)，美颜的设置通过 TXBeautyManager 来设置。 |

### 音频相关接口

| API                                                          | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [startMicrophone](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a368d5e7a2e660dee8e48acb3daa51f24) | 打开麦克风。           |
| [stopMicrophone](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a340ff45f184ca5c08acd4e834a4b78ef) | 关闭麦克风。           |
| [setAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a88956a3ad5e030af7b2f7f46899e5f13) | 设置推流音频质量。     |
| [enableVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#aeed74080dd72e52b15475a54ca5fd86b) | 启用采集音量大小提示。 |

### 音效相关接口
| API                                                          | 描述               |
| ------------------------------------------------------------ | ------------------ |
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__ios.html) | 获取音效管理对象。 |

###  设备管理相关接口
| API                                                          | 描述               |
| ------------------------------------------------------------ | ------------------ |
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXDeviceManager__ios.html) | 获取设备管理对象。 |

### 更多实用接口

| API                                                          | 描述                                  |
| ------------------------------------------------------------ | ------------------------------------- |
| [setProperty](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#aff881e005a44666337a5424c7bf47915) | 调用 V2TXLivePusher 的高级 API 接口。 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a4a4ce2993678b473eb355c1378be2898) | 设置云端的混流转码参数。              |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a94005f62b788b1030636b51bb5a0210a) | 显示仪表盘。                          |


## 点播（TXVodPlayer）

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

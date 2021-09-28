## 直播（V2TXLivePlayer）

### 视频播放器

请参见 [V2TXLivePlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html)。
主要负责从指定的直播流地址拉取音视频数据，并进行解码和本地渲染播放。
播放器包含如下能力：
- 支持 RTMP、HTTP-FLV、TRTC 以及 WebRTC 协议。
- 屏幕截图，可以截取当前直播流的视频画面。
- 延时调节，可以设置播放器缓存自动调整的最小和最大时间。
- 自定义的视频数据处理，您可以根据项目需要处理直播流中的视频数据后，再进行渲染以及播放。

### SDK 基础函数

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [setObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#aa851c4bf90929cddfd7067cfdd6049b4) | 设置播放器回调。 |

### 播放基础接口  
| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [setRenderView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#afc848d88fe99790b8c0988b8525dd4d9) | 设置播放器的视频渲染 TXCloudVideoView。 |
| [setRenderView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#af2ac91d628fe510008b3c169896a7e81) | 设置播放器的视频渲染 TextureView。 |
| [setRenderView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a6b8f02711afe98f327743e699632e6ee) | 设置播放器的视频渲染 SurfaceView。 |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a08f6166ca792b84b76980830f845461d) | 播放器开始播放。            |
| [stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a8c4e12608a45f5629dd198ed54d7d2b4) | 停止播放。                  |
| [isPlaying](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a69347e1e19d1f96a6c31977f90b8860b) | 是否正在播放。              |

### 视频相关接口

| API                   | 描述                       |
| --------------------- | -------------------------- |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#aa08046b0f429f318f36249fa9d0276f2)     | 设置播放器画面的旋转角度。 |
| [setRenderFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#af26f720280c7403e6ca23daf82a57c9a)     | 设置画面的填充模式。       |
| [pauseVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a0db95f1fb6d448b943400b3149bacff3)            | 暂停播放器的视频流。       |
| [resumeVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#ac6addf129d35e104ba087ee6a93718d3)           | 恢复播放器的视频流。       |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a2a507ea1cd894a1635dbfd772802fefd)              | 截取播放过程中的视频画面。 |
| [enableCustomRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a3c31a1de340f63433d486befa6371e7c) | 设置视频自定义渲染回调。   |

### 音频相关接口

| API                    | 描述                   |
| ---------------------- | ---------------------- |
| [pauseAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#aa4a006f050968e6d5e9405b40b8e299b)             | 暂停播放器的音频流。   |
| [resumeAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a4ca6a40a3adba3699caaf1843a81b701)            | 恢复播放器的音频流。   |
| [setPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a080762d51e26b2042c6d30de42f59288)       | 设置音量。             |
| [enableVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#aaa893a96eff34a7ba660441f7597d6d8) | 启用播放音量大小提示。 |

### 更多实用接口

| API                    | 描述                   |
| ---------------------- | ---------------------- |
| [setCacheParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#a8a4f8f8e220a6e4aa2a04ca3e866efcb)             | 设置播放器缓存自动调整的最小和最大时间 ( 单位：秒 )。   |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePlayer__android.html#ad3e02a7295f3ba2221fea015f352616b)            | 是否显示播放器状态信息的调试浮层。  |


## 点播（TXVodPlayer）

### 点播播放器

请参见 [TXVodPlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html)。
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
| [setConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#ae69bc2dd060217e595c38f0dc819290a) | 设置播放器配置信息，配置信息请参见 [TXVodPlayConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html) |
| [setPlayerView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a64eefab5bdb76cef17f609560eec5830) | 设置播放器的视频渲染 TXCloudVideoView                        |
| [setPlayerView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#aeb2f15f370d50b6261b7832f02a0f411) | 设置播放器的视频渲染 TextureView                             |
| [setSurface](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#ac06d94f1ed4ec1441c075e4ba556eb37) | 设置播放器的视频渲染 SurfaceView                             |

### 播放基础接口  
| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a32fe5a77dedc7fc903345f00e6c47c3a) | 播放 HTTP URL 形式地址 |
| [startPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a4fcde588ae5f6c1141c2d72bcc831ef8) | 以 fileId 形式播放 |
| [ stopPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a6abf34bf566c275476b1706593cb0fe1) | 停止播放 |
| [isPlaying](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#ac651fc45a9f04e4db6f258f8cdd7bbcf) | 是否正在播放      |
| [pause](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a7167f5c196fc5e167bfabde1a730e81d) | 暂停播放，停止获取流数据,保留最后一帧画面 |
| [resume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a41de8150eff044a237990c271d57ea27) | 恢复播放，重新获取流数据 |
| [seek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a914c54a0122cba5ad78d84f893df8578) | 跳转到视频流指定时间点，单位秒 |
| [seek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#aa5d7fcf690ac3a1102ffa3c02192674d) | 跳转到视频流指定时间点，单位毫秒 |
| [getCurrentPlaybackTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a128b89dd39053d6d19d262a5f45110cd) | 获取当前播放位置，单位秒 |
| [getBufferDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#acebd6ae9dd87e10c8959a24d3b6d5e7f) | 获取缓存的总时长，单位秒 |
| [getDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a83ee44393f1e0db930be75b73ff47812) | 获取总时长，单位秒。 |
| [getPlayableDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a37cb584556d48d043b93dfec33c40a97) | 获取可播放时长，单位秒。 |
| [getWidth](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a67a0997183f24da19b776d96c1052998) | 获取视频宽度。 |
| [getHeight](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a07efb2a4e9a982688c8bb3c3f21d1092) | 获取视频高度。 |
| [setAutoPlay](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a5e0e3d950eb3f525634adc7a9f60eab7) | 设置点播是否 startPlay 后自动开始播放，默认自动播放。 |
| [setStartTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a8f767f79fb69496cdbc532fced5dff33) | 设置播放开始时间。 |
| [setToken](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a5f9eadc88ca97238f84226462f095536) | 加密 HLS 的 token。 |
| [setLoop](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a3f5ae863c82509d1ed266503e8138781) | 设置是否循环播放。 |
| [isLoop](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#aaa3fcc823e0fce316dea1cc9162f1c8e) | 返回是否循环播放状态。 |

### 视频相关接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [enableHardwareDecode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a33b092e7e79aab66b494e7034021b2f9) | 启用或禁用视频硬解码。                                       |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a6f1c0c128052960f084ef6d1d7a77b09) | 获取当前视频帧图像。<br>**注意：由于获取当前帧图像是比较耗时的操作，所以截图会通过异步回调出来。** |
| [setMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a4add579d2ec825502c5e3832aced5bc1) | 设置镜像。                                                   |
| [setRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#add2bcd36c051900d697853155494865b) | 设置点播的播放速率，默认1.0。                                |
| [getBitrateIndex](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#af6f9e1e680baa611642fb168007b1c45) | 返回当前播放的码率索引。                                     |
| [setBitrateIndex](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a61f524a6ed275edaf9e9a0997f64d491) | 设置当前正在播放的码率索引，无缝切换清晰度。清晰度切换可能需要等待一小段时间。 |
| [setRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a6e1e1e12120b92f4884d3ea1a8e2cc94) | 设置 [图像平铺模式](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#a0645160ad90c67581f7f226a6c0c46ae)。 |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a1ae55363f74a78d935d63ea7b44130a8) | 设置 [图像渲染角度](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#ad00f3ee125e574cab63d955e03f5f23f)。 |

### 音频相关接口

| API                                                          | 描述                                    |
| ------------------------------------------------------------ | --------------------------------------- |
| [setMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a85d2bb3409165c1b7b2c53f8d61a03e2) | 设置是否静音播放。                      |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a9b8946403b8b3ac8e11f3a78e9d531ca) | 设置音量大小，范围：0 - 100。           |
| [setRequestAudioFocus](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a676f0935eca038719f58100d31f169b1) | 设置是否自动获取音频焦点 默认自动获取。 |

### 事件通知接口

| API                    | 描述                   |
| ---------------------- | ---------------------- |
| [setPlayListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a0735b006fe8c56875665cb66881af144) | 设置播放器的回调（已弃用，建议使用 [setVodListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#adb0e51670b947f15cca9a98d7d804e61)）。 |
| [setVodListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#adb0e51670b947f15cca9a98d7d804e61) | 设置播放器的回调。                                 |
| [onNotifyEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a1e4be8c3cfef68a8909d66a9243b6ec5) | 点播播放事件通知。                                 |
| [onNetSuccess](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#ae6febac01c1cba85f8fe387a0c14d9d0) | 点播播放网络状态通知。                             |
| [onNetFailed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a74942758292eb41138c7a01ed9056da2) | 播放 fileId 网络异常通知。                         |

### TRTC 相关接口

通过以下接口，可以把点播播放器的音视频流通过 TRTC  进行推送，更多 TRTC 服务请参见 [TRTC 产品概述](https://cloud.tencent.com/document/product/647/16788)。

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [attachTRTC](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#ad6bd04b37a89012102e7bb71ea5554a6) | 点播绑定到 [TRTC](https://cloud.tencent.com/document/product/647/16788) 服务。 |
| [detachTRTC](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a5b947acf9f4fc992f0f02f8d87de3334) | 点播解绑 [TRTC](https://cloud.tencent.com/document/product/647/16788) 服务。 |
| [publishVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a8298f704cb659c725da28a27e08afbed) | 开始推送视频流。                                             |
| [unpublishVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#aaa6ecf72bfa9e35078561dd98d62be0c) | 取消推送视频流。                                             |
| [ publishAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a7f1b46c4ae27f86188dc29f0f5d64b95) | 开始推送音频流。                                             |
| [unpublishAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#a206d786a74ae3b71766755135161773e) | 取消推送音频流。                                             |

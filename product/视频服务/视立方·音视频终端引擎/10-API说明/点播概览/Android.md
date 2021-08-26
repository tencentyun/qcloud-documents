## TXVodPlayer

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

## ITXVodPlayListener

腾讯云点播回调通知。
### SDK 基础回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onPlayEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITXVodPlayListener__android.html#aad1d875808cd4a68d429762e492aad05) | 点播播放事件通知，请参见 [播放事件列表](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#a3c3fa833bb8585df2f362da5b70c610a)、[事件参数](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#a5cb5e37938b510270847d4f5c751a594)。 |
| [onNetStatus](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITXVodPlayListener__android.html#a2be0a0294ae21e68e736ac8fa4d3085d) | 点播播放器 [网络状态通知](https://liteav.sdk.qcloud.com/doc/api/zh-cn/classcom_1_1tencent_1_1rtmp_1_1TXLiveConstants.html#aa7190fc964cf23a567b56d9793ad5737)。 |

## TXVodPlayConfig

点播播放器配置类。

### 基础配置接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [setConnectRetryCount](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a30911117043dc5b3f559abf5eb1e9ce9) | 设置播放器重连次数。                                         |
| [setConnectRetryInterval](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a5f3b8315c6276bd1c03c999ce01e4f8f) | 设置播放器重连间隔，单位秒。                                 |
| [setTimeout](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#ae44a6096c42cdb61adc10370ca2a42b6) | 设置播放器连接超时时间，单位秒。                             |
| [setCacheFolderPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a6ad0d546e6da3abacd5d4ea8bd6f94de) | 设置点播缓存目录，点播 MP4、HLS 有效。                       |
| [setMaxCacheItems](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#acc2f17764df9bb52163dac9faf81f11e) | 设置缓存文件个数。                                           |
| [setPlayerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a3594024855210dc07f50a6d7c5f8b088) | 设置播放器类型。                                             |
| [setHeaders](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a9ca40412371b505f9d52fbe95fdbaa6f) | 设置自定义 HTTP headers。                                    |
| [setEnableAccurateSeek](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a3caff179964976945f3754f1ec48a42b) | 设置是否精确 seek，默认 true。                               |
| [setAutoRotate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#ab360b681c220c2adb57de2758916b227) | 播放 MP4 文件时，若设为 YES 则根据文件中的旋转角度自动旋转。<br>旋转角度可在 PLAY_EVT_CHANGE_ROTATION 事件中获得。默认 YES。 |
| [setSmoothSwitchBitrate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a23fb393011e4663d0dfa765b72665a46) | 平滑切换多码率 HLS，默认 false。                             |
| [setCacheMp4ExtName](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#aaeccb662be133d4ded4fc17df29b94b5) | 缓存 MP4 文件扩展名。                                        |
| [setProgressInterval](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a01a46ce89e4979a6397b6deb2525007c) | 设置进度回调间隔，单位毫秒。                                 |
| [setMaxBufferSize](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayConfig__android.html#a2705841bfedb3c44839cc355eaad26dc) | 最大预加载大小，单位 MB。                                    |



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
| -2301 | PLAY_ERR_NET_DISCONNECT           | 网络断连,且经多次重连亦不能恢复,更多重试请自行重启播放。     |
| -2305 | PLAY_ERR_HLS_KEY                  | HLS 解密 key 获取失败。                                      |
| 2101  | PLAY_WARNING_VIDEO_DECODE_FAIL    | 当前视频帧解码失败。                                         |
| 2102  | PLAY_WARNING_AUDIO_DECODE_FAIL    | 当前音频帧解码失败                                           |
| 2103  | PLAY_WARNING_RECONNECT            | 网络断连, 已启动自动重连 (重连超过三次就直接抛送 PLAY_ERR_NET_DISCONNECT)。 |
| 2106  | PLAY_WARNING_HW_ACCELERATION_FAIL | 硬解启动失败，采用软解。                                     |
| -2304 | PLAY_ERR_HEVC_DECODE_FAIL         | H265 解码失败。                                              |
| -2303 | PLAY_ERR_FILE_NOT_FOUND           | 播放的文件不存在。                                           |

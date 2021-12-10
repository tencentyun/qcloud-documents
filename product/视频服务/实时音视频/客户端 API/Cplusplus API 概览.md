## C++ 全平台接口简介
自 8.0 版本起，我们在原有的 Windows（C++）接口的基础上，提供了全新的 C++ 接口，适用于 Windows、iOS、Mac、Android 平台。
如果您暂不清楚如何集成 C++ 接口，请参阅各平台的集成指引。  
- [iOS C++ 接口集成指引](https://cloud.tencent.com/document/product/647/32173#using_cpp)  
- [Android C++ 接口集成指引](https://cloud.tencent.com/document/product/647/32175#using_cpp)  
- [Mac C++ 接口集成指引](https://cloud.tencent.com/document/product/647/32176#using_cpp)  
- [Windows 集成指引](https://cloud.tencent.com/document/product/647/32178#using_cpp)  

>?
>- 目前 C++ 接口仅提供在精简版（TRTC）中。  
>- Windows 平台中，TRTC头文件已自动使用“trtc”命名空间，无需重复指定。

## ITRTCCloud @ TXLiteAVSDK

### 创建实例和事件回调
| API | 描述 |
|-----|-----|
| [getTRTCShareInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ga0ef57994050abf58a18a3defd4cc5fd0) | 创建 TRTCCloud 实例（单例模式） |
| [destroyTRTCShareInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#gaadc9070c962327451dbc949a4c5a4681) | 销毁 TRTCCloud 实例（单例模式）  |
| [addCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a6a8317825ffe59ddcf1159a778dd7577) | 设置 TRTC 事件回调 |
| [removeCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad088226e8af2d6764851efe7bd94652d) | 移除 TRTC 事件回调 |

### 房间相关接口函数
| API | 描述 |
|-----|-----|
| [enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0fab3ea6c23c6267112bd1c0b64aa50b) | 进入房间 |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ab3881c8829e7b8a3132e7b551e62fbf1) | 离开房间 |
| [switchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a4705f2f116a1ec85bbc60ecaf552c89d) | 切换角色 |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1f3bed34f92b3ff908beb2d0ed2866c9) | 切换房间 |
| [connectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ab5a0622e5d3d521d79ba4f85c44244eb) | 请求跨房通话 |
| [disconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a08870fd955f90d02879e966dcd02bfd3) | 退出跨房通话 |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a7a0238314fc1e1f49803c0b22c1019d5) | 设置订阅模式（需要在进入房前设置才能生效） |
| [createSubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a5ce8b3f393ad3e46a3af39b045c1c5a2) | 创建子房间示例（用于多房间并发观看） |
| [destroySubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a980cf4d173abfb58c00ef35a20e12c85) | 销毁子房间示例 |

### CDN 相关接口函数
| API | 描述 |
|-----|-----|
| [startPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a7cbe48ea2cd3fb05a5b10350b6d81265) | 开始向腾讯云直播 CDN 上发布音视频流 |
| [stopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ac4d3f88b6e067f32d1191878b6db1645) | 停止向腾讯云直播 CDN 上发布音视频流 |
| [startPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a26e2d0b06211185d52836ffbdeddc3d1) | 开始向非腾讯云 CDN 上发布音视频流 |
| [stopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a9cf56c1f3a9aadf4c6123f44e1494a1b) | 停止向非腾讯云 CDN 上发布音视频流 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a8c835f1d49ab0f80a85569e030689850) | 设置云端混流的排版布局和转码参数 |

### 视频相关接口函数
| API | 描述 |
|-----|-----|
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a8ac23e725c7ed75488df1be2ee514884) | 开启本地摄像头的预览画面（移动端） |
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a8ac23e725c7ed75488df1be2ee514884) | 开启本地摄像头的预览画面（桌面端） |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0af978a75d5ba671b7ce5f0b81b003c8) | 更新本地摄像头的预览画面 |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#af7003d2c12f5f783115ada43a715abe7) | 停止摄像头预览 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a22804c4112dee8c76475619f891e2eb5) | 暂停/恢复发布本地的视频流 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a5c5ea936418b106c2e801db57938dde9) | 订阅远端用户的视频流，并绑定视频渲染控件 |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a027a8b23a363dc91e6ce1c9773ee8664) | 更新远端用户的视频渲染控件 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#abd186570272cd61b4a6e4aea870437e1) | 停止订阅远端用户的视频流，并释放渲染控件 |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a7a55fb85c4135abfbe00af529cdaf9bc) | 停止订阅所有远端用户的视频流，并释放全部渲染资源 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a74d8d9922a771114804517db66657f65) | 暂停/恢复订阅远端用户的视频流 |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aa0d0d63eff6bbee7651ead569646b70b) | 暂停/恢复订阅所有远端用户的视频流 |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a55b0710284e44ba3703e22b07c3665c8) | 设置视频编码器的编码参数 |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad21668c7550aad44f1ed61265ffceb24) | 设置网络质量控制的相关参数 |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#acf1e58c46f0c160ab1a17706ea1aa735) | 设置本地画面的渲染参数 |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ab0bd203a8dd3c07910249b1c3e0df9e6) | 设置远端画面的渲染模式 |
| [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a932ff32ec07b20a0e0d83bb434cfb691) | 设置视频编码器输出的画面方向 |
| [setVideoEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a251af554d7257ec64e84027136ae21ef) | 设置编码器输出的画面镜像模式 |
| [enableSmallVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a5019a8005cd96662ce2cface662a811e) | 开启大小画面双路编码模式 |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad2c6cc256f6e24178cd7c9cd2290ea4d) | 切换指定远端用户的大小画面 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a8cf480979530c705c04d3c1715787f6c) | 视频画面截图 |

### 音频相关接口函数
| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a86c80ed357798e50ccf5c7ae47317f4c) | 开启本地音频的采集和发布 |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a47c51247d112b86d2397744c8f3c686b) | 停止本地音频的采集和发布 |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1e1f27f131da042ca6e80beaa18055a8) | 暂停/恢复发布本地的音频流 |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ae22224501b484166dac65c1873ecdbc3) | 暂停/恢复播放远端的音频流 |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a38177742eaf9bedf11109452230319c4) | 暂停/恢复播放所有远端用户的音频流 |
| [setRemoteAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ac49fa4a92105f01e2e296b20881a8324) | 设定某一个远端用户的声音播放音量 |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a8677a812326511ef92f963bbe049d42e) | 设定本地音频的采集音量 |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aed4cdd35906d151cd97f543332fb9f02) | 获取本地音频的采集音量 |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a338984f5503d59ae06d67f55bd8f0766) | 设定远端音频的播放音量 |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ae66cc77d6dfccb4c473eff062d0eb717) | 获取远端音频的播放音量 |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a3127ec82f1610ac2bc0cb7d32b9bb4b9) | 启用音量大小提示 |
| [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a5224523e00d5167eb75cee9b65f72677) | 开始录音 |
| [stopAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a052a606496ce98cdc5a7e93098598a32) | 停止录音 |
| [startLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a55c3e8982056532a6cce56e3f7f29241) | 开启本地媒体录制 |
| [stopLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a8b9b6f0608e48c27fc7c646718cb41ba) | 停止本地媒体录制 |
| [setRemoteAudioParallelParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0e6e6434aaa03ce878280125a9c0fa4b) | 设置远端音频流智能并发播放策略 |

### 设备管理相关接口
| API | 描述 |
|-----|-----|
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#acbe34e3a11decb05d8ea28eb494a113a) | 获取设备管理类（TXDeviceManager） |

### 美颜特效和图像水印
| API | 描述 |
|-----|-----|
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a78c7b8eaa17d721cfd6dcac0224dd50b) | 设置美颜、美白、红润等特效 |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a4a1c376670ff4f3fdac8cf30bec78576) | 添加水印 |

### 背景音乐和声音特效
| API | 描述 |
|-----|-----|
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad9da9a5121bb52fbb85890dd857d7e8a) | 获取音效管理类（TXAudioEffectManager） |
| [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a157639a4fa3cc73ffc1982bbd8a8985e) | 开启系统声音采集（仅适用于桌面系统） |
| [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aab0258238e4414c386657151d01ffb23) | 停止系统声音采集（仅适用于桌面系统） |
| [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a52d0f9a999296633b1d859f75d36d5e8) | 设置系统声音的采集音量 |

### 屏幕分享相关接口
| API | 描述 |
|-----|-----|
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ab1fc5a303726a666d30051c836e33fdd) | 开始桌面端屏幕分享（该接口仅支持桌面系统） |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0e09090fe4281c0e78d8eb38496a8ed0) | 停止屏幕分享 |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0dcd89ed2e23706239db98b55dd806d4) | 暂停屏幕分享 |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a9dc10db068b9d8c6a0fcb8b085359f33) | 恢复屏幕分享 |
| [getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad23c03ad142e8a42c49967ff9ccf9592) | 枚举可分享的屏幕和窗口（该接口仅支持桌面系统） |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a9d16af81b2ea2db7b91a8346add13393) | 选取要分享的屏幕或窗口（该接口仅支持桌面系统） |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a542913f5081fb2479137a7416c970e2d) | 设置屏幕分享（即辅路）的视频编码参数（桌面系统和移动系统均已支持） |
| [setSubStreamMixVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aff8dd1456e5bebff5495d84683c7f83e) | 设置屏幕分享时的混音音量大小（该接口仅支持桌面系统） |
| [addExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ac2a8a65dc2c1d0e4ffbd89eeae768fff) | 将指定窗口加入屏幕分享的排除列表中（该接口仅支持桌面系统） |
| [removeExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0bbbff5ea3cd764dbaaad0db887760bf) | 将指定窗口从屏幕分享的排除列表中移除（该接口仅支持桌面系统） |
| [removeAllExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#abb20ff837f1f5955bea349ff95002a10) | 将所有窗口从屏幕分享的排除列表中移除（该接口仅支持桌面系统） |
| [addIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a442186322939f9b93d6c6e0a3ace7bd3) | 将指定窗口加入屏幕分享的包含列表中（该接口仅支持桌面系统） |
| [removeIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a3674c0ee6514d118fddd9a500ccafb03) | 将指定窗口从屏幕分享的包含列表中移除（该接口仅支持桌面系统） |
| [removeAllIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a5d2812b4068e89e6d2a422cd74257246) | 将全部窗口从屏幕分享的包含列表中移除（该接口仅支持桌面系统） |

### 自定义采集和自定义渲染
| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aaeab72ed55be06685e293c3cf92b6f90) | 启用/关闭视频自定义采集模式 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1d8de868187164e20d0e657e44da0bc6) | 向 SDK 投送自己采集的视频帧 |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a166d6ea0b36bc1adf3d3eddde35207c3) | 启用音频自定义采集模式 |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) | 向 SDK 投送自己采集的音频数据 |
| [enableMixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a896ff4b2731488821dd1ce382276ca0c) | 启用/关闭自定义音轨 |
| [mixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a3c99feacd22af10926d5a521ca598ecd) | 向 SDK 混入自定义音轨 |
| [setMixExternalAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ae0031e4af8bb120ef6de164d99886418) | 设置推流时混入外部音频的推流音量和播放音量 |
| [generateCustomPTS](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a33ed1b26695b6b75dc9ce78e5280cbb4) | 生成自定义采集时的时间戳 |
| [setLocalVideoProcessCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a3f6d32bdf3cb0fe72b61455304b975c6) | 设置第三方美颜的视频数据回调 |
| [setLocalVideoRenderCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad64031e060146f7985263aad994fc733) | 设置本地视频自定义渲染回调 |
| [setRemoteVideoRenderCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1efc475e32f06c768330ff80ebffbc8a) | 设置远端视频自定义渲染回调 |
| [setAudioFrameCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a607dc63d8d944869537457c5b92b56e9) | 设置音频数据自定义回调 |
| [setMixedPlayAudioFrameCallbackFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1c4e3c6d0c2653609e748ceeda8bb46e) | 设置最终要由系统播放出的音频帧回调格式 |
| [enableCustomAudioRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a7047f52811cefa10cf020ee20db1b087) | 开启音频自定义播放 |
| [getCustomAudioRenderingFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ac986d3ec66ab6681d94c8eb933b519de) | 获取可播放的音频数据 |

### 自定义消息发送接口
| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a858b11d4d32ee0fd69b42d64a1d65389) | 使用 UDP 通道发送自定义消息给房间内所有用户  |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aa91b261d10bbdb43508e9e2c33697c29) | 使用 SEI 通道发送自定义消息给房间内所有用户  |

### 网络测试接口
| API | 描述 |
|-----|-----|
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ab9052b69fd4e12b5860da03a868e87d7) | 开始进行网速测试（进入房间前使用） |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ad6ba6ea2c5beace98b99ce98d326be4c) | 停止网络测速 |

### 调试相关接口
| API | 描述 |
|-----|-----|
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a11a1bc22514ac5a7bd9052a5cc444147) | 获取 SDK 版本信息 |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aa6551d4e61a7a003d91b045ed2e13466) | 设置 Log 输出级别 |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a589f4eefb2d7380e6bb145a9b0111634) | 启用/禁用控制台日志打印 |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a357393d1eb2f92b7219395162c531e65) | 启用/禁用日志的本地压缩 |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#afbacbfc33a72f8fdd6995cf1ec3d04a6) | 设置本地日志的保存路径 |
| [setLogCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a239c5b9962a95a1eb4662440fab682fd) | 设置日志回调 |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a7df528c2024556a073b4668879dff91f) | 显示仪表盘 |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a187cb56ce8bbdf9a74e347954d2c7c6a) | 调用实验性接口 |

### 废弃接口
| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#aaeab72ed55be06685e293c3cf92b6f90) | 启用视频自定义采集模式 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1d8de868187164e20d0e657e44da0bc6) | 投送自己采集的视频数据 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a22804c4112dee8c76475619f891e2eb5) | 暂停/恢复发布本地的视频流 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a74d8d9922a771114804517db66657f65) | 暂停 / 恢复订阅远端用户的视频流 |
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ab9052b69fd4e12b5860da03a868e87d7) |  开始进行网络测速（进入房间前使用） |

### 错误和警告事件
| API | 描述 |
|-----|-----|
| [onError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a9724da0b3da9b2eca5736fa8e54aa410) | 错误事件回调 |
| [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a53169ea41d90506cccbff507ba1932a4) | 警告事件回调 |

### 房间相关事件回调
| API | 描述 |
|-----|-----|
| [onEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a236a49e0525615b6435eaa826b7caffe) | 进入房间成功与否的事件回调 |
| [onExitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0a45883a23a200b0e9ea38fdde1da4bd) | 离开房间的事件回调 |
| [onSwitchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a248335805c125e225cfec249697f2299) | 切换角色的事件回调 |
| [onSwitchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ac5889e412f38769f2d21887f9bd7eeec) | 切换房间的结果回调 |
| [onConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a62333366a3a1ab09dc2b2f627a8a1bdd) | 请求跨房通话的结果回调 |
| [onDisconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a292d6661cb93ba30ff68b1f88cf173f1) | 结束跨房通话的结果回调 |

### 用户相关事件回调
| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a43704996ae1f50749b7c7140755350f1) | 有用户加入当前房间 |
| [onRemoteUserLeaveRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a5f7c705f3894d3a430ef1fac8bf8e2c5) | 有用户离开当前房间 |
| [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a091f1c94ff1e2bc39c36e9d34285e87a) | 某远端用户发布/取消了主路视频画面 |
| [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a460922e4fb4b000d1dbd27b596dd0e5c) | 某远端用户发布/取消了辅路视频画面 |
| [onUserAudioAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a6f449dc5294e369750bc15a39eaa856c) | 某远端用户发布/取消了自己的音频 |
| [onFirstVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ad28d27badd56ac274c44720cc9f253d5) | SDK 开始渲染自己本地或远端用户的首帧画面 |
| [onFirstAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a123616289b3219bc36137bc77e8e8b7a) | SDK 开始播放远端用户的首帧音频 |
| [onSendFirstLocalVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a454ea7e7103b2838440cafba3e524433) | 自己本地的首个视频帧已被发布出去 |
| [onSendFirstLocalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0bd950cb774fd40cfdc2fbff885295d2) | 自己本地的首个音频帧已被发布出去 |
| [onRemoteVideoStatusUpdated](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a967a9b593385a8081083e84d3f5648b5) | 远端视频状态变化的事件回调 |

### 网络和技术指标统计回调
| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a377441bace65d98a1218817914a12ecb) | 网络质量的实时统计回调 |
| [onStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ae7e4117f9c8004c9bcc5a29d64e840c9) | 音视频技术指标的实时统计回调 |
| [onSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a7bbfbd86185f20935f8a23d7dad94d9a) | 网速测试的结果回调 |

### 与云端连接情况的事件回调
| API | 描述 |
|-----|-----|
| [onConnectionLost](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a34c34705bb67127ff6d28700cf2ab591) | SDK 与云端的连接已经断开 |
| [onTryToReconnect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#afe74dff22fde93fe0f07fcf18153d334) | SDK 正在尝试重新连接到云端 |
| [onConnectionRecovery](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ae90cd149a676418016cb8736b217f1a8) | SDK 与云端的连接已经恢复 |

### 硬件设备相关事件回调
| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a13a9ad0933b7ab872987e432f005e8ad) | 摄像头准备就绪 |
| [onMicDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0ba02a5d9009ebb9c4e80c0c43c80bca) | 麦克风准备就绪 |
| [onUserVoiceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a61df1f9eec0bfcebf421be865275ffc5) | 音量大小的反馈回调 |
| [onDeviceChange](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ac86c1b0d445a33f6340394b3b78490bd) | 本地设备的通断状态发生变化（仅适用于桌面系统） |
| [onAudioDeviceCaptureVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a40eeba4a6034450bc055b8f62c763520) | 当前麦克风的系统采集音量发生变化 |
| [onAudioDevicePlayoutVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ad87c12c924b781b3b8429f8e8aafc338) | 当前系统的播放音量发生变化 |
| [onSystemAudioLoopbackError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a296665d16719c02dc055c983f88b40c3) | 系统声音采集是否被成功开启的事件回调（仅适用于 Mac 系统） |
| [onTestMicVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a9f0101fa8222c6163f1b23fcce81e22b) | 测试麦克风时的音量回调 |
| [onTestSpeakerVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a04bb10b06af17cdc43b7831336736539) | 测试扬声器时的音量回调 |

### 自定义消息的接收事件回调
| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0a5690652db3902e98e1168bad12ec1a) | 收到自定义消息的事件回调 |
| [onMissCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ab5d0cb61c24b77ecdb177ff19fc95075) | 自定义消息丢失的事件回调 |
| [onRecvSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ab364b929cd0d9ffff6e47c20ec52372c) | 收到 SEI 消息的回调 |

### CDN 相关事件回调
| API | 描述 |
|-----|-----|
| [onStartPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a345ab7b45a9d0027926dbf580e8e0258) | 开始向腾讯云直播 CDN 上发布音视频流的事件回调 |
| [onStopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a8e046f5bd34498b13ae057caaab64913) | 停止向腾讯云直播 CDN 上发布音视频流的事件回调 |
| [onStartPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a16164548764979e84d3b5301f28890ff) | 开始向非腾讯云 CDN 上发布音视频流的事件回调 |
| [onStopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0da75e040521c0945c3735f4893e6c09) | 停止向非腾讯云 CDN 上发布音视频流的事件回调 |
| [onSetMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0f11cee9e2659f7ea8484fdffd6b8583) | 设置云端混流的排版布局和转码参数的事件回调 |

### 屏幕分享相关事件回调
| API | 描述 |
|-----|-----|
| [onScreenCaptureStarted](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a8baff9a6c699ea1d82c5e7abb6ded97b) | 屏幕分享开启的事件回调 |
| [onScreenCapturePaused](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a32acecdafd9058cc7d70a3abe6995051) | 屏幕分享暂停的事件回调 |
| [onScreenCaptureResumed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a63c073daf1ad93cfa2e6c79695434e22) | 屏幕分享恢复的事件回调 |
| [onScreenCaptureStoped](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a4d182e6b60d8be536e69253d906af84d) | 屏幕分享停止的事件回调 |
| [onScreenCaptureCovered](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a490f827ffd6e7728a6ec49cba63875b1) | 屏幕分享的目标窗口被遮挡的事件回调（仅适用于 Windows 操作系统） |

### 本地录制和本地截图的事件回调
| API | 描述 |
|-----|-----|
| [onLocalRecordBegin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a4a40b1b338d93c871f73354d1d45f24b) | 本地录制任务已经开始的事件回调 |
| [onLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a0b226b8e627dad7850a880d48ffb91dd) | 本地录制任务正在进行中的进展事件回调 |
| [onLocalRecordComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a4455252d3e0f5d869db18641e24da106) | 本地录制任务已经结束的事件回调 |
| [onSnapshotComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a10501027a79d1d05231319570c0e5603) | 本地截图完成的事件回调 |

### 废弃的事件回调
| API | 描述 |
|-----|-----|
| [onUserEnter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ad606b861a3545832fb4821a7e0230925) | 有主播加入当前房间（已废弃） |
| [onUserExit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#abbc4fe2ccac90f77c80f55d46d6c8951) | 有主播离开当前房间（已废弃） |
| [onAudioEffectFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#aab3c91276b6e570ea9acfe1581e1aa51) | 音效播放已结束（已废弃） |
| [onPlayBGMBegin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ad93b8204416558e63c18349bf29ff592) | 开始播放背景音乐（已废弃） |
| [onPlayBGMProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a1879cc4e50492431a3346828e9130f21) | 背景音乐的播放进度回调（已废弃） |
| [onPlayBGMComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#abaf89c758a4dd21e21db488e997bef2a) | 背景音乐播放已经结束（已废弃） |
| [onSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a455264cfcf2a7a3f022f3bce0659f9f7) | 服务器测速的结果回调（已废弃） |

### 视频数据自定义回调
| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#aea602851c96370558a7eeb850d7eb6b8) | 自定义视频渲染回调 |
| [onProcessVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#aa416979597d1bec68dc268a9432619ae) | 用于对接第三方美颜组件的视频处理回调 |

### 音频数据自定义回调
| API | 描述 |
|-----|-----|
| [onCapturedRawAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a1488e35460441c351cab75d9702498f6) | 本地麦克风采集到的原始音频数据回调 |
| [onLocalProcessedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#affb432a77f938d1e8dfb6c0d5488dbcf) | 本地采集并经过音频模块前处理后的音频数据回调 |
| [onPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ab841da62beb88a9fa9bce58d25df6f23) | 混音前的每一路远程用户的音频数据 |
| [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a6649f62d4138d9bc73ae484e63dec081) | 将各路待播放音频混合之后并在最终提交系统播放之前的数据回调 |

### 更多事件回调接口
| API | 描述 |
|-----|-----|
| [onLog](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a2fa3d9997c9810ffa6a95e0a7a4a50d0) | 本地 LOG 的打印回调 |

### 视频相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#gace04ad7a0bf531f4d09dc6a540f09f95) | 视频分辨率 |
| [TRTCVideoResolutionMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#gaa6787a9059d7b725a30ffcf9f4aabb64) | 视频宽高比模式 |
| [TRTCVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga461563be214e8f0579a79741f37d18e3) | 视频流类型 |
| [TRTCVideoFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga496a32286104187149b4e40284cbfb36) | 视频画面填充模式 |
| [TRTCVideoRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga4f8ab82260baa03f83f123ebeaa82b2e) | 视频画面旋转方向 |
| [TRTCBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga46f49720df57d17b267054cb9ee4d079) | 美颜（磨皮）算法 |
| [TRTCVideoPixelFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga98b07c6c79303f486682b3b92fa88c7e) | 视频像素格式 |
| [TRTCVideoBufferType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga3a075ea5603cdd730550b37fc0032c68) | 视频数据传递方式 |
| [TRTCVideoMirrorType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga778fcc2797d6076745997327c8b20009) | 视频的镜像类型 |
| [TRTCSnapshotSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga65de3d8416c7faabe1a8b77a6fd9cc7c) | 本地视频截图的数据源 |

### 网络相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCAppScene](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#gaa57f4545ef7331e3157eee1639d28780) | 应用场景 |
| [TRTCRoleType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga42ff820a33d9f3535d203fd5d6782cb5) | 角色 |
| [TRTCQosControlMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga6615b296e31fc3d03c0df92e9755b5aa) | 流控模式（已废弃） |
| [TRTCVideoQosPreference](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga60efcaeea7692bbce8dc362856683319) | 画质偏好 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCQualityInfo) | 网络质量 |
| [TRTCAVStatusType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga9ab84e3f9458dacd479937e5a24c95f2) | 视频状态类型 |
| [TRTCAVStatusChangeReason](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga37b6311e4d5ba7376070ba65de520865) | 视频状态变化原因类型 |

### 音频相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga96f3d4cdcf3baa9df39ab4e1b3f0eb40) | 声音音质 |

### 更多枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#gafa83683b4840bcb3200d1da63c10276d) | Log 级别 |
| [TRTCScreenCaptureSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#gad96fcfd4a65c0f99579b0c35ef86645d) | 屏幕分享的目标类型（仅适用于桌面端） |
| [TRTCTranscodingConfigMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#gaec50c849a17b7706f6989d718fc6b7df) | 云端混流的排版模式 |
| [TRTCLocalRecordType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga92580ecee493fb524b84234305316238) | 媒体录制类型 |
| [TRTCMixInputType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga323584f89d0479be0a1b554ec05672f7) | 混流输入类型 |
| [TRTCDeviceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/namespaceliteav.html#abaf3d3254d2b2e11fb2064478975be17) | 设备类型（仅适用于桌面平台） |
| [TRTCAudioRecordingContent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ga5adbddb520b6eea48142c3b5be740205) | 音频录制内容类型 |

### TRTC 核心类型定义
| API | 描述 |
|-----|-----|
| [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCParams) | 进房参数 |
| [TRTCVideoEncParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCVideoEncParam) | 视频编码参数 |
| [TRTCNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCNetworkQosParam) | 网络流控（Qos）参数集 |
| [TRTCRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCRenderParams) | 视频画面的渲染参数 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCQualityInfo) | 网络质量 |
| [TRTCVolumeInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCVolumeInfo) | 音量大小 |
| [TRTCSpeedTestParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCSpeedTestParams) | 测速参数 |
| [TRTCSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCSpeedTestResult) | 网络测速结果 |
| [TRTCVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCVideoFrame) | 视频帧信息 |
| [TRTCAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCAudioFrame) | 音频帧数据 |
| [TRTCMixUser](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#ac5b1947f21f77726cbff822eaf0003f9) | 云端混流中各路画面的描述信息 |
| [TRTCTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCTranscodingConfig) | 云端混流的排版布局和转码参数 |
| [TRTCPublishCDNParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCPublishCDNParam) | 向非腾讯云 CDN 上发布音视频流时需设置的转推参数 |
| [TRTCAudioRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCAudioRecordingParams) | 本地音频文件的录制参数 |
| [TRTCLocalRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCLocalRecordingParams) | 本地媒体文件的录制参数 |
| [TRTCAudioEffectParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCAudioEffectParam) | 音效参数（已废弃） |
| [TRTCSwitchRoomConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCSwitchRoomConfig) | 房间切换参数 |
| [TRTCAudioFrameCallbackFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCAudioFrameCallbackFormat) | 音频自定义回调的格式参数 |
| [TRTCScreenCaptureSourceInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#structliteav_1_1TRTCScreenCaptureSourceInfo) | 屏幕分享的目标信息（仅适用于桌面系统） |
| [ITRTCScreenCaptureSourceList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__cplusplus.html#classliteav_1_1ITRTCScreenCaptureSourceList) | 可分享的屏幕和窗口的列表 |


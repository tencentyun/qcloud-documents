## TRTCCloud @ TXLiteAVSDK

### 创建实例和事件回调
| API | 描述 |
|-----|-----|
| [sharedInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab6884975e069628328d05cf0e2c3dc67) | 创建 TRTCCloud 实例（单例模式） |
| [destroySharedIntance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad8961d03736d8a52df5a3a991d0a77c4) | 销毁 TRTCCloud 实例（单例模式）  |
| [delegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6a8e20d57b7890e4dbf6652c426d7015) | 设置 TRTC 事件回调 |
| [delegateQueue](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a97158c52f2a4011454b4eb3ee369a8a1) | 设置驱动 TRTCCloudDelegate 事件回调的队列 |

### 房间相关接口函数
| API | 描述 |
|-----|-----|
| [enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d) | 进入房间 |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a715f5b669ad1d7587ae19733d66954f3) | 离开房间 |
| [switchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5f4598c59a9c1e66938be9bfbb51589c) | 切换角色 |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7c5a2aa06d649492f546d9c70a5de4a1) | 切换房间 |
| [connectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a062bc48550b479a6b7c1662836b8c4a5) | 请求跨房通话 |
| [disconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abd656e4c9b6a01231810ae897627e9bc) | 退出跨房通话 |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ada2e2155e0e7c3001c6bb6dca1d93048) | 设置订阅模式（需要在进入房前设置才能生效） |
| [createSubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6100a5f395442d38ce9adab922382caf) | 创建子房间示例（用于多房间并发观看） |
| [destroySubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a19e0d7921ac494fb588a4654d97abe86) | 销毁子房间示例 |

### CDN 相关接口函数
| API | 描述 |
|-----|-----|
| [startPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6d2f4d81f0944072053d7dc9e9265f22) | 开始向腾讯云直播 CDN 上发布音视频流 |
| [stopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afc00ba747be5299cd7235928a628339e) | 停止向腾讯云直播 CDN 上发布音视频流 |
| [startPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aad42e78d355fd563b959a5053bac54cb) | 开始向非腾讯云 CDN 上发布音视频流 |
| [stopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5d8a86795b8a2d7eaf9be7157dd9b8dd) | 停止向非腾讯云 CDN 上发布音视频流 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a8d589d96e548a26c7afb5d1f2361ec93) | 设置云端混流的排版布局和转码参数 |

### 视频相关接口函数
| API | 描述 |
|-----|-----|
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa94bd93a491a7302cc85245c4810a68c) | 开启本地摄像头的预览画面（移动端） |
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa94bd93a491a7302cc85245c4810a68c) | 开启本地摄像头的预览画面（桌面端） |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf20f249b4b43fff64f944b4aefe54cb) | 更新本地摄像头的预览画面 |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01ee967e3180a5e2fc0e37e9e99e85b3) | 停止摄像头预览 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac3a158f935a99abd4965d308c0f88977) | 暂停/恢复发布本地的视频流 |
| [setVideoMuteImage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad730c168c066599b6c4c987fd7b7c3a2) | 设置本地画面被暂停期间的替代图片 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5ef41fa3d7f5e88f638747325a0b9fa1) | 订阅远端用户的视频流，并绑定视频渲染控件 |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a518d3a8a3b4a4cfd8b5e0dfe7899756b) | 更新远端用户的视频渲染控件 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a07b8d05d93d2ef7d543772bff6d451a5) | 停止订阅远端用户的视频流，并释放渲染控件 |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aaa75cd1b98c226bb7b8a19412b204d2b) | 停止订阅所有远端用户的视频流，并释放全部渲染资源 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae5b271bc92a7a4d8ffbcbd4c2e509305) | 暂停/恢复订阅远端用户的视频流 |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#adf7cd002366760749c6f4d1ee9291db1) | 暂停/恢复订阅所有远端用户的视频流 |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a57938e5b62303d705da2ceecf119d74e) | 设置视频编码器的编码参数 |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac72a8a85131cb7716b1eec799250aba9) | 设置网络质量控制的相关参数 |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5d4f0aba952a355f153d374899e6dcec) | 设置本地画面的渲染参数 |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7147d9c93af6a92f594ea394fc796081) | 设置远端画面的渲染模式 |
| [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a200c174b27bbe7397b0639e707ee6547) | 设置视频编码器输出的画面方向 |
| [setVideoEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a29a7cae6b4e82098fc342d4f0066d2ad) | 设置编码器输出的画面镜像模式 |
| [setGSensorMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7a8c22e2f02d313590d4c499e18ebe3f) | 设置重力感应的适配模式 |
| [enableEncSmallVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2aa9c464203b1c62cbb9ccabccc6334a) | 开启大小画面双路编码模式 |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a49440df0907b12c0ad8fe9e93bdbed0d) | 切换指定远端用户的大小画面 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac0db9a4bcb61e3b369740a1986683cdf) | 视频画面截图 |

### 音频相关接口函数
| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acd85c726c425eda7cac82cba0f83a465) | 开启本地音频的采集和发布 |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab78601c38f1b872b03b662e6856be84c) | 停止本地音频的采集和发布 |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4ada386a75d8042a432da05fde5552d9) | 暂停/恢复发布本地的音频流 |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afede3cc79a8d68994857b410fb5572d2) | 暂停/恢复播放远端的音频流 |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a75148bf8a322c852965fe774cbc7dd14) | 暂停/恢复播放所有远端用户的音频流 |
| [setAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa62f2af2d86a64c0ebc7b9f00e4a54fe) | 设置音频路由 |
| [setRemoteAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a8d38580f2c35f7e9828c4e41c56db35a) | 设定某一个远端用户的声音播放音量 |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5475b81c1712323257c10baaf7ad6969) | 设定本地音频的采集音量 |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7ce26486575e72bc445432929fdff26c) | 获取本地音频的采集音量 |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af2602b1e9dfe932c89dd411f2f227192) | 设定远端音频的播放音量 |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aba445625df38b8676d599df4a67a8407) | 获取远端音频的播放音量 |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a57d48cb0dbd7705486453b46e30e3fea) | 启用音量大小提示 |
| [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9eadd65cef0ac6b9c04ddfd7265afb01) | 开始录音 |
| [stopAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac8c12476bbcf3d691060954fcdb6ebe6) | 停止录音 |
| [startLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5075d55a6fc31895eedd5b23a1b8826b) | 开启本地媒体录制 |
| [stopLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#affae72630393980fee79c21f2d20f602) | 停止本地媒体录制 |
| [setRemoteAudioParallelParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a02ad0bcebe3962fefee9af07039f0657) | 设置远端音频流智能并发播放策略 |

### 设备管理相关接口
| API | 描述 |
|-----|-----|
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a950f3f1c949def9e1e470f467db7b27a) | 获取设备管理类（TXDeviceManager） |

### 美颜特效和图像水印
| API | 描述 |
|-----|-----|
| [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4fb05ae6b5face276ace62558731280a) | 获取美颜管理类（TXBeautyManager） |
| [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad0bedbddf415d26cff8242d5842a0908) | 添加水印 |

### 背景音乐和声音特效
| API | 描述 |
|-----|-----|
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af962213fefe6988a08820ac9af00df66) | 获取音效管理类（TXAudioEffectManager） |
| [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2979e32c019708dcc9209bb6d2db9486) | 开启系统声音采集（仅适用于 Mac 系统） |
| [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#adef486f26a2c7d74a8cccb537367e66a) | 停止系统声音采集（仅适用于桌面系统） |
| [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afc45226807d84673bab78b21d1be54ae) | 设置系统声音的采集音量 |

### 屏幕分享相关接口
| API | 描述 |
|-----|-----|
| [startScreenCaptureInApp](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf51acf26b2212192f7145468886b791) | 开始应用内的屏幕分享（仅支持 iOS 13.0 及以上系统） |
| [startScreenCaptureByReplaykit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abebcd402e310d5d7dcbef9f6b601cfc4) | 开始全系统的屏幕分享（仅支持 iOS 11.0 及以上系统） |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a59b16baa51d86cc0465dc6edd3cbfc97) | 开始桌面端屏幕分享（该接口仅支持桌面系统） |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa8ea0235691fc9cde0a64833249230bb) | 停止屏幕分享 |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6f536bcc3df21b38885809d840698280) | 暂停屏幕分享 |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af257a8fb6969fe908ca68a039e6dba15) | 恢复屏幕分享 |
| [getScreenCaptureSourcesWithThumbnailSize](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a37df498cbc8d9b1135e3caafdcee906f) | 枚举可分享的屏幕和窗口（该接口仅支持 Mac OS 系统） |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01ead6fb3106ea266caa922f5901bf18) | 选取要分享的屏幕或窗口（该接口仅支持 Mac OS 系统） |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abc0f3cd5c320d0e65163bd07c3c0a735) | 设置屏幕分享（即辅路）的视频编码参数（桌面系统和移动系统均已支持） |
| [setSubStreamMixVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a18d3fb6535c9884784c5ad5f8dfd0b12) | 设置屏幕分享时的混音音量大小（该接口仅支持桌面系统） |
| [addExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa567171999b17a7f5655213b193415a7) | 将指定窗口加入屏幕分享的排除列表中（该接口仅支持桌面系统） |
| [removeExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a95b1f3fbc6ff755f67f7e9b86240ea5f) | 将指定窗口从屏幕分享的排除列表中移除（该接口仅支持桌面系统） |
| [removeAllExcludedShareWindows](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab2b6a778a528d58e2a42c9adfc7684f2) | 将所有窗口从屏幕分享的排除列表中移除（该接口仅支持桌面系统） |
| [addIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2e101f0ff00c8752eea1fa9a1a432233) | 将指定窗口加入屏幕分享的包含列表中（该接口仅支持桌面系统） |
| [removeIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a058ac1e2141d6eb1962219167add42bc) | 将指定窗口从屏幕分享的包含列表中移除（该接口仅支持桌面系统） |
| [removeAllIncludedShareWindows](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a18a20767a0e1076ba16cd473a2512156) | 将全部窗口从屏幕分享的包含列表中移除（该接口仅支持桌面系统） |

### 自定义采集和自定义渲染
| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af53f530fe2025d72e2479928dd6db52f) | 启用/关闭视频自定义采集模式 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5a68c4f0cd3a79100b331fc17d4b2858) | 向 SDK 投送自己采集的视频帧 |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab8f8aaa19d70c6a2c9d62ecceb6e974d) | 启用音频自定义采集模式 |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a62cab4ec7c336ae135c2f681aca25da1) | 向 SDK 投送自己采集的音频数据 |
| [enableMixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1101d883d65882f735e3d17f874a25cb) | 启用/关闭自定义音轨 |
| [mixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9f408915460e86e889056066ca4e0908) | 向 SDK 混入自定义音轨 |
| [setMixExternalAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abd8823c40d31e122ed34f7ac33c678a6) | 设置推流时混入外部音频的推流音量和播放音量 |
| [generateCustomPTS](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae5f2a974fa23954c5efd682dc464cdee) | 生成自定义采集时的时间戳 |
| [setLocalVideoProcessDelegete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2f73c33b1010a63bd3a06e639b3cf348) | 设置第三方美颜的视频数据回调 |
| [setLocalVideoRenderDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aba3d309645d27304b6d4ea31b21a4cda) | 设置本地视频自定义渲染回调 |
| [setRemoteVideoRenderDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5244e73ac27599370f966575e11959ff) | 设置远端视频自定义渲染回调 |
| [setAudioFrameDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01726b03b102c32222a2a26b16abcd48) | 设置音频数据自定义回调 |
| [setCapturedRawAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4b58b1ee04d0c692f383084d87111f86) | 设置本地麦克风采集出的原始音频帧回调格式 |
| [setLocalProcessedAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9ec7c7123eb2f333769508de193ea51f) | 设置经过前处理后的本地音频帧回调格式 |
| [setMixedPlayAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a24ad642b88cd3b2ca2d3044d72817090) | 设置最终要由系统播放出的音频帧回调格式 |
| [enableCustomAudioRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a325da4ec57db06b91b74da8699b47d7c) | 开启音频自定义播放 |
| [getCustomAudioRenderingFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aeebe3811918c8250d32d872fee83a2c2) | 获取可播放的音频数据 |

### 自定义消息发送接口
| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acbc86da0cb558c549f42e7e987c7beaf) | 使用 UDP 通道发送自定义消息给房间内所有用户  |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6de26e5efddf899d31158e4d48f17c02) | 使用 SEI 通道发送自定义消息给房间内所有用户  |

### 网络测试接口
| API | 描述 |
|-----|-----|
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a914bc4bdd1f0f0e02f27f873acb7e576) | 开始进行网速测试（进入房间前使用） |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a58d732ba648d1f9a3a460c02de79bb9b) | 停止网络测速 |

### 调试相关接口
| API | 描述 |
|-----|-----|
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ace5acd2fe597b6656b45aaa93e3e45a1) | 获取 SDK 版本信息 |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9d2b6a99e137a9667743edc8ac909493) | 设置 Log 输出级别 |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a177c4f1fbb2a011ff496417dc0245667) | 启用/禁用控制台日志打印 |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa51a341a43a854ac6e3fa1d0093fec95) | 启用/禁用日志的本地压缩 |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a93b48089741f7022aea1f8f93ce8fff9) | 设置本地日志的保存路径 |
| [setLogDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a41497e4242e3c42acfa35730cdc1ddf6) | 设置日志回调 |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3bd71c8a99029c1a4708bf1c176aa299) | 显示仪表盘 |
| [setDebugViewMargin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aad41ff6d5b5565046911acf27bb3dee4) | 设置仪表盘的边距 |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a16c53e91f9b32aaf4bf3d409a3790ef6) | 调用实验性接口 |

### 废弃接口
| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abb57991f5e4f4ca1b95c2181a7e538c8) | 设置麦克风的音量大小 |
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1336146862fb742de6cbe5718f9b7008) | 设置美颜、美白以及红润效果级别 |
| [setEyeScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae0e4341ef565cc5ba28101574179cd56) | 设置大眼级别 |
| [setFaceScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a52ad635b237ccb1eef53a4ed9e650035) | 设置瘦脸级别 |
| [setFaceVLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1bf6dd0f5a5c6c013323d31f60d494e2) | 设置 V 脸级别 |
| [setChinLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a145d4ed3d5790a449a9884d282420216) | 设置下巴拉伸或收缩幅度 |
| [setFaceShortLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac11082c88aba749acd7cd2c7a7caa953) | 设置短脸级别 |
| [setNoseSlimLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae94b107a9c476337585906c79b42ee95) | 设置瘦鼻级别 |
| [selectMotionTmpl](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3aa8c561d744e3d921dff6186a6e4ade) | 设置动效贴纸 |
| [setMotionMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa6689d734b9f46cb84a848b7e8f39cbd) | 设置动效静音 |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a59b16baa51d86cc0465dc6edd3cbfc97) | 启动屏幕分享 |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1b0c2a9e82a408881281c7468a74f2c0) | 设置色彩滤镜效果 |
| [setFilterConcentration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3b0d7db70674f961c14b316f4e8e7a2b) | 设置色彩滤镜浓度 |
| [setGreenScreenFile](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab4682edfc605ba06e24fd7b3e758ce5d) | 设置绿幕背景视频 |
| [playBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4d9983591fa2a847e226b7a30e8db294) | 启动播放背景音乐 |
| [stopBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a11004f1ba27b057985850a25307b0bec) | 停止播放背景音乐 |
| [pauseBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa4b92d4c989e99612f6c4dab03a78764) | 停止播放背景音乐 |
| [resumeBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aed6e8f224b5f834b1bc0c15f9701f692) | 停止播放背景音乐 |
| [getBGMDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac1f96932d02198cd045ee96f1306c8ba) | 获取背景音乐总时长（单位：毫秒） |
| [setBGMPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7fd043ae358c43f6a178837fb2846ef9) | 设置背景音乐的播放进度 |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#adbfc8e226df7c6caaaca1a89a9842f23) | 设置背景音乐的音量大小 |
| [setBGMPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a08c468f48d99aef0e89716111db1f422) | 设置背景音乐的本地播放音量 |
| [setBGMPublishVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a0cf0c090285038b23843c646009073d1) | 设置背景音乐的远端播放音量 |
| [setReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a555cde4eda63d13bbad0dbdba7094a47) | 设置混响效果 |
| [setVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa60f54923826cc59d8a4526669c4ea5e) | 设置变声类型 |
| [playAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2ae175694198a9b3d1b1647b7ce1dae0) | 播放音效 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a22854b4e9f698cceb1bbb7f7de466ec1) | 设置音效音量 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a22854b4e9f698cceb1bbb7f7de466ec1) | 停止播放音效 |
| [stopAllAudioEffects](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7066509af1de32c290b7cc297cd00f2b) | 停止所有音效 |
| [setAllAudioEffectsVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6b345c95b5b68198d8dbc64a3652ed35) | 设置所有音效音量 |
| [pauseAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab0d46ccb8fca811851b30e7731958024) | 暂停音效 |
| [resumeAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a207dd8909c05d4a8a1431d33e644d4fe) | 暂停音效 |
| [enableAudioEarMonitoring](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa26564f3388bc249ecbd2813d9c45390) | 开启（或关闭）耳返 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5ef41fa3d7f5e88f638747325a0b9fa1) | 开始显示远端视频画面 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a07b8d05d93d2ef7d543772bff6d451a5) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流 |
| [setRemoteViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afda6658d1bf7dc9bc1445838b95d21ff) | 设置远端图像的渲染模式 |
| [setRemoteViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2ef26a9ede0ba4fa6c5739229e1eee90) | 设置远端图像的顺时针旋转角度 |
| [setLocalViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a961596f832657bfca81fd675878a2d15) | 设置本地图像的渲染模式 |
| [setLocalViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4d2d95ad8fbaf8edce18667aa835848e) | 设置本地图像的顺时针旋转角度 |
| [setLocalViewMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af68f13fba5a02e4e9ca338596fb64916) | 设置本地摄像头预览画面的镜像模式 |
| [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a68d048ccd0d018995e33e9e714e14474) | 开始显示远端用户的辅路画面 |
| [stopRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acab6e31898857af876af66e779216203) | 停止显示远端用户的辅路画面 |
| [setRemoteSubStreamViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a487b3cd9a6b41581d4b45c752c5ede4c) | 设置辅路画面的填充模式 |
| [setRemoteSubStreamViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a72c66b67eacd24a0e796a3213219fb6d) | 设置辅路画面的顺时针旋转角度 |
| [setPriorRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2b2d43a3955480f2d6200bf20e66f3cf) | 设定优先观看大画面还是小画面 |
| [setAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2cdffa1529fcaec866404f4f9b92ec53) | 设置音频质量 |
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acd85c726c425eda7cac82cba0f83a465) | 设置音频质量 |
| [switchCamera](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa9a1952f442020bc92ce1beb65959e56) | 切换摄像头 |
| [isCameraZoomSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a8662b8ecab04a55a321ee9f16d0680a7) | 查询当前摄像头是否支持缩放 |
| [setZoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9777fe95f7830746c1ba6b10446c37a0) | 设置摄像头缩放倍数（焦距） |
| [isCameraTorchSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acd005524f8e2c2fbfcc415049e666ced) | 查询是否支持开关闪光灯 |
| [enbaleTorch](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af6b128ee01d91a63dc1976db7a9be555) | 开关/关闭闪光灯 |
| [isCameraFocusPositionInPreviewSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a0e164f727b990581a42f97dca1bf7548) | 查询摄像头是否支持设置焦点 |
| [setFocusPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6a77cc99c41b926cd99909ae1ace39ae) | 设置摄像头焦点坐标位置 |
| [isCameraAutoFocusFaceModeSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5af361145f04227ff1a451fee2705a77) | 查询是否支持自动识别人脸位置 |
| [enableAutoFaceFoucs](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a32a8f584879b17f211df75494a5be96c) | 开启/关闭人脸跟踪对焦 |
| [startCameraDeviceTestInView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1bd6289b969adde0096c83d6a5532332) | 开始进行摄像头测试 |
| [stopCameraDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1b67fa3f322efe538d924b381c06e676) | 开始进行摄像头测试 |
| [startMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa6f467c12fcea7e09cc97861d511498a) | 开始进行麦克风测试 |
| [stopMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a8cca1c5913ac021987680195075e5fc9) | 开始进行麦克风测试 |
| [startSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a60aa520016687bea03f17cb4ec19c1b6) | 开始进行扬声器测试 |
| [stopSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf383f971dc54f0254b2d40f100cc9ca) | 停止进行扬声器测试 |
| [getMicDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5e267aa0d820f78b761be1d485369b3b) | 获取麦克风设备列表 |
| [getCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afa6a82cbf407b0bd6eb63093940e189d) | 获取当前的麦克风设备 |
| [setCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5141fec83e7f071e913bfc539c193ac6) | 选定当前使用的麦克风 |
| [getCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af69d237159163eebcb6876e767d7692e) | 获取当前麦克风的设备音量 |
| [setCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aaa6810f64c153e779697dc2d5bd30f6a) | 设置当前麦克风的设备音量 |
| [getCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae9c936081b96348ce047337a1d3bb7b0) | 获取系统当前麦克风设备是否静音 |
| [setCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a88569e62fe75b7ea98cc012169f22bfe) | 设置系统当前麦克风设备的静音状态 |
| [getSpeakerDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5b888d0ebe697fdc5e11759f1b154fc3) | 获取扬声器设备列表 |
| [getCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9d6d48c3937e3cb2632ced9a6a002368) | 获取当前的扬声器设备 |
| [setCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6c951071ac218930680febd84314ee05) | 设置要使用的扬声器 |
| [getCurrentSpeakerDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa25ac85f6f84b352175aebb9c7007247) | 获取当前扬声器的设备音量 |
| [setCurrentSpeakerDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a019001b23569c8b6da7f3276af58e0a7) | 设置当前扬声器的设备音量 |
| [getCurrentSpeakerDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a793d11364882c7fac7f9200f8761400c) | 获取系统当前扬声器设备是否静音 |
| [setCurrentSpeakerDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a738ea0dffd48d5bc2b05b146eb79ec46) | 设置系统当前扬声器设备的静音状态 |
| [getCameraDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a0a1b764ff4238afaeaba41ee728a1451) | 获取摄像头设备列表 |
| [getCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa238683cb00f508b05b9ac031a17bc37) | 获取当前使用的摄像头 |
| [setCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aae9955bb39985586f7faba841d2692fc) | 选定当前要使用的摄像头 |
| [setSystemVolumeType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab098daa610ae506dbf6c2a4f666ae32c) | 设置系统音量类型 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac0db9a4bcb61e3b369740a1986683cdf) | 视频截图 |
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af53f530fe2025d72e2479928dd6db52f) | 启用视频自定义采集模式 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5a68c4f0cd3a79100b331fc17d4b2858) | 投送自己采集的视频数据 |
| [startScreenCaptureInApp](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf51acf26b2212192f7145468886b791) | 开始应用内的屏幕分享（iOS） |
| [startScreenCaptureByReplaykit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abebcd402e310d5d7dcbef9f6b601cfc4) | 开始全系统的屏幕分享（iOS） |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac3a158f935a99abd4965d308c0f88977) | 暂停/恢复发布本地的视频流 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae5b271bc92a7a4d8ffbcbd4c2e509305) | 暂停 / 恢复订阅远端用户的视频流 |
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a914bc4bdd1f0f0e02f27f873acb7e576) |  开始进行网络测速（进入房间前使用） |

### 错误和警告事件
| API | 描述 |
|-----|-----|
| [onError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a10a711eb68abcacc1ca690501fc7c9fb) | 错误事件回调 |
| [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a25ac0da9ad798a2313bdf8f296828541) | 警告事件回调 |

### 房间相关事件回调
| API | 描述 |
|-----|-----|
| [onEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6960aca54e2eda0f424f4f915908a3c5) | 进入房间成功与否的事件回调 |
| [onExitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6a98fcaac43fa754cf9dd80454897bea) | 离开房间的事件回调 |
| [onSwitchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ade2c2eab48a30e7ca1c9246e573b7f28) | 切换角色的事件回调 |
| [onSwitchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ad848cbee89f8b6258c9f03f4cb253a31) | 切换房间的结果回调 |
| [onConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a69e5b1d59857956f736c204fe765ea9a) | 请求跨房通话的结果回调 |
| [onDisconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a26b34d83afac68928a156096862c9c06) | 结束跨房通话的结果回调 |

### 用户相关事件回调
| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a390831928a4d2a7977c4c1572da8be58) | 有用户加入当前房间 |
| [onRemoteUserLeaveRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#afa7d16e1e4c66d938fc2bc69f3e34c28) | 有用户离开当前房间 |
| [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) | 某远端用户发布/取消了主路视频画面 |
| [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ac45fb0751f7dbd2466a35c8828c9911b) | 某远端用户发布/取消了辅路视频画面 |
| [onUserAudioAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8c885eeb269fc3d2e085a5711d4431d5) | 某远端用户发布/取消了自己的音频 |
| [onFirstVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7fc7fd0144af2bc4ce0797f9de530d96) | SDK 开始渲染自己本地或远端用户的首帧画面 |
| [onFirstAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aafc4536f552199368e48c8527783c410) | SDK 开始播放远端用户的首帧音频 |
| [onSendFirstLocalVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a17567554f413629a80b5970bdffdff7b) | 自己本地的首个视频帧已被发布出去 |
| [onSendFirstLocalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#acb73daf4ce82cd03f787f057b233b412) | 自己本地的首个音频帧已被发布出去 |
| [onRemoteVideoStatusUpdated](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af7fef48407b65423871ed6f7652e4176) | 远端视频状态变化的事件回调 |

### 网络和技术指标统计回调
| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a723002319845fbfc03db501aa9da6c28) | 网络质量的实时统计回调 |
| [onStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#afb0811035e97c8544dbc9ecbef461dd9) | 音视频技术指标的实时统计回调 |
| [onSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6ca73040b7226a8297814694e95478fc) | 网速测试的结果回调 |

### 与云端连接情况的事件回调
| API | 描述 |
|-----|-----|
| [onConnectionLost](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aed43a70b4a95eb95181e2b410013bf54) | SDK 与云端的连接已经断开 |
| [onTryToReconnect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a1c8654b64e4bde42a8a24954ecf2cb2d) | SDK 正在尝试重新连接到云端 |
| [onConnectionRecovery](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a36d96a42ec4b00a0e3808f7f8460cd7f) | SDK 与云端的连接已经恢复 |

### 硬件设备相关事件回调
| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aaa74021e5fd2564afb2df50e25eedeff) | 摄像头准备就绪 |
| [onMicDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#afdac7dee94451913a4dc9982badc8035) | 麦克风准备就绪 |
| [onAudioRouteChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a1859305732dfd03de63c9b780f99d513) | 当前音频路由发生变化（仅适用于移动设备） |
| [onUserVoiceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7775c3fbd84b8da3b7a75bdea27ed5c5) | 音量大小的反馈回调 |
| [onDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a0152908c497bd5ee5225251d9e93e500) | 本地设备的通断状态发生变化（仅适用于桌面系统） |
| [onAudioDeviceCaptureVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a1c36efd81dc4edf88fc3bc6af83b1b5a) | 当前麦克风的系统采集音量发生变化 |
| [onAudioDevicePlayoutVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af24c0f0258e83ab644e242ee0d01277f) | 当前系统的播放音量发生变化 |
| [onSystemAudioLoopbackError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8644f5136138d13ffa8e0ea68f5c3676) | 系统声音采集是否被成功开启的事件回调（仅适用于 Mac 系统） |

### 自定义消息的接收事件回调
| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsgUserId](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a324311b3d4f3930d9a50b8449b155dd3) | 收到自定义消息的事件回调 |
| [onMissCustomCmdMsgUserId](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af1b8e7d0f73773eca509afc1cf4c9ece) | 自定义消息丢失的事件回调 |
| [onRecvSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6e4365456cb4df6e1bdf870511b72042) | 收到 SEI 消息的回调 |

### CDN 相关事件回调
| API | 描述 |
|-----|-----|
| [onStartPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a75c6bf4a7c7ec60a24aabfe8e47ea1f4) | 开始向腾讯云直播 CDN 上发布音视频流的事件回调 |
| [onStopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a379dcf84e15f93b64efe2cb9f362877c) | 停止向腾讯云直播 CDN 上发布音视频流的事件回调 |
| [onStartPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a817783f364bf9f6f0a1df4bc26bad628) | 开始向非腾讯云 CDN 上发布音视频流的事件回调 |
| [onStopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aab032eb48a56e8351ada60ce5b510d5e) | 停止向非腾讯云 CDN 上发布音视频流的事件回调 |
| [onSetMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ab5c98341b7536b5b65c04b835c4d28fb) | 设置云端混流的排版布局和转码参数的事件回调 |

### 屏幕分享相关事件回调
| API | 描述 |
|-----|-----|
| [onScreenCaptureStarted](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7d15537d26fb001045ff95157d59ed3f) | 屏幕分享开启的事件回调 |
| [onScreenCapturePaused](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a9cc6106085b2049838e21bb50e192786) | 屏幕分享暂停的事件回调 |
| [onScreenCaptureResumed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ae9c08ef9dd260cf6fd946209fda8a011) | 屏幕分享恢复的事件回调 |
| [onScreenCaptureStoped](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a323d2b3e5b8b364722e0b161ab11c816) | 屏幕分享停止的事件回调 |

### 本地录制和本地截图的事件回调
| API | 描述 |
|-----|-----|
| [onLocalRecordBegin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a044ce179ac4bc0bc987a3b74ecd911e7) | 本地录制任务已经开始的事件回调 |
| [onLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ab4250c05ea4b843c27385f77d5004fc3) | 本地录制任务正在进行中的进展事件回调 |
| [onLocalRecordComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ae78ca25acea4152bfd9d0ccf71bd4108) | 本地录制任务已经结束的事件回调 |

### 废弃的事件回调
| API | 描述 |
|-----|-----|
| [onUserEnter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af26948706dc0dff24946470066e9c4e0) | 有主播加入当前房间（已废弃） |
| [onUserExit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a72f0a872a13500cb5394f77c586ab3f5) | 有主播离开当前房间（已废弃） |
| [onAudioEffectFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#accb36b0eb1d1b72f32cf72617bb1c730) | 音效播放已结束（已废弃） |

### 视频数据自定义回调
| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7b43888945a9d12f088ed99a5854e3c1) | 自定义视频渲染回调 |
| [onProcessVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8d4f000b4169a64a8a8af15e51e5dd95) | 用于对接第三方美颜组件的视频处理回调 |
| [onGLContextDestory](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a5f6d5ef01d3cd610959433107f78aa60) | SDK 内部 OpenGL 环境被销的通知 |

### 音频数据自定义回调
| API | 描述 |
|-----|-----|
| [onCapturedRawAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aeaeaf9e7091c75e1a072d576a57d7f5c) | 本地麦克风采集到的原始音频数据回调 |
| [onLocalProcessedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a73a3e7de3c5c340957f119bb0f8744b0) | 本地采集并经过音频模块前处理后的音频数据回调 |
| [onRemoteUserAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aa392c17c27bae1505f148bf541b7746a) | 混音前的每一路远程用户的音频数据 |
| [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a5a8a0bf6f8d02c33b2fe01c6175dfd4e) | 将各路待播放音频混合之后并在最终提交系统播放之前的数据回调 |
| [onMixedAllAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a905748efe966e94ec1212fda14161aee) | SDK 所有音频混合后的音频数据（包括采集到的和待播放的） |

### 更多事件回调接口
| API | 描述 |
|-----|-----|
| [onLog](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ab1364c78a6f31a8c08d0138c4f6e9647) | 本地 LOG 的打印回调 |

### 视频相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaa58db9156c82d75257499cb5e0cdf0e5) | 视频分辨率 |
| [TRTCVideoResolutionMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gafdfe57c064658b38b78b0fd11e2706c0) | 视频宽高比模式 |
| [TRTCVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga1974ff7e5e78b4455925faf74e38f1e8) | 视频流类型 |
| [TRTCVideoFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga1a66aad6fff71205c7a266268e16f55c) | 视频画面填充模式 |
| [TRTCVideoRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gae8bd6b06a2ca5f89f9b3cea393fc6eb9) | 视频画面旋转方向 |
| [TRTCBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga9bafd3233be6cec1b380d469017ed3e6) | 美颜（磨皮）算法 |
| [TRTCVideoPixelFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gabb58c142deac29da242c957f21c963e3) | 视频像素格式 |
| [TRTCVideoBufferType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga0fce6f58df3d3021696d15eff683ed8b) | 视频数据传递方式 |
| [TRTCVideoMirrorType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga13da9775774c3251999f1e46d279305f) | 视频的镜像类型 |
| [TRTCSnapshotSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga50f989651c9f893de7716ffbc2d2a5fc) | 本地视频截图的数据源 |

### 网络相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCAppScene](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga6ab617b26cf503a8c1bfec34a9918dbe) | 应用场景 |
| [TRTCRoleType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gad147b9b0249d0c2759cf1514c8978881) | 角色 |
| [TRTCQosControlMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga915f86fec1b00787147d40a189444823) | 流控模式（已废弃） |
| [TRTCVideoQosPreference](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga2c460e7365ad67ee0213545b0a67aa6d) | 画质偏好 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCQualityInfo) | 网络质量 |
| [TRTCAVStatusType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga0a200753a7e0c539ce4f584cd8d17510) | 视频状态类型 |
| [TRTCAVStatusChangeReason](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga349e42c3f8a2de5a031e90a1240d7f54) | 视频状态变化原因类型 |

### 音频相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCAudioSampleRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga346b09a7691ce8c9813bac0feb057d08) | 音频采样率 |
| [TRTCAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga865e618ff3a81236f9978723c00e86fb) | 声音音质 |
| [TRTCAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga81305fea3aae73346d04f0013e0194d4) | 音频路由（即声音的播放模式） |
| [TRTCReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga1c0a768f9f7855e87c486617816c7759) | 声音混响模式 |
| [TRTCVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaeb48457146f2279c912e345ce532ecef) | 变声类型 |
| [TRTCSystemVolumeType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaac0cd0da9dd789dcec4ba16471006f23) | 系统音量类型（仅适用于移动设备） |

### 更多枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gacefec5143acae6d0524b5500f0155908) | Log 级别 |
| [TRTCGSensorMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga894251078222f9ac4ba5815aac4b493c) | 重力感应开关（仅适用于移动端） |
| [TRTCScreenCaptureSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaeabd30a270055e48105a34c781c782b0) | 屏幕分享的目标类型（仅适用于桌面端） |
| [TRTCTranscodingConfigMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga907c7b1ef1f09fb7417a549e82110855) | 云端混流的排版模式 |
| [TRTCRecordType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga4bb9927d377aa27b781fcfef5cf1058a) | 媒体录制类型 |
| [TRTCMixInputType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga9359cd77f4759e5b1a82fe1b94de638d) | 混流输入类型 |
| [TRTCMediaDeviceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga4a04a7c25ed48ab15603e8c3db115b95) | 设备类型（仅适用于桌面平台） |
| [TRTCAudioRecordingContent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gade0f3fa25d9d1c876660e230152567b0) | 音频录制内容类型 |

### TRTC 核心类型定义
| API | 描述 |
|-----|-----|
| [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCParams) | 进房参数 |
| [TRTCVideoEncParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVideoEncParam) | 视频编码参数 |
| [TRTCNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCNetworkQosParam) | 网络流控（Qos）参数集 |
| [TRTCRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCRenderParams) | 视频画面的渲染参数 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCQualityInfo) | 网络质量 |
| [TRTCVolumeInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVolumeInfo) | 音量大小 |
| [TRTCSpeedTestParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCSpeedTestParams) | 测速参数 |
| [TRTCSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCSpeedTestResult) | 网络测速结果 |
| [TRTCVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVideoFrame) | 视频帧信息 |
| [TRTCAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioFrame) | 音频帧数据 |
| [TRTCMixUser](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCMixUser) | 云端混流中各路画面的描述信息 |
| [TRTCTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCTranscodingConfig) | 云端混流的排版布局和转码参数 |
| [TRTCPublishCDNParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCPublishCDNParam) | 向非腾讯云 CDN 上发布音视频流时需设置的转推参数 |
| [TRTCAudioRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioRecordingParams) | 本地音频文件的录制参数 |
| [TRTCLocalRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCLocalRecordingParams) | 本地媒体文件的录制参数 |
| [TRTCAudioEffectParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioEffectParam) | 音效参数（已废弃） |
| [TRTCSwitchRoomConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCSwitchRoomConfig) | 房间切换参数 |
| [TRTCAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioFrameDelegateFormat) | 音频自定义回调的格式参数 |
| [TRTCScreenCaptureSourceInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCScreenCaptureSourceInfo) | 屏幕分享的目标信息（仅适用于桌面系统） |


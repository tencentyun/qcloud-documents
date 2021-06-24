## TRTCCloud @ TXLiteAVSDK

### 创建与销毁

| API | 描述 |
|-----|-----|
| [delegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6a8e20d57b7890e4dbf6652c426d7015) | 设置回调接口 [TRTCCloudDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#protocolTRTCCloudDelegate)。 |
| [delegateQueue](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a97158c52f2a4011454b4eb3ee369a8a1) | 设置驱动 [TRTCCloudDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#protocolTRTCCloudDelegate) 回调的队列。 |
| [sharedInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab6884975e069628328d05cf0e2c3dc67) | 创建 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 单例。 |
| [destroySharedIntance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad8961d03736d8a52df5a3a991d0a77c4) | 销毁 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 单例。 |


### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d) | 进入房间。 |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a715f5b669ad1d7587ae19733d66954f3) | 离开房间。 |
| [switchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5f4598c59a9c1e66938be9bfbb51589c) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a062bc48550b479a6b7c1662836b8c4a5) | 请求跨房通话（主播 PK）。 |
| [disconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abd656e4c9b6a01231810ae897627e9bc) | 退出跨房通话。 |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ada2e2155e0e7c3001c6bb6dca1d93048) | 设置音视频数据接收模式，需要在进房前设置才能生效。 |
| [createSubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6100a5f395442d38ce9adab922382caf) | 创建子 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 实例。 |
| [destroySubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a19e0d7921ac494fb588a4654d97abe86) | 销毁子 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 实例。 |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7c5a2aa06d649492f546d9c70a5de4a1) | 切换房间。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6d2f4d81f0944072053d7dc9e9265f22) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afc00ba747be5299cd7235928a628339e) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aad42e78d355fd563b959a5053bac54cb) | 开始向友商云的直播 CDN 转推。 |
| [stopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5d8a86795b8a2d7eaf9be7157dd9b8dd) | 停止向非腾讯云地址转推。 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a8d589d96e548a26c7afb5d1f2361ec93) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3fc1ae11b21944b2f354db258438100e) | 开启本地视频的预览画面 (iOS 版本)。 |
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3fc1ae11b21944b2f354db258438100e) | 开启本地视频的预览画面 (Mac 版本)。 |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf20f249b4b43fff64f944b4aefe54cb) | 更新本地视频预览画面的窗口。 |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01ee967e3180a5e2fc0e37e9e99e85b3) | 停止本地视频采集及预览。 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85ea151beebda2f86c3802f3a6a9e82) | 暂停/恢复推送本地的视频数据。 |
| [setVideoMuteImage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad730c168c066599b6c4c987fd7b7c3a2) | 设置暂停推送本地视频时要推送的图片。 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) | 开始拉取并显示指定用户的远端画面。 |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a518d3a8a3b4a4cfd8b5e0dfe7899756b) | 更新远端视频画面的窗口。 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2b7e96e4b527798507ff743c61a6a066) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aaa75cd1b98c226bb7b8a19412b204d2b) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aaf4376c4822aa9924733f8f165f17683) | 暂停/恢复接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#adf7cd002366760749c6f4d1ee9291db1) | 暂停/恢复接收所有远端视频流。 |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a57938e5b62303d705da2ceecf119d74e) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac72a8a85131cb7716b1eec799250aba9) | 设置网络流控相关参数。 |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5d4f0aba952a355f153d374899e6dcec) | 本地图像的渲染设置。 |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5d4f0aba952a355f153d374899e6dcec) | 远端图像的渲染设置。 |
| [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a200c174b27bbe7397b0639e707ee6547) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。 |
| [setVideoEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a29a7cae6b4e82098fc342d4f0066d2ad) | 设置编码器输出的画面镜像模式。 |
| [setGSensorMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7a8c22e2f02d313590d4c499e18ebe3f) | 设置重力感应的适应模式。 |
| [enableEncSmallVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2aa9c464203b1c62cbb9ccabccc6334a) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a49440df0907b12c0ad8fe9e93bdbed0d) | 切换指定远端用户的大小画面。 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac0db9a4bcb61e3b369740a1986683cdf) | 视频画面截图。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acd85c726c425eda7cac82cba0f83a465) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab78601c38f1b872b03b662e6856be84c) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4ada386a75d8042a432da05fde5552d9) | 静音/取消静音本地的音频。 |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afede3cc79a8d68994857b410fb5572d2) | 静音/取消静音指定的远端用户的声音。 |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a75148bf8a322c852965fe774cbc7dd14) | 静音/取消静音所有用户的声音。 |
| [setAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa62f2af2d86a64c0ebc7b9f00e4a54fe) | 设置音频路由。 |
| [setRemoteAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a8d38580f2c35f7e9828c4e41c56db35a) | 设置某个远程用户的播放音量。 |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5475b81c1712323257c10baaf7ad6969) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7ce26486575e72bc445432929fdff26c) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af2602b1e9dfe932c89dd411f2f227192) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aba445625df38b8676d599df4a67a8407) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a57d48cb0dbd7705486453b46e30e3fea) | 启用音量大小提示。 |
| [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9eadd65cef0ac6b9c04ddfd7265afb01) | 开始录音。 |
| [stopAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac8c12476bbcf3d691060954fcdb6ebe6) | 停止录音。 |
| [startLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5075d55a6fc31895eedd5b23a1b8826b) | 开启本地媒体录制(iOS)。 |
| [stopLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#affae72630393980fee79c21f2d20f602) | 停止录制。 |
| [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2979e32c019708dcc9209bb6d2db9486) | 开始录制系统声音，仅适用 Mac 平台。 |
| [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#adef486f26a2c7d74a8cccb537367e66a) | 停止录制系统声音，仅适用 Mac 平台。 |
| [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afc45226807d84673bab78b21d1be54ae) | 设置系统声音采集的音量，仅适用 Mac 平台。 |


### 设备管理接口

| API | 描述 |
|-----|-----|
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a950f3f1c949def9e1e470f467db7b27a) | 获取设备管理类 TXDeviceManager。 |


### 美颜特效和变脸特效

| API | 描述 |
|-----|-----|
| [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4fb05ae6b5face276ace62558731280a) | 获取美颜管理对象。 |
| [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad0bedbddf415d26cff8242d5842a0908) | 添加水印。 |


### 音乐特效和人声特效

| API | 描述 |
|-----|-----|
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af962213fefe6988a08820ac9af00df66) | 获取音效管理类 TXAudioEffectManager。 |


### 屏幕分享相关接口函数

| API | 描述 |
|-----|-----|
| [startScreenCaptureInApp](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a16d30ca3f89863da2581ff3872bf31f0) | 开始应用内的屏幕分享（该接口仅支持 iOS 13.0 及以上的 iPhone 和 iPad）。 |
| [startScreenCaptureByReplaykit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a12414559fc82b18e671262c4da37b171) | 开始全系统的屏幕分享（该接口支持 iOS 11.0 及以上的 iPhone 和 iPad）。 |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9a4b3b61c39c1c65e3426b35b0ace95f) | 开始桌面端屏幕分享（该接口仅支持 Mac OS 桌面系统）。 |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3902b63a60bdaad59cfd38c493fef124) | 停止屏幕采集。 |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3902b63a60bdaad59cfd38c493fef124) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3902b63a60bdaad59cfd38c493fef124) | 恢复屏幕分享。 |
| [getScreenCaptureSourcesWithThumbnailSize](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa8e5286e1035b64b7d2bf8fadd721123) | 枚举可分享的屏幕窗口，仅支持 Mac OS 平台，建议在 startScreenCapture 之前调用。 |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01ead6fb3106ea266caa922f5901bf18) | 设置屏幕分享参数，仅支持 Mac OS 平台，该方法在屏幕分享过程中也可以调用。 |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abc0f3cd5c320d0e65163bd07c3c0a735) | 设置辅路视频的编码器参数，适用 iOS、Mac 平台。 |
| [setSubStreamMixVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a18d3fb6535c9884784c5ad5f8dfd0b12) | 设置屏幕分享的混音音量大小，仅适用 Mac 平台。 |
| [addExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa567171999b17a7f5655213b193415a7) | 将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去，仅适用 Mac 平台。 |
| [removeExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a95b1f3fbc6ff755f67f7e9b86240ea5f) | 将指定窗口从屏幕分享的排除列表中移除，仅适用 Mac 平台。 |
| [removeAllExcludedShareWindows](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab2b6a778a528d58e2a42c9adfc7684f2) | 将所有窗口从屏幕分享的排除列表中移除，仅适用 Mac 平台。 |
| [addIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2e101f0ff00c8752eea1fa9a1a432233) | 将指定窗口加入窗口分享的包含列表中，加入包含列表中的窗口会被一起分享出去，仅适用 Mac 平台。 |
| [removeIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a058ac1e2141d6eb1962219167add42bc) | 将指定窗口从窗口分享的包含列表中移除，仅适用 Mac 平台。 |
| [removeAllIncludedShareWindows](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a18a20767a0e1076ba16cd473a2512156) | 将所有窗口从窗口分享的包含列表中移除，仅适用 Mac 平台。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [generateCustomPTS](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae5f2a974fa23954c5efd682dc464cdee) | 生成自定义采集时间戳。 |
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af53f530fe2025d72e2479928dd6db52f) | 启用自定义视频采集模式。 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5a68c4f0cd3a79100b331fc17d4b2858) | 向 SDK 中指定 streamType 投送自己采集的视频数据。 |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab8f8aaa19d70c6a2c9d62ecceb6e974d) | 启用音频自定义采集模式。 |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a62cab4ec7c336ae135c2f681aca25da1) | 向 SDK 投送自己采集的音频数据。 |
| [enableMixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1101d883d65882f735e3d17f874a25cb) | 控制外部音频是否要混入推流和混入播放。 |
| [mixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9f408915460e86e889056066ca4e0908) | 向 SDK 投送自己附加的音频数据。 |
| [setLocalVideoProcessDelegete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2f73c33b1010a63bd3a06e639b3cf348) | 第三方美颜的视频数据回调。 |
| [setLocalVideoRenderDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aba3d309645d27304b6d4ea31b21a4cda) | 设置本地视频的自定义渲染回调。 |
| [setRemoteVideoRenderDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5244e73ac27599370f966575e11959ff) | 设置远端视频的自定义渲染回调。 |
| [setAudioFrameDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01726b03b102c32222a2a26b16abcd48) | 设置音频数据回调。 |
| [setCapturedRawAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4b58b1ee04d0c692f383084d87111f86) | 设置本地麦克风采集回调出来的 AudioFrame 格式。 |
| [setLocalProcessedAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9ec7c7123eb2f333769508de193ea51f) | 设置本地采集并经过音频模块前处理后的音频数据回调出来的 AudioFrame 格式。 |
| [setMixedPlayAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a24ad642b88cd3b2ca2d3044d72817090) | 设置送入扬声器播放的音频数据回调的 AudioFrame 格式。 |
|[enableCustomAudioRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a325da4ec57db06b91b74da8699b47d7c)| 开启音频自定义播放 。|
|[getCustomAudioRenderingFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aeebe3811918c8250d32d872fee83a2c2)| 获取可播放的音频数据。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acbc86da0cb558c549f42e7e987c7beaf) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6de26e5efddf899d31158e4d48f17c02) | 将小数据量的自定义数据嵌入视频帧中。 |


### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a058556b224315dcde3601ab621a09dee) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a58d732ba648d1f9a3a460c02de79bb9b) | 停止服务器测速。 |


### Log 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ace5acd2fe597b6656b45aaa93e3e45a1) | 获取 SDK 版本信息。 |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9d2b6a99e137a9667743edc8ac909493) | 设置 Log 输出级别。 |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a177c4f1fbb2a011ff496417dc0245667) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa51a341a43a854ac6e3fa1d0093fec95) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a93b48089741f7022aea1f8f93ce8fff9) | 修改日志保存路径。 |
| [setLogDelegate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a41497e4242e3c42acfa35730cdc1ddf6) | 设置日志回调。 |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3bd71c8a99029c1a4708bf1c176aa299) | 显示仪表盘。 |
| [setDebugViewMargin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aad41ff6d5b5565046911acf27bb3dee4) | 设置仪表盘的边距。 |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a16c53e91f9b32aaf4bf3d409a3790ef6) | 调用实验性 API 接口。 |




## TRTCCloudDelegate @ TXLiteAVSDK

### 错误事件和警告事件

| API | 描述 |
|-----|-----|
| [onError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a10a711eb68abcacc1ca690501fc7c9fb) | 错误回调，表示 SDK 不可恢复的错误，一定要监听并分情况给用户适当的界面提示。 |
| [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a25ac0da9ad798a2313bdf8f296828541) | 警告回调，用于告知您一些非严重性问题，例如出现了卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6960aca54e2eda0f424f4f915908a3c5) | 已加入房间的回调。 |
| [onExitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6a98fcaac43fa754cf9dd80454897bea) | 离开房间的事件回调。 |
| [onSwitchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ade2c2eab48a30e7ca1c9246e573b7f28) | 切换角色的事件回调。 |
| [onConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a69e5b1d59857956f736c204fe765ea9a) | 请求跨房通话（主播 PK）的结果回调。 |
| [onDisconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a26b34d83afac68928a156096862c9c06) | 结束跨房通话（主播 PK）的结果回调。 |
| [onSwitchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ad848cbee89f8b6258c9f03f4cb253a31) | 切换房间 (switchRoom) 的结果回调。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a390831928a4d2a7977c4c1572da8be58) | 有用户加入当前房间。 |
| [onRemoteUserLeaveRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#afa7d16e1e4c66d938fc2bc69f3e34c28) | 有用户离开当前房间。 |
| [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) | 远端用户是否存在可播放的主路画面（一般用于摄像头）。 |
| [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ac45fb0751f7dbd2466a35c8828c9911b) | 远端用户是否存在可播放的辅路画面（一般用于屏幕分享）。 |
| [onUserAudioAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8c885eeb269fc3d2e085a5711d4431d5) | 远端用户是否存在可播放的音频数据。 |
| [onFirstVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7fc7fd0144af2bc4ce0797f9de530d96) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aafc4536f552199368e48c8527783c410) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a17567554f413629a80b5970bdffdff7b) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#acb73daf4ce82cd03f787f057b233b412) | 首帧本地音频数据已经被送出。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a723002319845fbfc03db501aa9da6c28) | 网络质量，该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#afb0811035e97c8544dbc9ecbef461dd9) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aed43a70b4a95eb95181e2b410013bf54) | SDK 跟服务器的连接断开。 |
| [onTryToReconnect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a1c8654b64e4bde42a8a24954ecf2cb2d) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a36d96a42ec4b00a0e3808f7f8460cd7f) | SDK 跟服务器的连接恢复。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aaa74021e5fd2564afb2df50e25eedeff) | 摄像头准备就绪。 |
| [onMicDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#afdac7dee94451913a4dc9982badc8035) | 麦克风准备就绪。 |
| [onAudioRouteChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a1859305732dfd03de63c9b780f99d513) | 音频路由发生变化（仅 iOS），音频路由即声音由哪里输出（扬声器或听筒）。 |
| [onUserVoiceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7775c3fbd84b8da3b7a75bdea27ed5c5) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |
| [onDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a0152908c497bd5ee5225251d9e93e500) | 本地设备通断回调。 |
| [onAudioDeviceCaptureVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a1c36efd81dc4edf88fc3bc6af83b1b5a) | 当前音频采集设备音量变化回调。 |
| [onAudioDevicePlayoutVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af24c0f0258e83ab644e242ee0d01277f) | 当前音频播放设备音量变化回调。 |
| [onSystemAudioLoopbackError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8644f5136138d13ffa8e0ea68f5c3676) | 系统声音采集结果回调。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsgUserId](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a324311b3d4f3930d9a50b8449b155dd3) | 收到自定义消息回调。 |
| [onMissCustomCmdMsgUserId](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af1b8e7d0f73773eca509afc1cf4c9ece) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a6e4365456cb4df6e1bdf870511b72042) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a75c6bf4a7c7ec60a24aabfe8e47ea1f4) | 开始向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 中的 startPublishing() 接口。 |
| [onStopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a379dcf84e15f93b64efe2cb9f362877c) | 停止向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a817783f364bf9f6f0a1df4bc26bad628) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aab032eb48a56e8351ada60ce5b510d5e) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ab5c98341b7536b5b65c04b835c4d28fb) | 设置云端的混流转码参数的回调，对应于 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 中的 setMixTranscodingConfig() 接口。 |


### 音效回调

| API | 描述 |
|-----|-----|
| [onAudioEffectFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#accb36b0eb1d1b72f32cf72617bb1c730) | 播放音效结束回调。 |


### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureStarted](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7d15537d26fb001045ff95157d59ed3f) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a9cc6106085b2049838e21bb50e192786) | 当屏幕分享暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ae9c08ef9dd260cf6fd946209fda8a011) | 当屏幕分享恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStoped](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a323d2b3e5b8b364722e0b161ab11c816) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 媒体录制回调

| API | 描述 |
|-----|-----|
| [onLocalRecordBegin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a044ce179ac4bc0bc987a3b74ecd911e7) | 媒体录制回调。 |
| [onLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ab4250c05ea4b843c27385f77d5004fc3) | 录制信息更新回调。 |
| [onLocalRecordComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ae78ca25acea4152bfd9d0ccf71bd4108) | 录制任务已结束。 |


### 第三方美颜回调

| API | 描述 |
|-----|-----|
| [onProcessVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a8d4f000b4169a64a8a8af15e51e5dd95) | 第三方美颜的视频数据回调，需要使用 [TRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#interfaceTRTCCloud) 中的 setLocalVideoProcessDelegete 接口进行设置。 |
| [onGLContextDestory](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a5f6d5ef01d3cd610959433107f78aa60) | SDK 内部的 OpenGL 环境的销毁通知。 |


### 视频数据帧的自定义处理回调

| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a7b43888945a9d12f088ed99a5854e3c1) | 自定义视频渲染回调。 |


### 声音数据帧的自定义处理回调

| API | 描述 |
|-----|-----|
| [onCapturedRawAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aeaeaf9e7091c75e1a072d576a57d7f5c) | 本地麦克风采集到的原始音频数据回调。 |
| [onLocalProcessedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a73a3e7de3c5c340957f119bb0f8744b0) | 本地采集并经过音频模块前处理后的音频数据回调。 |
| [onRemoteUserAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aa392c17c27bae1505f148bf541b7746a) | 混音前的每一路远程用户的音频数据，即混音前的各路原始数据。例如，对某一路音频进行文字转换时，您必须使用该路音频的原始数据。 |
| [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a5a8a0bf6f8d02c33b2fe01c6175dfd4e) | 各路音频数据混合后的音频数据。 |
| [onMixedAllAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a905748efe966e94ec1212fda14161aee) | SDK所有音频数据混合后的数据回调（包括采集音频数据和所有播放音频数据）。 |


### 日志相关回调

建议在比较早初始化的类中设置回调委托对象，例如 AppDelegate。

| API | 描述 |
|-----|-----|
| [onLog](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ab1364c78a6f31a8c08d0138c4f6e9647) | 有日志打印时的回调。 |


## 关键类型定义
| 类名 | 描述 |
|-----|-----|
| [TRTCRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCRenderParams) | 视频渲染设置。 |
| [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCParams) | 进房相关参数。 |
| [TRTCAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioFrameDelegateFormat) | 回调音频帧数据格式。 |
| [TRTCVideoEncParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVideoEncParam) | 视频编码参数。 |
| [TRTCNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCNetworkQosParam) | 网络流控相关参数。 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCQualityInfo) | 网络质量。 |
| [TRTCVolumeInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVolumeInfo) | 音量大小。 |
| [TRTCScreenCaptureSourceInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCScreenCaptureSourceInfo) | 屏幕分享目标信息（仅 Mac）。 |
| [TRTCSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCSpeedTestResult) | 网络测速结果。 |
| [TRTCVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVideoFrame) | 视频帧信息。 |
| [TRTCAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioFrame) | 音频帧数据。 |
| [TRTCMixUser](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCMixUser) | 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCTranscodingConfig) | 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCPublishCDNParam) | CDN 旁路推流参数。 |
| [TRTCAudioRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioRecordingParams) | 录音参数。 |
| [TRTCAudioEffectParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioEffectParam) | 音效。 |
| [TRTCSwitchRoomConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCSwitchRoomConfig) | 切换房间。 |
| [TRTCLocalRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCLocalRecordingParams) | 本地媒体文件录制参数。 |
| [TRTCLocalStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCLocalStatistics) | 自己本地的音视频统计信息。 |
| [TRTCRemoteStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCStatisic__ios.html) | 远端成员的音视频统计信息。 |
| [TRTCStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCStatisic__ios.html) | 统计数据。 |

### 枚举值

| 枚举 | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaa58db9156c82d75257499cb5e0cdf0e5) | 视频分辨率。 |
| [TRTCVideoResolutionMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gafdfe57c064658b38b78b0fd11e2706c0) | 视频宽高比模式。 |
| [TRTCVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga1974ff7e5e78b4455925faf74e38f1e8) | 视频流类型。 |
| [TRTCVideoFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga1a66aad6fff71205c7a266268e16f55c) | 视频画面填充模式。 |
| [TRTCVideoRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gae8bd6b06a2ca5f89f9b3cea393fc6eb9) | 视频画面旋转方向。 |
| [TRTCBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga9bafd3233be6cec1b380d469017ed3e6) | 美颜（磨皮）算法。 |
| [TRTCVideoPixelFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gabb58c142deac29da242c957f21c963e3) | 视频像素格式。 |
| [TRTCVideoBufferType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga0fce6f58df3d3021696d15eff683ed8b) | 视频数据包装格式。 |
| [TRTCVideoMirrorType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga13da9775774c3251999f1e46d279305f) | 本地视频预览镜像类型。 |
| [TRTCSnapshotSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga50f989651c9f893de7716ffbc2d2a5fc) | 视频截图来源。 |
| [TRTCAppScene](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga6ab617b26cf503a8c1bfec34a9918dbe) | 应用场景。 |
| [TRTCRoleType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gad147b9b0249d0c2759cf1514c8978881) | 角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [TRTCQosControlMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga915f86fec1b00787147d40a189444823) | 流控模式。 |
| [TRTCVideoQosPreference](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga2c460e7365ad67ee0213545b0a67aa6d) | 画质偏好。 |
| [TRTCQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga25f9ccb045890cb18a5f647ef3c1f974) | 网络质量。 |
| [TRTCAudioSampleRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga346b09a7691ce8c9813bac0feb057d08) | 音频采样率。 |
| [TRTCAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga865e618ff3a81236f9978723c00e86fb) | 声音音质。 |
| [TRTCAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga81305fea3aae73346d04f0013e0194d4) | 声音播放模式（音频路由）。 |
| [TRTCReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga1c0a768f9f7855e87c486617816c7759) | 声音混响模式。 |
| [TRTCVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaeb48457146f2279c912e345ce532ecef) | 变声模式。 |
| [TRTCSystemVolumeType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaac0cd0da9dd789dcec4ba16471006f23) | 系统音量类型。 |
| [TRTCLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gacefec5143acae6d0524b5500f0155908) | Log 级别。 |
| [TRTCGSensorMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga894251078222f9ac4ba5815aac4b493c) | 重力感应开关。 |
| [TRTCScreenCaptureSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaeabd30a270055e48105a34c781c782b0) | 屏幕分享目标类型（仅 Mac）。 |
| [TRTCTranscodingConfigMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga907c7b1ef1f09fb7417a549e82110855) | 混流参数配置模式。 |
| [TRTCRecordType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga4bb9927d377aa27b781fcfef5cf1058a) | 媒体录制类型。 |


### 弃用接口（建议使用对应的新接口）

| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abb57991f5e4f4ca1b95c2181a7e538c8) | 设置麦克风的音量大小。 |
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1336146862fb742de6cbe5718f9b7008) | 设置美颜、美白以及红润效果级别。 |
| [setEyeScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae0e4341ef565cc5ba28101574179cd56) | 设置大眼级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFaceScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a52ad635b237ccb1eef53a4ed9e650035) | 设置瘦脸级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFaceVLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1bf6dd0f5a5c6c013323d31f60d494e2) | 设置 V 脸级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setChinLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a145d4ed3d5790a449a9884d282420216) | 设置下巴拉伸或收缩，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFaceShortLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac11082c88aba749acd7cd2c7a7caa953) | 设置短脸级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setNoseSlimLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae94b107a9c476337585906c79b42ee95) | 设置瘦鼻级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [selectMotionTmpl](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3aa8c561d744e3d921dff6186a6e4ade) | 选择使用哪一款 AI 动效挂件，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setMotionMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa6689d734b9f46cb84a848b7e8f39cbd) | 设置动效静音，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9a4b3b61c39c1c65e3426b35b0ace95f) | 启动屏幕分享。 |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1b0c2a9e82a408881281c7468a74f2c0) | 设置指定素材滤镜特效。 |
| [setFilterConcentration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3b0d7db70674f961c14b316f4e8e7a2b) | 设置滤镜浓度。 |
| [setGreenScreenFile](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab4682edfc605ba06e24fd7b3e758ce5d) | 设置绿幕背景视频（企业版有效，其它版本设置此参数无效）。 |
| [playBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4d9983591fa2a847e226b7a30e8db294) | 启动播放背景音乐。 |
| [getBGMDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ac1f96932d02198cd045ee96f1306c8ba) | 获取音乐文件总时长，单位毫秒。 |
| [setBGMPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a7fd043ae358c43f6a178837fb2846ef9) | 设置 BGM 播放进度。 |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#adbfc8e226df7c6caaaca1a89a9842f23) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a08c468f48d99aef0e89716111db1f422) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a0cf0c090285038b23843c646009073d1) | 设置背景音乐远端播放音量的大小。 |
| [setReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a555cde4eda63d13bbad0dbdba7094a47) | 设置混响效果，目前仅支持 iOS。 |
| [setVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa60f54923826cc59d8a4526669c4ea5e) | 设置变声类型，目前仅支持 iOS。 |
| [playAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2ae175694198a9b3d1b1647b7ce1dae0) | 播放音效。 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a22854b4e9f698cceb1bbb7f7de466ec1) | 设置音效音量。 |
| [stopAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aacf50bc1e6040c11331e3c23b319f97b) | 停止音效。 |
| [setAllAudioEffectsVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6b345c95b5b68198d8dbc64a3652ed35) | 设置所有音效音量。 |
| [pauseAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab0d46ccb8fca811851b30e7731958024) | 暂停音效。 |
| [resumeAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a207dd8909c05d4a8a1431d33e644d4fe) | 恢复音效。 |
| [enableAudioEarMonitoring](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa26564f3388bc249ecbd2813d9c45390) | 开启耳返。 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) | 开始显示远端视频画面。 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2b7e96e4b527798507ff743c61a6a066) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [setRemoteViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afda6658d1bf7dc9bc1445838b95d21ff) | 设置远端图像的渲染模式。 |
| [setRemoteViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2ef26a9ede0ba4fa6c5739229e1eee90) | 设置远端图像的顺时针旋转角度。 |
| [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a68d048ccd0d018995e33e9e714e14474) | 开始显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [stopRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#acab6e31898857af876af66e779216203) | 停止显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [setLocalViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a961596f832657bfca81fd675878a2d15) | 设置本地图像的渲染模式。 |
| [setLocalViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4d2d95ad8fbaf8edce18667aa835848e) | 设置本地图像的顺时针旋转角度。 |
| [setLocalViewMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a97a2c690c467d58f74e17efe871b8403) | 设置本地摄像头预览画面的镜像模式（iOS）。 |
| [setLocalViewMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a97a2c690c467d58f74e17efe871b8403) | 设置本地摄像头预览画面的镜像模式（Mac）。 |
| [setRemoteSubStreamViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a487b3cd9a6b41581d4b45c752c5ede4c) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的显示模式。 |
| [setRemoteSubStreamViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a72c66b67eacd24a0e796a3213219fb6d) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的顺时针旋转角度。 |
| [setPriorRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2b2d43a3955480f2d6200bf20e66f3cf) | 设定观看方优先选择的视频质量。 |
| [setAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2cdffa1529fcaec866404f4f9b92ec53) | 设置音频质量。 |
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3177329bc84e94727a1be97563800beb) | 开启本地音频的采集和上行。 |
| [setFocusPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6a77cc99c41b926cd99909ae1ace39ae) | 设置摄像头焦点，如果 enableAutoFaceFoucs 为 YES 时无效。 |
| [enableAutoFaceFoucs](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a32a8f584879b17f211df75494a5be96c) | 自动识别人脸位置。 |
| [setZoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a9777fe95f7830746c1ba6b10446c37a0) | 设置摄像头缩放因子（焦距）。 |
| [enbaleTorch](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af6b128ee01d91a63dc1976db7a9be555) | 开关闪光灯。 |
| [setSystemVolumeType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab098daa610ae506dbf6c2a4f666ae32c) | 设置通话时使用的系统音量类型。 |
| [startCameraDeviceTestInView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1bd6289b969adde0096c83d6a5532332) | 开始进行摄像头测试。 |
| [startMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa6f467c12fcea7e09cc97861d511498a) | 开始进行麦克风测试。 |
| [startSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a60aa520016687bea03f17cb4ec19c1b6) | 开始扬声器测试。 |
| [setCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5141fec83e7f071e913bfc539c193ac6) | 设置要使用的麦克风。 |
| [setCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aaa6810f64c153e779697dc2d5bd30f6a) | 设置麦克风设备的音量。 |
| [setCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a88569e62fe75b7ea98cc012169f22bfe) | 设置系统当前麦克风设备的静音状态。 |
| [setCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6c951071ac218930680febd84314ee05) | 设置要使用的扬声器。 |
| [setCurrentSpeakerDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a019001b23569c8b6da7f3276af58e0a7) | 设置当前扬声器音量。 |
| [setCurrentSpeakerDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a738ea0dffd48d5bc2b05b146eb79ec46) | 设置系统当前扬声器设备的静音状态。 |
| [setCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aae9955bb39985586f7faba841d2692fc) | 设置要使用的摄像头。 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a1a05f5145a6171155db20a2d59b7d562) | 视频画面截图。 |
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ade46563b03208042e61bcc693e4a5d06) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a76e8101153afc009f374bc2b242c6831) | 向 SDK 投送自己采集的视频数据。 |

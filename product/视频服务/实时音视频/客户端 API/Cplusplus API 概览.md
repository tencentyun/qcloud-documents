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
### 设置 ITRTCCloudCallback 回调

| API | 描述 |
|-----|-----|
| [addCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a6a8317825ffe59ddcf1159a778dd7577) | 设置回调接口 [ITRTCCloudCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__cplusplus.html#classtrtc_1_1ITRTCCloudCallback)。 |
| [removeCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad088226e8af2d6764851efe7bd94652d) | 移除事件回调。 |



### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0fab3ea6c23c6267112bd1c0b64aa50b) | 进入房间。 |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ab3881c8829e7b8a3132e7b551e62fbf1) | 离开房间。 |
| [switchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a4705f2f116a1ec85bbc60ecaf552c89d) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ab5a0622e5d3d521d79ba4f85c44244eb) | 请求跨房通话（主播 PK）。 |
| [disconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a08870fd955f90d02879e966dcd02bfd3) | 关闭跨房连麦。 |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a7a0238314fc1e1f49803c0b22c1019d5) | 设置音视频数据接收模式，需要在进房前设置才能生效。 |
| [createSubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a5ce8b3f393ad3e46a3af39b045c1c5a2) | 创建子 TRTCCloud 实例。 |
| [destroySubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a980cf4d173abfb58c00ef35a20e12c85) | 销毁子 TRTCCloud 实例。 |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a1f3bed34f92b3ff908beb2d0ed2866c9) | 切换房间。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a7cbe48ea2cd3fb05a5b10350b6d81265) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ac4d3f88b6e067f32d1191878b6db1645) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a26e2d0b06211185d52836ffbdeddc3d1) | 开始向友商云的直播 CDN 转推。 |
| [stopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a9cf56c1f3a9aadf4c6123f44e1494a1b) | 停止向非腾讯云地址转推。 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8c835f1d49ab0f80a85569e030689850) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aef6d61f571304066aaf839f7db00a17b) | 开启本地视频的预览画面(Windows、 Mac版本)。 |
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8ac23e725c7ed75488df1be2ee514884) | 开启本地视频的预览画面 (iOS、 Android版本) 在 enterRoom 之前调用此函数，SDK 只会开启摄像头，并一直等到您调用 enterRoom 之后才开始推流。 在 enterRoom 之后调用此函数，SDK 会开启摄像头并自动开始视频推流。 当开始渲染首帧摄像头画面时，您会收到 [ITRTCCloudCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__cplusplus.html#classtrtc_1_1ITRTCCloudCallback) 中的 onFirstVideoFrame(null) 回调。 |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0af978a75d5ba671b7ce5f0b81b003c8) | 更新本地视频预览画面的窗口。 |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#af7003d2c12f5f783115ada43a715abe7) | 停止本地视频采集及预览。 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a6070313a28d3302c94ad807c636eb60f) | 暂停/恢复推送本地的视频数据。 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a5c5ea936418b106c2e801db57938dde9) | 开始拉取并显示指定用户的远端画面。 |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a027a8b23a363dc91e6ce1c9773ee8664) | 更新远端视频渲染的窗口。 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#abd186570272cd61b4a6e4aea870437e1) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a7a55fb85c4135abfbe00af529cdaf9bc) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a22155f6fe17dde77a16c273e0d5a02a3) | 暂停/恢复接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aa0d0d63eff6bbee7651ead569646b70b) | 暂停/恢复接收所有远端视频流。 |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a55b0710284e44ba3703e22b07c3665c8) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad21668c7550aad44f1ed61265ffceb24) | 设置网络流控相关参数。 |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#acf1e58c46f0c160ab1a17706ea1aa735) | 设置本地图像（主流）的渲染参数。 |
| [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a932ff32ec07b20a0e0d83bb434cfb691) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。 |
| [setVideoEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a251af554d7257ec64e84027136ae21ef) | 设置编码器输出的画面镜像模式。 |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ab0bd203a8dd3c07910249b1c3e0df9e6) | 设置远端图像的渲染模式。 |
| [enableSmallVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a5019a8005cd96662ce2cface662a811e) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#abd330074a9e99cb9c75d42ef3d1d63a0) | 选定观看指定 userId 的大画面还是小画面。 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8cf480979530c705c04d3c1715787f6c) | 视频画面截图。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a86c80ed357798e50ccf5c7ae47317f4c) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a47c51247d112b86d2397744c8f3c686b) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a1e1f27f131da042ca6e80beaa18055a8) | 静音/取消静音本地的音频。 |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ae22224501b484166dac65c1873ecdbc3) | 静音/取消静音指定的远端用户的声音。 |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a38177742eaf9bedf11109452230319c4) | 静音/取消静音所有用户的声音。 |
| [setRemoteAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ac49fa4a92105f01e2e296b20881a8324) | 设置某个远程用户的播放音量。 |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8677a812326511ef92f963bbe049d42e) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aed4cdd35906d151cd97f543332fb9f02) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a338984f5503d59ae06d67f55bd8f0766) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ae66cc77d6dfccb4c473eff062d0eb717) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a3127ec82f1610ac2bc0cb7d32b9bb4b9) | 启用或关闭音量大小提示。 |
| [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a55c3e8982056532a6cce56e3f7f29241) | 开始录音。 |
| [stopAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a052a606496ce98cdc5a7e93098598a32) | 停止录音。 |
| [startLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a55c3e8982056532a6cce56e3f7f29241) | 开启本地录制。 |
| [stopLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8b9b6f0608e48c27fc7c646718cb41ba) | 停止本地录制。 |


### 设备相关接口函数

| API | 描述 |
|-----|-----|
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#acbe34e3a11decb05d8ea28eb494a113a) | 获取设备管理模块。 |


### 美颜特效和图像水印

| API | 描述 |
|-----|-----|
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a78c7b8eaa17d721cfd6dcac0224dd50b) | 设置美颜、美白、红润效果级别。 |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a4a1c376670ff4f3fdac8cf30bec78576) | 设置水印。 |


### 音乐特效和人声特效

| API | 描述 |
|-----|-----|
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad9da9a5121bb52fbb85890dd857d7e8a) | 获取音效管理类 ITXAudioEffectManager。 |
| [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad6a651a786871927917b087ae7094c8a) | 打开系统声音采集。 |
| [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aab0258238e4414c386657151d01ffb23) | 关闭系统声音采集。 |
| [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a52d0f9a999296633b1d859f75d36d5e8) | 设置系统声音采集的音量。 |


### 屏幕分享相关接口函数

| API | 描述 |
|-----|-----|
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ab1fc5a303726a666d30051c836e33fdd) | 启动屏幕分享。 |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0e09090fe4281c0e78d8eb38496a8ed0) | 停止屏幕采集。 |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0dcd89ed2e23706239db98b55dd806d4) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a9dc10db068b9d8c6a0fcb8b085359f33) | 恢复屏幕分享。 |
| [getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad23c03ad142e8a42c49967ff9ccf9592) | 枚举可分享的屏幕窗口，建议在 startScreenCapture 之前调用。 |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a9d16af81b2ea2db7b91a8346add13393) | 设置屏幕分享参数，该方法在屏幕分享过程中也可以调用。 |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a542913f5081fb2479137a7416c970e2d) | 设置屏幕分享的编码器参数。 |
| [setSubStreamMixVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aff8dd1456e5bebff5495d84683c7f83e) | 设置屏幕分享的混音音量大小。 |
| [addExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ac2a8a65dc2c1d0e4ffbd89eeae768fff) | 将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去。 |
| [removeExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0bbbff5ea3cd764dbaaad0db887760bf) | 将指定窗口从屏幕分享的排除列表中移除。 |
| [removeAllExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#abb20ff837f1f5955bea349ff95002a10) | 将所有窗口从屏幕分享的排除列表中移除。 |
| [addIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a442186322939f9b93d6c6e0a3ace7bd3) | 将指定窗口加入屏幕分享的包含列表中，加入包含列表中的窗口如果在采集窗口区域内会被分享出去。 |
| [removeIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a5d2812b4068e89e6d2a422cd74257246) | 将指定窗口从屏幕分享的包含列表中移除。 |
| [removeAllIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a5d2812b4068e89e6d2a422cd74257246) | 将所有窗口从屏幕分享的包含列表中移除。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aaeab72ed55be06685e293c3cf92b6f90) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a1d8de868187164e20d0e657e44da0bc6) | 向 SDK 投送自己采集的视频数据。 |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a166d6ea0b36bc1adf3d3eddde35207c3) | 启用音频自定义采集模式 开启该模式后，SDK 停止运行原有的音频采集流程，只保留编码和发送能力。 您需要用 [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) 不断地向 SDK 塞入自己采集的音频数据。 |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) | 向 SDK 投送自己采集的音频数据。 |
| [enableMixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a896ff4b2731488821dd1ce382276ca0c) | 控制外部音频是否要混入推流和混入播放。 |
| [mixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a3c99feacd22af10926d5a521ca598ecd) | 向 SDK 发送自定义辅流音频数据。 |
| [generateCustomPTS](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a33ed1b26695b6b75dc9ce78e5280cbb4) | 生成自定义采集时间戳。 |
| [setLocalVideoProcessCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a3f6d32bdf3cb0fe72b61455304b975c6)|设置第三方美颜的视频数据回调|
| [setLocalVideoRenderCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad64031e060146f7985263aad994fc733) | 设置本地视频自定义渲染。 |
| [setRemoteVideoRenderCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a1efc475e32f06c768330ff80ebffbc8a) | 设置远端视频自定义渲染。 |
| [setAudioFrameCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a607dc63d8d944869537457c5b92b56e9) | 设置音频数据回调。 |




### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a858b11d4d32ee0fd69b42d64a1d65389) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aa91b261d10bbdb43508e9e2c33697c29) | 将小数据量的自定义数据嵌入视频帧中。 |



### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#af86b2903b95b6e74f02d701701ce3380) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ad6ba6ea2c5beace98b99ce98d326be4c) | 停止网络测速。 |


### LOG 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a11a1bc22514ac5a7bd9052a5cc444147) | 获取 SDK 版本信息。 |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aa6551d4e61a7a003d91b045ed2e13466) | 设置 Log 输出级别。 |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a589f4eefb2d7380e6bb145a9b0111634) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a357393d1eb2f92b7219395162c531e65) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#afbacbfc33a72f8fdd6995cf1ec3d04a6) | 设置日志保存路径。 |
| [setLogCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a239c5b9962a95a1eb4662440fab682fd) | 设置日志回调。 |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a7df528c2024556a073b4668879dff91f) | 显示仪表盘。 |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ab15fc0877664a8ac257ca4d6e7afc7b0) | 调用实验性 API 接口。 |


### 弃用接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a26bfd13c4838d9088273aaad55b3c621) | 开启本地音频的采集和上行。 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a38ff46d7ee110cc4ed1b4832decc78e9) | 开始显示远端视频画面。 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aca1818ea1557ede57153f79bf24dd4e6) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [setLocalViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#adfd1abf930d90e48645033e8125f7ae6) | 设置本地图像的填充模式。 |
| [setLocalViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#acf7401863d4c53ca8b90448fae696f24) | 设置本地图像的顺时针旋转角度。 |
| [setLocalViewMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#acf7401863d4c53ca8b90448fae696f24) | 设置本地摄像头预览画面的镜像模式。 |
| [setRemoteViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae5eed51d0b55c2b2fd0410e2383a43aa) | 设置远端图像的渲染模式。 |
| [setRemoteViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a20cc5354ee7290a4fe0c561c5a1002ed) | 设置远端图像的顺时针旋转角度。 |
| [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a8c558caa6b4db039d6f778dc3d9ec0b8) | 开始显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [stopRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a56a7770d90cad9141aecbd70d93af588) | 停止显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 v8.0 版本弃用，请使用 stopRemoteView(userId,streamType) 接口。 |
| [setRemoteSubStreamViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a749827fd1626bdf6940486cf4f94fb81) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的显示模式。 |
| [setRemoteSubStreamViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aab3f678108829558bde252e4a44c9686) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的顺时针旋转角度。 |
| [setAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae9e231a18f3fc150efcbea4d31dde2c4) | 设置音频质量。 |
| [setPriorRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a03d1b864630501881eb7a5466a204bd7) | 设定观看方优先选择的视频质量。 |
| [getCameraDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aa6b352a78cdaa536a4f381c18b12baeb) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aae18b8f818dadc61fc69e781fa2564e3) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a5884efde03e6cbdd5956352821fc803e) | 获取当前使用的摄像头。 |
| [getMicDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a7f55dec965753a0e916daf545c4c02d1) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a6c9a18c9005436f93f2d78f66cb172ce) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a0ffc8eb4e9050536cc96069797283465) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a2f776bd91a3cae88c2b110cec0a2e4ad) | 获取系统当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a01e881b34e3876a04198731b7cbd929a) | 设置系统当前麦克风设备的音量。 |
| [setCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ac91001367c541cca16828440edcf532e) | 设置系统当前麦克风设备的是否静音。 |
| [getCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a3e501339c03f38e93be7596ff652675c) | 获取系统当前麦克风设备是否静音。 |
| [getSpeakerDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ace28dde50b14c71ea0487d5c90ed810a) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a67bf9270553f52ec9081b9e001436473) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a36ddc9e11deb0fb9689c4bb652ce8893) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#af2aa87f67810db076449fef67e0c7049) | 获取系统当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae5bed3e0181663b739c019be7b220dcf) | 设置系统当前扬声器设备音量。 |
| [setCurrentSpeakerDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae5bed3e0181663b739c019be7b220dcf) | 设置系统当前扬声器设备的是否静音。 |
| [getCurrentSpeakerDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ab33f3a25d63ba5dece8dc481934f0e42) | 获取系统当前扬声器设备是否静音。 |
| [startCameraDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a39d3c3f2fff4803eeaba090c3236eebc) | 开始进行摄像头测试。 |
| [startCameraDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aeb78c95028742c49d4ddd1e3b6e66aa2) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ab9c4b4fd13d707c7d009ebfd301cc08b) | 停止摄像头测试 v8.0 版本弃用，请使用 ITXDeviceManager::stopCameraDeviceTest 接口。 |
| [startMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae959c197b632783ec298c6f549c21030) | 开启麦克风测试。 |
| [stopMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aca5d21b834a8863263789410026a2183) | 停止麦克风测试 v8.0 版本弃用，请使用 ITXDeviceManager::stopMicDeviceTest 接口。 |
| [startSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a98d817ca58986e756ae7a7e14002b60e) | 开启扬声器测试。 |
| [stopSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae8b569605b72a467eb6a01c664afa999) | 停止扬声器测试 v8.0 版本弃用，请使用 ITXDeviceManager::stopSpeakerDeviceTest 接口。 |
| [setMicVolumeOnMixing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a9fc6194bde0fc945a2cda4562116fd7c) | 设置麦克风的音量大小。 |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ac2abdde0c55332bc883e70ab794e929d) | 启动屏幕分享。 |
| [playBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ad489b4bd998bc1ce911b01b6561c7633) | 启动播放背景音乐。 |
| [stopBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#afc2d9d18c1f3187be7507c2b58b8e62f) | 停止播放背景音乐。 |
| [pauseBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#ae92ddbca534bba79c82ddc2a4cbbb119) | 暂停播放背景音乐。 |
| [resumeBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#acf40ba767f62e49b54d5461639268126) | 继续播放背景音乐。 |
| [getBGMDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a4e9542c204fba5deeda5a23d21ab936f) | 获取音乐文件总时长，单位毫秒。 |
| [setBGMPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a6d11b2bae707addba872b54bc591d3f9) | 设置 BGM 播放进度。 |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a8fa9cc7afdab2998a0fc04ee5ac28845) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a5f2340b5b3549f7491977174b03d9e57) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a9a5c74f8adf60b91c0b8053b62636c75) | 设置背景音乐远端播放音量的大小。 |
| [playAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#adf967d9f8b43c2136067a56acb3cf706) | 播放音效。 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a863d956d20f2d856ea4cb6e4dfe068b0) | 设置音效音量。 |
| [stopAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aac03904c97a44815b4395a3b479dcd88) | 停止音效。 |
| [stopAllAudioEffects](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a68ca8ad66ec47323708f766d1222435c) | 停止所有音效。 |
| [setAllAudioEffectsVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a3ab679a79420e3c2200690b800b80d07) | 设置所有音效的音量。 |
| [pauseAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#aa41cf52f6c97467c83dfcec4d7b0587d) | 暂停音效。 |
| [resumeAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a86593fb0c5bfb5e608f714dbcc78fff7) | 恢复音效。 |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a428eb11858f268c8f4350424cd7f84e7) | 设置屏幕共享参数。 |
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#af297f4b7cc710c8cd7cfe5cd02470c81) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__IDeprecatedTRTCCloud__cplusplus.html#a598de64893203c591b99d521946d46ce) | 向 SDK 投送自己采集的视频数据。|


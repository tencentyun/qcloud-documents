## ITRTCCloud @ TXLiteAVSDK
### 设置 ITRTCCloudCallback 回调

| API | 描述 |
|-----|-----|
| [addCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a6a8317825ffe59ddcf1159a778dd7577) | 设置回调接口 [ITRTCCloudCallback](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#classtrtc_1_1ITRTCCloudCallback)。 |
| [removeCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad088226e8af2d6764851efe7bd94652d) | 移除事件回调。 |


### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac73c4ad51eda05cd2bcec820c847e84f) | 进入房间。 |
| [exitRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab3881c8829e7b8a3132e7b551e62fbf1) | 离开房间。 |
| [switchRole](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4705f2f116a1ec85bbc60ecaf552c89d) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae472af11c30db29fcd21ea01854ab32f) | 请求跨房通话（主播 PK）。 |
| [disconnectOtherRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a08870fd955f90d02879e966dcd02bfd3) | 关闭跨房连麦。 |
| [setDefaultStreamRecvMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7a0238314fc1e1f49803c0b22c1019d5) | 设置音视频数据接收模式，需要在进房前设置才能生效。 |
| [createSubCloud](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a5ce8b3f393ad3e46a3af39b045c1c5a2) | 创建子 TRTCCloud 实例。 |
| [destroySubCloud](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0555e9e9d9d02c8c116946915f969d18) | 销毁子 TRTCCloud 实例。 |
| [switchRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1f3bed34f92b3ff908beb2d0ed2866c9) | 切换房间。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac2f616263c108bf6ac5ef2b66b83a380) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac4d3f88b6e067f32d1191878b6db1645) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a26e2d0b06211185d52836ffbdeddc3d1) | 开始向友商云的直播 CDN 转推。 |
| [stopPublishCDNStream](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9cf56c1f3a9aadf4c6123f44e1494a1b) | 停止向非腾讯云地址转推。 |
| [setMixTranscodingConfig](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a8c835f1d49ab0f80a85569e030689850) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a64a9d40eba291e0447b63542a6a66f3c) | 开启本地视频的预览画面(Windows、 Mac 版本)。 |
| [startLocalPreview](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aaf4651f9913924560859f4541211f2df) | 开启本地视频的预览画面 (iOS、 Android 版本) 在 enterRoom 之前调用此函数，SDK 只会开启摄像头，并一直等到您调用 enterRoom 之后才开始推流。 在 enterRoom 之后调用此函数，SDK 会开启摄像头并自动开始视频推流。 当开始渲染首帧摄像头画面时，您会收到 [ITRTCCloudCallback](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#classtrtc_1_1ITRTCCloudCallback) 中的 onFirstVideoFrame(null) 回调。 |
| [updateLocalView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a6db572d1e387b21328c6c78de561838c) | 更新本地视频预览画面的窗口。 |
| [stopLocalPreview](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af7003d2c12f5f783115ada43a715abe7) | 停止本地视频采集及预览。 |
| [muteLocalVideo](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a6070313a28d3302c94ad807c636eb60f) | 暂停/恢复推送本地的视频数据。 |
| [startRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a50ec31c281de91903a1ef492a2ec7997) | 开始拉取并显示指定用户的远端画面。 |
| [updateRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9f774f9abb7970fb32c3172fa3229fd2) | 更新远端视频渲染的窗口。 |
| [stopRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a20d2004010563e37804a6b82ed9d09ec) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7a55fb85c4135abfbe00af529cdaf9bc) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a22155f6fe17dde77a16c273e0d5a02a3) | 暂停/恢复接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa0d0d63eff6bbee7651ead569646b70b) | 暂停/恢复接收所有远端视频流。 |
| [setVideoEncoderParam](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa2bc2739031035b40e8f2a76184c20d9) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a374f1000d443de80d70747cba876f879) | 设置网络流控相关参数。 |
| [setLocalRenderParams](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#acf1e58c46f0c160ab1a17706ea1aa735) | 设置本地图像（主流）的渲染参数。 |
| [setVideoEncoderRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a932ff32ec07b20a0e0d83bb434cfb691) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。 |
| [setVideoEncoderMirror](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a251af554d7257ec64e84027136ae21ef) | 设置编码器输出的画面镜像模式。 |
| [setRemoteRenderParams](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab0bd203a8dd3c07910249b1c3e0df9e6) | 设置远端图像的渲染模式。 |
| [enableSmallVideoStream](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a80648f76afbda35c9bf5d96701c62a9e) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#abd330074a9e99cb9c75d42ef3d1d63a0) | 选定观看指定 userId 的大画面还是小画面。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a86c80ed357798e50ccf5c7ae47317f4c) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47c51247d112b86d2397744c8f3c686b) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1e1f27f131da042ca6e80beaa18055a8) | 静音/取消静音本地的音频。 |
| [muteRemoteAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae22224501b484166dac65c1873ecdbc3) | 静音/取消静音指定的远端用户的声音。 |
| [muteAllRemoteAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a38177742eaf9bedf11109452230319c4) | 静音/取消静音所有用户的声音。 |
| [setRemoteAudioVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac49fa4a92105f01e2e296b20881a8324) | 设置某个远程用户的播放音量。 |
| [setAudioCaptureVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a8677a812326511ef92f963bbe049d42e) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aed4cdd35906d151cd97f543332fb9f02) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a338984f5503d59ae06d67f55bd8f0766) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae66cc77d6dfccb4c473eff062d0eb717) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3127ec82f1610ac2bc0cb7d32b9bb4b9) | 启用或关闭音量大小提示。 |
| [startAudioRecording](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a15b74c793aea807ef9142230c088473b) | 开始录音。 |
| [stopAudioRecording](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a052a606496ce98cdc5a7e93098598a32) | 停止录音。 |


### 设备相关接口函数

| API | 描述 |
|-----|-----|
| [getDeviceManager](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#acbe34e3a11decb05d8ea28eb494a113a) | 获取设备管理模块。 |


### 美颜特效和图像水印

| API | 描述 |
|-----|-----|
| [setBeautyStyle](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a78c7b8eaa17d721cfd6dcac0224dd50b) | 设置美颜、美白、红润效果级别。 |
| [setWaterMark](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4a1c376670ff4f3fdac8cf30bec78576) | 设置水印。 |


### 音乐特效和人声特效

| API | 描述 |
|-----|-----|
| [getAudioEffectManager](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad9da9a5121bb52fbb85890dd857d7e8a) | 获取音效管理类 ITXAudioEffectManager。 |
| [startSystemAudioLoopback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad6a651a786871927917b087ae7094c8a) | 打开系统声音采集。 |
| [stopSystemAudioLoopback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aab0258238e4414c386657151d01ffb23) | 关闭系统声音采集。 |
| [setSystemAudioLoopbackVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a52d0f9a999296633b1d859f75d36d5e8) | 设置系统声音采集的音量。 |


### 屏幕分享相关接口函数

| API | 描述 |
|-----|-----|
| [startScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab0f8b23d8c48b9a056ca0e61ddcc894f) | 启动屏幕分享。 |
| [stopScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0e09090fe4281c0e78d8eb38496a8ed0) | 停止屏幕采集。 |
| [pauseScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0dcd89ed2e23706239db98b55dd806d4) | 暂停屏幕分享。 |
| [resumeScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9dc10db068b9d8c6a0fcb8b085359f33) | 恢复屏幕分享。 |
| [getScreenCaptureSources](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3777e1506f1aa806bee116e7117993b5) | 枚举可分享的屏幕窗口，建议在 startScreenCapture 之前调用。 |
| [selectScreenCaptureTarget](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#adc372b21294cd36bf4f4af0d1ac6624a) | 设置屏幕分享参数，该方法在屏幕分享过程中也可以调用。 |
| [setSubStreamEncoderParam](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#abdc3d6339afd741bd8d3ed88ea551282) | 设置屏幕分享的编码器参数。 |
| [setSubStreamMixVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aff8dd1456e5bebff5495d84683c7f83e) | 设置屏幕分享的混音音量大小。 |
| [addExcludedShareWindow](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0edaac7111c63d9a00b7749ee0c7b137) | 将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去。 |
| [removeExcludedShareWindow](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a39db493034f2898788898e6669168c61) | 将指定窗口从屏幕分享的排除列表中移除。 |
| [removeAllExcludedShareWindow](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#abb20ff837f1f5955bea349ff95002a10) | 将所有窗口从屏幕分享的排除列表中移除。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac9d547341170330a70623299b366c44a) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3a53ae79c1bd28825cb276c7555500fe) | 向 SDK 投送自己采集的视频数据。 |
| [enableCustomAudioCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a166d6ea0b36bc1adf3d3eddde35207c3) | 启用音频自定义采集模式 开启该模式后，SDK 停止运行原有的音频采集流程，只保留编码和发送能力。 您需要用 [sendCustomAudioData()](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) 不断地向 SDK 塞入自己采集的音频数据。 |
| [sendCustomAudioData](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) | 向 SDK 投送自己采集的音频数据。 |
| [setLocalVideoRenderCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad64031e060146f7985263aad994fc733) | 设置本地视频自定义渲染。 |
| [setRemoteVideoRenderCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1efc475e32f06c768330ff80ebffbc8a) | 设置远端视频自定义渲染。 |
| [setAudioFrameCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a607dc63d8d944869537457c5b92b56e9) | 设置音频数据回调。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a858b11d4d32ee0fd69b42d64a1d65389) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa91b261d10bbdb43508e9e2c33697c29) | 将小数据量的自定义数据嵌入视频帧中。 |


### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af86b2903b95b6e74f02d701701ce3380) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad6ba6ea2c5beace98b99ce98d326be4c) | 停止网络测速。 |


### LOG 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a11a1bc22514ac5a7bd9052a5cc444147) | 获取 SDK 版本信息。 |
| [setLogLevel](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa6551d4e61a7a003d91b045ed2e13466) | 设置 Log 输出级别。 |
| [setConsoleEnabled](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a589f4eefb2d7380e6bb145a9b0111634) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a357393d1eb2f92b7219395162c531e65) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#afbacbfc33a72f8fdd6995cf1ec3d04a6) | 设置日志保存路径。 |
| [setLogCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a239c5b9962a95a1eb4662440fab682fd) | 设置日志回调。 |
| [showDebugView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7df528c2024556a073b4668879dff91f) | 显示仪表盘。 |
| [callExperimentalAPI](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab15fc0877664a8ac257ca4d6e7afc7b0) | 调用实验性 API 接口。 |


### 弃用接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a05765322423454da0ad304faa7efba4a) | 开启本地音频的采集和上行。 |
| [startRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a50ec31c281de91903a1ef492a2ec7997) | 开始显示远端视频画面。 |
| [stopRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a20d2004010563e37804a6b82ed9d09ec) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [setLocalViewFillMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#acdfe0dc822f074d5c42dfe308dc313a0) | 设置本地图像的填充模式。 |
| [setLocalViewRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4447783c52960cffbaedb7ccd7c456a2) | 设置本地图像的顺时针旋转角度。 |
| [setLocalViewMirror](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a5a04c60eb2e9997e745412374b7b8d19) | 设置本地摄像头预览画面的镜像模式。 |
| [setRemoteViewFillMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab5be71379d671f77b99cf6ccd86cdbc7) | 设置远端图像的渲染模式。 |
| [setRemoteViewRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a385042d69e79468c9ef60dee8ec8cc96) | 设置远端图像的顺时针旋转角度。 |
| [startRemoteSubStreamView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a5935a852496c1a033576cc6fbf676746) | 开始显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [stopRemoteSubStreamView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a56a7770d90cad9141aecbd70d93af588) | 停止显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 v8.0 版本弃用，请使用 stopRemoteView(userId,streamType) 接口。 |
| [setRemoteSubStreamViewFillMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7832e5870431ccb0e75614b51af51205) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的显示模式。 |
| [setRemoteSubStreamViewRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab63344839afca9bd4a890f6f609fd9e7) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的顺时针旋转角度。 |
| [setAudioQuality](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a742eefe8508e744918f704e2fa0d3405) | 设置音频质量。 |
| [setPriorRemoteVideoStreamType](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a074579fcbcd5f4639ab40a2d5884fa3f) | 设定观看方优先选择的视频质量。 |
| [getCameraDevicesList](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ace7e563213b43c1763b1eb60d5b2e8c5) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af5ce3a160a7f0dc889322983f5cfa68a) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0f4a19bdc82b81dd1e0a8ac8b735261a) | 获取当前使用的摄像头。 |
| [getMicDevicesList](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab85ff9472d499bd740f953ccff549147) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a5a17cc110f2b9c146df4498aa35eebc6) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aded68bf47cb1e381961b0b69dde8931b) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#addb5ea84bf67a3fdd49eee30e66f4826) | 获取系统当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aaa35154699a59962bc065519e79761fa) | 设置系统当前麦克风设备的音量。 |
| [setCurrentMicDeviceMute](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a44453f04c53f19f65ca362a1cb55963b) | 设置系统当前麦克风设备的是否静音。 |
| [getCurrentMicDeviceMute](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac7df6f29e11ded5faf7996334d4af61b) | 获取系统当前麦克风设备是否静音。 |
| [getSpeakerDevicesList](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a20fa0073543ed1bd1df5dbb825b408bf) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0ac0ecdbf0d077563fd6d2fb1ee65bee) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a768367aba35b104f8529740b86802b73) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#accb2d6bc752f550b968462ba5a5c0538) | 获取系统当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae99882060b048467a0f39f13b168775f) | 设置系统当前扬声器设备音量。 |
| [setCurrentSpeakerDeviceMute](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad8c3800ba3e2101ff63de7117dc729f3) | 设置系统当前扬声器设备的是否静音。 |
| [getCurrentSpeakerDeviceMute](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa4ec49fc0c07c04031d328db5814793f) | 获取系统当前扬声器设备是否静音。 |
| [startCameraDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a32c469879fca0afec360690ee36c1b6b) | 开始进行摄像头测试。 |
| [startCameraDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a32c469879fca0afec360690ee36c1b6b) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3cb3fd62d04b5975c9c50210e98f0a2d) | 停止摄像头测试 v8.0 版本弃用，请使用 ITXDeviceManager::stopCameraDeviceTest 接口。 |
| [startMicDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aca6add13bdd6535bed6d28407b5468af) | 开启麦克风测试。 |
| [stopMicDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a29c2a5a42f65108074174e0bc58c0aee) | 停止麦克风测试 v8.0 版本弃用，请使用 ITXDeviceManager::stopMicDeviceTest 接口。 |
| [startSpeakerDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af60f0db87d1f7001860f1bf330eeee3c) | 开启扬声器测试。 |
| [stopSpeakerDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa4b7a172067664fe50015c758e02a822) | 停止扬声器测试 v8.0 版本弃用，请使用 ITXDeviceManager::stopSpeakerDeviceTest 接口。 |
| [setMicVolumeOnMixing](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4e3fb7ca730f15b6ab201e73e21f1260) | 设置麦克风的音量大小。 |
| [startScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a984f461eebe77819f40c4129fc5a71bb) | 启动屏幕分享。 |
| [playBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a815aa5a969dcb0617e02f955a9ee7cd4) | 启动播放背景音乐。 |
| [stopBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a8eec0a8a7edf45d3b49b897286154b4f) | 停止播放背景音乐。 |
| [pauseBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aed6272ead63eb14b9f64a92a59196c28) | 暂停播放背景音乐。 |
| [resumeBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a221c73557814b71880c9a9323e3f31d2) | 继续播放背景音乐。 |
| [getBGMDuration](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a487cff035a50da09ab39e87f7488d647) | 获取音乐文件总时长，单位毫秒。 |
| [setBGMPosition](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a2e2050b96d2b453e0ca83e483efec02c) | 设置 BGM 播放进度。 |
| [setBGMVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab651d0daff2d1b7e25b43606a4776796) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9c083e91e2af46503e522443a7b51b32) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af193ff23e008485cf949d761028ce6e9) | 设置背景音乐远端播放音量的大小。 |
| [playAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4db6f176c155c0f83d11eb302f6e1dab) | 播放音效。 |
| [setAudioEffectVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a401d82c610be2136896c0f60621d66cf) | 设置音效音量。 |
| [stopAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a254acc2f0fe96ffcce33629eb4309877) | 停止音效。 |
| [stopAllAudioEffects](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a07a2dfd7ce4e76b28172d73ee8405dbe) | 停止所有音效。 |
| [setAllAudioEffectsVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a06219d65076c6c7024fab30d2516b167) | 设置所有音效的音量。 |
| [pauseAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a2b004f3a3a7bdde7b2926930f31afa6c) | 暂停音效。 |
| [resumeAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af10583316f15ed709247590a081b2307) | 恢复音效。 |
| [selectScreenCaptureTarget](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#adc372b21294cd36bf4f4af0d1ac6624a) | 设置屏幕共享参数。 |



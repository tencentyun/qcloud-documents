## ITRTCCloud @ TXLiteAVSDK

### 设置 TRTCCloudCallback 回调

| API | 描述 |
|-----|-----|
| [addCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a6a8317825ffe59ddcf1159a778dd7577) | 设置回调接口 [ITRTCCloudCallback](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#classTRTC_1_1ITRTCCloudCallback)。 |
| [removeCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad088226e8af2d6764851efe7bd94652d) | 移除事件回调。 |


### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac73c4ad51eda05cd2bcec820c847e84f) | 进入房间，若房间不存在，系统将自动创建一个新房间。 |
| [exitRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab3881c8829e7b8a3132e7b551e62fbf1) | 离开房间。 |
| [switchRole](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4705f2f116a1ec85bbc60ecaf552c89d) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae472af11c30db29fcd21ea01854ab32f) | 请求跨房通话（主播 PK）。 |
| [disconnectOtherRoom](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a08870fd955f90d02879e966dcd02bfd3) | 关闭跨房连麦。 |
| [setDefaultStreamRecvMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7a0238314fc1e1f49803c0b22c1019d5) | 设置音视频数据接收模式，需要在进房前设置才能生效。 |


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
| [startLocalPreview](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0a3067221345da8eb3f32a3430dd42ff) | 开启本地视频的预览画面。 |
| [stopLocalPreview](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af7003d2c12f5f783115ada43a715abe7) | 停止本地视频采集及预览。 |
| [muteLocalVideo](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a6070313a28d3302c94ad807c636eb60f) | 暂停/恢复推送本地的视频数据。 |
| [startRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a33a6e3765d6ca52d572224bc6e25dbcb) | 开始显示远端视频画面。 |
| [stopRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7749979db2dd017d7cd8377c73e92720) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7a55fb85c4135abfbe00af529cdaf9bc) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a22155f6fe17dde77a16c273e0d5a02a3) | 暂停/恢复接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa0d0d63eff6bbee7651ead569646b70b) | 暂停/恢复接收所有远端视频流。 |
| [setVideoEncoderParam](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa2bc2739031035b40e8f2a76184c20d9) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a374f1000d443de80d70747cba876f879) | 设置网络流控相关参数。 |
| [setLocalViewFillMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af05757058905160ae641266caafc9516) | 设置本地图像的渲染模式。 |
| [setRemoteViewFillMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0d665a28bb540815de7a2028854db260) | 设置远端图像的渲染模式。 |
| [setLocalViewRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47859830694b7f71d447939d2c938455) | 设置本地图像的顺时针旋转角度。 |
| [setRemoteViewRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a571cbfb2eaef9f92b09f9e60b22cfd2b) | 设置远端图像的顺时针旋转角度。 |
| [setVideoEncoderRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a932ff32ec07b20a0e0d83bb434cfb691) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。 |
| [setLocalViewMirror](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4ec409aae9d635222458316fca1e8a4d) | 设置本地摄像头预览画面的镜像模式。 |
| [setVideoEncoderMirror](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a251af554d7257ec64e84027136ae21ef) | 设置编码器输出的画面镜像模式。 |
| [enableSmallVideoStream](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a80648f76afbda35c9bf5d96701c62a9e) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#abd330074a9e99cb9c75d42ef3d1d63a0) | 选定观看指定 userId 的大画面还是小画面。 |
| [setPriorRemoteVideoStreamType](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a24642910f76b7fdf78b435d736a0d7ba) | 设定观看方优先选择的视频质量。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a72ba04e850009e56505ee1cae0433abe) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47c51247d112b86d2397744c8f3c686b) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1e1f27f131da042ca6e80beaa18055a8) | 静音/取消静音本地的音频。 |
| [muteRemoteAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae22224501b484166dac65c1873ecdbc3) | 静音/取消静音指定的远端用户的声音。 |
| [muteAllRemoteAudio](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a38177742eaf9bedf11109452230319c4) | 静音/取消静音所有用户的声音。 |
| [setAudioCaptureVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a8677a812326511ef92f963bbe049d42e) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aed4cdd35906d151cd97f543332fb9f02) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a338984f5503d59ae06d67f55bd8f0766) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae66cc77d6dfccb4c473eff062d0eb717) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3127ec82f1610ac2bc0cb7d32b9bb4b9) | 启用或关闭音量大小提示。 |
| [startAudioRecording](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a15b74c793aea807ef9142230c088473b) | 开始录音。 |
| [stopAudioRecording](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a052a606496ce98cdc5a7e93098598a32) | 停止录音。 |


### 摄像头相关接口函数

| API | 描述 |
|-----|-----|
| [getCameraDevicesList](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa129bdc4cfd2d81ff7d57a2aab20da52) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af9e6848cc5f6b20268c2cf6eef034326) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a25042fd580b846102e06ff92a74b8417) | 获取当前使用的摄像头。 |


### 音频设备相关接口函数

| API | 描述 |
|-----|-----|
| [getMicDevicesList](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a84a4d58010c498d2bc44d8ff225e7a90) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a31669c8a64f8003b93e8fc7359e5ed11) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4edae1445c3195d5d2ba2333ccbe4fff) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a342920bf68b0286b91a049f540de5ccb) | 获取系统当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a227e6698697648b7a7ee9470a87f12f1) | 设置系统当前麦克风设备的音量。 |
| [getSpeakerDevicesList](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad500c64d8823bed4c4a31ab6b19c1e08) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad0dc1a89532d3654b271ed724b4281fd) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ab11c3c87d603a71dc1d3f2caef05bf98) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a24c9e3210c99e6331a3dff598f7fb490) | 获取系统当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad8393f22304422cb143a1362c03cca59) | 设置系统当前扬声器设备音量。 |


### 美颜相关接口函数

| API | 描述 |
|-----|-----|
| [setBeautyStyle](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a5aeffc60ba8101363f267f40dd8425d8) | 设置美颜、美白、红润效果级别。 |
| [setWaterMark](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4a1c376670ff4f3fdac8cf30bec78576) | 设置水印。 |


### 屏幕分享相关接口函数

| API | 描述 |
|-----|-----|
| [startScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae0d5f03fd15dbb7b101bb3c6df70f630) | 启动屏幕分享。 |
| [stopScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0e09090fe4281c0e78d8eb38496a8ed0) | 停止屏幕采集。 |
| [pauseScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0dcd89ed2e23706239db98b55dd806d4) | 暂停屏幕分享。 |
| [resumeScreenCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9dc10db068b9d8c6a0fcb8b085359f33) | 恢复屏幕分享。 |
| [getScreenCaptureSources](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3777e1506f1aa806bee116e7117993b5) | 枚举可分享的屏幕窗口，建议在 startScreenCapture 之前调用。 |
| [selectScreenCaptureTarget](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa5c3c7ed12993c155de77fb43ba0cf3b) | 设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。 |
| [startRemoteSubStreamView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af82052cffdcd1fd2a8d50744b806ff7d) | 开始显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [stopRemoteSubStreamView](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a4264ad8ab90a2582dc94617a3c686a46) | 停止显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [setRemoteSubStreamViewFillMode](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a0059bffb1af2385304595917e85d1cf3) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的显示模式。 |
| [setRemoteSubStreamViewRotation](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a11a2965ee1192569afd1482cfce6816e) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的顺时针旋转角度。 |
| [setSubStreamEncoderParam](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#abdc3d6339afd741bd8d3ed88ea551282) | 设置屏幕分享的编码器参数。 |
| [setSubStreamMixVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aff8dd1456e5bebff5495d84683c7f83e) | 设置屏幕分享的混音音量大小。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ac9d547341170330a70623299b366c44a) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3a53ae79c1bd28825cb276c7555500fe) | 向 SDK 投送自己采集的视频数据。 |
| [enableCustomAudioCapture](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a166d6ea0b36bc1adf3d3eddde35207c3) | 启用音频自定义采集模式，开启该模式后，SDK 停止运行原有的音频采集流程，只保留编码和发送能力。 您需要用 [sendCustomAudioData()](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) 不断地向 SDK 塞入自己采集的音频数据。 |
| [sendCustomAudioData](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a47ba3ba599134e902299dda9c5596c0d) | 向 SDK 投送自己采集的音频数据。 |
| [setLocalVideoRenderCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad64031e060146f7985263aad994fc733) | 设置本地视频自定义渲染。 |
| [setRemoteVideoRenderCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1efc475e32f06c768330ff80ebffbc8a) | 设置远端视频自定义渲染。 |
| [setAudioFrameCallback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a607dc63d8d944869537457c5b92b56e9) | 设置音频数据回调。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a858b11d4d32ee0fd69b42d64a1d65389) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa91b261d10bbdb43508e9e2c33697c29) | 将小数据量的自定义数据嵌入视频帧中。 |


### 背景混音相关接口函数

| API | 描述 |
|-----|-----|
| [playBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a15279ba49cc9101b9997ab6b1f386eeb) | 启动播放背景音乐。 |
| [stopBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a88211d59391d170ce225ef581383b0d4) | 停止播放背景音乐。 |
| [pauseBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1c9e7cd3a3f523776cc995378fe5ff95) | 暂停播放背景音乐。 |
| [resumeBGM](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a71ed3b4ff11839504fd7c35c764ca613) | 继续播放背景音乐。 |
| [getBGMDuration](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a484c22d9617415d5c28b1adba03a0e1a) | 获取音乐文件总时长，单位毫秒。 |
| [setBGMPosition](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a5c83c0c819e72d46300da6a407044493) | 设置 BGM 播放进度。 |
| [setBGMVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a7169cc4769a427265770b4f762e695e4) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3f1954560ae150f1029151b3aa906b3b) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a700c0ccdfbdc7571366571485a2a20dd) | 设置背景音乐远端播放音量的大小。 |
| [startSystemAudioLoopback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad6a651a786871927917b087ae7094c8a) | 打开系统声音采集，64位 SDK 暂不支持系统混音能力。 |
| [stopSystemAudioLoopback](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aab0258238e4414c386657151d01ffb23) | 关闭系统声音采集。 |
| [setSystemAudioLoopbackVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a52d0f9a999296633b1d859f75d36d5e8) | 设置系统声音采集的音量。 |


### 音效相关接口函数

| API | 描述 |
|-----|-----|
| [playAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a812b3bd8b5105cf120f781b380cc0596) | 播放音效。 |
| [setAudioEffectVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a1ced69ab948cd574e28e747965ec3282) | 设置音效音量。 |
| [stopAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3fe8704074d3f23eaaeb2ad51280aa27) | 停止音效。 |
| [stopAllAudioEffects](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a10ae64378e00e7b59c91e441f67a954c) | 停止所有音效。 |
| [setAllAudioEffectsVolume](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a8341d84cd74198c2cb6ed4964413a9bc) | 设置所有音效的音量。 |
| [pauseAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a3c2b8eac492de2eabfbe0cecb87e429f) | 暂停音效。 |
| [resumeAudioEffect](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a27b203785e4f9eceb3820dd0077f1e3c) | 恢复音效。 |


### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#af86b2903b95b6e74f02d701701ce3380) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ad6ba6ea2c5beace98b99ce98d326be4c) | 停止网络测速。 |
| [startCameraDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a27478c88ea2f0c3ad4d1747995bf4bad) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9aa02ead51d4ba3119869c7c2ac57b9d) | 停止摄像头测试。 |
| [startMicDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ae9982f55fa0e47646f43da2515584183) | 开启麦克风测试。 |
| [stopMicDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a60b8449c0b9c9ce8068e3e9960ea2237) | 停止麦克风测试。 |
| [startSpeakerDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a93ff8bfeb6ddcc0432c90fb6ac54be94) | 开启扬声器测试。 |
| [stopSpeakerDeviceTest](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#aa2a27282ca4aaf6ccc347ec1fa14da1c) | 停止扬声器测试。 |


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
| [setMicVolumeOnMixing](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#a9fc6194bde0fc945a2cda4562116fd7c) | 从 v6.9 版本开始废弃。 |


### 创建与销毁 ITRTCCloud 单例

| API | 描述 |
|-----|-----|
| [getTRTCShareInstance](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ga2fc755520711d5d8fd469f93bc9c2dc6) | 用于动态加载 dll 时，获取 [ITRTCCloud](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#classTRTC_1_1ITRTCCloud) 对象指针。 |
| [destroyTRTCShareInstance](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#ga1b494c61ef1fe41531ce283aae4e015d) | 释放 [ITRTCCloud](http://doc.qcloudtrtc.com/group__ITRTCCloud__cplusplus.html#classTRTC_1_1ITRTCCloud) 单例对象。 |


## TRTCCloudCallback @ TXLiteAVSDK

腾讯云视频通话功能的回调接口类。

### 错误事件和警告事件

| API | 描述 |
|-----|-----|
| [onError](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a9724da0b3da9b2eca5736fa8e54aa410) | 错误回调，表示 SDK 不可恢复的错误，一定要监听并分情况给用户适当的界面提示。 |
| [onWarning](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a53169ea41d90506cccbff507ba1932a4) | 警告回调，用于告知您一些非严重性问题，例如出现了卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a236a49e0525615b6435eaa826b7caffe) | 已加入房间的回调。 |
| [onExitRoom](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a0a45883a23a200b0e9ea38fdde1da4bd) | 离开房间的事件回调。 |
| [onSwitchRole](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a248335805c125e225cfec249697f2299) | 切换角色的事件回调。 |
| [onConnectOtherRoom](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a62333366a3a1ab09dc2b2f627a8a1bdd) | 请求跨房通话（主播 PK）的结果回调。 |
| [onDisconnectOtherRoom](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a292d6661cb93ba30ff68b1f88cf173f1) | 结束跨房通话（主播 PK）的结果回调。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a43704996ae1f50749b7c7140755350f1) | 有用户加入当前房间。 |
| [onRemoteUserLeaveRoom](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a5f7c705f3894d3a430ef1fac8bf8e2c5) | 有用户离开当前房间。 |
| [onUserVideoAvailable](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a091f1c94ff1e2bc39c36e9d34285e87a) | 远端用户是否存在可播放的主路画面（一般用于摄像头）。 |
| [onUserSubStreamAvailable](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a460922e4fb4b000d1dbd27b596dd0e5c) | 远端用户是否存在可播放的辅路画面（一般用于屏幕分享）。 |
| [onUserAudioAvailable](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a6f449dc5294e369750bc15a39eaa856c) | 远端用户是否存在可播放的音频数据。 |
| [onFirstVideoFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ad28d27badd56ac274c44720cc9f253d5) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a123616289b3219bc36137bc77e8e8b7a) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a454ea7e7103b2838440cafba3e524433) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a0bd950cb774fd40cfdc2fbff885295d2) | 首帧本地音频数据已经被送出。 |
| [onUserEnter](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ad606b861a3545832fb4821a7e0230925) | 废弃接口：有主播加入当前房间。 |
| [onUserExit](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#abbc4fe2ccac90f77c80f55d46d6c8951) | 废弃接口：有主播离开当前房间。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a377441bace65d98a1218817914a12ecb) | 网络质量，该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a681d301a576e65b354408576748c4477) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a34c34705bb67127ff6d28700cf2ab591) | SDK 跟服务器的连接断开。 |
| [onTryToReconnect](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#afe74dff22fde93fe0f07fcf18153d334) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ae90cd149a676418016cb8736b217f1a8) | SDK 跟服务器的连接恢复。 |
| [onSpeedTest](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a455264cfcf2a7a3f022f3bce0659f9f7) | 服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a13a9ad0933b7ab872987e432f005e8ad) | 摄像头准备就绪。 |
| [onMicDidReady](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a0ba02a5d9009ebb9c4e80c0c43c80bca) | 麦克风准备就绪。 |
| [onUserVoiceVolume](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a61df1f9eec0bfcebf421be865275ffc5) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |
| [onDeviceChange](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ac86c1b0d445a33f6340394b3b78490bd) | 本地设备通断回调。 |
| [onTestMicVolume](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a9f0101fa8222c6163f1b23fcce81e22b) | 麦克风测试音量回调。 |
| [onTestSpeakerVolume](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a04bb10b06af17cdc43b7831336736539) | 扬声器测试音量回调。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a0a5690652db3902e98e1168bad12ec1a) | 收到自定义消息回调。 |
| [onMissCustomCmdMsg](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ab5d0cb61c24b77ecdb177ff19fc95075) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ab364b929cd0d9ffff6e47c20ec52372c) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishing](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a345ab7b45a9d0027926dbf580e8e0258) | 开始向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 startPublishing() 接口。 |
| [onStopPublishing](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a8e046f5bd34498b13ae057caaab64913) | 停止向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a16164548764979e84d3b5301f28890ff) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a0da75e040521c0945c3735f4893e6c09) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#af228d4fa55fa17a48eb7424fb6ffe2b4) | 设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。 |


### 音效回调

| API | 描述 |
|-----|-----|
| [onAudioEffectFinished](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#aab3c91276b6e570ea9acfe1581e1aa51) | 播放音效结束回调。 |


### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureCovered](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a490f827ffd6e7728a6ec49cba63875b1) | 当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。 |
| [onScreenCaptureStarted](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a8baff9a6c699ea1d82c5e7abb6ded97b) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a32acecdafd9058cc7d70a3abe6995051) | 当屏幕分享暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a63c073daf1ad93cfa2e6c79695434e22) | 当屏幕分享恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStoped](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a4d182e6b60d8be536e69253d906af84d) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 背景混音事件回调

| API | 描述 |
|-----|-----|
| [onPlayBGMBegin](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ad93b8204416558e63c18349bf29ff592) | 开始播放背景音乐。 |
| [onPlayBGMProgress](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a1879cc4e50492431a3346828e9130f21) | 播放背景音乐的进度。 |
| [onPlayBGMComplete](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#abaf89c758a4dd21e21db488e997bef2a) | 播放背景音乐结束。 |


### 自定义视频渲染回调

| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#aea602851c96370558a7eeb850d7eb6b8) | 自定义视频渲染回调。 |


### 音频数据回调

| API | 描述 |
|-----|-----|
| [onCapturedAudioFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a57460e97c668b605a00ac498fc4aa40c) | 本地麦克风采集到的音频数据回调。 |
| [onPlayAudioFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#ab841da62beb88a9fa9bce58d25df6f23) | 混音前的每一路远程用户的音频数据，即混音前的各路原始数据。例如，对某一路音频进行文字转换时，您必须使用该路音频的原始数据。 |
| [onMixedPlayAudioFrame](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a6649f62d4138d9bc73ae484e63dec081) | 各路音频数据混合后送入喇叭播放的音频数据。 |


### 日志相关回调

| API | 描述 |
|-----|-----|
| [onLog](http://doc.qcloudtrtc.com/group__ITRTCCloudCallback__cplusplus.html#a2fa3d9997c9810ffa6a95e0a7a4a50d0) | 有日志打印时的回调。 |


## 关键类型定义

| 类名 | 描述 |
|-----|-----|
| [TRTCParams](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a7ff9e03272f5c8e7b585e8c4eea784e1) | 进房相关参数。 |
| [TRTCVideoEncParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a43a83bd5122296aa87cc7f6e964921c5) | 视频编码参数。 |
| [TRTCNetworkQosParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a7cd5c078b248a32557a85226f1d30697) | 网络流控相关参数。 |
| [TRTCQualityInfo](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#af6aab62536869726ee32b158ddbbf5ce) | 视频质量。 |
| [TRTCVolumeInfo](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#abdeba26e639757957fd75f528ba14f6e) | 音量大小。 |
| [TRTCSpeedTestResult](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a8858167e09ab4d55f5e49c89bd4a1848) | 网络测速结果。 |
| [TRTCMixUser](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ac5b1947f21f77726cbff822eaf0003f9) | 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a6066a5537ad8c1bc6158d43e8a4765db) | 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a0b977361cb4d84b1ece0b26c949dcde6) | CDN 旁路推流参数。 |
| [TRTCAudioRecordingParams](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a724e3aa5cbc2249b7ce31bd7f9362d7b) | 录音参数。 |
| [TRTCAudioEffectParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#a87aff2ab3ece9f1130a73981838baf04) | 音效。 |
| [TRTCLocalStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#structTRTC_1_1TRTCLocalStatistics) | 自己本地的音视频统计信息。 |
| [TRTCRemoteStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#structTRTC_1_1TRTCRemoteStatistics) | 远端成员的音视频统计信息。 |
| [TRTCStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#structTRTC_1_1TRTCStatistics) | 统计数据。 |

### 枚举值

| 枚举 | 描述 |
|-----|-----|
| [TRTCVideoResolution](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gace04ad7a0bf531f4d09dc6a540f09f95) | 视频分辨率。 |
| [TRTCVideoResolutionMode](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gaa6787a9059d7b725a30ffcf9f4aabb64) | 视频分辨率模式。 |
| [TRTCVideoStreamType](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga461563be214e8f0579a79741f37d18e3) | 视频流类型。 |
| [TRTCQuality](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gaa33845a1c994d38435a8f4a332cc3e95) | 画质级别。 |
| [TRTCVideoFillMode](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga496a32286104187149b4e40284cbfb36) | 视频画面填充模式。 |
| [TRTCBeautyStyle](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga46f49720df57d17b267054cb9ee4d079) | 美颜（磨皮）算法。 |
| [TRTCAppScene](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gaa57f4545ef7331e3157eee1639d28780) | 应用场景。 |
| [TRTCRoleType](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga42ff820a33d9f3535d203fd5d6782cb5) | 角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [TRTCQosControlMode](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga6615b296e31fc3d03c0df92e9755b5aa) | 流控模式。 |
| [TRTCVideoQosPreference](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga60efcaeea7692bbce8dc362856683319) | 画质偏好。 |
| [TRTCLogLevel](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gafa83683b4840bcb3200d1da63c10276d) | Log 级别。 |
| [TRTCDeviceState](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gac93bb27d49c2aeea8fc04242c5d0fc7e) | 设备操作。 |
| [TRTCDeviceType](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#ga76eabab111ddd8a7b2e44d2cbcf45794) | 设备类型。 |
| [TRTCWaterMarkSrcType](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gab3426c24d07508781330231a35be0ae0) | 水印图片的源类型。 |
| [TRTCTranscodingConfigMode](http://doc.qcloudtrtc.com/group__TRTCCloudDef__cplusplus.html#gaec50c849a17b7706f6989d718fc6b7df) | 混流参数配置模式。 |



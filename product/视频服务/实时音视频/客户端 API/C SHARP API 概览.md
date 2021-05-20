## ITRTCCloud @ TXLiteAVSDK

### 创建与销毁 ITRTCCloud 单例

| API | 描述 |
|-----|-----|
| [getTRTCShareInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aaab1651edd65e6ab0abec12efb945714) | 获取 [ITRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#classManageLiteAV_1_1ITRTCCloud) 单例对象。 |
| [destroyTRTCShareInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a4a0722972418aa87ae602f7e12d466ac) | 释放 [ITRTCCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#classManageLiteAV_1_1ITRTCCloud) 单例对象。 |


### 设置 TRTCCloudCallback 回调

| API | 描述 |
|-----|-----|
| [addCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a09b1c2ec021a62334da5fff4bd36d805) | 设置回调接口 [ITRTCCloudCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#interfaceManageLiteAV_1_1ITRTCCloudCallback)。 |
| [removeCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#afdcaecebad62bfcceecb97f5cbe2bf88) | 移除事件回调。 |


### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a28b2d3ec27af8c9bfd5cf687dd8e002b) | 进入房间。 |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a715f5b669ad1d7587ae19733d66954f3) | 离开房间。 |
| [switchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a94ab2e8a7df0c120def9d4b0c7658d84) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aa29407e4c40f2bf61777bbe054f6bf0f) | 请求跨房通话（主播 PK）。 |
| [disconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#abd656e4c9b6a01231810ae897627e9bc) | 关闭跨房连麦。 |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ae870243f89b5829cd7ac5612ec958cdf) | 设置音视频数据接收模式（需要在进房前设置才能生效）。 |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab3ea127e2b270b8045fa139edab1dc1c) | 切换房间。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad23040b25685bed8a9fa35bec28024bd) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#afc00ba747be5299cd7235928a628339e) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adf6a56b335c9860c3ea1a090cad9bf7b) | 开始向友商云的直播 CDN 转推。 |
| [stopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5d8a86795b8a2d7eaf9be7157dd9b8dd) | 停止向非腾讯云地址转推。 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a9a92140403d83a22f4334c0002f71d8d) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a74a3e5ec77196bd9bca67bf422e25b14) | 开启本地视频的预览画面。 |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a1ac7c1b6934150c07a7e9ee1918cfebe) | 更新本地视频预览画面的窗口。 |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a01ee967e3180a5e2fc0e37e9e99e85b3) | 停止本地视频采集及预览。 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad531b6af4f07d93b937901aea73d9008) | 暂停/恢复推送本地的视频数据。 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab4024c7f416d583dba3ef7cbcdb4145c) | 开始拉取并显示指定用户的远端画面。 |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aacca47d45d316473d5a5615e9d8a4e26) | 更新远端视频渲染的窗口。 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a8fca9a14fc9a214bf7c9caac59d4b52f) | 停止显示远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aaa75cd1b98c226bb7b8a19412b204d2b) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a3ab42b16228893891003df17c51fa2c4) | 暂停/恢复接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a129fb0485b0ba8b002e5806e57642715) | 暂停/恢复接收所有远端视频流。 |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a9445f85f7e8aef1c63829842ea801c11) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aa1b61a44d79e6f6b11163594077d93b7) | 设置网络流控相关参数。 |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a73b2e0cd0da9c721d35f813bb662cf17) | 设置本地图像（主流）的渲染参数。 |
| [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a291f1c48e5446135c29188f759f023cb) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。 |
| [setVideoEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a3e6dae3e385f1e15d528ec3d6f57a59c) | 设置编码器输出的画面镜像模式。 |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ae2cf26ff0b2680527ace23f316548af4) | 设置远端图像的渲染模式。 |
| [enableSmallVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a4a83369f8798e273caf0a6550cb19cfe) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a0c980fb80401d6fc14a69bfd16283b76) | 选定观看指定 userId 的大画面还是小画面。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a3177329bc84e94727a1be97563800beb) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab78601c38f1b872b03b662e6856be84c) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a16d9b4a197a7bc1955240a1ede889246) | 静音/取消静音本地的音频。 |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#abe535ac1d0a74de860c85ae09a3317df) | 静音/取消静音指定的远端用户的声音。 |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a9c118b189a47109289528b3c00019649) | 静音/取消静音所有用户的声音。 |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a53681962139b81140f2d66abc4ea6a0f) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad3dd226f138590f0e2c6b03f108c4e38) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a9b8946403b8b3ac8e11f3a78e9d531ca) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#acd6e6336d8f314cef76de9da831a58dd) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ac5711f9704dbea303cf746da26b16a6a) | 启用或关闭音量大小提示。 |
| [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a8e34f7bd3e4b1d63eced9a5273f5afa9) | 开始录音。 |
| [stopAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ac8c12476bbcf3d691060954fcdb6ebe6) | 停止录音。 |


### 设备相关接口函数

| API | 描述 |
|-----|-----|
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aa76f8d5680282b409b90158abd01886e) | 获取设备管理模块。 |


### 美颜特效和图像水印

| API | 描述 |
|-----|-----|
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a3eb000f9a504e96d2f12fc1d8a6e47b9) | 设置美颜、美白、红润效果级别。 |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ac6451172a12f33274215785b029be727) | 设置水印。 |


### 音乐特效和人声特效

| API | 描述 |
|-----|-----|
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab43456e2e7d83986fd66708131d8c264) | 获取音效管理类 ITXAudioEffectManager。 |
| [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aac7057a9556fc1b1b106733a87069e06) | 打开系统声音采集。 |
| [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adef486f26a2c7d74a8cccb537367e66a) | 关闭系统声音采集。 |
| [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a2bb76d46a5fcf037c560ab8f09b1825f) | 设置系统声音采集的音量。 |


### 屏幕分享相关接口函数

| API | 描述 |
|-----|-----|
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adde6382876b0afab78bab89e8be8e254) | 启动屏幕分享。 |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad02093be5c603f66f356978169946a18) | 停止屏幕采集。 |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a448e432a91c092f80421d377425fb1bb) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad1fc32927622168e9b3cbb3f70043450) | 恢复屏幕分享。 |
| [getScreenCaptureSources](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a1eda1853bfc49c43a35e4d945dfccd7a) | 枚举可分享的屏幕窗口，建议在 startScreenCapture 之前调用。 |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a2aabe079ed38fb5122be988434a81a92) | 设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。 |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ae8c2f4248a165d3b8846316e035c9b3b) | 设置屏幕分享的编码器参数。 |
| [setSubStreamMixVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aabc643e4be3add7e08b8fb3f1a9789a9) | 设置屏幕分享的混音音量大小。 |
| [addExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab975f0d54e63bf810b1a92539ad78057) | 将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去。 |
| [removeExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a3794c820d0d45cf55802b7162df063c9) | 将指定窗口从屏幕分享的排除列表中移除。 |
| [removeAllExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a179d325cc9f043d049cdedc35a64497a) | 将所有窗口从屏幕分享的排除列表中移除。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a87dace307d0df1eb4a5801d65517f40b) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5d27319a247b7a592726994055b3c318) | 向 SDK 投送自己采集的视频数据。 |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a6cf1f1f480d3a6228f55d7e57ad506a8) | 启用音频自定义采集模式。 |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a0a4c65597f32583b10fc9340d679ac2e) | 向 SDK 投送自己采集的音频数据。 |
| [setLocalVideoRenderCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad229dd9299a1bc2f025443045bf4a83d) | 设置本地视频自定义渲染。 |
| [setRemoteVideoRenderCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a9bca8939353ec025d81db79f2791206f) | 设置远端视频自定义渲染。 |
| [setAudioFrameCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ae5b754d3ca87d0a653ae604238465efc) | 设置音频数据回调。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a824ae2f32e2b2cf553b1a9709bea9f30) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a253023d332139a09cbb4d592042b84e6) | 将小数据量的自定义数据嵌入视频帧中。 |


### 网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a7dc88d324541c15e2781d1df10625fed) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a58d732ba648d1f9a3a460c02de79bb9b) | 停止网络测速。 |


### LOG 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a85b31ef9401eadb11981cce536e1e85e) | 获取 SDK 版本信息。 |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab941d390cf7df8034c522edd8dd2f3eb) | 设置 Log 输出级别。 |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a452f7778aaba21498765444f907bb0a0) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#af6d9f433c0c17ca34b040c51403865db) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#acca01dd55d9e0b30cfaac7df0ed3fe55) | 设置日志保存路径。 |
| [setLogCallback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a44ad1112f3666f86131c5e8cbf3093eb) | 设置日志回调。 |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a08d4c264ef3f43eea7616e4264a1e4e6) | 显示仪表盘。 |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#add201789a0da7c5893cc5636ad9e783e) | 调用实验性 API 接口。 |


### 弃用接口函数

| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a1fff2c9d17bc4197c0097c01397bf70e) | 设置麦克风的音量大小。 |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adde6382876b0afab78bab89e8be8e2542) | 启动屏幕分享。 |
| [playBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a2dc777ac9dbc51c01eb735a62318fcc5) | 启动播放背景音乐。 |
| [stopBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a11004f1ba27b057985850a25307b0bec) | 停止播放背景音乐。 |
| [pauseBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aa4b92d4c989e99612f6c4dab03a78764) | 暂停播放背景音乐。 |
| [resumeBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aed6e8f224b5f834b1bc0c15f9701f692) | 继续播放背景音乐。 |
| [getBGMDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a05d821f12515462f9f1f441a30064e10) | 获取音乐文件总时长，单位毫秒。 |
| [setBGMPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a4e0ae301ab2c14afe7f7a5656e4b0693) | 设置 BGM 播放进度。 |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aaf6c2319fd42b0453b7408d3f3d60cb4) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a74be58163008d9a85701663e8cfcd3d0) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad3dd3d419d87c3518088bce81fd5749b) | 设置背景音乐远端播放音量的大小。 |
| [playAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aa0464fd4855bf9d3275036d04a3e4c74) | 播放音效。 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a942a6f358980c8520e2155fb4ef55bd0) | 设置音效音量。 |
| [stopAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a61561195216ac575235b67d410070563) | 停止音效。 |
| [stopAllAudioEffects](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a7066509af1de32c290b7cc297cd00f2b) | 停止所有音效。 |
| [setAllAudioEffectsVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a19416181cce88c58052a4eb2e87adeb8) | 设置所有音效的音量。 |
| [pauseAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a43f83a1323cc39c1610c61cf79ab652c) | 暂停音效。 |
| [resumeAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a23b65446d7dd9835da888b5285867629) | 恢复音效。 |
| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a2aabe079ed38fb5122be988434a81a922) | 设置屏幕共享参数。 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ab4024c7f416d583dba3ef7cbcdb4145c2) | 开始显示远端视频画面。 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a8fca9a14fc9a214bf7c9caac59d4b52f2) | 停止显示远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [setLocalViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ada1aa39d0b579f0f939d17c3ca78df92) | 设置本地图像的渲染模式。 |
| [setRemoteViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a4d3e1c147a6c6656873246c069980d5e) | 设置远端图像的渲染模式。 |
| [setLocalViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a8d5dc6995392c71257493353e3571e86) | 设置本地图像的顺时针旋转角度。 |
| [setRemoteViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5a14374fb4547d496b0c9bdf98458f37) | 设置远端图像的顺时针旋转角度。 |
| [setLocalViewMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a050a53b8bed638f76a64ad82ecd89078) | 设置本地摄像头预览画面的镜像模式。 |
| [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#af3e5347c5973c34594ce32e677cd105a) | 开始显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [stopRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a00d9b103bdee9c4b9424aa669d8bb6c8) | 停止显示远端用户的辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）。 |
| [setRemoteSubStreamViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#af18f341b99546110d255ac48b8f17647) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的显示模式。 |
| [setRemoteSubStreamViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#afdf43dda66b2618071c780f937d326a7) | 设置辅路画面（TRTCVideoStreamTypeSub，一般用于屏幕分享）的顺时针旋转角度。 |
| [setPriorRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5cc9f8652845ff0d7adc5b2d24b8a269) | 设定观看方优先选择的视频质量。 |
| [setAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ae241d03683fdde1e033078a6057f609c) | 设置音频质量。 |
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a3177329bc84e94727a1be97563800beb2) | 开启本地音频的采集和上行。 |
| [getCameraDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ac089937783fa14655f4944e7137e9fe6) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a38d1826dcbb34fa6300b81dd0de82799) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a24ac636304cb989cce4e43a460ad659e) | 获取当前使用的摄像头。 |
| [getMicDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#af52dcefa14a0838a98d878620e4a8e83) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aeea733cfe13334913e7e8d1cbb4d35ff) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a410ac986bd2b77180987b8a4789e99f7) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5feaad27747bc7e909de43444aa86e2f) | 获取系统当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a02cdbf0a22ec4effeb662da83d7b5218) | 设置系统当前麦克风设备的音量。 |
| [getSpeakerDevicesList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a9f680a2953562c62e5024ef98e691803) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#af38430fc0b347637e5b050481b2d6065) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a44bb513e08eefd17d1f0c18adea68f6d) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a1617113ec7db9d646b27233da8132b48) | 获取系统当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a5fe7bfacc946565df7d14a91f6de9f21) | 设置系统当前扬声器设备音量。 |
| [startCameraDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adfdfd81465003ac6d21e5be20c119c41) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a1b67fa3f322efe538d924b381c06e676) | 停止摄像头测试。 |
| [startMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#aaa98e72f47a57ee2ff4e8b3670573688) | 开启麦克风测试。 |
| [stopMicDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a8cca1c5913ac021987680195075e5fc9) | 停止麦克风测试。 |
| [startSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ac68c3a3fd8215ba6377936a210d400c1) | 开启扬声器测试。 |
| [stopSpeakerDeviceTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#abf383f971dc54f0254b2d40f100cc9ca) | 停止扬声器测试。 |


## TRTCCloudCallback @ TXLiteAVSDK

腾讯云视频通话功能的回调接口类。

### 错误事件和警告事件

| API | 描述 |
|-----|-----|
| [onError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aa90039556e52de79965ca4d338c83ebf) | 错误回调，SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。 |
| [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a2e4c89560e538402907c1aa8fa6b68d1) | 警告回调：用于告知您一些非严重性问题，例如出现了卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a9540be761c1563aa2d8eddb62ccb5578) | 已加入房间的回调。 |
| [onExitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ad5ac26478033ea9c0339462c69f9c89e) | 离开房间的事件回调。 |
| [onSwitchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a497f7b16f98dae3e8aa735d7d19df1ff) | 切换角色结果回调。 |
| [onConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a9bc4aec6ac8593f3171f8ab6b6e91658) | 请求跨房通话（主播 PK）的结果回调。 |
| [onDisconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a6c11aecb5474f578ce0b83e346b14cac) | 结束跨房通话（主播 PK）的结果回调。 |
| [onSwitchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aff76a17875e1eda9c4c7112a9c280f23) | 切换房间 (switchRoom) 的结果回调。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ac917f8d9bfc0ba8fdf86a33baba14149) | 有用户加入当前房间。 |
| [onRemoteUserLeaveRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a7d921af747d72aa87a88ade6a238efc0) | 有用户离开当前房间。 |
| [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#af6669bcf5f2fd63ee63fd6d3f6b5823a) | 用户是否开启摄像头视频。 |
| [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a15be39bb902bf917321b26701e961286) | 用户是否开启屏幕分享。 |
| [onUserAudioAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a166aaaff75287cfbb84f64e0dcab79dc) | 用户是否开启音频上行。 |
| [onFirstVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aa25eb882b81fd83b1aedf7a4248fd15a) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a6c059e46c986cfae0f959cd833a08130) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a266f7551ab47384616b36ad2783615d1) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#acb73daf4ce82cd03f787f057b233b412) | 首帧本地音频数据已经被送出。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a7a959df0ee5e4d6fa45f0e0785998daf) | 网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ab392e7b7325c89a260ce47b1a6b7dde4) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aed43a70b4a95eb95181e2b410013bf54) | SDK 跟服务器的连接断开。 |
| [onTryToReconnect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a1c8654b64e4bde42a8a24954ecf2cb2d) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a36d96a42ec4b00a0e3808f7f8460cd7f) | SDK 跟服务器的连接恢复。 |
| [onSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#abeea4e8810cce9a13a4cbb2e020f0da8) | 服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aaa74021e5fd2564afb2df50e25eedeff) | 摄像头准备就绪。 |
| [onMicDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#afdac7dee94451913a4dc9982badc8035) | 麦克风准备就绪。 |
| [onUserVoiceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a04422f826fccefdd91d4ecd42b124686) | 用于提示音量大小的回调,包括每个 userId 的音量和远端总音量。 |
| [onDeviceChange](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a2ce42edc00da08dd4aafa5e1e60927be) | 本地设备通断回调。 |
| [onTestMicVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a199c708ee69b2667e89515d14250de5f) | 麦克风测试音量回调。 |
| [onTestSpeakerVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a7cc29016572d6aa30f389df92d70c048) | 扬声器测试音量回调。 |
| [onAudioDeviceCaptureVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a32109c06ac9c5be57d1be55d70d17ef1) | 当前音频采集设备音量变化通知。 |
| [onAudioDevicePlayoutVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aa1340bc299119aede65225ca6f1ddd0e) | 当前音频播放设备音量变化通知。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ad8a3be194ced8ec841e628a285f64703) | 收到自定义消息回调。 |
| [onMissCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a19d8b754611731c2c2e321293ba0d9dc) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aa6b8f609e33400155de150bbf1231121) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a04ff5d445af7afbe35a68fde8c41b57a) | 开始向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 startPublishing() 接口。 |
| [onStopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#acfd26e70f6c71dd1723b42c4be603eb8) | 停止向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#afc7d31fcd57646ec375cc3ddc51b2d6c) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ab491cc44a65e04adb1d5230707e84597) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a77631560b26c7343df3d9bc9a2e0390e) | 设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。 |


### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureCovered](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aca39d43f65ee8d5007ce075d8c808dc1) | 当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。 |
| [onScreenCaptureStarted](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a7d15537d26fb001045ff95157d59ed3f) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a9e49f6e6887d63e3e817033681f0ad95) | 当屏幕分享暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a399959bd81e349cb76c9b7c939202410) | 当屏幕分享恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStoped](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ad0c359a7cefb8f246d498a3fbf52b1ac) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 弃用接口回调

| API | 描述 |
|-----|-----|
| [onUserEnter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aff18b3bc5b1e448b21b7614e5716e73e) | 废弃接口：有主播加入当前房间。 |
| [onUserExit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a0d1361e52e96b4c7c1a5f1b89f4ef0fb) | 废弃接口：有用户（主播）离开当前房间。 |
| [onAudioEffectFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#abe967d855abae66836877fe0dacf8b5f) | 废弃接口：播放音效结束回调。 |
| [onPlayBGMBegin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a61d9fa641b1790094e955aeb355cca92) | 废弃接口：开始播放背景音乐。 |
| [onPlayBGMProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a6dade9af4a799d8f47fba53c5f1015b6) | 废弃接口：播放背景音乐的进度。 |
| [onPlayBGMComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#aff8d7c6c3d2a5984ddd6448008041340) | 废弃接口：播放背景音乐结束。 |


### 视频数据帧的自定义处理回调

| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a183dde7faae6b9c62b0b6d9e8422de65) | 自定义视频渲染回调。 |


### 声音数据帧的自定义处理回调（只读）

回调函数是在 SDK 内部线程同步抛出来的，请不要做耗时操作。 
>?请按需定义相关函数实现，减少不必要的性能损耗。

| API | 描述 |
|-----|-----|
| [onCapturedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ad207bbc5b8ab7885540fb5a2de1e4d3d) | 本地麦克风采集到的音频数据回调。 |
| [onPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a0014b81d218cde7372580dd5995a1b24) | 混音前的每一路远程用户的音频数据（例如您要对某一路的语音进行文字转换，必须要使用这里的原始数据，而不是混音之后的数据）。 |
| [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#ac5262e14766154bda8ad437923285567) | 各路音频数据混合后送入喇叭播放的音频数据。 |


### 日志相关回调

| API | 描述 |
|-----|-----|
| [onLog](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a12a92b897208733ffa67af6fe959611d) | 有日志打印时的回调。 |


## 关键类型定义

| 类名 | 描述 |
|-----|-----|
| [TRTCImageBuffer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a115d7544222e40e31d1766f7770f4619) | 图缓存。 |
| [TRTCScreenCaptureSourceInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a78b6e0861f6c951b7269e5b0e13b8c36) | 屏幕采集信息。 |
| [SIZE](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#classManageLiteAV_1_1SIZE) | 记录 buffer 的长宽。 |
| [ITRTCScreenCaptureSourceList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#interfaceManageLiteAV_1_1ITRTCScreenCaptureSourceList) | 屏幕窗口列表。 |
| [ITRTCDeviceCollection](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#interfaceManageLiteAV_1_1ITRTCDeviceCollection) | 设备列表。 |
| [ITRTCDeviceInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#interfaceManageLiteAV_1_1ITRTCDeviceInfo) | 设备 Item 信息。 |
| [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a7ff9e03272f5c8e7b585e8c4eea784e1) | 进房相关参数。 |
| [TRTCVideoEncParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a43a83bd5122296aa87cc7f6e964921c5) | 视频编码参数。 |
| [TRTCNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a7cd5c078b248a32557a85226f1d30697) | 网络流控相关参数。 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#af6aab62536869726ee32b158ddbbf5ce) | 视频质量。 |
| [TRTCVolumeInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#abdeba26e639757957fd75f528ba14f6e) | 音量大小。 |
| [TRTCVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a0f5d7607bc170be903d207b4e0c87fab) | 视频帧数据。 |
| [TRTCAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a3c9f428bf1fc390b37a9c74accf226c6) | 音频帧数据。 |
| [TRTCSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a8858167e09ab4d55f5e49c89bd4a1848) | 网络测速结果。 |
| [RECT](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a04ac63459343f4b03b918f0496fdde7e) | 记录矩形的四个点坐标。 |
| [TRTCMixUser](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#ac5b1947f21f77726cbff822eaf0003f9) | 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a6066a5537ad8c1bc6158d43e8a4765db) | 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a0b977361cb4d84b1ece0b26c949dcde6) | CDN 旁路推流参数。 |
| [TRTCAudioRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#a724e3aa5cbc2249b7ce31bd7f9362d7b) | 录音参数。 |
| [TRTCAudioEffectParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#ada7b7fc07d775f1a553049e9d6f3f98c) | 音效播放。 |
| [TRTCLocalStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#classManageLiteAV_1_1TRTCLocalStatistics) | 自己本地的音视频统计信息。 |
| [TRTCRemoteStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#classManageLiteAV_1_1TRTCRemoteStatistics) | 远端成员的音视频统计信息。 |
| [TRTCStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__csharp.html#classManageLiteAV_1_1TRTCStatistics) | 统计数据。 |

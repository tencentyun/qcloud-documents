## TRTCCloud @ TXLiteAVSDK

### 基础方法

| API | 描述 |
|-----|-----|
| [sharedInstance](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ac5da416bb06d461c7e1e555e3fd143ee) | 创建 [TRTCCloud](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloud) 单例。 |
| [destroySharedInstance](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a69e76ca12b727c7cbcbdda274fc007a2) | 销毁 [TRTCCloud](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloud) 单例。 |
| [setListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a22fe2f31f2ef62fb3c6cba083dc6c016) | 设置回调接口 TRTCCloudListener，用户获得来自 [TRTCCloud](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloud) 的各种状态通知。 |
| [setListenerHandler](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a48c867145dcc09289f7af41871b4fdd9) | 设置驱动 [TRTCCloudListener](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudListener) 回调的队列。 |


### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c) | 进入房间，若房间不存在，系统将自动创建一个新房间。 |
| [exitRoom](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a41d16a97a9cb8f16ef92f5ef5bfebee1) | 离开房间。 |
| [switchRole](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a915a4b3abca0e41f057022a4587faf66) | 切换角色，仅适用于直播场景（TRTC_APP_SCENE_LIVE 和 TRTC_APP_SCENE_VOICE_CHATROOM）。 |
| [ConnectOtherRoom](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ac1ab7e4a017b99bb91d89ce1b0fac5fd) | 请求跨房通话（主播 PK）。 |
| [DisconnectOtherRoom](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#af777ac398ac47c8e5649c983fa2053fa) | 退出跨房通话。 |
| [setDefaultStreamRecvMode](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0b8d004665d5003ce1d9a48a9ab551b3) | 设置音视频数据接收模式，需要在进房前设置才能生效。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a1c168a9aa35ccd0b24981526425e4730) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3067efa528fb9ffb8cf7685ce29925d4) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a41aefb8be652f8f6803020e543acaadc) | 开始向友商云的直播 CDN 转推。 |
| [stopPublishCDNStream](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0e1e8a1eb1cac3f5e5d4433b4aa21e8e) | 停止向非腾讯云地址转推。 |
| [setMixTranscodingConfig](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#af7cf5544f9b8027e9526c32319a13838) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a84098740a2e69e3d1f02735861614116) | 开启本地视频的预览画面。 |
| [stopLocalPreview](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#af6ee50bf2c4c592294061077fc727505) | 停止本地视频采集及预览。 |
| [muteLocalVideo](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a13a2e406bffafecb96bfeac48d82746b) | 暂停/恢复推送本地的视频数据。 |
| [startRemoteView](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) | 开始显示远端视频画面。 |
| [stopRemoteView](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a8f3e86bc219090d0e8f2d5c2fab4467a) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#addaac0786ac0bd6e73a5f35c038df127) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a79f78532789dc6bbf67b128d004fab6a) | 暂停/恢复接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a2d8a7b74068026a85158262cc9aedd66) | 暂停/恢复接收所有远端视频流。 |
| [setVideoEncoderParam](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ae047d96922cb1c19135433fa7908e6ce) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a02631a5e4251657875535c38ab319239) | 设置网络流控相关参数。 |
| [setLocalViewFillMode](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#af36ab721c670e5871e5b21a41518b51d) | 设置本地图像的渲染模式。 |
| [setRemoteViewFillMode](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ab4197bc2efb62b471b49f926bab9352f) | 设置远端图像的渲染模式。 |
| [setLocalViewRotation](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a87fd1307871debc7c051de4878eb6d69) | 设置本地图像的顺时针旋转角度。 |
| [setRemoteViewRotation](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a8478d804d2a07520ce2bc5466b727839) | 设置远端图像的顺时针旋转角度。 |
| [setVideoEncoderRotation](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a272afecae1d291033cb9cd4b1d7b52e0) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。|
| [setLocalViewMirror](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa353b5cf5662c43252eb8e5132f041c1) | 设置本地摄像头预览画面的镜像模式。 |
| [setVideoEncoderMirror](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a32d9ba3696b305373508253f9bee8236) | 设置编码器输出的画面镜像模式。 |
| [setGSensorMode](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#abbbe1548bfba0bd082a08478ce35e9bc) | 设置重力感应的适应模式。 |
| [enableEncSmallVideoStream](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3a040c5012cf572b9dfabcca87f2cbb7) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a2a018cc1010587ea9b0fbd791eb3c54f) | 选定观看指定 uid 的大画面或小画面。 |
| [setPriorRemoteVideoStreamType](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ad2efc2703c86ee009bd4a1d440d0c1e0) | 设定观看方优先选择的视频质量。 |
| [snapshotVideo](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ae75285c95fc53651e24fa23c4141093b) | 视频画面截图。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a9428ef48d67e19ba91272c9cf967e35e) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a272bba21d046347ac42d76069ba5972c) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a37f52481d24fa0f50842d3d8cc380d86) | 静音/取消静音本地的音频。 |
| [setAudioRoute](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a4a3dda74823afa597b42b981257e9e22) | 设置音频路由。 |
| [muteRemoteAudio](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a8d8b8edf120036d4049cc3639a1ce81f) | 静音/取消静音指定的远端用户的声音。 |
| [muteAllRemoteAudio](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a5b63c0796404b80323ae67aafe0384ba) | 静音/取消静音所有用户的声音。 |
| [setAudioCaptureVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a6af5e2c4819a683042f382688aff41e9) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a81037b960fb2b3501b1e8e60f2b5f9f3) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0b20e1eec637c82190c5264d78d686af) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a5a1636fa1300b0b4e2829846c36450a2) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ad1dbca6b3f22072d7b3963473d02e0d7) | 启用音量大小提示。 |
| [startAudioRecording](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#af89a64fd6ccb822850f9bf7e8a1c8462) | 开始录音。 |
| [stopAudioRecording](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a7d55e5f15d1291afc89f7e1dfe0a25d8) | 停止录音。 |
| [setSystemVolumeType](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a5438dcc45dc2f26a3771a5feddcdef5d) | 设置通话时使用的系统音量类型。 |
| [enableAudioEarMonitoring](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a9306bca7c6a13e0443a3fa1b40c9f343) | 开启耳返。 |


### 摄像头相关接口函数

| API | 描述 |
|-----|-----|
| [switchCamera](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a1b43a65a32f9dcb81b39b9c51c5bc4c6) | 切换摄像头。 |
| [isCameraZoomSupported](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ac7ae26eca2f9a673121803d6d175b034) | 查询当前摄像头是否支持缩放。 |
| [setZoom](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a9f761eebdf04f724e0d1591c41c6045f) | 设置摄像头缩放因子（焦距）。 |
| [isCameraTorchSupported](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a645183ba7c0cea748973796cb38aad8c) | 查询是否支持开关闪光灯（手电筒模式）。 |
| [enableTorch](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a09253f6547914d54058831b61325e770) | 开关闪光灯。 |
| [isCameraFocusPositionInPreviewSupported](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#abd39aca40adfc8da6beaf32141f84cfa) | 查询是否支持设置焦点。 |
| [setFocusPosition](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa7c65fb033727804e7a79b8f135c776c) | 设置摄像头焦点。 |
| [isCameraAutoFocusFaceModeSupported](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a23f25ffb81215a32517da78455459ff2) | 查询是否支持自动识别人脸位置。 |


### 美颜滤镜相关接口函数

| API | 描述 |
|-----|-----|
| [getBeautyManager](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3fdfeb3204581c27bbf1c8b5598714fb) | 获取美颜管理对象。 |
| [setWatermark](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a1083aaf0441e3d90ce6641d278a97a63) | 添加水印。 |


### 辅流相关接口函数

| API | 描述 |
|-----|-----|
| [startScreenCapture](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa643c448da33d5c9f40b4442a2691f4d) | 启动屏幕分享。 |
| [stopScreenCapture](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ab6c3014f6f88c775aa91fccea19ce8a4) | 停止屏幕采集。 |
| [pauseScreenCapture](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a56af9ada2d43cfb497fe44fa6d4b99cf) | 暂停屏幕分享。 |
| [resumeScreenCapture](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a155ed7b6bcf2edf3259d26b8f8fdfe7e) | 恢复屏幕分享。 |
| [startRemoteSubStreamView](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#acdbe3829d20f58cedd5a0c2f49ea24dc) | 开始显示远端用户的屏幕分享画面。 |
| [stopRemoteSubStreamView](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ae5f540d795425046c9166b0a2361a8de) | 停止显示远端用户的屏幕分享画面。 |
| [setRemoteSubStreamViewFillMode](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a73f66e66ffee44e19ebb4d8c56c89718) | 设置屏幕分享画面的显示模式。 |
| [setRemoteSubStreamViewRotation](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#affdf177b468fdf40a41782e2e47524cc) | 设置屏幕分享画面的顺时针旋转角度。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a68187fc9a1656bb32cf825363745f7e7) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a39b79b77e3795e918383e945e9513d35) | 向 SDK 投送自己采集的视频数据。 |
| [setLocalVideoRenderListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa3cbb7a501c3151d94473965e2538c7a) | 设置本地视频的自定义渲染回调。 |
| [setRemoteVideoRenderListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a4fca6803d13e4c7ff00dcac2974637e4) | 设置远端视频的自定义渲染回调。 |
| [enableCustomAudioCapture](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a206b9ce3594aa535b633d4f7c8f97210) | 启用音频自定义采集模式。 |
| [sendCustomAudioData](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a30a542b7d540c8699595a22ca3401f29) | 向 SDK 投送自己采集的音频数据。 |
| [setAudioFrameListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a034b6fce9a517267acd874c243efc575) | 设置音频数据回调。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa4847ad53acc9ab5990194b21ff5b070) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a034f9e1effbdadf8b9bfb7f3f06486c4) | 将小数据量的自定义数据嵌入视频帧中。 |


### 背景混音相关接口函数

| API | 描述 |
|-----|-----|
| [playBGM](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3df738557f5c658c37174ac9aeae9684) | 启动播放背景音乐。 |
| [stopBGM](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3ee7bdd15de4ba9010aa5ece3abff0ab) | 停止播放背景音乐。 |
| [pauseBGM](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a21ddee03e6f4cec028a24e5d5e30955e) | 暂停播放背景音乐。 |
| [resumeBGM](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aaa8b34ef2b334bd22a1cb6541a4c6702) | 继续播放背景音乐。 |
| [getBGMDuration](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ae7342a8bcfda22a872aa684f06a4677f) | 获取音乐文件总时长，单位毫秒。 |
| [setBGMPosition](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a78f901b6175352a31b0236776bfdc661) | 设置 BGM 播放进度。 |
| [setBGMVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ada9c2b4aaf9a1a9ab9cd846593fdf9e6) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ab1e1c94c9efd967dbffb46d3ba08fef5) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a535eab48f9df390f4de5ebd5afcd59e3) | 设置背景音乐远端播放音量的大小。 |
| [setReverbType](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a6f4f89be3c810acfa2430ad65fd7ea68) | 设置混响效果。 |
| [setVoiceChangerType](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a37acaf3b2539e0b1c18123a646e91189) | 设置变声类型。 |


### 音效相关接口函数

| API | 描述 |
|-----|-----|
| [playAudioEffect](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ad1ed7667282eccfac1992c1e547a5aeb) | 播放音效。 |
| [setAudioEffectVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a214846db40c2d1be2fe8008c6637f631) | 设置音效的音量。 |
| [stopAudioEffect](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a18e4ca6939d005a1d67cef397ee8b8d4) | 停止音效。 |
| [stopAllAudioEffects](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a770543c80d3a5629a26d1382535fb6c4) | 停止所有音效。 |
| [setAllAudioEffectsVolume](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a9bb41c4ff1a5b24ca742fe3ce45a2bc0) | 设置所有音效的音量。 |
| [pauseAudioEffect](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ab32923d04ce164b82879b3e05833959f) | 暂停音效。 |
| [resumeAudioEffect](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a33ab6e798d3da245435166464b702d4f) | 恢复音效。 |


### 网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0dbceb18d61d99ca33e967427dd0a344) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3e862cef0e818ddecdc3dc4d66a6f8f9) | 停止服务器测速。 |


### Log 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aeb5168abbd62c631b65247e6289d1e2d) | 获取 SDK 版本信息。 |
| [setLogLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a0ec9520dda7e2062f7455956d093113b) | 设置 Log 输出级别。 |
| [setConsoleEnabled](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a2942d9d05045d3f0e0add45a3e10b3ee) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a495d2122a4098ab371d825c1f0bb90f5) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a44c20358d08da798e0f15d142c9c3914) | 修改日志保存路径。 |
| [setLogListener](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a299a71f4addb3638c7790de446fbdf37) | 设置日志回调。 |
| [showDebugView](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ad2cdb5d447114534f53bad5bdc48afba) | 显示仪表盘。 |
| [setDebugViewMargin](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa2014c293033e9ea60aa6ffd525ee2fa) | 设置仪表盘的边距。 |
| [TRTCViewMargin](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#adeb72b7f954af864743cdbeb283c534b) | 视图边距。 |
| [callExperimentalAPI](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a37f331dd0cfff51ab5a3becf4950a55e) | 调用实验性 API 接口。 |


### 弃用接口函数

| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#ab356494d1b7dd924be69b23aa631a85a) | 设置麦克风的音量大小。 |
| [setBeautyStyle](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a46ffe2b60f916a87345fb357110adf10) | 设置美颜、美白、红润效果级别。 |
| [setEyeScaleLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a4ff69ce783f648f23dd737641344ac52) | 设置大眼级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFaceSlimLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a78a159a2a45d24dbd5722eb73d237e8a) | 设置瘦脸级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFaceVLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a58bb7ce1fbbc40a50647d64693ac5d41) | 设置 V 脸级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setChinLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a774eb948494cecec024771434ccd9d3c) | 设置下巴拉伸或收缩，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFaceShortLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aa14091f0d02330cbd02da5186e9dd874) | 设置短脸级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setNoseSlimLevel](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3f806534b2596d7e29ea0ea6c070b591) | 设置瘦鼻级别，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [selectMotionTmpl](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a521a0446d0922d480a1eec4b86f1ecb2) | 选择使用哪一款 AI 动效挂件，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setMotionMute](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a066cbf8f4f6c1cd23fe9451b82c5a073) | 设置动效静音，该接口仅在 [企业版 SDK](https://cloud.tencent.com/document/product/647/32689#Enterprise) 中生效。 |
| [setFilter](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a925323ab809957ccaeb4cef30841cb72) | 设置指定素材滤镜特效。 |
| [setFilterConcentration](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a5fb4c8bc9948e61a75b9ef85f618309d) | 设置滤镜浓度。 |
| [setGreenScreenFile](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#aef56a36b901d5e525ee539e7d5642063) | 设置绿幕背景视频（企业版有效，其它版本设置此参数无效）。 |


### 播放背景音乐的回调接口

播放背景音乐的回调接口。

| API | 描述 |
|-----|-----|
| [onBGMStart](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#af7f9f419dafff42ef750256f953a88c9) | 音乐播放开始的回调通知。 |
| [onBGMProgress](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a30ab555520fa5a478f633394b9cd4d14) | 音乐播放进度的回调通知。 |
| [onBGMComplete](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a444c6749e7cb77466940ec1de1c88546) | 音乐播放结束的回调通知。 |



## TRTCCloudListener @ TXLiteAVSDK

腾讯云视频通话功能的事件回调接口。

### 错误事件和警告事件

| API | 描述 |
|-----|-----|
| [onError](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a511d0007e1990e63e853e46ce3f02670) | 错误回调，表示 SDK 不可恢复的错误，一定要监听并分情况给用户适当的界面提示。 |
| [onWarning](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a9871472ee8195dfc5d0c34fae3294465) | 警告回调，用于告知您一些非严重性问题，例如出现卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#abf0525c3433cbd923fd1f13b42c416a2) | 已加入房间的回调。 |
| [onExitRoom](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ad5ac26478033ea9c0339462c69f9c89e) | 离开房间的事件回调。 |
| [onSwitchRole](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a6a4b7f39bc5dfb0c5d75ef8802e2e758) | 切换角色的事件回调。 |
| [onConnectOtherRoom](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ac9fd524ab9de446f4aaf502f80859e95) | 请求跨房通话（主播 PK）的结果回调。 |
| [onDisConnectOtherRoom](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a6f7db4f0aaadad2cdfa822ba0060414c) | 结束跨房通话（主播 PK）的结果回调。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a891f38e4cdeaf3ff18937726f0269c2c) | 有用户加入当前房间。 |
| [onRemoteUserLeaveRoom](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#abfec3607f97823956fad77a7a63dc441) | 有用户离开当前房间。 |
| [onUserVideoAvailable](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) | 远端用户是否存在可播放的主路画面（一般用于摄像头）。 |
| [onUserSubStreamAvailable](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a80bcaac82e5372245746a4bc63656390) | 远端用户是否存在可播放的辅路画面（一般用于屏幕分享）。 |
| [onUserAudioAvailable](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ac474bbf919f96c0cfda87c93890d871f) | 远端用户是否存在可播放的音频数据。 |
| [onFirstVideoFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a0c1ccf1bec2d3261e9f11894b32e357e) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a3516aaef4cb63e512cd713e4ec96d118) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a181788d7441d41022ce014095ee05353) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#acb73daf4ce82cd03f787f057b233b412) | 首帧本地音频数据已经被送出。 |
| [onUserEnter](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#aff18b3bc5b1e448b21b7614e5716e73e) | 废弃接口：有主播加入当前房间。 |
| [onUserExit](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a0d1361e52e96b4c7c1a5f1b89f4ef0fb) | 废弃接口：有主播离开当前房间。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#aba07d4191391dadef900422521f34e5b) | 网络质量，该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a003278cb7647cd577702e8367c9e0a58) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#aed43a70b4a95eb95181e2b410013bf54) | SDK 跟服务器的连接断开。 |
| [onTryToReconnect](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a1c8654b64e4bde42a8a24954ecf2cb2d) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a36d96a42ec4b00a0e3808f7f8460cd7f) | SDK 跟服务器的连接恢复。 |
| [onSpeedTest](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ab77a0dff287e1642527cd414fc5fe5f5) | 服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#aaa74021e5fd2564afb2df50e25eedeff) | 摄像头准备就绪。 |
| [onMicDidReady](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#afdac7dee94451913a4dc9982badc8035) | 麦克风准备就绪。 |
| [onAudioRouteChanged](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a1a608275247d2912e26bd83f648d6378) | 音频路由发生变化，音频路由即声音由哪里输出（扬声器或听筒）。 |
| [onUserVoiceVolume](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a4e3b79968ccbb86de5b79e326a2daafa) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a51fd654c5ec030ff84f208f2ba50298d) | 收到自定义消息回调。 |
| [onMissCustomCmdMsg](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a98af11ba5b25d3124bd9533dc5197127) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ad3640e6bf80a1f93991644701e9b0d96) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishing](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a03d0ef687b2973b9b13cb041bd35bb85) | 开始向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloud) 中的 startPublishing() 接口。 |
| [onStopPublishing](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ad3cb7e5ceb69954d762eafca5a0e3a62) | 停止向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloud) 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a64df36d6c56dd69d8b6f051fd9fffcbc) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a6c3d63538897ddb9ed1b170819c41dca) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#af1c79a5ec3e0c106939e7f0d7849d694) | 设置云端的混流转码参数的回调，对应于 [TRTCCloud](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloud) 中的 setMixTranscodingConfig() 接口。 |


### 音效回调

| API | 描述 |
|-----|-----|
| [onAudioEffectFinished](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#abe967d855abae66836877fe0dacf8b5f) | 播放音效结束回调。 |


### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureStarted](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a7d15537d26fb001045ff95157d59ed3f) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a12c57991389e32f04a56774df5d1ce76) | 当屏幕分享调用 [TRTCCloud.pauseScreenCapture()](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a56af9ada2d43cfb497fe44fa6d4b99cf) 暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#ade88963a254d297d3be1993e8a599f6e) | 当屏幕分享调用 [TRTCCloud.resumeScreenCapture()](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a155ed7b6bcf2edf3259d26b8f8fdfe7e) 恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStopped](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a6c09b21b733da7d314d1db2cb03c8bcb) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 视频数据帧的自定义渲染回调

| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a41b44f9b0583bbf56ad9e96065ea825c) | 自定义视频渲染回调。 |


### 声音数据帧的自定义处理回调（只读）

| API | 描述 |
|-----|-----|
| [onCapturedAudioFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a13dfcc17ca7ea6bcff7b0f5f6d167e33) | 本地麦克风采集到的音频数据回调。 |
| [onPlayAudioFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a60a54a148edf641a85fbc07bc294fe11) | 混音前的每一路远程用户的音频数据，即混音前的各路原始数据。例如，对某一路音频进行文字转换时，您必须使用该路音频的原始数据。 |
| [onMixedPlayAudioFrame](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a580e94224357c38adf6ed883ab3321f7) | 各路音频数据混合后送入喇叭播放的音频数据。 |


### 日志相关回调
>?建议在比较早初始化的类中设置回调对象，例如 Application。

| API | 描述 |
|-----|-----|
| [onLog](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#a77d78090666e330606b670bf8ce2d854) | 有日志打印时的回调。 |


### 截图回调

| API | 描述 |
|-----|-----|
| [onSnapshotComplete](http://doc.qcloudtrtc.com/group__TRTCCloudListener__android.html#aa9c6d0488175f6d19f5f38f6307cfea4) | 截图完成时回调。 |


## 关键类型定义

| 类名 | 描述 |
|-----|-----|
| [TRTCParams](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#a674b3c744a0522802d68dfd208763b59) | 进房参数。 |
| [TRTCVideoEncParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoEncParam) | 编码参数。 |
| [TRTCNetworkQosParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCNetworkQosParam) | 网络流控相关参数。 |
| [TRTCQuality](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCQuality) | 视频（或网络）质量。 |
| [TRTCTexture](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCTexture) | 视频纹理数据，包含纹理 ID 及 EGL 环境。 |
| [TRTCVideoFrame](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoFrame) | 视频帧信息。 |
| [TRTCAudioFrame](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioFrame) | 音频帧数据。 |
| [TRTCVolumeInfo](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVolumeInfo) | 音量大小。 |
| [TRTCSpeedTestResult](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCSpeedTestResult) | 网络测速结果。 |
| [TRTCMixUser](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#afe6b433091e7b7219c4e55194855612e) | 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#a6066a5537ad8c1bc6158d43e8a4765db) | 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCPublishCDNParam) | 旁路推流参数。 |
| [TRTCAudioRecordingParams](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioRecordingParams) | 录音参数。 |
| [TRTCAudioEffectParam](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#ad82a59c2209c0596dabaee1152820494) | 音效。 |
| [TRTCScreenShareParams](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCScreenShareParams) | 屏幕分享参数。 |
| [TRTCStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCStatistics) | 统计数据。 |
| [TRTCRemoteStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCStatistics_1_1TRTCRemoteStatistics) | 远端成员的音视频统计信息。 |
| [TRTCLocalStatistics](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCStatistics_1_1TRTCLocalStatistics) | 自己本地的音视频统计信息。 |

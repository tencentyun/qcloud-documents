## ITRTCCloud @ TXLiteAVSDK

腾讯云视频通话功能的主要接口类。


### 创建与销毁

| API | 描述 |
|-----|-----|
| [getTRTCShareInstance](https://cloud.tencent.com/document/product/647/36778#gettrtcshareinstance) | 创建 ITRTCCloud 单例。         |
| [destroyTRTCShareInstance](https://cloud.tencent.com/document/product/647/36778#destroytrtcshareinstance) | 释放 ITRTCCloud 单例对象。          |


### 设置 TRTCCloudCallback 回调

| API | 描述 |
|-----|-----|
| [addCallback](https://cloud.tencent.com/document/product/647/36778#addcallback) | 设置回调接口 [ITRTCCloudCallback](https://cloud.tencent.com/document/product/647/36779#itrtccloudcallback)。 |
| [removeCallback](https://cloud.tencent.com/document/product/647/36778#removecallback) | 移除事件回调。 |


### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](https://cloud.tencent.com/document/product/647/36778#enterroom) | 进入房间。 |
| [exitRoom](https://cloud.tencent.com/document/product/647/36778#exitroom) | 离开房间。 |
| [switchRole](https://cloud.tencent.com/document/product/647/36778#switchrole) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE）。 |
| [connectOtherRoom](https://cloud.tencent.com/document/product/647/36778#connectotherroom) | 请求跨房通话（主播 PK）。 |
| [disconnectOtherRoom](https://cloud.tencent.com/document/product/647/36778#disconnectotherroom) | 关闭跨房连麦。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](https://cloud.tencent.com/document/product/647/36778#startlocalpreview) | 开启本地视频的预览画面。 |
| [stopLocalPreview](https://cloud.tencent.com/document/product/647/36778#stoplocalpreview) | 停止本地视频采集及预览。 |
| [muteLocalVideo](https://cloud.tencent.com/document/product/647/36778#mutelocalvideo) | 是否屏蔽自己的视频画面。 |
| [startRemoteView](https://cloud.tencent.com/document/product/647/36778#startremoteview) | 开始显示远端视频画面。 |
| [stopRemoteView](https://cloud.tencent.com/document/product/647/36778#stopremoteview) | 停止显示远端视频画面。 |
| [stopAllRemoteView](https://cloud.tencent.com/document/product/647/36778#stopallremoteview) | 停止显示所有远端视频画面。 |
| [muteRemoteVideoStream](https://cloud.tencent.com/document/product/647/36778#muteremotevideostream) | 暂停接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](https://cloud.tencent.com/document/product/647/36778#muteallremotevideostreams) | 停止接收所有远端视频流。 |
| [setVideoEncoderParam](https://cloud.tencent.com/document/product/647/36778#setvideoencoderparam) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](https://cloud.tencent.com/document/product/647/36778#setnetworkqosparam) | 设置网络流控相关参数。 |
| [setLocalViewFillMode](https://cloud.tencent.com/document/product/647/36778#setlocalviewfillmode) | 设置本地图像的渲染模式。 |
| [setRemoteViewFillMode](https://cloud.tencent.com/document/product/647/36778#setremoteviewfillmode) | 设置远端图像的渲染模式。 |
| [setLocalViewRotation](https://cloud.tencent.com/document/product/647/36778#setlocalviewrotation) | 设置本地图像的顺时针旋转角度。 |
| [setRemoteViewRotation](https://cloud.tencent.com/document/product/647/36778#setremoteviewrotation) | 设置远端图像的顺时针旋转角度。 |
| [setVideoEncoderRotation](https://cloud.tencent.com/document/product/647/36778#setvideoencoderrotation) | 设置视频编码输出的（即远端用户所观看到的，以及服务器录制下来的）画面方向。 |
| [setLocalViewMirror](https://cloud.tencent.com/document/product/647/36778#setlocalviewmirror) | 设置本地摄像头预览画面的镜像模式。 |
| [setVideoEncoderMirror](https://cloud.tencent.com/document/product/647/36778#setvideoencodermirror) | 设置编码器输出的画面镜像模式。 |
| [enableSmallVideoStream](https://cloud.tencent.com/document/product/647/36778#enablesmallvideostream) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](https://cloud.tencent.com/document/product/647/36778#setremotevideostreamtype) | 选定观看指定 userId 的大画面或小画面。 |
| [setPriorRemoteVideoStreamType](https://cloud.tencent.com/document/product/647/36778#setpriorremotevideostreamtype) | 设定观看方优先选择的视频质量。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://cloud.tencent.com/document/product/647/36778#startlocalaudio) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](https://cloud.tencent.com/document/product/647/36778#stoplocalaudio) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](https://cloud.tencent.com/document/product/647/36778#mutelocalaudio) | 静音本地的音频。 |
| [muteRemoteAudio](https://cloud.tencent.com/document/product/647/36778#muteremoteaudio) | 静音掉某一个用户的声音。 |
| [muteAllRemoteAudio](https://cloud.tencent.com/document/product/647/36778#muteallremoteaudio) | 静音掉所有用户的声音。 |
| [enableAudioVolumeEvaluation](https://cloud.tencent.com/document/product/647/36778#enableaudiovolumeevaluation) | 启用或关闭音量大小提示。 |
| [startAudioRecording](https://cloud.tencent.com/document/product/647/36778#startaudiorecording) | 开始录音。 |
| [stopAudioRecording](https://cloud.tencent.com/document/product/647/36778#stopaudiorecording) | 停止录音。 |


### 摄像头相关接口函数

| API | 描述 |
|-----|-----|
| [getCameraDevicesList](https://cloud.tencent.com/document/product/647/36778#getcameradeviceslist) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](https://cloud.tencent.com/document/product/647/36778#setcurrentcameradevice) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](https://cloud.tencent.com/document/product/647/36778#getcurrentcameradevice) | 获取当前使用的摄像头。 |


### 音频设备相关接口函数

| API | 描述 |
|-----|-----|
| [getMicDevicesList](https://cloud.tencent.com/document/product/647/36778#getmicdeviceslist) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](https://cloud.tencent.com/document/product/647/36778#getcurrentmicdevice) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](https://cloud.tencent.com/document/product/647/36778#setcurrentmicdevice) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](https://cloud.tencent.com/document/product/647/36778#getcurrentmicdevicevolume) | 获取当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](https://cloud.tencent.com/document/product/647/36778#setcurrentmicdevicevolume) | 设置麦克风设备的音量。 |
| [getSpeakerDevicesList](https://cloud.tencent.com/document/product/647/36778#getspeakerdeviceslist) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](https://cloud.tencent.com/document/product/647/36778#getcurrentspeakerdevice) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](https://cloud.tencent.com/document/product/647/36778#setcurrentspeakerdevice) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](https://cloud.tencent.com/document/product/647/36778#getcurrentspeakervolume) | 当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](https://cloud.tencent.com/document/product/647/36778#setcurrentspeakervolume) | 设置当前扬声器音量。 |


### 美颜相关接口函数

| API | 描述 |
|-----|-----|
| [setBeautyStyle](https://cloud.tencent.com/document/product/647/36778#setbeautystyle) | 设置美颜、美白以及红润效果级别。 |
| [setWaterMark](https://cloud.tencent.com/document/product/647/36778#setwatermark) | 设置水印。 |


### 辅流相关接口函数

| API | 描述 |
|-----|-----|
| [startRemoteSubStreamView](https://cloud.tencent.com/document/product/647/36778#startremotesubstreamview) | 开始渲染远端用户辅流画面。 |
| [stopRemoteSubStreamView](https://cloud.tencent.com/document/product/647/36778#stopremotesubstreamview) | 停止显示远端用户的屏幕分享画面。 |
| [setRemoteSubStreamViewFillMode](https://cloud.tencent.com/document/product/647/36778#setremotesubstreamviewfillmode) | 设置辅流画面的渲染模式。 |
| [getScreenCaptureSources](https://cloud.tencent.com/document/product/647/36778#getscreencapturesources) | 枚举可共享的窗口列表。 |
| [selectScreenCaptureTarget](https://cloud.tencent.com/document/product/647/36778#selectscreencapturetarget) | 设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。 |
| [startScreenCapture](https://cloud.tencent.com/document/product/647/36778#startscreencapture) | 启动屏幕分享。 |
| [pauseScreenCapture](https://cloud.tencent.com/document/product/647/36778#pausescreencapture) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://cloud.tencent.com/document/product/647/36778#resumescreencapture) | 恢复屏幕分享。 |
| [stopScreenCapture](https://cloud.tencent.com/document/product/647/36778#stopscreencapture) | 停止屏幕采集。 |
| [setSubStreamEncoderParam](https://cloud.tencent.com/document/product/647/36778#setsubstreamencoderparam) | 设置屏幕分享的编码器参数。 |
| [setSubStreamMixVolume](https://cloud.tencent.com/document/product/647/36778#setsubstreammixvolume) | 设置辅流的混音音量大小。 |


### 自定义采集和渲染

| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://cloud.tencent.com/document/product/647/36778#enablecustomvideocapture) | 启用视频自定义采集模式。 |
| [sendCustomVideoData](https://cloud.tencent.com/document/product/647/36778#sendcustomvideodata) | 向 SDK 投送自己采集的视频数据。 |
| [enableCustomAudioCapture](https://cloud.tencent.com/document/product/647/36778#enablecustomaudiocapture) | 启用音频自定义采集模式。开启该模式后，SDK 停止运行原有的音频采集流程，只保留编码和发送能力。 您需要用 [sendCustomAudioData()](https://cloud.tencent.com/document/product/647/36778#sendcustomaudiodata) 不断地向 SDK 塞入自己采集的视频画面。 |
| [sendCustomAudioData](https://cloud.tencent.com/document/product/647/36778#sendcustomaudiodata) | 向 SDK 投送自己采集的音频数据。 |
| [setLocalVideoRenderCallback](https://cloud.tencent.com/document/product/647/36778#setlocalvideorendercallback) | 设置本地视频自定义渲染。 |
| [setRemoteVideoRenderCallback](https://cloud.tencent.com/document/product/647/36778#setremotevideorendercallback) | 设置远端视频自定义渲染。 |
| [setAudioFrameCallback](https://cloud.tencent.com/document/product/647/36778#setaudioframecallback) | 设置音频数据回调。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://cloud.tencent.com/document/product/647/36778#sendcustomcmdmsg) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](https://cloud.tencent.com/document/product/647/36778#sendseimsg) | 将小数据量的自定义数据嵌入视频帧中。 |


### 背景混音相关接口函数

| API | 描述 |
|-----|-----|
| [playBGM](https://cloud.tencent.com/document/product/647/36778#playbgm) | 启动播放背景音乐。 |
| [stopBGM](https://cloud.tencent.com/document/product/647/36778#stopbgm) | 停止播放背景音乐。 |
| [pauseBGM](https://cloud.tencent.com/document/product/647/36778#pausebgm) | 暂停播放背景音乐。 |
| [resumeBGM](https://cloud.tencent.com/document/product/647/36778#resumebgm) | 继续播放背景音乐。 |
| [getBGMDuration](https://cloud.tencent.com/document/product/647/36778#getbgmduration) | 获取音乐文件总时长，单位：毫秒。 |
| [setBGMPosition](https://cloud.tencent.com/document/product/647/36778#setbgmposition) | 设置 BGM 播放进度。 |
| [setMicVolumeOnMixing](https://cloud.tencent.com/document/product/647/36778#setmicvolumeonmixing) | 设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。 |
| [setBGMVolume](https://cloud.tencent.com/document/product/647/36778#setbgmvolume) | 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。 |
| [startSystemAudioLoopback](https://cloud.tencent.com/document/product/647/36778#startsystemaudioloopback) | 打开系统声音采集。 |
| [stopSystemAudioLoopback](https://cloud.tencent.com/document/product/647/36778#stopsystemaudioloopback) | 关闭系统声音采集。 |
| [setSystemAudioLoopbackVolume](https://cloud.tencent.com/document/product/647/36778#setsystemaudioloopbackvolume) | 设置系统声音采集的音量。 |


### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](https://cloud.tencent.com/document/product/647/36778#startspeedtest) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://cloud.tencent.com/document/product/647/36778#stopspeedtest) | 停止服务器测速。 |
| [startCameraDeviceTest](https://cloud.tencent.com/document/product/647/36778#startcameradevicetest) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](https://cloud.tencent.com/document/product/647/36778#stopcameradevicetest) | 停止摄像头测试。 |
| [startMicDeviceTest](https://cloud.tencent.com/document/product/647/36778#startmicdevicetest) | 开启麦克风测试。 |
| [stopMicDeviceTest](https://cloud.tencent.com/document/product/647/36778#stopmicdevicetest) | 停止麦克风测试。 |
| [startSpeakerDeviceTest](https://cloud.tencent.com/document/product/647/36778#startspeakerdevicetest) | 开启扬声器测试。 |
| [stopSpeakerDeviceTest](https://cloud.tencent.com/document/product/647/36778#stopspeakerdevicetest) | 停止扬声器测试。 |


### 混流转码以及 CDN 旁路推流

| API | 描述 |
|-----|-----|
| [setMixTranscodingConfig](https://cloud.tencent.com/document/product/647/36778#setmixtranscodingconfig) | 启动（更新）云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。 |
| [startPublishCDNStream](https://cloud.tencent.com/document/product/647/36778#startpublishcdnstream) | 旁路转推到指定的推流地址。 |
| [stopPublishCDNStream](https://cloud.tencent.com/document/product/647/36778#stoppublishcdnstream) | 停止旁路推流。 |


### LOG 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](https://cloud.tencent.com/document/product/647/36778#getsdkversion) | 获取 SDK 版本信息。 |
| [setLogLevel](https://cloud.tencent.com/document/product/647/36778#setloglevel) | 设置 Log 输出级别。 |
| [setConsoleEnabled](https://cloud.tencent.com/document/product/647/36778#setconsoleenabled) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](https://cloud.tencent.com/document/product/647/36778#setlogcompressenabled) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](https://cloud.tencent.com/document/product/647/36778#setlogdirpath) | 设置日志保存路径。 |
| [setLogCallback](https://cloud.tencent.com/document/product/647/36778#setlogcallback) | 设置日志回调。 |
| [showDebugView](https://cloud.tencent.com/document/product/647/36778#showdebugview) | 显示仪表盘。 |
| [callExperimentalAPI](https://cloud.tencent.com/document/product/647/36778#callexperimentalapi) | 调用实验性 API 接口。 |


## TRTCCloudCallback @ TXLiteAVSDK

腾讯云视频通话功能的回调接口类。

### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](https://cloud.tencent.com/document/product/647/36779#onerror) | 错误回调：SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。 |
| [onWarning](https://cloud.tencent.com/document/product/647/36779#onwarning) | 警告回调：用于告知您一些非严重性问题，例如出现了卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](https://cloud.tencent.com/document/product/647/36779#onenterroom) | 已加入房间的回调。 |
| [onExitRoom](https://cloud.tencent.com/document/product/647/36779#onexitroom) | 离开房间的事件回调。 |
| [onSwitchRole](https://cloud.tencent.com/document/product/647/36779#onswitchrole) | 切换角色的事件回调。 |
| [onConnectOtherRoom](https://cloud.tencent.com/document/product/647/36779#onconnectotherroom) | 请求跨房通话（主播 PK）的结果回调。 |
| [onDisconnectOtherRoom](https://cloud.tencent.com/document/product/647/36779#ondisconnectotherroom) | 结束跨房通话（主播 PK）的结果回调。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onUserEnter](https://cloud.tencent.com/document/product/647/36779#onuserenter) | 有用户（主播）加入当前房间。 |
| [onUserExit](https://cloud.tencent.com/document/product/647/36779#onuserexit) | 有用户（主播）离开当前房间。 |
| [onUserVideoAvailable](https://cloud.tencent.com/document/product/647/36779#onuservideoavailable) | 用户是否开启摄像头视频。 |
| [onUserSubStreamAvailable](https://cloud.tencent.com/document/product/647/36779#onusersubstreamavailable) | 用户是否开启屏幕分享。 |
| [onUserAudioAvailable](https://cloud.tencent.com/document/product/647/36779#onuseraudioavailable) | 用户是否开启音频上行。 |
| [onFirstVideoFrame](https://cloud.tencent.com/document/product/647/36779#onfirstvideoframe) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](https://cloud.tencent.com/document/product/647/36779#onfirstaudioframe) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](https://cloud.tencent.com/document/product/647/36779#onsendfirstlocalvideoframe) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](https://cloud.tencent.com/document/product/647/36779#onsendfirstlocalaudioframe) | 首帧本地音频数据已经被送出。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://cloud.tencent.com/document/product/647/36779#onnetworkquality) | 网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://cloud.tencent.com/document/product/647/36779#onstatistics) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](https://cloud.tencent.com/document/product/647/36779#onconnectionlost) | SDK 跟服务器的连接断开。 |
| [onTryToReconnect](https://cloud.tencent.com/document/product/647/36779#ontrytoreconnect) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](https://cloud.tencent.com/document/product/647/36779#onconnectionrecovery) | SDK 跟服务器的连接恢复。 |
| [onSpeedTest](https://cloud.tencent.com/document/product/647/36779#onspeedtest) | 服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://cloud.tencent.com/document/product/647/36779#oncameradidready) | 摄像头准备就绪。 |
| [onMicDidReady](https://cloud.tencent.com/document/product/647/36779#onmicdidready) | 麦克风准备就绪。 |
| [onUserVoiceVolume](https://cloud.tencent.com/document/product/647/36779#onuservoicevolume) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |
| [onDeviceChange](https://cloud.tencent.com/document/product/647/36779#ondevicechange) | 本地设备通断回调。 |
| [onTestMicVolume](https://cloud.tencent.com/document/product/647/36779#ontestmicvolume) | 麦克风测试音量回调。 |
| [onTestSpeakerVolume](https://cloud.tencent.com/document/product/647/36779#ontestspeakervolume) | 扬声器测试音量回调。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](https://cloud.tencent.com/document/product/647/36779#onrecvcustomcmdmsg) | 收到自定义消息回调。 |
| [onMissCustomCmdMsg](https://cloud.tencent.com/document/product/647/36779#onmisscustomcmdmsg) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](https://cloud.tencent.com/document/product/647/36779#onrecvseimsg) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishCDNStream](https://cloud.tencent.com/document/product/647/36779#onstartpublishcdnstream) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](https://cloud.tencent.com/document/product/647/36779#onstoppublishcdnstream) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](https://cloud.tencent.com/document/product/647/36779#onsetmixtranscodingconfig) | 设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。 |


### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureCovered](https://cloud.tencent.com/document/product/647/36779#onscreencapturecovered) | 当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。 |
| [onScreenCaptureStarted](https://cloud.tencent.com/document/product/647/36779#onscreencapturestarted) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](https://cloud.tencent.com/document/product/647/36779#onscreencapturepaused) | 当屏幕分享暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](https://cloud.tencent.com/document/product/647/36779#onscreencaptureresumed) | 当屏幕分享恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStoped](https://cloud.tencent.com/document/product/647/36779#onscreencapturestoped) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 背景混音事件回调

| API | 描述 |
|-----|-----|
| [onPlayBGMBegin](https://cloud.tencent.com/document/product/647/36779#onplaybgmbegin) | 开始播放背景音乐。 |
| [onPlayBGMProgress](https://cloud.tencent.com/document/product/647/36779#onplaybgmprogress) | 播放背景音乐的进度。 |
| [onPlayBGMComplete](https://cloud.tencent.com/document/product/647/36779#onplaybgmcomplete) | 播放背景音乐结束。 |


### 自定义视频渲染回调
该回调接口通过 [ITRTCVideoRenderCallback](https://cloud.tencent.com/document/product/647/36779#itrtcvideorendercallback) 类定义。

| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](https://cloud.tencent.com/document/product/647/36779#onrendervideoframe) | 自定义视频渲染回调。 |


### 音频数据回调
该回调接口通过 [ITRTCAudioFrameCallback](https://cloud.tencent.com/document/product/647/36779#itrtcaudioframecallback) 类定义。

| API | 描述 |
|-----|-----|
| [onCapturedAudioFrame](https://cloud.tencent.com/document/product/647/36779#oncapturedaudioframe) | 本地麦克风采集到的音频数据回调。 |
| [onPlayAudioFrame](https://cloud.tencent.com/document/product/647/36779#onplayaudioframe) | 混音前的每一路远程用户的音频数据（例如您需要对某一路的语音进行文字转换，必须要使用这里的原始数据，而不是混音之后的数据）。 |
| [onMixedPlayAudioFrame](https://cloud.tencent.com/document/product/647/36779#onmixedplayaudioframe) | 各路音频数据混合后送入喇叭播放的音频数据。 |


### 日志相关回调
该回调接口通过 [ITRTCLogCallback](https://cloud.tencent.com/document/product/647/36779#itrtclogcallback) 类定义。

| API | 描述 |
|-----|-----|
| [onLog](https://cloud.tencent.com/document/product/647/36779#onlog) | 有日志打印时的回调。 |


## 关键类型定义

| 类名 | 描述 |
|-----|-----|
| [TRTCParams](https://cloud.tencent.com/document/product/647/36780#trtcparams) | 进房相关参数。 |
| [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/36780#trtcvideoencparam) | 视频编码参数。 |
| [TRTCNetworkQosParam](https://cloud.tencent.com/document/product/647/36780#trtcnetworkqosparam) | 网络流控相关参数。 |
| [TRTCQualityInfo](https://cloud.tencent.com/document/product/647/36780#trtcqualityinfo) | 视频质量。 |
| [TRTCVolumeInfo](https://cloud.tencent.com/document/product/647/36780#trtcvolumeinfo) | 音量大小。 |
| [TRTCSpeedTestResult](https://cloud.tencent.com/document/product/647/36780#trtcspeedtestresult) | 网络测速结果。 |
| [TRTCMixUser](https://cloud.tencent.com/document/product/647/36780#trtcmixuser) | 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/36780#trtctranscodingconfig) | 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](https://cloud.tencent.com/document/product/647/36780#trtcpublishcdnparam) | CDN 旁路推流参数。 |
| [TRTCAudioRecordingParams](https://cloud.tencent.com/document/product/647/36780#trtcaudiorecordingparams) | 录音参数。 |
| [TRTCLocalStatistics](https://cloud.tencent.com/document/product/647/36780#trtclocalstatistics) | 自己本地的音视频统计信息。 |
| [TRTCRemoteStatistics](https://cloud.tencent.com/document/product/647/36780#trtcremotestatistics) | 远端成员的音视频统计信息。 |
| [TRTCStatistics](https://cloud.tencent.com/document/product/647/36780#trtcstatistics) | 统计数据。 |

### 枚举值

| 枚举 | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://cloud.tencent.com/document/product/647/36780#trtcvideoresolution) | 视频分辨率。 |
| [TRTCVideoResolutionMode](https://cloud.tencent.com/document/product/647/36780#trtcvideoresolutionmode) | 视频分辨率模式。 |
| [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/36780#trtcvideostreamtype) | 视频流类型。 |
| [TRTCQuality](https://cloud.tencent.com/document/product/647/36780#trtcquality) | 画质级别。 |
| [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/36780#trtcvideofillmode) | 视频画面填充模式。 |
| [TRTCBeautyStyle](https://cloud.tencent.com/document/product/647/36780#trtcbeautystyle) | 美颜（磨皮）算法。 |
| [TRTCAppScene](https://cloud.tencent.com/document/product/647/36780#trtcappscene) | 应用场景。 |
| [TRTCRoleType](https://cloud.tencent.com/document/product/647/36780#trtcroletype) | 角色，仅适用于直播场景（TRTCAppSceneLIVE）。 |
| [TRTCQosControlMode](https://cloud.tencent.com/document/product/647/36780#trtcqoscontrolmode) | 流控模式。 |
| [TRTCVideoQosPreference](https://cloud.tencent.com/document/product/647/36780#trtcvideoqospreference) | 画质偏好。 |
| [TRTCLogLevel](https://cloud.tencent.com/document/product/647/36780#trtcloglevel) | Log 级别。 |
| [TRTCDeviceState](https://cloud.tencent.com/document/product/647/36780#trtcdevicestate) | 设备操作。 |
| [TRTCDeviceType](https://cloud.tencent.com/document/product/647/36780#trtcdevicetype) | 设备类型。 |
| [TRTCWaterMarkSrcType](https://cloud.tencent.com/document/product/647/36780#trtcwatermarksrctype) | 水印图片的源类型。 |
| [TRTCTranscodingConfigMode](https://cloud.tencent.com/document/product/647/36780#trtctranscodingconfigmode) | 混流参数配置模式。 |



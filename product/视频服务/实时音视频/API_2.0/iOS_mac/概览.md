<div id="trtc-doc">


# TRTCCloud

## 房间相关接口函数


| API | 描述 |
|-----|-----|
| enterRoom | 进入房间  |
| exitRoom | 离开房间  |



## 视频相关接口函数


| API | 描述 |
|-----|-----|
| startLocalPreview | 开启本地视频的预览画面 (iOS版本)  |
| startLocalPreview | 开启本地视频的预览画面 (Mac版本)  |
| stopLocalPreview | 停止本地视频采集及预览  |
| startRemoteView | 启动渲染远端视频画面  |
| stopRemoteView | 停止渲染远端视频画面  |
| stopAllRemoteView | 停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭  |
| setLocalVideoQuality | 设置本地的视频编码质量  |
| muteLocalVideo | 是否屏蔽本地视频 |
| setLocalViewFillMode | 设置本地图像的渲染模式 |
| setRemoteViewFillMode | 设置远端图像的渲染模式 |
| setLocalViewRotation | 设置本地图像的顺时针旋转角度  |
| setRemoteViewRotation | 设置远端图像的顺时针旋转角度  |
| setVideoOutputRotation | 设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向  |
| setGSensorMode | 设置重力感应的适应模式  |
| enableEncSmallVideoStream | 开启大小画面双路编码模式 |
| setRemoteVideoStreamType | 选定观看指定 uid 的大画面还是小画面 |
| setPriorRemoteVideoStreamType | 设定观看方优先选择的视频质量 |



## 音频相关接口函数


| API | 描述 |
|-----|-----|
| muteLocalAudio | 是否屏蔽本地音频 |
| setAudioRoute | 设置音频路由  |
| muteRemoteAudio | 设置指定用户是否静音  |
| muteAllRemoteAudio | 设置所有远端用户是否静音  |
| setRemoteAudioVolume | 设置指定用户音量  |
| enableAudioVolumeEvaluation | 启用音量大小提示 |



## 摄像头相关接口函数


| API | 描述 |
|-----|-----|
| switchCamera | 切换摄像头  |
| isCameraZoomSupported | 查询当前摄像头是否支持缩放  |
| setZoom | 设置摄像头缩放因子（焦距）  |
| isCameraTorchSupported | 查询是否支持手电筒模式  |
| enbaleTorch | 开关闪光灯  |
| isCameraFocusPositionInPreviewSupported | 查询是否支持设置焦点  |
| setFocusPosition | 设置摄像头焦点  |
| isCameraAutoFocusFaceModeSupported | 查询是否支持自动识别人脸位置  |
| enableAutoFaceFoucs | 自动识别人脸位置  |
| getCameraDevicesList | 获取摄像头设备列表  |
| getCurrentCameraDevice | 获取当前要使用的摄像头  |
| setCurrentCameraDevice | 设置要使用的摄像头  |



## 音频设备相关接口函数


| API | 描述 |
|-----|-----|
| getMicDevicesList | 获取麦克风设备列表  |
| getCurrentMicDevice | 获取当前的麦克风设备  |
| setCurrentMicDevice | 设置要使用的麦克风  |
| getCurrentMicDeviceVolume | 获取当前麦克风设备音量  |
| setCurrentMicDeviceVolume | 设置麦克风设备的音量  |
| getSpeakerDevicesList | 获取扬声器设备列表  |
| getCurrentSpeakerDevice | 获取当前的扬声器设备  |
| setCurrentSpeakerDevice | 设置要使用的扬声器  |
| getCurrentSpeakerDeviceVolume | 当前扬声器设备音量  |
| setCurrentSpeakerDeviceVolume | 设置当前扬声器音量  |



## 美颜滤镜相关接口函数


| API | 描述 |
|-----|-----|
| setBeautyStyle | 设置美颜、美白、红润效果级别  |
| setFilter | 设置指定素材滤镜特效  |
| addWatermark | 添加水印  |



## 屏幕共享接口函数(MAC)


| API | 描述 |
|-----|-----|
| startScreenCaptureWithDisplayID | 开始全屏采集  |
| startScreenCaptureWithWindowID | 开始窗口采集  |
| stopScreenCapture | 停止屏幕采集 |
| resetScreenCaptureRect | 更新采集区域 |



## 自定义音视频数据


| API | 描述 |
|-----|-----|
| enableCustomVideoCapture | 启用视频自定义采集模式  |
| sendVideoSampleBuffer | 发送自定义的SampleBuffer |
| enableCustomAudioCapture | 启用音频自定义采集模式  |
| sendCustomPCMData | 发送客户自定义的音频PCM数据 |



## 自定义消息发送


| API | 描述 |
|-----|-----|
| sendCustomCmdMsg | 发送自定义消息给房间内所有用户 |



## 背景混音相关接口函数


| API | 描述 |
|-----|-----|
| playBGM | 播放背景音乐  |
| stopBGM | 停止播放背景音乐  |
| pauseBGM | 暂停播放背景音乐  |
| resumeBGM | 继续播放背景音乐  |
| getBGMDuration | 获取音乐文件总时长，单位毫秒  |
| setBGMPosition | 设置BGM播放进度  |
| setMicVolumeOnMixing | 设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小  |
| setReverbType | 设置混响效果 (目前仅iOS)  |
| setVoiceChangerType | 设置变声类型 (目前仅iOS)  |



## 设备和网络测试


| API | 描述 |
|-----|-----|
| startSpeedTest | 开始进行网络测速(视屏通话期间请勿测试，以免影响通话质量) |
| stopSpeedTest | 停止服务器测速  |
| startCameraDeviceTestInView | 开始进行摄像头测试  |
| stopCameraDeviceTest | 结束视频测试预览  |
| startMicDeviceTest | 开始进行麦克风测试 该方法测试麦克风是否能正常工作, volume的取值范围为 0~100  |
| stopMicDeviceTest | 停止麦克风测试  |
| startSpeakerDeviceTest | 开始扬声器测试 该方法播放指定的音频文件测试播放设备是否能正常工作。如果能听到声音，说明播放设备能正常工作。  |
| stopSpeakerDeviceTest | 停止扬声器测试  |



## LOG相关接口函数


| API | 描述 |
|-----|-----|
| showDebugView | 显示仪表盘 |
| setDebugViewMargin | 设置仪表盘的边距 |
| getSDKVersion | 获取SDK版本信息  |
| setLogLevel | 设置log输出级别  |
| setConsoleEnabled | 启用或禁用控制台日志打印  |
| setLogCompressEnabled | 启用或禁用Log的本地压缩。 |
| setLogDirPath | 修改日志保存路径 |
| setLogDelegate | 设置日志回调  |




| 属性 | 类型 | 描述 |
|-----|-----|-----|
| delegate | id< TRTCCloudDelegate > | 设置回调接口 TRTCCloudDelegate，用户获得来自  |
| delegateQueue | dispatch_queue_t | 设置驱动回调的队列，默认会采用 Main Queue。 也就是说，如果您不指定 delegateQueue，那么直接在 TRTCCloudDelegate 的回调函数中操作 UI 界面将是安全的  |



## TRTCParams


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| sdkAppId | UInt32 | 应用标识 [必填] 腾讯视频云基于 sdkAppId 完成计费统计  |
| userId | NSString *_Nonnull | 用户标识 [必填] 当前用户的 userid，相当于用户名  |
| userSig | NSString *_Nonnull | 用户签名 [必填] 当前 userId 对应的验证签名，相当于登录密码  |
| roomId | UInt32 | 房间号码 [必填] 指定房间号，在同一个房间里的用户（userId）可以彼此看到对方并进行视频通话  |
| privateMapKey | NSString *_Nonnull | 房间签名 [非必选] 如果您希望某个房间（roomId）只让特定的某些用户（userId）才能进入，就需要使用 privateMapKey 进行权限保护  |
| bussInfo | NSString *_Nonnull | 业务数据 [非必选] 某些非常用的高级特性才需要用到此字段  |



## TRTCVideoEncParam


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| videoResolution | TRTCVideoResolution | 视频分辨率 |
| resMode | TRTCVideoResolutionMode | 分辨率模式（横屏分辨率 - 竖屏分辨率） |
| codecMode | TRTCVideoCodecMode | 编码器的编码模式（流畅 - 兼容） |
| videoFps | int | 视频采集帧率，推荐设置为 15fps 或 20fps，10fps以下会有明显的卡顿感，20fps以上则没有必要 |
| videoBitrate | int | 视频上行码率 |



## TRTCVolumeInfo


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | NSString * | 说话者的userId, nil为自己  |
| volume | NSUInteger | 说话者的音量, 取值范围 0~100  |



## TRTCQualityInfo


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | NSString * | 用户ID  |
| quality | TRTCQuality | 视频质量  |



## TRTCMediaDeviceInfo


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| type | TRTCMediaDeviceType | 设备类型  |
| deviceId | NSString * | 设备ID  |
| deviceName | NSString * | 设备名称  |



## TRTCSpeedTestResult


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| ip | NSString * | 服务器ip地址  |
| quality | TRTCQuality | 网络质量  |
| upLostRate | float | 上行丢包率，范围是[0,1.0]  |
| downLostRate | float | 下行丢包率，范围是[0,1.0]  |
| rtt | uint32_t | 延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好  |



# TRTCCloudDelegate

TRTCCloudDelegate 是 TRTCCloud


| API | 描述 |
|-----|-----|
| onError | 错误回调: SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示  |
| onWarning | 警告回调  |
| onEnterRoom | 加入房间  |
| onExitRoom | 离开房间 离开房间成功的回调  |
| onUserEnter | 成员进入房间事件  |
| onUserExit | 成员离开房间事件  |
| onUserVideoAvailable | 成员屏蔽自己的画面  |
| onUserAudioAvailable | 成员屏蔽自己的声音  |
| onUserVoiceVolume | 成员语音音量回调 通过调用 TRTCCloud |
| onNetworkQuality | 网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid == nil 代表自己当前的视频质量  |
| onStatistics | 技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调  |
| onFirstVideoFrame | 首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面  |
| onFirstAudioFrame | 首帧音频数据到达  |
| onConnectionLost | SDK 跟服务器的连接断开  |
| onTryToReconnect | SDK 尝试重新连接到服务器  |
| onConnectionRecovery | SDK 跟服务器的连接恢复  |
| onCameraDidReady | SDK 跟服务器的连接断开 （暂无） 7.1 摄像头准备就绪  |
| onAudioRouteChanged | 音频路由发生变化(仅iOS)，音频路由即声音由哪里输出（扬声器、听筒）  |
| onDevice | 本地设备通断回调，  |
| onRecvCustomCmdMsg | 收到对端用户发来的消息  |
| onRecvCustomCmdMsgError | 接收对方数据流消息错误的回调，只有发送端设置了可靠传输，该接口才起作用  |



# TRTCLogDelegate

日志事件回调对象

建议在一个比较早初始化的类中设置回调委托对象，如AppDelegate 


| API | 描述 |
|-----|-----|
| onLog | 有日志打印时的回调  |



## TRTCLocalStatistics


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| width | uint32_t | 视频宽度  |
| height | uint32_t | 视频高度  |
| frameRate | uint32_t | 帧率（fps）  |
| videoBitrate | uint32_t | 视频发送码率（Kbps）  |
| audioSampleRate | uint32_t | 音频采样率（Hz）  |
| audioBitrate | uint32_t | 音频发送码率（Kbps）  |
| streamType | TRTCVideoStreamType | 流类型（大画面 &#124; 小画面 &#124; 辅路画面）  |



## TRTCRemoteStatistics


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | NSString * | 用户ID，指定是哪个用户的视频流  |
| finalLoss | uint32_t | 该线路的总丢包率(%) |
| width | uint32_t | 视频宽度  |
| height | uint32_t | 视频高度  |
| frameRate | uint32_t | 接收帧率（fps）  |
| videoBitrate | uint32_t | 视频码率（Kbps）  |
| audioSampleRate | uint32_t | 音频采样率（Hz）  |
| audioBitrate | uint32_t | 音频码率（Kbps）  |
| streamType | TRTCVideoStreamType | 流类型（大画面 &#124; 小画面 &#124; 辅路画面）  |



## TRTCStatistics


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| upLoss | uint32_t | C -> S 上行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着 SDK 向服务器发送的每 10 个数据包中就会有 3 个会在上行传输中丢失  |
| downLoss | uint32_t | S -> C 下行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着服务器向 SDK 发送的每 10 个数据包中就会有 3 个会在下行传输中丢失  |
| appCpu | uint32_t | 当前 App 的 CPU 使用率 (%)  |
| systemCpu | uint32_t | 当前系统的 CPU 使用率 (%)  |
| rtt | uint32_t | 延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好 一般低于 50ms 的 rtt 是比较理想的情况，而高于 100ms 的 rtt 会引入较大的通话延时 由于数据上下行共享一条网络连接，所以 local 和 remote 的 rtt 相同  |
| receivedBytes | uint64_t | 总接收字节数(包含信令及音视频)  |
| sentBytes | uint64_t | 总发送字节数(包含信令及音视频)  |
| localStatistics | NSArray< TRTCLocalStatistics * > * | 自己本地的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组  |
| remoteStatistics | NSArray< TRTCRemoteStatistics * > * | 远端成员的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组  |



</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

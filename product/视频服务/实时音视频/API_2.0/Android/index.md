<div id="trtc-doc">


# TRTCCloud

## 基础方法


| API | 描述 |
|-----|-----|
| create | 创建TRTCEngine实例(同一时间只会存在一个实例)  |
| destroy | 销毁TRTCEngine实例  |
| setDelegate | 设置回调接口 TRTCCloudDelegate，用户获得来自 TRTCCloud |
| setDelegateHandler | 设置驱动回调的线程，默认会采用 Main Thread。 也就是说，如果您不指定 delegateHandler，那么直接在 TRTCCloudDelegate |



## 房间相关接口函数


| API | 描述 |
|-----|-----|
| enterRoom | 进入房间  |
| exitRoom | 离开房间  |



## 视频相关接口函数


| API | 描述 |
|-----|-----|
| startLocalPreview | 开启本地视频的预览画面  |
| stopLocalPreview | 停止本地视频采集及预览  |
| startRemoteView | 启动渲染远端视频画面  |
| stopRemoteView | 停止渲染远端视频画面  |
| stopAllRemoteView | 停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭  |
| setLocalVideoQuality | 设置本地的视频编码质量  |
| muteLocalVideo | 是否屏蔽本地视频 当屏蔽本地视频后，房间里的其它成员会收到 onUserVideoAvailable 回调通知  |
| setLocalViewFillMode | 设置本地图像的渲染模式  |
| setRemoteViewFillMode | 设置远端图像的渲染模式  |
| setLocalViewRotation | 设置本地图像的顺时针旋转角度  |
| setRemoteViewRotation | 设置远端图像的顺时针旋转角度  |
| setVideoOutputRotation | 设置视频编码出的（供录制和远程观看的）画面方向  |
| setGSensorMode | 设置重力感应的适应模式  |
| enableEncSmallVideoStream | 开启大小画面双路编码模式 如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面  |
| setRemoteVideoStreamType | 选定观看指定 uid 的大画面还是小画面 |
| setPriorRemoteVideoStreamType | 设定观看方优先选择的视频质量 |



## 音频相关接口函数


| API | 描述 |
|-----|-----|
| muteLocalAudio | 是否屏蔽本地音频 当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知  |
| setAudioRoute | 设置音频路由  |
| muteRemoteAudio | 设置指定用户是否静音  |
| muteAllRemoteAudio | 设置所有远端用户是否静音  |
| setRemoteAudioVolume | 设置指定用户音量  |
| enableAudioVolumeEvaluation | 启用音量大小提示 开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估  |



## 摄像头相关操作


| API | 描述 |
|-----|-----|
| switchCamera | 切换摄像头  |
| isCameraZoomSupported | 查询当前摄像头是否支持缩放  |
| setZoom | 设置摄像头缩放因子（焦距）  |
| isCameraTorchSupported | 查询是否支持手电筒模式  |
| enableTorch | 开关闪光灯  |
| isCameraFocusPositionInPreviewSupported | 查询是否支持设置焦点  |
| setFocusPosition | 设置摄像头焦点  |
| isCameraAutoFocusFaceModeSupported | 查询是否支持自动识别人脸位置  |
| enableAutoFaceFocus | 自动识别人脸位置  |



## 美颜滤镜相关接口函数


| API | 描述 |
|-----|-----|
| setBeautyStyle | 设置美颜、美白、红润效果级别  |
| setFilter | 设置指定素材滤镜特效  |
| addWatermark | 添加水印，height不用设置，sdk内部会根据水印宽高比自动计算height  |



## 自定义音视频数据


| API | 描述 |
|-----|-----|
| enableCustomVideoCapture | 启用视频自定义采集模式  |
| sendCustomVideoData | 发送自定义的视频数据  |
| enableCustomAudioCapture | 启用音频自定义采集模式  |
| sendCustomPCMData | 发送客户自定义的音频PCM数据 说明：目前SDK只支持16位采样的PCM编码；如果是单声道，请保证传入的PCM长度为2048；如果是双声道，请保证传入的PCM长度为4096  |



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
| setBGMPosition | 设置背景音乐播放进度  |
| setMicVolumeOnMixing | 设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小  |
| setReverbType | 设置混响效果  |
| setVoiceChangerType | 设置变声类型  |



## 网络测试


| API | 描述 |
|-----|-----|
| startSpeedTest | 开始进行网络测速(视屏通话期间请勿测试，以免影响通话质量) |
| stopSpeedTest | 停止服务器测速  |



## LOG相关接口函数


| API | 描述 |
|-----|-----|
| mTXLogListener |  |
| getSDKVersion | 获取SDK版本信息  |
| setLogLevel | 设置log输出级别  |
| setConsoleEnabled | 启用或禁用控制台日志打印  |
| setLogCompressEnabled | 启用或禁用Log的本地压缩。 开启压缩后，log存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读 禁用压缩后，log采用明文存储，可以直接用记事本打开阅读，但占用空间较大。  |
| setLogDirPath | 修改日志保存路径, 默认保存在 /sdcard//log/tencent/liteav 下，如需修改, 必须在所有方法前调用，并且保证目录存在及应用有目录的读写权限  |
| setLogDelegate | 设置日志回调  |
| showDebugView | 显示仪表盘（状态统计和事件消息浮层view），方便调试  |
| setDebugViewMargin | 设置仪表盘的边距，必须在 showDebugView 调用前设置才会生效  |



## 播放背景音乐的回调接口 

播放背景音乐的回调接口 


| API | 描述 |
|-----|-----|
| onBGMStart | 音乐播放开始的回调通知  |
| onBGMProgress | 音乐播放进度的回调通知 |
| onBGMComplete | 音乐播放结束的回调通知 |



## 视图边距 

视图边距 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| leftMargin | float | 距离左边的百分比，取值范围为0-1  |
| topMargin | float | 距离左边的百分比，取值范围为0-1  |
| rightMargin | float | 距离左边的百分比，取值范围为0-1  |
| bottomMargin | float | 距离左边的百分比，取值范围为0-1  |




| API | 描述 |
|-----|-----|
| TRTCViewMargin |  |



## TRTCCloudDef

## TRTCVideoFrame

视频帧数据 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| videoFormat | int | 视频帧的格式  |
| textureId | int | 视频纹理  |
| data | byte [] | 视频数据  |
| width | int | 画面的宽度  |
| height | int | 画面的高度  |
| timestamp | long | 时间戳  |
| rotation | int | 画面旋转角度  |



## TRTCAudioFrame

音频帧数据 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| audioFormat | int | 音频帧的格式  |
| data | byte [] | 音频数据  |
| sampleRate | int | 采样率  |
| channel | int | 声道数  |
| timestamp | long | 时间戳  |



## TRTCQuality

网络质量 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | String | 用户id  |
| quality | int | 网络质量  |



## TRTCParams

进房参数 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| sdkAppId | int | 应用标识 [必填] 腾讯视频云基于 sdkAppId 完成计费统计  |
| userId | String | 用户标识 [必填] 当前用户的 userid，相当于用户名  |
| userSig | String | 用户签名 [必填] 当前 userId 对应的验证签名，相当于登录密码  |
| roomId | int | 房间号码 [必填] 指定房间号，在同一个房间里的用户（userId）可以彼此看到对方并进行视频通话  |
| privateMapKey | String | 房间签名 [非必选] 如果您希望某个房间（roomId）只让特定的某些用户（userId）才能进入，就需要使用 privateMapKey 进行权限保护  |
| businessInfo | String | 业务数据 [非必选] 某些非常用的高级特性才需要用到此字段  |




| API | 描述 |
|-----|-----|
| TRTCParams |  |



## TRTCVideoEncParam

编码参数 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| videoResolution | int | 视频分辨率 |
| videoResolutionMode | int | 分辨率模式（横屏分辨率 - 竖屏分辨率） |
| codecMode | int | 编码器的编码模式（流畅 - 兼容） |
| videoFps | int | 视频采集帧率，推荐设置为 15fps 或 20fps，10fps以下会有明显的卡顿感，20fps以上则没有必要 |
| videoBitrate | int | 视频上行码率 |



## TRTCVolumeInfo

音量大小 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | String | 说话者的userId, 空则为自己  |
| volume | int | 说话者的音量, 取值范围 0~100  |



## TRTCSpeedTestResult

网络测速结果 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| ip | String | 服务器ip地址  |
| quality | int | 网络质量  |
| upLostRate | float | 上行丢包率，范围是[0,1.0]  |
| downLostRate | float | 下行丢包率，范围是[0,1.0]  |
| rtt | int | 延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好  |



# TRTCCloudDelegate

TRTCCloudDelegateTRTCCloud


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
| onNetworkQuality | 网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid 为"" 代表自己当前的视频质量  |
| onStatistics | 技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调  |
| onFirstVideoFrame | 首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面  |
| onFirstAudioFrame | 首帧音频数据到达  |
| onConnectionLost | SDK 跟服务器的连接断开  |
| onTryToReconnect | SDK 尝试重新连接到服务器  |
| onConnectionRecovery | SDK 跟服务器的连接恢复  |
| onSpeedTest | SDK 跟服务器的连接断开 （暂无） ：6.5 服务器测速的回调，SDK 对多个服务器IP做测速，每个IP的测速结果通过这个回调通知  |
| onCameraDidReady | 摄像头准备就绪  |
| onAudioRouteChanged | 音频路由发生变化，音频路由即声音由哪里输出（扬声器、听筒）  |
| onRecvCustomCmdMsg | 收到数据流消息  |
| onRecvCustomCmdMsgError | 接收对方数据流消息错误的回调，只有发送端设置了可靠传输，该接口才起作用  |



# TRTCLogDelegate

日志事件回调对象

建议在一个比较早初始化的类中设置回调对象，如Application 


| API | 描述 |
|-----|-----|
| onLog |  |



## TRTCStatistics


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| appCpu | int | 当前 App 的 CPU 使用率 (%)  |
| systemCpu | int | 当前系统的 CPU 使用率 (%)  |
| rtt | int | 延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好 一般低于 50ms 的 rtt 是比较理想的情况，而高于 100ms 的 rtt 会引入较大的通话延时 由于数据上下行共享一条网络连接，所以 local 和 remote 的 rtt 相同  |
| upLoss | int | C -> S 上行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着 SDK 向服务器发送的每 10 个数据包中就会有 3 个会在上行传输中丢失  |
| downLoss | int | S -> C 下行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着服务器向 SDK 发送的每 10 个数据包中就会有 3 个会在下行传输中丢失  |
| sendBytes | long | 发送字节总数，注意是字节数（bytes），不是比特数（bits）  |
| receiveBytes | long | 接收字节总数，注意是字节数（bytes），不是比特数（bits）  |
| localArray | ArrayList< TRTCLocalStatistics > | 自己本地的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组  |
| remoteArray | ArrayList< TRTCRemoteStatistics > | 远端成员的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组  |



## TRTCRemoteStatistics


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | String | 用户ID，指定是哪个用户的视频流  |
| finalLoss | int | 该线路的总丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 这个丢包率是该线路的 userid 从上行到服务器再到下行的总丢包率 如果 downLoss 为 0%, 但是 finalLoss 不为 0，说明该 userId 在上行就出现了无法恢复的丢包  |
| width | int | 视频宽度  |
| height | int | 视频高度  |
| frameRate | int | 接收帧率（fps）  |
| videoBitrate | int | 视频码率（Kbps）  |
| audioSampleRate | int | 音频采样率（Hz）  |
| audioBitrate | int | 音频码率（Kbps）  |
| streamType | int | 流类型（大画面 &#124; 小画面 &#124; 辅路画面）  |



## TRTCLocalStatistics


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| width | int | 视频宽度  |
| height | int | 视频高度  |
| frameRate | int | 帧率（fps）  |
| videoBitrate | int | 视频发送码率（Kbps）  |
| audioSampleRate | int | 音频采样率（Hz）  |
| audioBitrate | int | 音频发送码率（Kbps）  |
| streamType | int | 流类型（大画面 &#124; 小画面 &#124; 辅路画面）  |



</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

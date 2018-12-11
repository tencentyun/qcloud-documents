<div id="trtc-doc">


# TRTCCloud

## 房间相关接口函数


| API | 描述 |
|-----|-----|
| enterRoom | 进入房间  |
| exitRoom | 退出房间  |



## 视频相关接口函数


| API | 描述 |
|-----|-----|
| startLocalPreview | 启动本地摄像头采集和预览  |
| stopLocalPreview | 关闭本地摄像头采集和预览  |
| startRemoteView | 开始渲染远端用户画面  |
| stopRemoteView | 停止渲染远端用户画面  |
| stopAllRemoteView | 停止渲染所有远端用户画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭  |
| setLocalVideoQuality | 设置画面质量参数  |
| muteLocalVideo | 是否屏蔽本地视频  |
| setLocalViewFillMode | 设置本地图像的渲染模式  |
| setRemoteViewFillMode | 设置远端图像的渲染模式  |
| setLocalViewRotation | 设置本地图像的顺时针旋转角度  |
| setRemoteViewRotation | 设置远端图像的顺时针旋转角度  |
| setVideoOutputRotation | 设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向  |
| enableSmallVideoStream | 开启大小画面双路编码模式  |
| setRemoteVideoStreamType | 选择某一路的画面质量：当网络不好时可以切换到低清晰度的小画面  |
| setPriorRemoteVideoStreamType | 设定观看方优先选择的视频质量  |



## 音频相关接口函数


| API | 描述 |
|-----|-----|
| muteLocalAudio | 是否屏蔽本地音频  |
| muteRemoteAudio | 屏蔽指定远端音频  |
| muteAllRemoteAudio | 远端所有用户全部静音  |
| enableAudioVolumeEvaluation | 启用或关闭音量大小提示  |



## 摄像头相关接口函数


| API | 描述 |
|-----|-----|
| getCameraDevicesList | 查询摄像头列表  |
| setCurrentCameraDevice | 设置要使用的摄像头  |
| getCurrentCameraDevice | 获取当前使用的摄像头  |



## 音频设备相关接口函数


| API | 描述 |
|-----|-----|
| getMicDevicesList | 查询麦克风列表  |
| setCurrentMicDevice | 选择指定的麦克风作为录音设备，不调用该接口时，默认选择索引为0的麦克风  |
| getCurrentMicDevice | 获取当前选择的麦克风  |
| getCurrentMicDeviceVolume | 查询已选择麦克风的音量  |
| setCurrentMicDeviceVolume | 设置已选择麦克风的音量  |
| getSpeakerDevicesList | 查询扬声器列表  |
| setCurrentSpeakerDevice | 选择指定的扬声器作为音频播放的设备，不调用该接口时，默认选择索引为0的扬声器  |
| getCurrentSpeakerDevice | 获取已选择的扬声器  |
| getCurrentSpeakerVolume | 查询已选择扬声器的音量，注意查询得到不是系统扬声器的音量大小  |
| setCurrentSpeakerVolume | 设置SDK播放的音量，注意设置的不是系统扬声器的音量大小  |



## 美颜相关接口函数


| API | 描述 |
|-----|-----|
| setBeautyStyle | 设置美颜、美白、红润  |



## 屏幕采集共享操作


| API | 描述 |
|-----|-----|
| startScreenCapture | 启动屏幕分享  |
| resetScreenCaptureRect | 更新采集区域  |
| stopScreenCapture | 关闭屏幕分享  |



## 自定义音视频数据


| API | 描述 |
|-----|-----|
| setVideoFrameProcessCallback | 设置视频数据回调  |
| setAudioFrameProcessCallback | 设置音频数据回调  |
| enableCustomVideoCapture | 启用视频自定义采集模式  |
| sendCustomVideoData | 发送客户自定义的视频数据  |
| enableCustomAudioCapture | 启用音频自定义采集模式  |
| sendCustomAudioData | 发送客户自定义的音频PCM数据  |



## 自定义消息发送


| API | 描述 |
|-----|-----|
| sendCustomCmdMsg | 发送自定义消息给房间内所有用户  |



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



## 设备和网络测试


| API | 描述 |
|-----|-----|
| startSpeedTest | 开始进行网络测速(视屏通话期间请勿测试，以免影响通话质量)  |
| stopSpeedTest | 停止服务器测速  |
| startCameraDeviceTest | 开启摄像头测速，会触发 onLocalVideoFrameAfterProcess 回调接口  |
| stopCameraDeviceTest | 停止摄像头测速  |
| startMicDeviceTest | 开启麦克风测试，回调接口 onTestMicVolume 获取视频数据  |
| stopMicDeviceTest | 关闭麦克风测试  |
| startSpeakerDeviceTest | 开启扬声器测试，回调接口 onTestSpeakerVolume 获取视频数据  |
| stopSpeakerDeviceTest | 停止扬声器测试  |



## 调试相关函数


| API | 描述 |
|-----|-----|
| getSDKVersion | 获取SDK版本信息  |
| setLogLevel | 设置log输出级别  |
| setConsoleEnabled | 启用或禁用控制台日志打印  |
| setLogCompressEnabled | 启用或禁用Log的本地压缩  |
| setLogDirPath | 设置日志保存路径  |
| setLogCallback | 设置日志回调  |
| showDebugView | 显示仪表盘（状态统计和事件消息浮层view），方便调试  |




| API | 描述 |
|-----|-----|
| TRTCCloud |  |
| ~TRTCCloud |  |
| addCallback | 添加事件回调  |
| removeCallback | 移除事件回调  |



## ITRTCCloudCallback

### 通用事件回调


| API | 描述 |
|-----|-----|
| onError | 错误回调，SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示  |
| onWarning | 警告回调  |



### 房间事件回调


| API | 描述 |
|-----|-----|
| onEnterRoom | 进房成功通知  |
| onExitRoom | 退房通知  |



### 成员事件回调


| API | 描述 |
|-----|-----|
| onUserEnter | 房间成员进房通知，在这个回调中调用 startRemoteView 接口  |
| onUserExit | 房间成员退房通知，在这个回调中调用 stopRemoteView 接口  |
| onUserVideoAvailable | 远端用户屏蔽自己的画面  |
| onUserAudioAvailable | 远端用户屏蔽自己的声音  |
| onUserVoiceVolume | 成员语音音量回调，通过调用 TRTCCloud |



### 统计和质量回调


| API | 描述 |
|-----|-----|
| onNetworkQuality | 网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量  |
| onStatistics | 技术指标统计回调，每2秒回调一次  |



### 音视频事件回调


| API | 描述 |
|-----|-----|
| onFirstVideoFrame | 首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面  |
| onFirstAudioFrame | 首帧音频数据到达  |
| onPlayBGMBegin | 开始播放背景音乐  |
| onPlayBGMProgress | 播放背景音乐的进度  |
| onPlayBGMComplete | 播放背景音乐结束  |



### 服务器事件回调


| API | 描述 |
|-----|-----|
| onConnectionLost | SDK 跟服务器的连接断开  |
| onTryToReconnect | SDK 尝试重新连接到服务器  |
| onConnectionRecovery | SDK 跟服务器的连接恢复  |
| onSpeedTest | 服务器测速的回调，SDK 对多个服务器IP做测速，每个IP的测速结果通过这个回调通知  |



### 硬件设备事件回调


| API | 描述 |
|-----|-----|
| onCameraDidReady | 摄像头准备就绪，表示摄像头打开成功，如果打开失败，在 onError 中通知  |
| onDeviceChange | 设备事件的回调  |
| onTestMicVolume | 麦克风测试音量回调，麦克风测试接口 startMicDeviceTest 会触发这个回调  |
| onTestSpeakerVolume | 扬声器测试音量回调，扬声器测试接口 startSpeakerDeviceTest 会触发这个回调  |




| API | 描述 |
|-----|-----|
| ~ITRTCCloudCallback |  |



## ITRTCVideoFrameProcessCallback

### 自定义数据通道回调


| API | 描述 |
|-----|-----|
| onLocalVideoFrameAfterProcess | 本地经过预处理后的视频数据，预处理做到事情可能有美颜、裁剪、缩放和旋转  |
| onRemoteVideoFrame | 获取远端用户的视频  |




| API | 描述 |
|-----|-----|
| ~ITRTCVideoFrameProcessCallback |  |



## ITRTCAudioFrameProcessCallback

### 自定义数据通道回调


| API | 描述 |
|-----|-----|
| onCaptureAudioFrame | 获取 SDK 本地采集的音频数据  |
| onRemoteAudioFrameBeforeMixing | 获取 SDK 混音前要播放的音频数据  |
| onRemoteAudioFrameAfterMixing | 获取 SDK 混音后要播放的音频数据，如果您需要自己播放声音，只需要返回 false 即可接管声音的播放  |




| API | 描述 |
|-----|-----|
| ~ITRTCAudioFrameProcessCallback |  |



## ITRTCLogCallback

### Log 信息回调


| API | 描述 |
|-----|-----|
| onLog | 日志回调  |




| API | 描述 |
|-----|-----|
| ~ITRTCLogCallback |  |



## TRTCVideoEncParam


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| videoResolution | TRTCVideoResolution | 视频分辨率 |
| codecMode | TRTCVideoCodecMode | 编码器的编码模式（流畅 - 兼容） |
| videoFps | uint32_t | 视频采集帧率，推荐设置为 15fps 或 20fps，10fps以下会有明显的卡顿感，20fps以上则没有必要 |
| videoBitrate | uint32_t | 视频上行码率 |




| API | 描述 |
|-----|-----|
| TRTCVideoEncParam |  |



## TRTCVolumeInfo


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | TXString | 说话者的userId  |
| volume | uint32_t | 说话者的音量, 取值范围 0~100  |




| API | 描述 |
|-----|-----|
| TRTCVolumeInfo |  |



## TRTCQualityInfo


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | TXString | 用户标识  |
| quality | TRTCQuality | 视频质量  |




| API | 描述 |
|-----|-----|
| TRTCQualityInfo |  |



## TRTCParams


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| sdkAppId | uint32_t | 应用标识 - [必填] - 腾讯视频云基于 sdkAppId 完成计费统计  |
| roomId | uint32_t | 房间号码 - [必填] - 指定房间号，在同一个房间里的用户（userId）可以彼此看到对方并进行视频通话  |
| userId | TXString | 用户标识 - [必填] - 当前用户的 userid，相当于用户名  |
| userSig | TXString | 用户签名 - [必填] - 当前 userId 对应的验证签名，相当于登录密码  |
| privateMapKey | TXString | 房间签名 - [非必选] - 如果您希望某个房间（roomId）只让特定的某些用户（userId）才能进入，就需要使用 privateMapKey 进行权限保护  |
| businessInfo | TXString | 业务数据 - [非必选] - 某些非常用的高级特性才需要用到此字段  |




| API | 描述 |
|-----|-----|
| TRTCParams |  |



## TRTCVideoFrame

视频帧数据 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| videoFormat | TRTCVideoFrameFormat | 视频帧的格式  |
| data | char * | 视频数据  |
| length | uint32_t | 视频数据的长度，单位是字节，对于i420而言， length = width * height * 3 / 2，对于BGRA32而言， length = width * height * 4  |
| width | uint32_t | 画面的宽度  |
| height | uint32_t | 画面的高度  |
| timestamp | uint64_t | 时间戳，单位ms  |
| rotation | TRTCVideoRotation | 画面旋转角度  |




| API | 描述 |
|-----|-----|
| TRTCVideoFrame |  |



## TRTCAudioFrame

视频帧数据 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| audioFormat | TRTCAudioFrameFormat | 音频帧的格式  |
| data | char * | 音频数据  |
| length | uint32_t | 音频数据的长度  |
| sampleRate | uint32_t | 采样率  |
| channel | uint32_t | 声道数  |
| timestamp | uint64_t | 时间戳，单位ms  |




| API | 描述 |
|-----|-----|
| TRTCAudioFrame |  |



## TRTCSpeedTestResult


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| ip | TXString | 服务器ip地址  |
| quality | TRTCQuality | 网络质量  |
| upLostRate | float | 上行丢包率，范围是[0,1.0]  |
| downLostRate | float | 下行丢包率，范围是[0,1.0]  |
| rtt | int | 延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，-1表示都未收到服务器的回复包，说明网络非常差  |




| API | 描述 |
|-----|-----|
| TRTCSpeedTestResult |  |



## TRTCLocalStatistics

本地用户统计数据 


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

远端用户统计数据 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| userId | TXString | 用户ID，指定是哪个用户的视频流  |
| finalLoss | uint32_t | 该线路的总丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好  |
| width | uint32_t | 视频宽度  |
| height | uint32_t | 视频高度  |
| frameRate | uint32_t | 接收帧率（fps）  |
| videoBitrate | uint32_t | 视频码率（Kbps）  |
| audioSampleRate | uint32_t | 音频采样率（Hz）  |
| audioBitrate | uint32_t | 音频码率（Kbps）  |
| streamType | TRTCVideoStreamType | 流类型（大画面 &#124; 小画面 &#124; 辅路画面）  |



## TRTCStatistics

统计数据 


| 属性 | 类型 | 描述 |
|-----|-----|-----|
| upLoss | uint32_t | 上行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好，  |
| downLoss | uint32_t | S -》 C 下行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好，  |
| appCpu | uint32_t | 当前 App 的 CPU 使用率 (%)  |
| systemCpu | uint32_t | 当前系统的 CPU 使用率 (%)  |
| rtt | uint32_t | 延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好  |
| receivedBytes | uint32_t | 总接收字节数（包含信令和音视频）  |
| sentBytes | uint32_t | 总发送字节总数（包含信令和音视频）  |
| localStatisticsArray | TRTCLocalStatistics * | 自己本地的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组  |
| localStatisticsArraySize | uint32_t | 数组localStatisticsArray的大小  |
| remoteStatisticsArray | TRTCRemoteStatistics * | 远端成员的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组  |
| remoteStatisticsArraySize | uint32_t | 数组remoteStatisticsArray的大小  |



</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

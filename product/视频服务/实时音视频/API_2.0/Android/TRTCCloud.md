## 基础方法

### create
```
TRTCCloud create(Context context, TRTCCloudDelegate delegate)
```


__功能__


创建TRTCEngine实例(同一时间只会存在一个实例)         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| context | Context | 上下文  |
| delegate | TRTCCloudDelegate | 事件回调(可通过addDelegate额外添加)  |

<br/>

### destroy
```
void destroy()
```


__功能__


销毁TRTCEngine实例         

<br/>

### setDelegate
```
abstract void setDelegate(TRTCCloudDelegate delegate)
```


__功能__


设置回调接口 TRTCCloudDelegate，用户获得来自 TRTCCloud 的各种状态通知         

<br/>

### setDelegateHandler
```
abstract void setDelegateHandler(Handler delegateHandler)
```


__功能__


设置驱动回调的线程，默认会采用 Main Thread。 也就是说，如果您不指定 delegateHandler，那么直接在 TRTCCloudDelegate 的回调函数中操作 UI 界面将是安全的         

<br/>


## 房间相关接口函数

### enterRoom
```
abstract void enterRoom(TRTCCloudDef.TRTCParams param)
```


__功能__


进入房间         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCCloudDef.TRTCParams | 进房参数，请参考 DOC-TO-DO  |

__说明__

不管进房是否成功，都必须与exitRoom配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题 

<br/>

### exitRoom
```
abstract void exitRoom()
```


__功能__


离开房间         

<br/>


## 视频相关接口函数

### startLocalPreview
```
abstract void startLocalPreview(boolean frontCamera, TXCloudVideoView view)
```


__功能__


开启本地视频的预览画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frontCamera | boolean | true:前置摄像头 false:后置摄像头  |
| view | TXCloudVideoView | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染本地摄像头的视频画面  |

<br/>

### stopLocalPreview
```
abstract void stopLocalPreview()
```


__功能__


停止本地视频采集及预览         

<br/>

### startRemoteView
```
abstract void startRemoteView(String userId, TXCloudVideoView view)
```


__功能__


启动渲染远端视频画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识  |
| view | TXCloudVideoView | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染远端画面  |

<br/>

### stopRemoteView
```
abstract void stopRemoteView(String userId)
```


__功能__


停止渲染远端视频画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识  |

<br/>

### stopAllRemoteView
```
abstract void stopAllRemoteView()
```


__功能__


停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭         

<br/>

### setLocalVideoQuality
```
abstract void setLocalVideoQuality(TRTCCloudDef.TRTCVideoEncParam param, int qosMode, int qosPreference)
```


__功能__


设置本地的视频编码质量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCCloudDef.TRTCVideoEncParam | 视频编码参数，详情请参考 TRTCCloudDef.h 中的 TRTCVideoEncParam 定义  |
| qosMode | int | 流控模式选择，默认选择【云控】模式，便于获得更好的效果，【终端】模式则用于特殊的调试场景  |
| qosPreference | int | 画面质量偏好，有【流畅】和【清晰】两种模式可供选择，详情请参考 TRTC_VIDEO_QOS_PREFERENCE 的定义  |

<br/>

### muteLocalVideo
```
abstract void muteLocalVideo(boolean mute)
```


__功能__


是否屏蔽本地视频 当屏蔽本地视频后，房间里的其它成员会收到 onUserVideoAvailable 回调通知         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | boolean | true:屏蔽 false:开启  |

<br/>

### setLocalViewFillMode
```
abstract void setLocalViewFillMode(int mode)
```


__功能__


设置本地图像的渲染模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | int | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边）  |

<br/>

### setRemoteViewFillMode
```
abstract void setRemoteViewFillMode(String userId, int mode)
```


__功能__


设置远端图像的渲染模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| mode | int | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边）  |

<br/>

### setLocalViewRotation
```
abstract void setLocalViewRotation(int rotation)
```


__功能__


设置本地图像的顺时针旋转角度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | int | 支持 90、180、270 旋转角度  |

<br/>

### setRemoteViewRotation
```
abstract void setRemoteViewRotation(String userId, int rotation)
```


__功能__


设置远端图像的顺时针旋转角度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识  |
| rotation | int | 支持 90、180、270 旋转角度  |

<br/>

### setVideoOutputRotation
```
abstract void setVideoOutputRotation(int rotation)
```


__功能__


设置视频编码出的（供录制和远程观看的）画面方向         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | int | 支持 90、180、270 旋转角度  |

<br/>

### setGSensorMode
```
abstract void setGSensorMode(int mode)
```


__功能__


设置重力感应的适应模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | int | 重力感应模式，详情请参考 TRTC_GSENSOR_MODE 的定义  |

<br/>

### enableEncSmallVideoStream
```
abstract int enableEncSmallVideoStream(boolean enable, TRTCCloudDef.TRTCVideoEncParam smallVideoEncParam)
```


__功能__


开启大小画面双路编码模式 如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | 是否开启小画面编码  |
| smallVideoEncParam | TRTCCloudDef.TRTCVideoEncParam | 小流的视频参数  |

<br/>

### setRemoteVideoStreamType
```
abstract int setRemoteVideoStreamType(String userId, int streamType)
```


__功能__


选定观看指定 uid 的大画面还是小画面

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户的uid  |
| streamType | int | 视频流类型，即选择看大画面(TRTC_VIDEO_STREAM_TYPE_BIG)还是小画面(TRTC_VIDEO_STREAM_TYPE_SMALL)  |

__介绍__

此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式 如果该 uid 没有开启双路编码模式，则此操作无效         

<br/>

### setPriorRemoteVideoStreamType
```
abstract int setPriorRemoteVideoStreamType(int streamType)
```


__功能__


设定观看方优先选择的视频质量

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| streamType | int | 默认观看大画面(TRTC_VIDEO_STREAM_TYPE_BIG)还是小画面(TRTC_VIDEO_STREAM_TYPE_SMALL)  |

__介绍__

低端设备推荐优先选择低清晰度的小画面 如果对方没有开启双路视频模式，则此操作无效         

<br/>


## 音频相关接口函数

### muteLocalAudio
```
abstract void muteLocalAudio(boolean mute)
```


__功能__


是否屏蔽本地音频 当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | boolean | true:屏蔽 false:开启  |

<br/>

### setAudioRoute
```
abstract void setAudioRoute(int route)
```


__功能__


设置音频路由         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | int | 音频路由即声音由哪里输出 如：扬声器(TRTC_AUDIO_ROUTE_SPEAKER)、听筒(TRTC_AUDIO_ROUTE_EARPIECE）  |

<br/>

### muteRemoteAudio
```
abstract void muteRemoteAudio(String userId, boolean mute)
```


__功能__


设置指定用户是否静音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识  |
| mute | boolean | true:静音 false:非静音  |

<br/>

### muteAllRemoteAudio
```
abstract void muteAllRemoteAudio(boolean mute)
```


__功能__


设置所有远端用户是否静音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | boolean | true:静音 false:非静音  |

<br/>

### setRemoteAudioVolume
```
abstract void setRemoteAudioVolume(String userId, float volume)
```


__功能__


设置指定用户音量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识  |
| volume | float | 音量  |

<br/>

### enableAudioVolumeEvaluation
```
abstract void enableAudioVolumeEvaluation(int intervalMs, int smoothLevel)
```


__功能__


启用音量大小提示 开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| intervalMs | int | 报告间隔单位为ms, 最小间隔20ms, 如果小于等于0则会关闭回调，建议设置为大于200ms  |
| smoothLevel | int | 灵敏度，[0,10], 数字越大，波动越灵敏  |

<br/>


## 摄像头相关操作

### switchCamera
```
abstract void switchCamera()
```


__功能__


切换摄像头         

<br/>

### isCameraZoomSupported
```
abstract boolean isCameraZoomSupported()
```


__功能__


查询当前摄像头是否支持缩放         

<br/>

### setZoom
```
abstract void setZoom(int distance)
```


__功能__


设置摄像头缩放因子（焦距）         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| distance | int | 取值范围 1~5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清  |

<br/>

### isCameraTorchSupported
```
abstract boolean isCameraTorchSupported()
```


__功能__


查询是否支持手电筒模式         

<br/>

### enableTorch
```
abstract boolean enableTorch(boolean enable)
```


__功能__


开关闪光灯         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | true:开启 false:关闭  |

<br/>

### isCameraFocusPositionInPreviewSupported
```
abstract boolean isCameraFocusPositionInPreviewSupported()
```


__功能__


查询是否支持设置焦点         

<br/>

### setFocusPosition
```
abstract void setFocusPosition(int x, int y)
```


__功能__


设置摄像头焦点         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| x | int | 焦点位置x坐标  |
| y | int | 焦点位置y坐标  |

<br/>

### isCameraAutoFocusFaceModeSupported
```
abstract boolean isCameraAutoFocusFaceModeSupported()
```


__功能__


查询是否支持自动识别人脸位置         

<br/>

### enableAutoFaceFocus
```
abstract void enableAutoFaceFocus(boolean enable)
```


__功能__


自动识别人脸位置         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | true:打开 false:关闭  |

<br/>


## 美颜滤镜相关接口函数

### setBeautyStyle
```
abstract void setBeautyStyle(int beautyStyle, int beautyLevel, int whitenessLevel, int ruddinessLevel)
```


__功能__


设置美颜、美白、红润效果级别         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| beautyStyle | int | 美颜风格 ,平滑(TRTCBeautyStyleSmooth)或自然(TRtcBeautyStyleNature)  |
| beautyLevel | int | 美颜级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显  |
| whitenessLevel | int | 美白级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显  |
| ruddinessLevel | int | 红润级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显  |

<br/>

### setFilter
```
abstract void setFilter(Bitmap image)
```


__功能__


设置指定素材滤镜特效         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | Bitmap | 指定素材，即颜色查找表图片。注意：一定要用png格式！！！  |

<br/>

### setWatermark
```
abstract void setWatermark(Bitmap image, float x, float y, float width)
```


__功能__


添加水印，height不用设置，sdk内部会根据水印宽高比自动计算height         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | Bitmap | 水印图片 null 表示清除水印  |
| x | float | 归一化水印位置的X轴坐标，取值[0,1]  |
| y | float | 归一化水印位置的Y轴坐标，取值[0,1]  |
| width | float | 归一化水印宽度，取值[0,1]  |

<br/>


## 自定义音视频数据

### enableCustomVideoCapture
```
abstract void enableCustomVideoCapture(boolean enable)
```


__功能__


启用视频自定义采集模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | 是否启用 true:启用 false:关闭  |

<br/>

### sendCustomVideoData
```
abstract int sendCustomVideoData(byte [] buffer, int bufferType, int w, int h)
```


__功能__


发送自定义的视频数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| buffer | byte [] | 视频数据.  |
| bufferType | int | 视频格式.  |
| w | int | 视频图像的宽度.  |
| h | int | 视频图像的高度.  |

<br/>

### enableCustomAudioCapture
```
abstract void enableCustomAudioCapture(boolean enable)
```


__功能__


启用音频自定义采集模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | 是否启用 true:启用 false:关闭  |

<br/>

### sendCustomPCMData
```
abstract void sendCustomPCMData(byte [] pcmBuffer)
```


__功能__


发送客户自定义的音频PCM数据 说明：目前SDK只支持16位采样的PCM编码；如果是单声道，请保证传入的PCM长度为2048；如果是双声道，请保证传入的PCM长度为4096         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pcmBuffer | byte [] | pcm音频数据  |

<br/>

### setLocalVideoRenderDelegate
```
abstract void setLocalVideoRenderDelegate(int pixelFormat, int bufferType, TRTCCloudDelegate.TRTCVideoRenderDelegate delegate)
```


__功能__


设置本地视频自定义渲染         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pixelFormat | int | 指定视频帧的像素格式，如 TRTC_VIDEO_PIXEL_FORMAT_I420  |
| bufferType | int | 指定视频帧的数据结构，如 TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER， TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY  |
| delegate | TRTCCloudDelegate.TRTCVideoRenderDelegate | 自定义视频渲染回调，每一帧视频数据回调一次  |

__说明__

设置此方法，SDK内部会把采集到的数据回调出来，SDK跳过渲染逻辑 

<br/>

### setRemoteVideoRenderDelegate
```
abstract void setRemoteVideoRenderDelegate(String userId, int pixelFormat, int bufferType, TRTCCloudDelegate.TRTCVideoRenderDelegate delegate)
```


__功能__


设置远端视频自定义渲染         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识  |
| pixelFormat | int | 指定视频帧的像素格式，如 TRTC_VIDEO_PIXEL_FORMAT_I420  |
| bufferType | int | 指定视频帧的数据结构，如 TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER， TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY  |
| delegate | TRTCCloudDelegate.TRTCVideoRenderDelegate | 自定义视频渲染回调，每一帧视频数据回调一次  |

__说明__

设置此方法，SDK内部会把远端的数据解码后回调出来，SDK跳过渲染逻辑 

<br/>


## 自定义消息发送

### sendCustomCmdMsg
```
abstract boolean sendCustomCmdMsg(int cmdID, byte [] data, boolean reliable, boolean ordered)
```


__功能__


发送自定义消息给房间内所有用户

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdID | int | 消息ID，取值范围为 1 ~ 10  |
| data | byte [] | 待发送的消息，最大支持 1KB（1000字节）的数据大小  |
| reliable | boolean | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传  |
| ordered | boolean | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息  |

__说明__

限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息 限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃 限制3：每个客户端每秒最多能发送总计 8 KB 数据

<br/>


## 背景混音相关接口函数

### playBGM
```
abstract void playBGM(String path, BGMNotify notify)
```


__功能__


播放背景音乐         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | String | 音乐文件路径  |
| notify | BGMNotify | 播放背景音乐的回调  |

<br/>

### stopBGM
```
abstract void stopBGM()
```


__功能__


停止播放背景音乐         

<br/>

### pauseBGM
```
abstract void pauseBGM()
```


__功能__


暂停播放背景音乐         

<br/>

### resumeBGM
```
abstract void resumeBGM()
```


__功能__


继续播放背景音乐         

<br/>

### getBGMDuration
```
abstract int getBGMDuration(String path)
```


__功能__


获取音乐文件总时长，单位毫秒         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | String | 音乐文件路径，如果path为空，那么返回当前正在播放的music时长  |

<br/>

### setBGMPosition
```
abstract int setBGMPosition(int pos)
```


__功能__


设置背景音乐播放进度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | int | 单位毫秒  |

<br/>

### setMicVolumeOnMixing
```
abstract void setMicVolumeOnMixing(float volume)
```


__功能__


设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | float | 音量大小，1为正常音量，建议值为0~2  |

<br/>

### setReverbType
```
abstract void setReverbType(int reverbType)
```


__功能__


设置混响效果         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reverbType | int | ：混响类型 ，详见 TRTC_REVERB_TYPE  |

<br/>

### setVoiceChangerType
```
abstract boolean setVoiceChangerType(int voiceChangerType)
```


__功能__


设置变声类型         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| voiceChangerType | int | 变声类型, 详见 TRTC_VOICE_CHANGER_TYPE  |

<br/>


## 网络测试

### startSpeedTest
```
abstract void startSpeedTest(int sdkAppId, String userId, String userSig)
```


__功能__


开始进行网络测速(视频通话期间请勿测试，以免影响通话质量)

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sdkAppId | int | 应用标识  |
| userId | String | 用户标识  |
| userSig | String | 用户签名  |

__介绍__

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们最佳的服务器 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络
注意：测速本身会消耗一定的流量，所以也会产生少量额外的流量费用 测试结果通过TRTCCloudDelegate.onSpeedTest回调出来         

<br/>

### stopSpeedTest
```
abstract void stopSpeedTest()
```


__功能__


停止服务器测速         

<br/>


## LOG相关接口函数

### mTXLogListener
```
None
```

<br/>

### getSDKVersion
```
String getSDKVersion()
```


__功能__


获取SDK版本信息         

<br/>

### setLogLevel
```
void setLogLevel(int level)
```


__功能__


设置log输出级别         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | int | 参见 TRTC_LOG_LEVEL  |

<br/>

### setConsoleEnabled
```
void setConsoleEnabled(boolean enabled)
```


__功能__


启用或禁用控制台日志打印         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | boolean | 指定是否启用 true : 启用，false : 不启用  |

<br/>

### setLogCompressEnabled
```
void setLogCompressEnabled(boolean enabled)
```


__功能__


启用或禁用Log的本地压缩。 开启压缩后，log存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读 禁用压缩后，log采用明文存储，可以直接用记事本打开阅读，但占用空间较大。。

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | boolean | 指定是否启用 true : 启用，false : 不启用  |

<br/>

### setLogDirPath
```
void setLogDirPath(String path)
```


__功能__


修改日志保存路径, 默认保存在 /sdcard//log/tencent/liteav 下，如需修改, 必须在所有方法前调用，并且保证目录存在及应用有目录的读写权限         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | String | 存储日志路径  |

<br/>

### setLogDelegate
```
void setLogDelegate(final TRTCCloudDelegate.TRTCLogDelegate logDelegate)
```


__功能__


设置日志回调         

<br/>

### showDebugView
```
abstract void showDebugView(int showType)
```


__功能__


显示仪表盘（状态统计和事件消息浮层view），方便调试         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | int | 0:不显示 1:显示精简版 2:显示全量版  |

<br/>

### setDebugViewMargin
```
abstract void setDebugViewMargin(String userId, TRTCViewMargin margin)
```


__功能__


设置仪表盘的边距，必须在 showDebugView 调用前设置才会生效         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| margin | TRTCViewMargin | 仪表盘内边距，注意这里是基于parentView的百分比，margin的取值范围是0 |

<br/>



### 播放背景音乐的回调接口     

`TRTCCloud.BGMNotify`
### onBGMStart
```
void onBGMStart()
```


__功能__


音乐播放开始的回调通知         

<br/>

### onBGMProgress
```
void onBGMProgress(long progress, long duration)
```


__功能__


音乐播放进度的回调通知

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| progress | long | 当前BGM已播放时间(ms)  |
| duration | long | 当前BGM总时间(ms)  |

<br/>

### onBGMComplete
```
void onBGMComplete(int err)
```


__功能__


音乐播放结束的回调通知

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| err | int | 0：正常结束 -1：出错结束  |

<br/>


### 视图边距     

`TRTCCloud.TRTCViewMargin`
### 属性列表
#### leftMargin
```
float leftMargin
```

距离左边的百分比，取值范围为0-1         
#### topMargin
```
float topMargin
```

距离左边的百分比，取值范围为0-1         
#### rightMargin
```
float rightMargin
```

距离左边的百分比，取值范围为0-1         
#### bottomMargin
```
float bottomMargin
```

距离左边的百分比，取值范围为0-1         

#### TRTCViewMargin
```
 TRTCViewMargin(float leftMargin, float rightMargin, float topMargin, float bottomMargin)
```

<br/>



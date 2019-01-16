## 基础方法
### create
创建 TRTCEngine 实例(同一时间只会存在一个实例)。
```
TRTCCloud create(Context context, TRTCCloudListener listener)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| context | Context | 上下文 |
| listener | TRTCCloudListener | 事件回调(可通过 setListener 额外添加) |

### destroy
销毁 TRTCEngine 实例。
```
abstract void destroy()
```

### setListener
设置回调接口 TRTCCloudListener，用户获得来自 TRTCCloud 的各种状态通知。
```
abstract void setListener(TRTCCloudListener listener)
```

### setListenerHandler
设置驱动回调的线程，默认会采用 Main Thread。即如果您不指定 listenerHandler，那么直接在 TRTCCloudListener 的回调函数中操作 UI 界面将是安全的。
```
abstract void setListenerHandler(Handler listenerHandler)
```

## 房间相关接口函数
### enterRoom
进入房间。
```
abstract void enterRoom(TRTCCloudDef.TRTCParams param)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCCloudDef.TRTCParams | 进房参数，详情参考TRTCParams定义 |

__说明__
不管进房是否成功，都必须与 exitRoom 配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。

### exitRoom
离开房间。
```
abstract void exitRoom()
```

## 视频相关接口函数
### startLocalPreview
开启本地视频的预览画面。
```
abstract void startLocalPreview(boolean frontCamera, TXCloudVideoView view)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frontCamera | boolean | true:前置摄像头 false:后置摄像头 |
| view | TXCloudVideoView | 指定渲染控件所在的父控件，SDK 会在 view 内部创建一个等大的子控件用来渲染本地摄像头的视频画面 |

### stopLocalPreview
停止本地视频采集及预览。
```
abstract void stopLocalPreview()
```

### startRemoteView
启动渲染远端视频画面。
```
abstract void startRemoteView(String userId, TXCloudVideoView view)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识 |
| view | TXCloudVideoView | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染远端画面 |

### stopRemoteView
停止渲染远端视频画面。
```
abstract void stopRemoteView(String userId)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识 |

### stopAllRemoteView
停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭。
```
abstract void stopAllRemoteView()
```

### muteLocalVideo
是否屏蔽本地视频。当屏蔽本地视频后，房间里的其它成员会收到 onUserVideoAvailable 回调通知。
```
abstract void muteLocalVideo(boolean mute)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | boolean | true：屏蔽，false：开启 |

### setVideoEncoderParam
设置视频编码器相关参数，该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。
```
abstract void setVideoEncoderParam(TRTCCloudDef.TRTCVideoEncParam param)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCCloudDef.TRTCVideoEncParam | 视频编码参数，详情请参考 TRTCCloudDef.java 中的 TRTCVideoEncParam 定义 |

### setNetworkQosParam
设置网络流控相关参数，该设置决定了 SDK 在各种网络环境下的调控策略（比如弱网下是“保清晰”还是“保流畅”）。
```
abstract void setNetworkQosParam(TRTCCloudDef.TRTCNetworkQosParam param)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCCloudDef.TRTCNetworkQosParam | 网络流控参数，详情请参考 TRTCCloudDef.java 中的 TRTCNetworkQosParam 定义 |

### setLocalViewFillMode
设置本地图像的渲染模式。
```
abstract void setLocalViewFillMode(int mode)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | int | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |

### setRemoteViewFillMode
设置远端图像的渲染模式。
```
abstract void setRemoteViewFillMode(String userId, int mode)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| mode | int | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |

### setLocalViewRotation
设置本地图像的顺时针旋转角度。
```
abstract void setLocalViewRotation(int rotation)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | int | 支持 90、180、270 旋转角度 |

### setRemoteViewRotation
设置远端图像的顺时针旋转角度。
```
abstract void setRemoteViewRotation(String userId, int rotation)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识 |
| rotation | int | 支持 90、180、270 旋转角度 |

### setVideoEncoderRotation
设置视频编码出的（供录制和远程观看的）画面方向。
```
abstract void setVideoEncoderRotation(int rotation)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | int | 支持 90、180、270 旋转角度 |

### setGSensorMode
设置重力感应的适应模式。
```
abstract void setGSensorMode(int mode)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | int | 重力感应模式，详情请参考 TRTC_GSENSOR_MODE 的定义 |

### enableEncSmallVideoStream
开启大小画面双路编码模式。如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式。开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源，对于同一房间的远程观众而言，如果有些人的下行网络很好，可以选择观看【高清】画面，如果有些人的下行网络不好，可以选择观看【低清】画面。
```
abstract int enableEncSmallVideoStream(boolean enable, TRTCCloudDef.TRTCVideoEncParam smallVideoEncParam)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | 是否开启小画面编码 |
| smallVideoEncParam | TRTCCloudDef.TRTCVideoEncParam | 小流的视频参数 |

### setRemoteVideoStreamType
选定观看指定 uid 的大画面还是小画面。
>?此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式 如果该 uid 没有开启双路编码模式，则此操作无效。

```
abstract int setRemoteVideoStreamType(String userId, int streamType)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户的 uid |
| streamType | int | 视频流类型，即选择看大画面(TRTC_VIDEO_STREAM_TYPE_BIG)还是小画面(TRTC_VIDEO_STREAM_TYPE_SMALL) |

### setPriorRemoteVideoStreamType
设定观看方优先选择的视频质量。
>?低端设备推荐优先选择低清晰度的小画面 如果对方没有开启双路视频模式，则此操作无效。

```
abstract int setPriorRemoteVideoStreamType(int streamType)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| streamType | int | 默认观看大画面(TRTC_VIDEO_STREAM_TYPE_BIG)还是小画面(TRTC_VIDEO_STREAM_TYPE_SMALL) |

## 音频相关接口函数
### startLocalAudio
开启本地音频流，该函数会启动麦克风采集，并将音频数据广播给房间里的其他用户。
>?TRTC SDK 并不会默认打开本地的麦克风采集。
该函数会检查麦克风使用权限，如果没有麦克风权限，SDK 会向用户申请开启。

```
abstract void startLocalAudio()
```

### stopLocalAudio
关闭本地音频流。
```
abstract void stopLocalAudio()
```

### muteLocalAudio
是否屏蔽本地音频。当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知。
```
abstract void muteLocalAudio(boolean mute)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | boolean | true：屏蔽，false：开启 |

### setAudioRoute
设置音频路由。
```
abstract void setAudioRoute(int route)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | int | 音频路由即声音由哪里输出。如：扬声器(TRTC_AUDIO_ROUTE_SPEAKER)、听筒(TRTC_AUDIO_ROUTE_EARPIECE） |

### muteRemoteAudio
设置指定用户是否静音。
```
abstract void muteRemoteAudio(String userId, boolean mute)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识 |
| mute | boolean | true：静音，false：非静音 |

### muteAllRemoteAudio
设置所有远端用户是否静音。
```
abstract void muteAllRemoteAudio(boolean mute)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | boolean | true:静音 false:非静音 |

### enableAudioVolumeEvaluation
启用音量大小提示。开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估。
```
abstract void enableAudioVolumeEvaluation(int intervalMs, int smoothLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| intervalMs | int | 报告间隔单位为ms, 最小间隔20ms, 如果小于等于0则会关闭回调，建议设置为大于200ms |
| smoothLevel | int | 灵敏度，[0,10], 数字越大，波动越灵敏 |

## 摄像头相关操作
### switchCamera
切换摄像头。
```
abstract void switchCamera()
```

### isCameraZoomSupported
查询当前摄像头是否支持缩放。
```
abstract boolean isCameraZoomSupported()
```

### setZoom
设置摄像头缩放因子（焦距）。
```
abstract void setZoom(int distance)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| distance | int | 取值范围 1~5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清 |

### isCameraTorchSupported
查询是否支持手电筒模式。
```
abstract boolean isCameraTorchSupported()
```

### enableTorch
开关闪光灯。
```
abstract boolean enableTorch(boolean enable)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | boolean | true：开启，false：关闭 |

### isCameraFocusPositionInPreviewSupported
查询是否支持设置焦点。
```
abstract boolean isCameraFocusPositionInPreviewSupported()
```

### setFocusPosition
设置摄像头焦点。
```
abstract void setFocusPosition(int x, int y)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| x | int | 焦点位置 x 坐标 |
| y | int | 焦点位置 y 坐标 |

### isCameraAutoFocusFaceModeSupported
查询是否支持自动识别人脸位置。
```
abstract boolean isCameraAutoFocusFaceModeSupported()
```

## 美颜滤镜相关接口函数
### setBeautyStyle
设置美颜、美白、红润效果级别。
```
abstract void setBeautyStyle(int beautyStyle, int beautyLevel, int whitenessLevel, int ruddinessLevel)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| beautyStyle | int | 美颜风格 ,平滑(TRTCBeautyStyleSmooth)或自然(TRtcBeautyStyleNature) |
| beautyLevel | int | 美颜级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显 |
| whitenessLevel | int | 美白级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显 |
| ruddinessLevel | int | 红润级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显 |

### setFilter
设置指定素材滤镜特效。
```
abstract void setFilter(Bitmap image)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | Bitmap | 指定素材，即颜色查找表图片。注意：一定要用 png 格式！ |

### setWatermark
添加水印，height 不用设置，sdk 内部会根据水印宽高比自动计算 height。
```
abstract void setWatermark(Bitmap image, float x, float y, float width)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | Bitmap | 水印图片 null 表示清除水印 |
| x | float | 归一化水印位置的 X 轴坐标，取值[0,1] |
| y | float | 归一化水印位置的 Y 轴坐标，取值[0,1] |
| width | float | 归一化水印宽度，取值[0,1] |

## 音视频自定义接口
### setLocalVideoRenderListener
设置本地视频自定义渲染。
>?设置此方法后，SDK内部会把采集到的数据回调出来，SDK跳过自己原来的渲染流程，您需要自己完成画面的渲染。

```
abstract int setLocalVideoRenderListener(int pixelFormat, int bufferType, TRTCCloudListener.TRTCVideoRenderListener listener)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pixelFormat | int | 指定视频帧的像素格式，如 TRTC_VIDEO_PIXEL_FORMAT_I420 |
| bufferType | int | 指定视频帧的数据结构，如 TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER， TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY |
| listener | TRTCCloudListener.TRTCVideoRenderListener | 自定义视频渲染回调，每一帧视频数据回调一次 |

### setRemoteVideoRenderListener
设置远端视频自定义渲染。
>?设置此方法后，SDK 内部会把远端的数据解码后回调出来，SDK 跳过自己原来的渲染流程，您需要自己完成画面的渲染。
需要调用 startRemoteView 来开始渲染。

```
abstract int setRemoteVideoRenderListener(String userId, int pixelFormat, int bufferType, TRTCCloudListener.TRTCVideoRenderListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 对方的用户标识 |
| pixelFormat | int | 指定视频帧的像素格式，如 TRTC_VIDEO_PIXEL_FORMAT_I420 |
| bufferType | int | 指定视频帧的数据结构，如 TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER， TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY |
| listener | TRTCCloudListener.TRTCVideoRenderListener | 自定义视频渲染回调，每一帧视频数据回调一次 |

## 自定义消息发送
### sendCustomCmdMsg
发送自定义消息给房间内所有用户。
>?限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息。
限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃。
限制3：每个客户端每秒最多能发送总计 8 KB 数据。

```
abstract boolean sendCustomCmdMsg(int cmdID, byte [] data, boolean reliable, boolean ordered)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdID | int | 消息ID，取值范围为 1 ~ 10 |
| data | byte [] | 待发送的消息，最大支持 1KB（1000字节）的数据大小 |
| reliable | boolean | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传 |
| ordered | boolean | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息 |

## 背景混音相关接口函数
### playBGM
播放背景音乐。
```
abstract void playBGM(String path, BGMNotify notify)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | String | 音乐文件路径 |
| notify | BGMNotify | 播放背景音乐的回调 |

### stopBGM
停止播放背景音乐。
```
abstract void stopBGM()
```

### pauseBGM
暂停播放背景音乐。
```
abstract void pauseBGM()
```

### resumeBGM
继续播放背景音乐。
```
abstract void resumeBGM()
```

### getBGMDuration
获取音乐文件总时长，单位毫秒。
```
abstract int getBGMDuration(String path)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | String | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长 |

### setBGMPosition
设置背景音乐播放进度。
```
abstract int setBGMPosition(int pos)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | int | 单位毫秒 |

### setMicVolumeOnMixing
设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。
```
abstract void setMicVolumeOnMixing(int volume)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | int | 音量大小，100为正常音量，建议值为0~200 |

### setBGMVolume
设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。
```
abstract void setBGMVolume(int volume)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | int | 音量大小，100为正常音量，建议值为0~200，如果需要调大背景音量可以设置更大的值 |

### setReverbType
设置混响效果。
```
abstract void setReverbType(int reverbType)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reverbType | int | ：混响类型 ，详见 TRTC_REVERB_TYPE |

### setVoiceChangerType
设置变声类型。
```
abstract boolean setVoiceChangerType(int voiceChangerType)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| voiceChangerType | int | 变声类型, 详见 TRTC_VOICE_CHANGER_TYPE |

## 网络测试
### startSpeedTest
开始进行网络测速(视频通话期间请勿测试，以免影响通话质量)。

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们最佳的服务器 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络
>!测速本身会消耗一定的流量，所以也会产生少量额外的流量费用 测试结果通过 TRTCCloudListener.onSpeedTest 回调出来。

```
abstract void startSpeedTest(int sdkAppId, String userId, String userSig)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sdkAppId | int | 应用标识 |
| userId | String | 用户标识 |
| userSig | String | 用户签名 |

### stopSpeedTest
停止服务器测速。
```
abstract void stopSpeedTest()
```

## 混流转码并发布到CDN
### startPublishCDNStream
启动 CDN 发布：通过腾讯云将当前房间的音视频流发布到直播 CDN 上。

由于 TRTC 的线路费用是按照时长收费的，并且房间容量有限（< 1000人） 当您有大规模并发观看的需求时，将房间里的音视频流发布到低成本高并发的直播CDN上是一种较为理想的选择。
目前支持两种发布方案：
【1】先混流在发布，TRTCPublishCDNParam.enableTranscoding = YES 需要您先调用startCloudMixTranscoding对多路画面进行混合，发布到CDN上的是混合之后的音视频流
【2】不混流直接发布，TRTCPublishCDNParam.enableTranscoding = NO 发布当前房间里的各路音视频画面，每一路画面都有一个独立的地址，相互之间无影响，调用 startCloudMixTranscoding 将无效。

```
abstract void startPublishCDNStream(TRTCCloudDef.TRTCPublishCDNParam param)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCCloudDef.TRTCPublishCDNParam | 请参考 TRTCCloudDef.java 中关于 TRTCPublishCDNParam 的介绍 |


### stopPublishCDNStream
停止 CDN 发布。
<pre>
【画面1】=> 解码 => =>
                       \
【画面2】=> 解码 =>  画面混合 => 编码 => 【混合后的画面】
                       /
【画面3】=> 解码 => =>
</pre>
```
abstract void stopPublishCDNStream()
```

### startCloudMixTranscoding
启动云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。
```
abstract void startCloudMixTranscoding(TRTCCloudDef.TRTCTranscodingConfig config)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| config | TRTCCloudDef.TRTCTranscodingConfig | 请参考 TRTCCloudDef.java 中关于 TRTCTranscodingConfig 的介绍 |

### stopCloudMixTranscoding
停止云端的混流转码。
```
abstract void stopCloudMixTranscoding()
```

## LOG 相关接口函数
### getSDKVersion
获取 SDK 版本信息。
```
String getSDKVersion()
```

### setLogLevel
设置 log 输出级别。
```
void setLogLevel(int level)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | int | 参见 TRTC_LOG_LEVEL |

### setConsoleEnabled
启用或禁用控制台日志打印。
```
void setConsoleEnabled(boolean enabled)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | boolean | 指定是否启用 true : 启用，false : 不启用 |

### setLogCompressEnabled
启用或禁用 Log 的本地压缩。开启压缩后，log 存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读。禁用压缩后，log 采用明文存储，可以直接用记事本打开阅读，但占用空间较大。
```
void setLogCompressEnabled(boolean enabled)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | boolean | 指定是否启用 true : 启用，false : 不启用 |

### setLogDirPath
修改日志保存路径, 默认保存在 /sdcard//log/tencent/liteav 下，如需修改, 必须在所有方法前调用，并且保证目录存在及应用有目录的读写权限。
```
void setLogDirPath(String path)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | String | 存储日志路径 |

### setLogListener
设置日志回调。
```
void setLogListener(final TRTCCloudListener.TRTCLogListener logListener)
```

### showDebugView
显示仪表盘（状态统计和事件消息浮层 view），方便调试。
```
abstract void showDebugView(int showType)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | int | 0:不显示 1:显示精简版 2:显示全量版 |

### setDebugViewMargin
设置仪表盘的边距，必须在用户进房后设置才生效。
```
abstract void setDebugViewMargin(String userId, TRTCViewMargin margin)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| margin | TRTCViewMargin | 仪表盘内边距，注意这里是基于 parentView 的百分比，margin 的取值范围是 0-1 |

## 播放背景音乐的回调接口
__相关类__
`TRTCCloud.BGMNotify`
### onBGMStart
音乐播放开始的回调通知。
```
void onBGMStart(int errCode)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | int | 0：播放成功 -1：播放失败 |

### onBGMProgress
音乐播放进度的回调通知。
```
void onBGMProgress(long progress, long duration)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| progress | long | 当前BGM已播放时间(ms) |
| duration | long | 当前BGM总时间(ms) |

### onBGMComplete
音乐播放结束的回调通知。
```
void onBGMComplete(int err)
```
__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| err | int | 0：正常结束 -1：出错结束 |

## 视图边距
__相关类__
`TRTCCloud.TRTCViewMargin`
### 属性列表
#### leftMargin
距离左边的百分比，取值范围为0-1。
```
float leftMargin
```
#### topMargin
距离顶部的百分比，取值范围为0-1。
```
float topMargin
```
#### rightMargin
距离右边的百分比，取值范围为0-1。
```
float rightMargin
```
#### bottomMargin
距离底部的百分比，取值范围为0-1。
```
float bottomMargin
```
#### TRTCViewMargin
构造方法。
```
 TRTCViewMargin(float leftMargin, float rightMargin, float topMargin, float bottomMargin)
```

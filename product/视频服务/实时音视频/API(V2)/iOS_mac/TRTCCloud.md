## 房间相关接口函数

### enterRoom

进入房间。

```
 - (void)enterRoom:(TRTCParams *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCParams * | 进房参数，请参考 TRTCParams |

__说明__


不管进房是否成功，都必须与exitRoom配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。


<br/>


### exitRoom

离开房间。

```
 - (void)exitRoom
```

<br/>



## 视频相关接口函数

### startLocalPreview

开启本地视频的预览画面 (iOS版本)。

```
 - (void)startLocalPreview:(BOOL)frontCamera view:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frontCamera | BOOL | YES:前置摄像头 NO:后置摄像头 |
| view | TXView * | 承载预览画面的控件所在的父控件 |

<br/>


### startLocalPreview

开启本地视频的预览画面 (Mac版本)。

```
 - (void)startLocalPreview:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| view | TXView * | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染本地摄像头的视频画面 |

__说明__


在调用该方法前，请先调用 setCurrentCameraDevice 选择使用 Mac 自带的摄像头还是外接摄像头。


<br/>


### stopLocalPreview

停止本地视频采集及预览。

```
 - (void)stopLocalPreview
```

<br/>


### startRemoteView

启动渲染远端视频画面。

```
 - (void)startRemoteView:(NSString *)userId view:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |
| view | TXView * | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染远端画面 |

<br/>


### stopRemoteView

停止渲染远端视频画面。

```
 - (void)stopRemoteView:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |

<br/>


### stopAllRemoteView

停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭。

```
 - (void)stopAllRemoteView
```

<br/>


### muteLocalVideo

是否屏蔽本地视频。

```
 - (void)muteLocalVideo:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES:屏蔽 NO:开启 |

__介绍__


当屏蔽本地视频后，房间里的其它成员将会收到 onUserVideoAvailable 回调通知。


<br/>


### setVideoEncoderParam

设置视频编码器相关参数，该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。

```
 - (void)setVideoEncoderParam:(TRTCVideoEncParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCVideoEncParam * | 视频编码参数，详情请参考 TRTCCloudDef.h 中的 TRTCVideoEncParam 定义 |

<br/>


### setNetworkQosParam

设置网络流控相关参数，该设置决定了SDK在各种网络环境下的调控策略（比如弱网下是“保清晰”还是“保流畅”）。

```
 - (void)setNetworkQosParam:(TRTCNetworkQosParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCNetworkQosParam * | 网络流控参数，详情请参考 TRTCCloudDef.h 中的 TRTCNetworkQosParam 定义 |

<br/>


### setLocalViewFillMode

设置本地图像的渲染模式。

```
 - (void)setLocalViewFillMode:(TRTCVideoFillMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |

<br/>


### setRemoteViewFillMode

设置远端图像的渲染模式。

```
 - (void)setRemoteViewFillMode:(NSString *)userId mode:(TRTCVideoFillMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的id |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |

<br/>


### setLocalViewRotation

设置本地图像的顺时针旋转角度。

```
 - (void)setLocalViewRotation:(TRTCVideoRotation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度 |

<br/>


### setRemoteViewRotation

设置远端图像的顺时针旋转角度。

```
 - (void)setRemoteViewRotation:(NSString *)userId rotation:(TRTCVideoRotation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id |
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度 |

<br/>


### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。

```
 - (void)setVideoEncoderRotation:(TRTCVideoRotation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 0 和 180 两个旋转角度 |

<br/>


### setGSensorMode

设置重力感应的适应模式。

```
 - (void)setGSensorMode:(TRTCGSensorMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCGSensorMode | 重力感应模式，详情请参考 TRTCGSensorMode 的定义 |

<br/>


### enableEncSmallVideoStream

开启大小画面双路编码模式。

```
 - (int)enableEncSmallVideoStream:(BOOL)enable withQuality:(TRTCVideoEncParam *)smallVideoEncParam 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | 是否开启小画面编码 |
| smallVideoEncParam | TRTCVideoEncParam * | 小流的视频参数 |

__介绍__


如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面。


<br/>


### setRemoteVideoStreamType

选定观看指定 uid 的大画面还是小画面。

```
 - (void)setRemoteVideoStreamType:(NSString *)userId type:(TRTCVideoStreamType)type 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的uid |
| type | TRTCVideoStreamType | 视频流类型，即选择看大画面还是小画面 |

__介绍__


此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式 如果该 uid 没有开启双路编码模式，则此操作无效。


<br/>


### setPriorRemoteVideoStreamType

设定观看方优先选择的视频质量。

```
 - (void)setPriorRemoteVideoStreamType:(TRTCVideoStreamType)type 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| type | TRTCVideoStreamType | 默认观看大画面还是小画面 |

__介绍__


低端设备推荐优先选择低清晰度的小画面 如果对方没有开启双路视频模式，则此操作无效。


<br/>


### setLocalVideoMirror

设置摄像头本地预览是否开镜像。

```
 - (void)setLocalVideoMirror:(BOOL)mirror 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mirror | BOOL | 是否开启预览镜像 |

<br/>



## 音频相关接口函数

### startLocalAudio

开启本地音频流，该函数会启动麦克风采集，并将音频数据广播给房间里的其他用户。

```
 - (void)startLocalAudio
```

__说明__


TRTC SDK 并不会默认打开本地的麦克风采集。 
该函数会检查麦克风使用权限，如果没有麦克风权限，SDK 会向用户申请开启。


<br/>


### stopLocalAudio

关闭本地音频流。

```
 - (void)stopLocalAudio
```

<br/>


### muteLocalAudio

是否屏蔽本地音频。

```
 - (void)muteLocalAudio:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES:屏蔽 NO:开启 |

__介绍__


当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知。


<br/>


### setAudioRoute

设置音频路由。

```
 - (void)setAudioRoute:(TRTCAudioRoute)route 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | TRTCAudioRoute | 音频路由即声音由哪里输出（扬声器、听筒） |

<br/>


### muteRemoteAudio

设置指定用户是否静音。

```
 - (void)muteRemoteAudio:(NSString *)userId mute:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |
| mute | BOOL | YES:静音 NO:非静音 |

<br/>


### muteAllRemoteAudio

设置所有远端用户是否静音。

```
 - (void)muteAllRemoteAudio:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES:静音 NO:非静音 |

<br/>


### enableAudioVolumeEvaluation

启用音量大小提示。

```
 - (void)enableAudioVolumeEvaluation:(NSUInteger)interval smooth:(NSInteger)smoothLevel 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | NSUInteger | 报告间隔单位为ms, 最小间隔20ms, 如果小于等于0则会关闭回调，建议设置为大于200ms |
| smoothLevel | NSInteger | 灵敏度，[0,10], 数字越大，波动越灵敏 |

__介绍__


开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估。


<br/>



## 摄像头相关接口函数

### switchCamera

切换摄像头。

```
 - (void)switchCamera
```

<br/>


### isCameraZoomSupported

查询当前摄像头是否支持缩放。

```
 - (BOOL)isCameraZoomSupported
```

<br/>


### setZoom

设置摄像头缩放因子（焦距）。

```
 - (void)setZoom:(CGFloat)distance 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| distance | CGFloat | 取值范围 1~5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清 |

<br/>


### isCameraTorchSupported

查询是否支持手电筒模式。

```
 - (BOOL)isCameraTorchSupported
```

<br/>


### enbaleTorch

开关闪光灯。

```
 - (BOOL)enbaleTorch:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | YES:开启 NO:关闭 |

<br/>


### isCameraFocusPositionInPreviewSupported

查询是否支持设置焦点。

```
 - (BOOL)isCameraFocusPositionInPreviewSupported
```

<br/>


### setFocusPosition

设置摄像头焦点。

```
 - (void)setFocusPosition:(CGPoint)touchPoint 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| touchPoint | CGPoint | 对焦位置 |

<br/>


### isCameraAutoFocusFaceModeSupported

查询是否支持自动识别人脸位置。

```
 - (BOOL)isCameraAutoFocusFaceModeSupported
```

<br/>


### enableAutoFaceFoucs

自动识别人脸位置。

```
 - (void)enableAutoFaceFoucs:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | YES:打开 NO:关闭 |

<br/>


### getCameraDevicesList

获取摄像头设备列表。

```
 - (NSArray< TRTCMediaDeviceInfo * > *)getCameraDevicesList
```

<br/>


### getCurrentCameraDevice

获取当前要使用的摄像头。

```
 - (TRTCMediaDeviceInfo *)getCurrentCameraDevice
```

<br/>


### setCurrentCameraDevice

设置要使用的摄像头。

```
 - (int)setCurrentCameraDevice:(NSString *)deviceId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从getCameraDevicesList中得到的设备id |

<br/>



## 音频设备相关接口函数

### getMicDevicesList

获取麦克风设备列表。

```
 - (NSArray< TRTCMediaDeviceInfo * > *)getMicDevicesList
```

<br/>


### getCurrentMicDevice

获取当前的麦克风设备。

```
 - (TRTCMediaDeviceInfo *)getCurrentMicDevice
```

<br/>


### setCurrentMicDevice

设置要使用的麦克风。

```
 - (int)setCurrentMicDevice:(NSString *)deviceId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从getMicDevicesList中得到的设备id |

<br/>


### getCurrentMicDeviceVolume

获取当前麦克风设备音量。

```
 - (float)getCurrentMicDeviceVolume
```

<br/>


### setCurrentMicDeviceVolume

设置麦克风设备的音量。

```
 - (void)setCurrentMicDeviceVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 麦克风音量值, 范围0~100 |

<br/>


### getSpeakerDevicesList

获取扬声器设备列表。

```
 - (NSArray< TRTCMediaDeviceInfo * > *)getSpeakerDevicesList
```

<br/>


### getCurrentSpeakerDevice

获取当前的扬声器设备。

```
 - (TRTCMediaDeviceInfo *)getCurrentSpeakerDevice
```

<br/>


### setCurrentSpeakerDevice

设置要使用的扬声器。

```
 - (int)setCurrentSpeakerDevice:(NSString *)deviceId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从getSpeakerDevicesList中得到的设备id |

<br/>


### getCurrentSpeakerDeviceVolume

当前扬声器设备音量。

```
 - (float)getCurrentSpeakerDeviceVolume
```

<br/>


### setCurrentSpeakerDeviceVolume

设置当前扬声器音量。

```
 - (int)setCurrentSpeakerDeviceVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 设置的扬声器音量, 范围0~100 |

<br/>



## 美颜滤镜相关接口函数

### setBeautyStyle

设置美颜、美白、红润效果级别。

```
 - (void)setBeautyStyle:(TRTCBeautyStyle)beautyStyle beautyLevel:(NSInteger)beautyLevel whitenessLevel:(NSInteger)whitenessLevel ruddinessLevel:(NSInteger)ruddinessLevel 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| beautyStyle | TRTCBeautyStyle | 美颜风格 |
| beautyLevel | NSInteger | 美颜级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显 |
| whitenessLevel | NSInteger | 美白级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显 |
| ruddinessLevel | NSInteger | 红润级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显 |

<br/>


### setFilter

设置指定素材滤镜特效。

```
 - (void)setFilter:(TXImage *)image 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | TXImage * | 指定素材，即颜色查找表图片。注意：一定要用png格式！！！ |

<br/>


### setWatermark

添加水印。

```
 - (void)setWatermark:(TXImage *)image rect:(CGRect)rect 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | TXImage * | 水印图片 |
| rect | CGRect | 水印相对于编码分辨率的归一化坐标，x,y,width,height 取值范围 0~1；height不用设置，sdk内部会根据水印宽高比自动计算height |

<br/>



## 音视频自定义接口

### setLocalVideoRenderDelegate

设置本地视频的自定义渲染回调。

```
 - (int)setLocalVideoRenderDelegate:(id< TRTCVideoRenderDelegate >)delegate pixelFormat:(TRTCVideoPixelFormat)pixelFormat bufferType:(TRTCVideoBufferType)bufferType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| delegate | id< TRTCVideoRenderDelegate > | 自定义渲染回调 |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式, 目前仅支持 TRTCVideoPixelFormat_I420 |
| bufferType | TRTCVideoBufferType | SDK为了提高回调性能，提供了两种PixelBuffer格式，一种是iOS原始的(TRTCVideoBufferType_PixelBuffer)，一种是经过内存整理的(TRTCVideoBufferType_NSData) |

__说明__


设置此方法后，SDK内部会把采集到的数据回调出来，SDK跳过自己原来的渲染流程，您需要自己完成画面的渲染。


<br/>


### setRemoteVideoRenderDelegate

设置远端视频的自定义渲染回调。

```
 - (int)setRemoteVideoRenderDelegate:(NSString *)userId delegate:(id< TRTCVideoRenderDelegate >)delegate pixelFormat:(TRTCVideoPixelFormat)pixelFormat bufferType:(TRTCVideoBufferType)bufferType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 自定义渲染回调 |
| delegate | id< TRTCVideoRenderDelegate > | 自定义渲染的回调 |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式，目前仅支持 TRTCVideoPixelFormat_I420 |
| bufferType | TRTCVideoBufferType | SDK为了提高回调性能，提供了两种PixelBuffer格式，一种是iOS原始的(TRTCVideoBufferType_PixelBuffer)，一种是经过内存整理的(TRTCVideoBufferType_NSData) |

__说明__


设置此方法后，SDK内部会把远端的数据解码后回调出来，SDK跳过自己原来的渲染流程，您需要自己完成画面的渲染 
需要调用 startRemoteView 来决定回调哪一路 userid 的视频画面。


<br/>



## 自定义消息发送

### sendCustomCmdMsg

发送自定义消息给房间内所有用户。

```
 - (BOOL)sendCustomCmdMsg:(NSInteger)cmdID data:(NSData *)data reliable:(BOOL)reliable ordered:(BOOL)ordered 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdID | NSInteger | 消息ID，取值范围为 1 ~ 10 |
| data | NSData * | 待发送的消息，最大支持 1KB（1000字节）的数据大小 |
| reliable | BOOL | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传 |
| ordered | BOOL | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息 |

__说明__


限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息 限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃 限制3：每个客户端每秒最多能发送总计 8 KB 数据。


<br/>



## 背景混音相关接口函数

### playBGM

播放背景音乐。

```
 - (void)playBGM:(NSString *)path withBeginNotify:(void(^)(NSInteger errCode))beginNotify withProgressNotify:(void(^)(NSInteger progressMS, NSInteger durationMS))progressNotify andCompleteNotify:(void(^)(NSInteger errCode))completeNotify 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 音乐文件路径 |
| beginNotify | void(^)(NSInteger errCode) | 音乐播放开始的回调通知 |
| progressNotify | void(^)(NSInteger progressMS, NSInteger durationMS) | 音乐播放的进度通知，单位毫秒 |
| completeNotify | void(^)(NSInteger errCode) | 音乐播放结束的回调通知 |

<br/>


### stopBGM

停止播放背景音乐。

```
 - (void)stopBGM
```

<br/>


### pauseBGM

暂停播放背景音乐。

```
 - (void)pauseBGM
```

<br/>


### resumeBGM

继续播放背景音乐。

```
 - (void)resumeBGM
```

<br/>


### getBGMDuration

获取音乐文件总时长，单位毫秒。

```
 - (NSInteger)getBGMDuration:(NSString *)path 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 音乐文件路径，如果path为空，那么返回当前正在播放的music时长 |

<br/>


### setBGMPosition

设置BGM播放进度。

```
 - (int)setBGMPosition:(NSInteger)pos 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | NSInteger | 单位毫秒 |

<br/>


### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
 - (void)setMicVolumeOnMixing:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 音量大小，100为正常音量，值为0~200 |

<br/>


### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
 - (void)setBGMVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 音量大小，100为正常音量，建议值为0~200，如果需要调大背景音量可以设置更大的值 |

<br/>


### setReverbType

设置混响效果 (目前仅iOS)。

```
 - (void)setReverbType:(TRTCReverbType)reverbType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reverbType | TRTCReverbType | ：混响类型 ，详见 TXReverbType |

<br/>


### setVoiceChangerType

设置变声类型 (目前仅iOS)。

```
 - (void)setVoiceChangerType:(TRTCVoiceChangerType)voiceChangerType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| voiceChangerType | TRTCVoiceChangerType | 变声类型, 详见 TXVoiceChangerType |

<br/>



## 设备和网络测试

### startSpeedTest

开始进行网络测速(视频通话期间请勿测试，以免影响通话质量)。

```
 - (void)startSpeedTest:(uint32_t)sdkAppId userId:(NSString *)userId userSig:(NSString *)userSig completion:(void(^)(TRTCSpeedTestResult *result, NSInteger completedCount, NSInteger totalCount))completion 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sdkAppId | uint32_t | 应用标识 |
| userId | NSString * | 用户标识 |
| userSig | NSString * | 用户签名 |
| completion | void(^)(TRTCSpeedTestResult *result, NSInteger completedCount, NSInteger totalCount) | 测试回调，会分多次回调 |

__介绍__


测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们最佳的服务器 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络
注意：测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。


<br/>


### stopSpeedTest

停止服务器测速。

```
 - (void)stopSpeedTest
```

<br/>


### startCameraDeviceTestInView

开始进行摄像头测试。

```
 - (void)startCameraDeviceTestInView:(NSView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| view | NSView * | 预览控件所在的父控件 |

__说明__


在测试过程中可以使用 setCurrentCameraDevice 接口切换摄像头。


<br/>


### stopCameraDeviceTest

结束视频测试预览。

```
 - (void)stopCameraDeviceTest
```

<br/>


### startMicDeviceTest

开始进行麦克风测试 该方法测试麦克风是否能正常工作, volume的取值范围为 0~100。

```
 - (void)startMicDeviceTest:(NSInteger)interval testEcho:(void(^)(NSInteger volume))testEcho 
```

<br/>


### stopMicDeviceTest

停止麦克风测试。

```
 - (void)stopMicDeviceTest
```

<br/>


### startSpeakerDeviceTest

开始扬声器测试 该方法播放指定的音频文件测试播放设备是否能正常工作。如果能听到声音，说明播放设备能正常工作。         

```
 - (void)startSpeakerDeviceTest:(NSString *)audioFilePath onVolumeChanged:(void(^)(NSInteger volume, BOOL isLastFrame))volumeBlock 
```

<br/>


### stopSpeakerDeviceTest

停止扬声器测试。

```
 - (void)stopSpeakerDeviceTest
```

<br/>



## 混流转码并发布到CDN

### startPublishCDNStream

启动CDN发布：通过腾讯云将当前房间的音视频流发布到直播CDN上。

```
 - (void)startPublishCDNStream:(TRTCPublishCDNParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCPublishCDNParam * | 请参考 TRTCCloudDef.h 中关于 TRTCPublishCDNParam 的介绍 |

__介绍__


由于 TRTC 的线路费用是按照时长收费的，并且房间容量有限（< 1000人） 当您有大规模并发观看的需求时，将房间里的音视频流发布到低成本高并发的直播CDN上是一种较为理想的选择。
目前支持两种发布方案：
【1】先混流在发布，TRTCPublishCDNParam.enableTranscoding = YES 需要您先调用startCloudMixTranscoding对多路画面进行混合，发布到CDN上的是混合之后的音视频流
【2】不混流直接发布，TRTCPublishCDNParam.enableTranscoding = NO 发布当前房间里的各路音视频画面，每一路画面都有一个独立的地址，相互之间无影响，调用startCloudMixTranscoding将无效。


<br/>


### stopPublishCDNStream

停止CDN发布。

```
 - (void)stopPublishCDNStream
```

<br/>


### startCloudMixTranscoding

启动云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。

```
 - (void)startCloudMixTranscoding:(TRTCTranscodingConfig *)config 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| config | TRTCTranscodingConfig * | 请参考 TRTCCloudDef.h 中关于 TRTCTranscodingConfig 的介绍 |

__介绍__


<pre>
【画面1】=> 解码 => =>
                        \
【画面2】=> 解码 =>  画面混合 => 编码 => 【混合后的画面】
                        /
【画面3】=> 解码 => =>
</pre>

        


<br/>


### stopCloudMixTranscoding

停止云端的混流转码。

```
 - (void)stopCloudMixTranscoding
```

<br/>



## LOG相关接口函数

### showDebugView

显示仪表盘。

```
 - (void)showDebugView:(NSInteger)showType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | NSInteger | 0:不显示 1:显示精简版 2:显示全量版 |

__介绍__


仪表盘是状态统计和事件消息浮层view，方便调试。


<br/>


### setDebugViewMargin

设置仪表盘的边距。

```
 - (void)setDebugViewMargin:(NSString *)userId margin:(TXEdgeInsets)margin 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id |
| margin | TXEdgeInsets | 仪表盘内边距，注意这里是基于parentView的百分比，margin的取值范围是01 |

__介绍__


必须在 showDebugView 调用前设置才会生效。


<br/>


### getSDKVersion

获取SDK版本信息。

```
 + (NSString *)getSDKVersion
```

<br/>


### setLogLevel

设置log输出级别。

```
 + (void)setLogLevel:(TRTCLogLevel)level 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | TRTCLogLevel | 参见 TRTCLogLevel |

<br/>


### setConsoleEnabled

启用或禁用控制台日志打印。

```
 + (void)setConsoleEnabled:(BOOL)enabled 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | BOOL | 指定是否启用 |

<br/>


### setLogCompressEnabled

启用或禁用Log的本地压缩。

```
 + (void)setLogCompressEnabled:(BOOL)enabled 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | BOOL | 指定是否启用 |

__介绍__


开启压缩后，log存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读 禁用压缩后，log采用明文存储，可以直接用记事本打开阅读，但占用空间较大。 
        


<br/>


### setLogDirPath

修改日志保存路径。

```
 + (void)setLogDirPath:(NSString *)path 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 存储日志路径 |

__说明__


默认保存在 sandbox Documents/log 下，如需修改, 必须在所有方法前调用。


<br/>


### setLogDelegate

设置日志回调。

```
 + (void)setLogDelegate:(id< TRTCLogDelegate >)logDelegate 
```

<br/>



## 属性列表
### delegate

设置回调接口 TRTCCloudDelegate，用户获得来自 TRTCCloud 的各种状态通知。

```
@property (nonatomic, weak) id< TRTCCloudDelegate > delegate;
```

<br/>

### delegateQueue

设置驱动回调的队列，默认会采用 Main Queue。 也就是说，如果您不指定 delegateQueue，那么直接在 TRTCCloudDelegate 的回调函数中操作 UI 界面将是安全的。

```
@property (nonatomic, strong) dispatch_queue_t delegateQueue;
```

<br/>



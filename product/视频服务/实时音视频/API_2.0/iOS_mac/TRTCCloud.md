
腾讯云视频通话功能的主要接口类     
## 房间相关接口函数

### enterRoom
```
 - (void)enterRoom:(TRTCParams *)param 
```


__功能__


进入房间         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCParams * | 进房参数，请参考 DOC-TO-DO  |

__说明__

不管进房是否成功，都必须与exitRoom配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题 

<br/>

### exitRoom
```
 - (void)exitRoom
```


__功能__


离开房间         

<br/>


## 视频相关接口函数

### startLocalPreview
```
 - (void)startLocalPreview:(BOOL)frontCamera view:(TXView *)view 
```


__功能__


开启本地视频的预览画面 (iOS版本)         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frontCamera | BOOL | YES:前置摄像头 NO:后置摄像头  |
| view | TXView * | 承载预览画面的控件所在的父控件  |

<br/>

### startLocalPreview
```
 - (void)startLocalPreview:(TXView *)view 
```


__功能__


开启本地视频的预览画面 (Mac版本)         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| view | TXView * | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染本地摄像头的视频画面  |

__说明__

在调用该方法前，请先调用 setCurrentCameraDevice 选择使用 Mac 自带的摄像头还是外接摄像头 

<br/>

### stopLocalPreview
```
 - (void)stopLocalPreview
```


__功能__


停止本地视频采集及预览         

<br/>

### startRemoteView
```
 - (void)startRemoteView:(NSString *)userId view:(TXView *)view 
```


__功能__


启动渲染远端视频画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识  |
| view | TXView * | 指定渲染控件所在的父控件，SDK会在 view 内部创建一个等大的子控件用来渲染远端画面  |

<br/>

### stopRemoteView
```
 - (void)stopRemoteView:(NSString *)userId 
```


__功能__


停止渲染远端视频画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识  |

<br/>

### stopAllRemoteView
```
 - (void)stopAllRemoteView
```


__功能__


停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭         

<br/>

### setLocalVideoQuality
```
 - (void)setLocalVideoQuality:(TRTCVideoEncParam *)param qosControl:(TRTCQosMode)qosControl qosPreference:(TRTCVideoQosPreference)qosPreference 
```


__功能__


设置本地的视频编码质量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCVideoEncParam * | 视频编码参数，详情请参考 TRTCCloudDef.h 中的  |
| qosControl | TRTCQosMode | 流控模式选择，默认选择【云控】模式，便于获得更好的效果，【终端】模式则用于特殊的调试场景  |
| qosPreference | TRTCVideoQosPreference | 画面质量偏好，有【流畅】和【清晰】两种模式可供选择，详情请参考 TRTCVideoQosPreference 的定义  |

<br/>

### muteLocalVideo
```
 - (void)muteLocalVideo:(BOOL)mute 
```


__功能__


是否屏蔽本地视频

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES:屏蔽 NO:开启  |

__介绍__

当屏蔽本地视频后，房间里的其它成员将会收到 onUserVideoAvailable 回调通知         

<br/>

### setLocalViewFillMode
```
 - (void)setLocalViewFillMode:(TRTCVideoFillMode)mode 
```


__功能__


设置本地图像的渲染模式

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边）  |

<br/>

### setRemoteViewFillMode
```
 - (void)setRemoteViewFillMode:(NSString *)userId mode:(TRTCVideoFillMode)mode 
```


__功能__


设置远端图像的渲染模式

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的id  |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边）  |

<br/>

### setLocalViewRotation
```
 - (void)setLocalViewRotation:(TRTCVideoRotation)rotation 
```


__功能__


设置本地图像的顺时针旋转角度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度  |

<br/>

### setRemoteViewRotation
```
 - (void)setRemoteViewRotation:(NSString *)userId rotation:(TRTCVideoRotation)rotation 
```


__功能__


设置远端图像的顺时针旋转角度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id  |
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度  |

<br/>

### setVideoOutputRotation
```
 - (void)setVideoOutputRotation:(TRTCVideoRotation)rotation 
```


__功能__


设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度  |

<br/>

### setGSensorMode
```
 - (void)setGSensorMode:(TRTCGSensorMode)mode 
```


__功能__


设置重力感应的适应模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCGSensorMode | 重力感应模式，详情请参考 TRTCGSensorMode 的定义  |

<br/>

### enableEncSmallVideoStream
```
 - (int)enableEncSmallVideoStream:(BOOL)enable withQuality:(TRTCVideoEncParam *)smallVideoEncParam 
```


__功能__


开启大小画面双路编码模式

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | 是否开启小画面编码  |
| smallVideoEncParam | TRTCVideoEncParam * | 小流的视频参数  |

__介绍__

如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面         

<br/>

### setRemoteVideoStreamType
```
 - (void)setRemoteVideoStreamType:(NSString *)userId type:(TRTCVideoStreamType)type 
```


__功能__


选定观看指定 uid 的大画面还是小画面

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的uid  |
| type | TRTCVideoStreamType | 视频流类型，即选择看大画面还是小画面  |

__介绍__

此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式 如果该 uid 没有开启双路编码模式，则此操作无效         

<br/>

### setPriorRemoteVideoStreamType
```
 - (void)setPriorRemoteVideoStreamType:(TRTCVideoStreamType)type 
```


__功能__


设定观看方优先选择的视频质量

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| type | TRTCVideoStreamType | 默认观看大画面还是小画面  |

__介绍__

低端设备推荐优先选择低清晰度的小画面 如果对方没有开启双路视频模式，则此操作无效         

<br/>


## 音频相关接口函数

### muteLocalAudio
```
 - (void)muteLocalAudio:(BOOL)mute 
```


__功能__


是否屏蔽本地音频

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES:屏蔽 NO:开启  |

__介绍__

当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知         

<br/>

### setAudioRoute
```
 - (void)setAudioRoute:(TRTCAudioRoute)route 
```


__功能__


设置音频路由         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | TRTCAudioRoute | 音频路由即声音由哪里输出（扬声器、听筒）  |

<br/>

### muteRemoteAudio
```
 - (void)muteRemoteAudio:(NSString *)userId mute:(BOOL)mute 
```


__功能__


设置指定用户是否静音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识  |
| mute | BOOL | YES:静音 NO:非静音  |

<br/>

### muteAllRemoteAudio
```
 - (void)muteAllRemoteAudio:(BOOL)mute 
```


__功能__


设置所有远端用户是否静音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES:静音 NO:非静音  |

<br/>

### setRemoteAudioVolume
```
 - (void)setRemoteAudioVolume:(NSString *)userId volume:(float)volume 
```


__功能__


设置指定用户音量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id  |
| volume | float | 音量  |

<br/>

### enableAudioVolumeEvaluation
```
 - (void)enableAudioVolumeEvaluation:(NSUInteger)interval smooth:(NSInteger)smoothLevel 
```


__功能__


启用音量大小提示

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | NSUInteger | 报告间隔单位为ms, 最小间隔20ms, 如果小于等于0则会关闭回调，建议设置为大于200ms  |
| smoothLevel | NSInteger | 灵敏度，[0,10], 数字越大，波动越灵敏  |

__介绍__

开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估         

<br/>


## 摄像头相关接口函数

### switchCamera
```
 - (void)switchCamera
```


__功能__


切换摄像头         

<br/>

### isCameraZoomSupported
```
 - (BOOL)isCameraZoomSupported
```


__功能__


查询当前摄像头是否支持缩放         

<br/>

### setZoom
```
 - (void)setZoom:(CGFloat)distance 
```


__功能__


设置摄像头缩放因子（焦距）         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| distance | CGFloat | 取值范围 1~5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清  |

<br/>

### isCameraTorchSupported
```
 - (BOOL)isCameraTorchSupported
```


__功能__


查询是否支持手电筒模式         

<br/>

### enbaleTorch
```
 - (BOOL)enbaleTorch:(BOOL)enable 
```


__功能__


开关闪光灯         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | YES:开启 NO:关闭  |

<br/>

### isCameraFocusPositionInPreviewSupported
```
 - (BOOL)isCameraFocusPositionInPreviewSupported
```


__功能__


查询是否支持设置焦点         

<br/>

### setFocusPosition
```
 - (void)setFocusPosition:(CGPoint)touchPoint 
```


__功能__


设置摄像头焦点         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| touchPoint | CGPoint | 对焦位置  |

<br/>

### isCameraAutoFocusFaceModeSupported
```
 - (BOOL)isCameraAutoFocusFaceModeSupported
```


__功能__


查询是否支持自动识别人脸位置         

<br/>

### enableAutoFaceFoucs
```
 - (void)enableAutoFaceFoucs:(BOOL)enable 
```


__功能__


自动识别人脸位置         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | YES:打开 NO:关闭  |

<br/>

### getCameraDevicesList
```
 - (NSArray< TRTCMediaDeviceInfo * > *)getCameraDevicesList
```


__功能__


获取摄像头设备列表         

<br/>

### getCurrentCameraDevice
```
 - (TRTCMediaDeviceInfo *)getCurrentCameraDevice
```


__功能__


获取当前要使用的摄像头         

<br/>

### setCurrentCameraDevice
```
 - (int)setCurrentCameraDevice:(NSString *)deviceId 
```


__功能__


设置要使用的摄像头         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从getCameraDevicesList中得到的设备id  |

<br/>


## 音频设备相关接口函数

### getMicDevicesList
```
 - (NSArray< TRTCMediaDeviceInfo * > *)getMicDevicesList
```


__功能__


获取麦克风设备列表         

<br/>

### getCurrentMicDevice
```
 - (TRTCMediaDeviceInfo *)getCurrentMicDevice
```


__功能__


获取当前的麦克风设备         

<br/>

### setCurrentMicDevice
```
 - (int)setCurrentMicDevice:(NSString *)deviceId 
```


__功能__


设置要使用的麦克风         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从getMicDevicesList中得到的设备id  |

<br/>

### getCurrentMicDeviceVolume
```
 - (float)getCurrentMicDeviceVolume
```


__功能__


获取当前麦克风设备音量         

<br/>

### setCurrentMicDeviceVolume
```
 - (void)setCurrentMicDeviceVolume:(float)volume 
```


__功能__


设置麦克风设备的音量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | float | 麦克风音量值, 范围0~100  |

<br/>

### getSpeakerDevicesList
```
 - (NSArray< TRTCMediaDeviceInfo * > *)getSpeakerDevicesList
```


__功能__


获取扬声器设备列表         

<br/>

### getCurrentSpeakerDevice
```
 - (TRTCMediaDeviceInfo *)getCurrentSpeakerDevice
```


__功能__


获取当前的扬声器设备         

<br/>

### setCurrentSpeakerDevice
```
 - (int)setCurrentSpeakerDevice:(NSString *)deviceId 
```


__功能__


设置要使用的扬声器         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从getSpeakerDevicesList中得到的设备id  |

<br/>

### getCurrentSpeakerDeviceVolume
```
 - (float)getCurrentSpeakerDeviceVolume
```


__功能__


当前扬声器设备音量         

<br/>

### setCurrentSpeakerDeviceVolume
```
 - (int)setCurrentSpeakerDeviceVolume:(float)volume 
```


__功能__


设置当前扬声器音量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | float | 设置的扬声器音量, 范围0~100  |

<br/>


## 美颜滤镜相关接口函数

### setBeautyStyle
```
 - (void)setBeautyStyle:(TRTCBeautyStyle)beautyStyle beautyLevel:(NSInteger)beautyLevel whitenessLevel:(NSInteger)whitenessLevel ruddinessLevel:(NSInteger)ruddinessLevel 
```


__功能__


设置美颜、美白、红润效果级别         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| beautyStyle | TRTCBeautyStyle | 美颜风格  |
| beautyLevel | NSInteger | 美颜级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显  |
| whitenessLevel | NSInteger | 美白级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显  |
| ruddinessLevel | NSInteger | 红润级别，取值范围 0 ~ 9； 0 表示关闭， 1 ~ 9值越大，效果越明显  |

<br/>

### setFilter
```
 - (void)setFilter:(TXImage *)image 
```


__功能__


设置指定素材滤镜特效         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | TXImage * | 指定素材，即颜色查找表图片。注意：一定要用png格式！！！  |

<br/>

### setWatermark
```
 - (void)setWatermark:(TXImage *)image rect:(CGRect)rect 
```


__功能__


添加水印         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | TXImage * | 水印图片  |
| rect | CGRect | 水印相对于编码分辨率的归一化坐标，x,y,width,height 取值范围 0~1；height不用设置，sdk内部会根据水印宽高比自动计算height  |

<br/>


## 屏幕共享接口函数(MAC)

### startScreenCaptureWithDisplayID
```
 - (int)startScreenCaptureWithDisplayID:(CGDirectDisplayID)displayID captureFreq:(NSUInteger)captureFreq bitRate:(NSInteger)bitRate rect:(CGRect)rect renderView:(NSView *)view 
```


__功能__


开始全屏采集         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| displayID | CGDirectDisplayID | 显示器Id  |
| captureFreq | NSUInteger | 采集fps  |
| bitRate | NSInteger | 采集码率  |
| rect | CGRect | 采集区域  |
| view | NSView * | 预览View  |

<br/>

### startScreenCaptureWithWindowID
```
 - (int)startScreenCaptureWithWindowID:(CGWindowID)windowID captureFreq:(NSUInteger)captureFreq bitRate:(NSInteger)bitRate renderView:(NSView *)view 
```


__功能__


开始窗口采集         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| windowID | CGWindowID | 窗口ID  |
| captureFreq | NSUInteger | 采集fps  |
| bitRate | NSInteger | 采集码率  |
| view | NSView * | 预览View  |

<br/>

### stopScreenCapture
```
 - (int)stopScreenCapture
```


__功能__


停止屏幕采集

<br/>

### resetScreenCaptureRect
```
 - (int)resetScreenCaptureRect:(CGRect)rect 
```


__功能__


更新采集区域

<br/>


## 自定义音视频数据

### enableCustomVideoCapture
```
 - (void)enableCustomVideoCapture:(BOOL)enable 
```


__功能__


启用视频自定义采集模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | 是否启用  |

<br/>

### sendVideoSampleBuffer
```
 - (void)sendVideoSampleBuffer:(CMSampleBufferRef)sampleBuffer 
```


__功能__


发送自定义的SampleBuffer

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sampleBuffer | CMSampleBufferRef | sampleBuffer视频数据  |

__介绍__

内部有简单的帧率控制，发太快会自动丢帧；超时则会重发最后一帧         

__说明__

相关属性设置请参考TXLivePushConfig，autoSampleBufferSize优先级高于sampleBufferSize 

<br/>

### enableCustomAudioCapture
```
 - (void)enableCustomAudioCapture:(BOOL)enable 
```


__功能__


启用音频自定义采集模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | 是否启用  |

<br/>

### sendCustomPCMData
```
 - (void)sendCustomPCMData:(unsigned char *)data len:(unsigned int)len 
```


__功能__


发送客户自定义的音频PCM数据

__说明__

目前SDK只支持16位采样的PCM编码；如果是单声道，请保证传入的PCM长度为2048；如果是双声道，请保证传入的PCM长度为4096 

<br/>

### setLocalVideoRenderDelegate
```
 - (void)setLocalVideoRenderDelegate:(id< TRTCVideoRenderDelegate >)delegate withPixelFormat:(TRTCVideoPixelFormat)pixelFormat 
```


__功能__


设置本地视频自定义渲染         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| delegate | id< TRTCVideoRenderDelegate > | 自定义渲染回调  |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式  |

__说明__

设置此方法，SDK内部会把采集到的数据回调出来，SDK跳过渲染逻辑 

<br/>

### setRemoteVideoRenderDelegate
```
 - (void)setRemoteVideoRenderDelegate:(id< TRTCVideoRenderDelegate >)delegate withUserId:(NSString *)userId pixelFormat:(TRTCVideoPixelFormat)pixelFormat 
```


__功能__


设置远端视频自定义渲染         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| delegate | id< TRTCVideoRenderDelegate > | 自定义渲染回调  |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式  |

__说明__

设置此方法，SDK内部会把远端的数据解码后回调出来，SDK跳过渲染逻辑 

<br/>


## 自定义消息发送

### sendCustomCmdMsg
```
 - (BOOL)sendCustomCmdMsg:(NSInteger)cmdID data:(NSData *)data reliable:(BOOL)reliable ordered:(BOOL)ordered 
```


__功能__


发送自定义消息给房间内所有用户

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdID | NSInteger | 消息ID，取值范围为 1 ~ 10  |
| data | NSData * | 待发送的消息，最大支持 1KB（1000字节）的数据大小  |
| reliable | BOOL | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传  |
| ordered | BOOL | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息  |

__说明__

限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息 限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃 限制3：每个客户端每秒最多能发送总计 8 KB 数据

<br/>


## 背景混音相关接口函数

### playBGM
```
 - (void)playBGM:(NSString *)path withBeginNotify:(void(^)(NSInteger errCode))beginNotify withProgressNotify:(void(^)(NSInteger progressMS, NSInteger durationMS))progressNotify andCompleteNotify:(void(^)(NSInteger errCode))completeNotify 
```


__功能__


播放背景音乐         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 音乐文件路径  |
| beginNotify | void(^)(NSInteger errCode) | 音乐播放开始的回调通知  |
| progressNotify | void(^)(NSInteger progressMS, NSInteger durationMS) | 音乐播放的进度通知，单位毫秒  |
| completeNotify | void(^)(NSInteger errCode) | 音乐播放结束的回调通知  |

<br/>

### stopBGM
```
 - (void)stopBGM
```


__功能__


停止播放背景音乐         

<br/>

### pauseBGM
```
 - (void)pauseBGM
```


__功能__


暂停播放背景音乐         

<br/>

### resumeBGM
```
 - (void)resumeBGM
```


__功能__


继续播放背景音乐         

<br/>

### getBGMDuration
```
 - (NSInteger)getBGMDuration:(NSString *)path 
```


__功能__


获取音乐文件总时长，单位毫秒         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 音乐文件路径，如果path为空，那么返回当前正在播放的music时长  |

<br/>

### setBGMPosition
```
 - (int)setBGMPosition:(NSInteger)pos 
```


__功能__


设置BGM播放进度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | NSInteger | 单位毫秒  |

<br/>

### setMicVolumeOnMixing
```
 - (void)setMicVolumeOnMixing:(float)volume 
```


__功能__


设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | float | 音量大小，1为正常音量，值为0~2  |

<br/>

### setReverbType
```
 - (void)setReverbType:(TRTCReverbType)reverbType 
```


__功能__


设置混响效果 (目前仅iOS)         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reverbType | TRTCReverbType | ：混响类型 ，详见 TXReverbType  |

<br/>

### setVoiceChangerType
```
 - (void)setVoiceChangerType:(TRTCVoiceChangerType)voiceChangerType 
```


__功能__


设置变声类型 (目前仅iOS)         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| voiceChangerType | TRTCVoiceChangerType | 变声类型, 详见 TXVoiceChangerType  |

<br/>


## 设备和网络测试

### startSpeedTest
```
 - (void)startSpeedTest:(uint32_t)sdkAppId userId:(NSString *)userId userSig:(NSString *)userSig completion:(void(^)(TRTCSpeedTestResult *result, NSInteger completedCount, NSInteger totalCount))completion 
```


__功能__


开始进行网络测速(视频通话期间请勿测试，以免影响通话质量)

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sdkAppId | uint32_t | 应用标识  |
| userId | NSString * | 用户标识  |
| userSig | NSString * | 用户签名  |
| completion | void(^)(TRTCSpeedTestResult *result, NSInteger completedCount, NSInteger totalCount) | 测试回调，会分多次回调  |

__介绍__

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们最佳的服务器 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络
注意：测速本身会消耗一定的流量，所以也会产生少量额外的流量费用

<br/>

### stopSpeedTest
```
 - (void)stopSpeedTest
```


__功能__


停止服务器测速         

<br/>

### startCameraDeviceTestInView
```
 - (void)startCameraDeviceTestInView:(NSView *)view 
```


__功能__


开始进行摄像头测试         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| view | NSView * | 预览控件所在的父控件  |

__说明__

同startLocalPreview一样使用setCurrentCameraDevice接口选中的摄像头设备 

<br/>

### stopCameraDeviceTest
```
 - (void)stopCameraDeviceTest
```


__功能__


结束视频测试预览         

<br/>

### startMicDeviceTest
```
 - (void)startMicDeviceTest:(NSInteger)interval testEcho:(void(^)(NSInteger volume))testEcho 
```


__功能__


开始进行麦克风测试 该方法测试麦克风是否能正常工作, volume的取值范围为 0~100         

<br/>

### stopMicDeviceTest
```
 - (void)stopMicDeviceTest
```


__功能__


停止麦克风测试         

<br/>

### startSpeakerDeviceTest
```
 - (void)startSpeakerDeviceTest:(NSString *)audioFilePath onVolumeChanged:(void(^)(NSInteger volume, BOOL isLastFrame))volumeBlock 
```


__功能__


开始扬声器测试 该方法播放指定的音频文件测试播放设备是否能正常工作。如果能听到声音，说明播放设备能正常工作。。

<br/>

### stopSpeakerDeviceTest
```
 - (void)stopSpeakerDeviceTest
```


__功能__


停止扬声器测试         

<br/>


## LOG相关接口函数

### showDebugView
```
 - (void)showDebugView:(NSInteger)showType 
```


__功能__


显示仪表盘

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | NSInteger | 0:不显示 1:显示精简版 2:显示全量版  |

__介绍__

仪表盘是状态统计和事件消息浮层view，方便调试         

<br/>

### setDebugViewMargin
```
 - (void)setDebugViewMargin:(NSString *)userId margin:(TXEdgeInsets)margin 
```


__功能__


设置仪表盘的边距

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id  |
| margin | TXEdgeInsets | 仪表盘内边距，注意这里是基于parentView的百分比，margin的取值范围是0 |

__介绍__

必须在 showDebugView 调用前设置才会生效         

<br/>

### getSDKVersion
```
 + (NSString *)getSDKVersion
```


__功能__


获取SDK版本信息         

<br/>

### setLogLevel
```
 + (void)setLogLevel:(TRTCLogLevel)level 
```


__功能__


设置log输出级别         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | TRTCLogLevel | 参见 TRTCLogLevel  |

<br/>

### setConsoleEnabled
```
 + (void)setConsoleEnabled:(BOOL)enabled 
```


__功能__


启用或禁用控制台日志打印         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | BOOL | 指定是否启用  |

<br/>

### setLogCompressEnabled
```
 + (void)setLogCompressEnabled:(BOOL)enabled 
```


__功能__


启用或禁用Log的本地压缩。。

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | BOOL | 指定是否启用  |

__介绍__

开启压缩后，log存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读 禁用压缩后，log采用明文存储，可以直接用记事本打开阅读，但占用空间较大。。

<br/>

### setLogDirPath
```
 + (void)setLogDirPath:(NSString *)path 
```


__功能__


修改日志保存路径

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 存储日志路径  |

__说明__

默认保存在 sandbox Documents/log 下，如需修改, 必须在所有方法前调用 

<br/>

### setLogDelegate
```
 + (void)setLogDelegate:(id< TRTCLogDelegate >)logDelegate 
```


__功能__


设置日志回调         

<br/>


## 属性列表
### delegate
```
@property (weak) id< TRTCCloudDelegate > delegate;
```

设置回调接口 TRTCCloudDelegate，用户获得来自 
### delegateQueue
```
@property (strong) dispatch_queue_t delegateQueue;
```

设置驱动回调的队列，默认会采用 Main Queue。 也就是说，如果您不指定 delegateQueue，那么直接在 TRTCCloudDelegate 的回调函数中操作 UI 界面将是安全的 


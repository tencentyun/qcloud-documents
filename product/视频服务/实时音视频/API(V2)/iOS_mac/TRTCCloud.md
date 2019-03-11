## 创建与销毁

### sharedInstance

创建 TRTCCloud 单例。

```
 + (instancetype)sharedInstance
```




### destroySharedIntance

销毁 TRTCCloud 单例。

```
 + (void)destroySharedIntance
```





## 房间相关接口函数

### enterRoom

进入房间。

```
 - (void)enterRoom:(TRTCParams *)param appScene:(TRTCAppScene)scene
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCParams * | 进房参数，请参考 TRTCParams |
| scene | TRTCAppScene | 应用场景，目前支持视频通话（VideoCall）和在线直播（Live）两种场景 |

__说明__


不管进房是否成功，都必须与 exitRoom 配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。





### exitRoom

离开房间。

```
 - (void)exitRoom
```





## 视频相关接口函数

### startLocalPreview

开启本地视频的预览画面（iOS 版本）。

```
 - (void)startLocalPreview:(BOOL)frontCamera view:(TXView *)view
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frontCamera | BOOL | YES：前置摄像头；NO：后置摄像头 |
| view | TXView * | 承载预览画面的控件所在的父控件 |




### startLocalPreview

开启本地视频的预览画面（Mac 版本）。

```
 - (void)startLocalPreview:(TXView *)view
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| view | TXView * | 指定渲染控件所在的父控件，SDK 会在 view 内部创建一个等大的子控件用来渲染本地摄像头的视频画面 |

__说明__


在调用该方法前，请先调用 setCurrentCameraDevice 选择使用 Mac 自带的摄像头还是外接摄像头。





### stopLocalPreview

停止本地视频采集及预览。

```
 - (void)stopLocalPreview
```




### startRemoteView

启动渲染远端视频画面。

```
 - (void)startRemoteView:(NSString *)userId view:(TXView *)view
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |
| view | TXView * | 指定渲染控件所在的父控件，SDK 会在 view 内部创建一个等大的子控件用来渲染远端画面 |

__说明__


在 onUserVideoAvailable 回调时，调用这个接口。





### stopRemoteView

停止渲染远端视频画面。

```
 - (void)stopRemoteView:(NSString *)userId
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |




### stopAllRemoteView

停止渲染远端视频画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭。

```
 - (void)stopAllRemoteView
```




### muteLocalVideo

是否屏蔽本地视频。

```
 - (void)muteLocalVideo:(BOOL)mute
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES：屏蔽；NO：开启 |

__介绍__


当屏蔽本地视频后，房间里的其它成员将会收到 onUserVideoAvailable 回调通知。





### setVideoEncoderParam

设置视频编码器相关参数，该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。

```
 - (void)setVideoEncoderParam:(TRTCVideoEncParam *)param
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCVideoEncParam * | 视频编码参数，详情请参考 TRTCCloudDef.h 中的 TRTCVideoEncParam 定义 |




### setNetworkQosParam

设置网络流控相关参数，该设置决定了 SDK 在各种网络环境下的调控策略（比如弱网下是“保清晰”还是“保流畅”）。

```
 - (void)setNetworkQosParam:(TRTCNetworkQosParam *)param
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCNetworkQosParam * | 网络流控参数，详情请参考 TRTCCloudDef.h 中的 TRTCNetworkQosParam 定义 |




### setLocalViewFillMode

设置本地图像的渲染模式。

```
 - (void)setLocalViewFillMode:(TRTCVideoFillMode)mode
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |




### setRemoteViewFillMode

设置远端图像的渲染模式。

```
 - (void)setRemoteViewFillMode:(NSString *)userId mode:(TRTCVideoFillMode)mode
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的 ID |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |




### setLocalViewRotation

设置本地图像的顺时针旋转角度。

```
 - (void)setLocalViewRotation:(TRTCVideoRotation)rotation
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持90、180、270旋转角度 |




### setRemoteViewRotation

设置远端图像的顺时针旋转角度。

```
 - (void)setRemoteViewRotation:(NSString *)userId rotation:(TRTCVideoRotation)rotation
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户 ID |
| rotation | TRTCVideoRotation | 支持90、180、270旋转角度 |




### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。

```
 - (void)setVideoEncoderRotation:(TRTCVideoRotation)rotation
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持0和180两个旋转角度 |




### setGSensorMode

设置重力感应的适应模式。

```
 - (void)setGSensorMode:(TRTCGSensorMode)mode
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCGSensorMode | 重力感应模式，详情请参考 TRTCGSensorMode 的定义 |




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


如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式。开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源。对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面；如果有些人的下行网络不好，可以选择观看【低清】画面。





### setRemoteVideoStreamType

选定观看指定 uid 的大画面还是小画面。

```
 - (void)setRemoteVideoStreamType:(NSString *)userId type:(TRTCVideoStreamType)type
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的 uid |
| type | TRTCVideoStreamType | 视频流类型，即选择看大画面还是小画面 |

__介绍__


此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式。如果该 uid 没有开启双路编码模式，则此操作无效。





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


低端设备推荐优先选择低清晰度的小画面。如果对方没有开启双路视频模式，则此操作无效。





### setLocalVideoMirror

设置摄像头本地预览是否开镜像。

```
 - (void)setLocalVideoMirror:(BOOL)mirror
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mirror | BOOL | 是否开启预览镜像 |





## 音频相关接口函数

### startLocalAudio

开启本地音频流，该函数会启动麦克风采集，并将音频数据广播给房间里的其他用户。

```
 - (void)startLocalAudio
```

__说明__


TRTC SDK 并不会默认打开本地的麦克风采集。
该函数会检查麦克风使用权限，如果没有麦克风权限，SDK 会向用户申请开启。





### stopLocalAudio

关闭本地音频流。

```
 - (void)stopLocalAudio
```




### muteLocalAudio

是否屏蔽本地音频。

```
 - (void)muteLocalAudio:(BOOL)mute
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES：屏蔽；NO：开启 |

__介绍__


当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知。





### setAudioRoute

设置音频路由。

```
 - (void)setAudioRoute:(TRTCAudioRoute)route
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | TRTCAudioRoute | 音频路由即声音由哪里输出（扬声器、听筒） |




### muteRemoteAudio

设置指定用户是否静音。

```
 - (void)muteRemoteAudio:(NSString *)userId mute:(BOOL)mute
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |
| mute | BOOL | YES：静音；NO：非静音 |




### muteAllRemoteAudio

设置所有远端用户是否静音。

```
 - (void)muteAllRemoteAudio:(BOOL)mute
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | BOOL | YES：静音；NO：非静音 |




### enableAudioVolumeEvaluation

启用音量大小提示。

```
 - (void)enableAudioVolumeEvaluation:(NSUInteger)interval smooth:(NSInteger)smoothLevel
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | NSUInteger | 报告间隔单位为ms，最小间隔20ms，如果小于等于0则会关闭回调，建议设置为大于200ms |
| smoothLevel | NSInteger | 灵敏度，[0,10]，数字越大，波动越灵敏 |

__介绍__


开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估。






## 摄像头相关接口函数

### switchCamera

切换摄像头。

```
 - (void)switchCamera
```




### isCameraZoomSupported

查询当前摄像头是否支持缩放。

```
 - (BOOL)isCameraZoomSupported
```




### setZoom

设置摄像头缩放因子（焦距）。

```
 - (void)setZoom:(CGFloat)distance
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| distance | CGFloat | 取值范围1 - 5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清 |




### isCameraTorchSupported

查询是否支持手电筒模式。

```
 - (BOOL)isCameraTorchSupported
```




### enbaleTorch

开关闪光灯。

```
 - (BOOL)enbaleTorch:(BOOL)enable
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | YES：开启；NO：关闭 |




### isCameraFocusPositionInPreviewSupported

查询是否支持设置焦点。

```
 - (BOOL)isCameraFocusPositionInPreviewSupported
```




### setFocusPosition

设置摄像头焦点。

```
 - (void)setFocusPosition:(CGPoint)touchPoint
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| touchPoint | CGPoint | 对焦位置 |




### isCameraAutoFocusFaceModeSupported

查询是否支持自动识别人脸位置。

```
 - (BOOL)isCameraAutoFocusFaceModeSupported
```




### enableAutoFaceFoucs

自动识别人脸位置。

```
 - (void)enableAutoFaceFoucs:(BOOL)enable
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | YES：打开；NO：关闭 |




### getCameraDevicesList

获取摄像头设备列表。

```
 - (NSArray< TRTCMediaDeviceInfo * > *)getCameraDevicesList
```




### getCurrentCameraDevice

获取当前要使用的摄像头。

```
 - (TRTCMediaDeviceInfo *)getCurrentCameraDevice
```




### setCurrentCameraDevice

设置要使用的摄像头。

```
 - (int)setCurrentCameraDevice:(NSString *)deviceId
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从 getCameraDevicesList 中得到的设备 ID |





## 音频设备相关接口函数

### getMicDevicesList

获取麦克风设备列表。

```
 - (NSArray< TRTCMediaDeviceInfo * > *)getMicDevicesList
```




### getCurrentMicDevice

获取当前的麦克风设备。

```
 - (TRTCMediaDeviceInfo *)getCurrentMicDevice
```




### setCurrentMicDevice

设置要使用的麦克风。

```
 - (int)setCurrentMicDevice:(NSString *)deviceId
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从 getMicDevicesList 中得到的设备 ID |




### getCurrentMicDeviceVolume

获取当前麦克风设备音量。

```
 - (float)getCurrentMicDeviceVolume
```




### setCurrentMicDeviceVolume

设置麦克风设备的音量。

```
 - (void)setCurrentMicDeviceVolume:(NSInteger)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 麦克风音量值，范围0 - 100 |




### getSpeakerDevicesList

获取扬声器设备列表。

```
 - (NSArray< TRTCMediaDeviceInfo * > *)getSpeakerDevicesList
```




### getCurrentSpeakerDevice

获取当前的扬声器设备。

```
 - (TRTCMediaDeviceInfo *)getCurrentSpeakerDevice
```




### setCurrentSpeakerDevice

设置要使用的扬声器。

```
 - (int)setCurrentSpeakerDevice:(NSString *)deviceId
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 从 getSpeakerDevicesList 中得到的设备 ID |




### getCurrentSpeakerDeviceVolume

当前扬声器设备音量。

```
 - (float)getCurrentSpeakerDeviceVolume
```




### setCurrentSpeakerDeviceVolume

设置当前扬声器音量。

```
 - (int)setCurrentSpeakerDeviceVolume:(NSInteger)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 设置的扬声器音量，范围0 - 100 |





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
| beautyLevel | NSInteger | 美颜级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显 |
| whitenessLevel | NSInteger | 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显 |
| ruddinessLevel | NSInteger | 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显 |




### setFilter

设置指定素材滤镜特效。

```
 - (void)setFilter:(TXImage *)image
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | TXImage * | 指定素材，即颜色查找表图片。注意：一定要用png格式！！！ |




### setFilterConcentration

设置滤镜浓度。

```
 - (void)setFilterConcentration:(float)concentration
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| concentration | float | 从0到1，越大滤镜效果越明显，默认值为0.5 |




### setWatermark

添加水印。

```
 - (void)setWatermark:(TXImage *)image streamType:(TRTCVideoStreamType)streamType rect:(CGRect)rect
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| image | TXImage * | 水印图片 |
| streamType | TRTCVideoStreamType | (TRTCVideoStreamTypeBig、TRTCVideoStreamTypeSub) |
| rect | CGRect | 水印相对于编码分辨率的归一化坐标，x，y，width，height，取值范围0 - 1；height 不用设置，sdk 内部会根据水印宽高比自动计算 height |





## 辅流相关接口函数(MAC)

### startRemoteSubStreamView

开始渲染远端用户辅流画面。对应于 startRemoteView() 用于观看远端的主路画面，该接口只能用于观看辅路（屏幕分享、远程播片）画面。

```
 - (void)startRemoteSubStreamView:(NSString *)userId view:(TXView *)view
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |
| view | TXView * | 渲染控件所在的父控件 |

__说明__


在 onUserSubStreamAvailable 回调时，调用这个接口。





### stopRemoteSubStreamView

停止渲染远端用户屏幕分享画面。

```
 - (void)stopRemoteSubStreamView:(NSString *)userId
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 对方的用户标识 |




### setRemoteSubStreamViewFillMode

设置辅流画面的渲染模式。对应于setRemoteViewFillMode() 于设置远端的主路画面，该接口用于设置远端的辅路（屏幕分享、远程播片）画面。

```
 - (void)setRemoteSubStreamViewFillMode:(NSString *)userId mode:(TRTCVideoFillMode)mode
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户的 ID |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |




### getScreenCaptureSourcesWithThumbnailSize

【屏幕共享】枚举可用的屏幕分享窗口。

```
 - (NSArray< TRTCScreenCaptureSourceInfo * > *)getScreenCaptureSourcesWithThumbnailSize:(CGSize)thumbnailSize iconSize:(CGSize)iconSize
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| thumbnailSize | CGSize |  指定要获取的窗口缩略图大小，缩略图可用于绘制在窗口选择界面上 |
| iconSize | CGSize |  指定要获取的窗口图标大小 |




### selectScreenCaptureTarget

【屏幕共享】设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。

```
 - (void)selectScreenCaptureTarget:(TRTCScreenCaptureSourceInfo *)screenSource rect:(CGRect)rect capturesCursor:(BOOL)capturesCursor highlight:(BOOL)highlight
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| screenSource | TRTCScreenCaptureSourceInfo * | 指定分享源 |
| rect | CGRect | 指定捕获的区域（传 CGRectZero 则默认分享全屏）|
| capturesCursor | BOOL | 是否捕获鼠标光标 |
| highlight | BOOL | 是否高亮正在分享的窗口 |




### startScreenCapture

【屏幕共享】启动屏幕分享。

```
 - (void)startScreenCapture:(NSView *)view
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| view | NSView * | 渲染控件所在的父控件 |




### stopScreenCapture

【屏幕共享】停止屏幕采集。

```
 - (int)stopScreenCapture
```




### pauseScreenCapture

【屏幕共享】暂停屏幕分享。

```
 - (int)pauseScreenCapture
```




### resumeScreenCapture

【屏幕共享】恢复屏幕分享。

```
 - (int)resumeScreenCapture
```




### setSubStreamEncoderParam

设置辅路视频编码器参数，对应于 setVideoEncoderParam() 设置主路画面的编码质量。该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。

```
 - (void)setSubStreamEncoderParam:(TRTCVideoEncParam *)param
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCVideoEncParam * | 辅流编码参数，详情请参考 TRTCCloudDef.h 中的 TRTCVideoEncParam 定义 |




### setSubStreamMixVolume

设置辅流的混音音量大小，这个数值越高，辅流音量占比就越高，麦克风音量占比就越小。

```
 - (void)setSubStreamMixVolume:(NSInteger)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 设置的音量大小，范围[0,100] |





## 自定义采集和渲染

### enableCustomVideoCapture

启用视频自定义采集模式，即放弃 SDK 原来的视频采集流程，改用 sendCustomVideoData 向 SDK 塞入自己采集的视频画面。

```
 - (void)enableCustomVideoCapture:(BOOL)enable
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | BOOL | 是否启用 |




### sendCustomVideoData

发送自定义的 SampleBuffer。

```
 - (void)sendCustomVideoData:(TRTCVideoFrame *)frame
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCVideoFrame * | 视频数据，仅支持 PixelBuffer I420 数据 |

__说明__


SDK 内部不做帧率控制，请务必保证调用该函数的频率和 TXLivePushConfig 中设置的帧率一致，否则编码器输出的码率会不受控制。





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
| bufferType | TRTCVideoBufferType | SDK 为了提高回调性能，提供了两种 PixelBuffer 格式，一种是 iOS 原始的 (TRTCVideoBufferType_PixelBuffer)，一种是经过内存整理的 (TRTCVideoBufferType_NSData) |

__说明__


设置此方法后，SDK 内部会把采集到的数据回调出来，SDK 跳过自己原来的渲染流程，您需要自己完成画面的渲染。





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
| bufferType | TRTCVideoBufferType | SDK 为了提高回调性能，提供了两种 PixelBuffer 格式，一种是 iOS 原始的 (TRTCVideoBufferType_PixelBuffer)，一种是经过内存整理的 (TRTCVideoBufferType_NSData) |

__说明__


设置此方法后，SDK 内部会把远端的数据解码后回调出来，SDK 跳过自己原来的渲染流程，您需要自己完成画面的渲染。
setRemoteVideoRenderDelegate 之前需要调用 startRemoteView 来开启对应 userid 的视频画面，才有数据回调出来。





### callExperimentalAPI

调用实验性 API 接口。

```
 - (void)callExperimentalAPI:(NSString *)jsonStr
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| jsonStr | NSString * | 接口及参数描述的 json 字符串 |

__说明__


该接口用于调用一些实验性功能。






## 自定义消息发送

### sendCustomCmdMsg

发送自定义消息给房间内所有用户。

```
 - (BOOL)sendCustomCmdMsg:(NSInteger)cmdID data:(NSData *)data reliable:(BOOL)reliable ordered:(BOOL)ordered
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdID | NSInteger | 消息 ID，取值范围为1 - 10 |
| data | NSData * | 待发送的消息，最大支持1KB（1000字节）的数据大小 |
| reliable | BOOL | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传 |
| ordered | BOOL | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息 |

__说明__


>?限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息。
限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃。
限制3：每个客户端每秒最多能发送总计 8 KB 数据。





### sendSEIMsg

发送自定义消息给房间内所有用户。

```
 - (BOOL)sendSEIMsg:(NSData *)data repeatCount:(int)repeatCount
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| data | NSData * | 待发送的数据，最大支持 1kb（1000字节）的数据大小 |
| repeatCount | int | 发送数据次数 |

__说明__


>?限制1：数据在接口调用完后不会被即时发送出去，而是从下一帧视频帧开始带在视频帧中发送。
限制2：发送消息到房间内所有用户，每秒最多能发送 30 条消息 (与 sendCustomCmdMsg 共享限制)。
限制3：每个包最大为1KB，若发送大量数据，会导致视频码率增大，可能导致视频画质下降甚至卡顿 (与 sendCustomCmdMsg 共享限制).
限制4：每个客户端每秒最多能发送总计 8 KB 数据 (与 sendCustomCmdMsg 共享限制)。
限制5：若指定多次发送（repeatCount>1）,则数据会被带在后续的连续 repeatCount 个视频帧中发送出去，同样会导致视频码率增大。
限制6: 如果repeatCount>1,多次发送，接收消息 onRecvSEIMsg 回调也可能会收到多次相同的消息，需要去重 。






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




### stopBGM

停止播放背景音乐。

```
 - (void)stopBGM
```




### pauseBGM

暂停播放背景音乐。

```
 - (void)pauseBGM
```




### resumeBGM

继续播放背景音乐。

```
 - (void)resumeBGM
```




### getBGMDuration

获取音乐文件总时长，单位毫秒。

```
 - (NSInteger)getBGMDuration:(NSString *)path
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | NSString * | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长 |




### setBGMPosition

设置 BGM 播放进度。

```
 - (int)setBGMPosition:(NSInteger)pos
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | NSInteger | 单位毫秒 |




### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
 - (void)setMicVolumeOnMixing:(NSInteger)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 音量大小，100为正常音量，值为0 - 200 |




### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
 - (void)setBGMVolume:(NSInteger)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | NSInteger | 音量大小，100为正常音量，建议值为0 - 200，如果需要调大背景音量可以设置更大的值 |




### setReverbType

设置混响效果（目前仅 iOS）。

```
 - (void)setReverbType:(TRTCReverbType)reverbType
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reverbType | TRTCReverbType | 混响类型，详见 TXReverbType |




### setVoiceChangerType

设置变声类型（目前仅 iOS）。

```
 - (void)setVoiceChangerType:(TRTCVoiceChangerType)voiceChangerType
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| voiceChangerType | TRTCVoiceChangerType | 变声类型, 详见 TXVoiceChangerType |





## 设备和网络测试

### startSpeedTest

开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。

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


测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们选择最佳的服务器。同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络。
>!测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。





### stopSpeedTest

停止服务器测速。

```
 - (void)stopSpeedTest
```




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





### stopCameraDeviceTest

结束视频测试预览。

```
 - (void)stopCameraDeviceTest
```




### startMicDeviceTest

开始进行麦克风测试。该方法测试麦克风是否能正常工作，volume 的取值范围为0 - 100。

```
 - (void)startMicDeviceTest:(NSInteger)interval testEcho:(void(^)(NSInteger volume))testEcho
```




### stopMicDeviceTest

停止麦克风测试。

```
 - (void)stopMicDeviceTest
```




### startSpeakerDeviceTest

开始扬声器测试。该方法播放指定的音频文件测试播放设备是否能正常工作，如果能听到声音，说明播放设备能正常工作。

```
 - (void)startSpeakerDeviceTest:(NSString *)audioFilePath onVolumeChanged:(void(^)(NSInteger volume, BOOL isLastFrame))volumeBlock
```




### stopSpeakerDeviceTest

停止扬声器测试。

```
 - (void)stopSpeakerDeviceTest
```





## 混流转码并发布到CDN

### startPublishCDNStream

启动 CDN 发布：通过腾讯云将当前房间的音视频流发布到直播 CDN 上。

```
 - (void)startPublishCDNStream:(TRTCPublishCDNParam *)param
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | TRTCPublishCDNParam * | 请参考 TRTCCloudDef.h 中关于 TRTCPublishCDNParam 的介绍 |

__介绍__


由于 TRTC 的线路费用是按照时长收费的，并且房间容量有限（< 1000人） 当您有大规模并发观看的需求时，将房间里的音视频流发布到低成本高并发的直播 CDN 上是一种较为理想的选择。目前支持两种发布方案：
【1】需要您先调用 setMixTranscodingConfig 对多路画面进行混合，发布到 CDN 上的是混合之后的音视频流。
【2】发布当前房间里的各路音视频画面，每一路画面都有一个独立的地址，相互之间无影响。





### stopPublishCDNStream

停止 CDN 发布。

```
 - (void)stopPublishCDNStream
```




### setMixTranscodingConfig

启动（更新）云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。

```
 - (void)setMixTranscodingConfig:(TRTCTranscodingConfig *)config
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| config | TRTCTranscodingConfig * | 请参考 TRTCCloudDef.h 中关于 TRTCTranscodingConfig 的介绍，传入 null 表示取消云端混流转码 |

__介绍__


<pre>
【画面1】=> 解码 => =>
                        \
【画面2】=> 解码 =>  画面混合 => 编码 => 【混合后的画面】
                        /
【画面3】=> 解码 => =>
</pre>








## LOG 相关接口函数

### getSDKVersion

获取 SDK 版本信息。

```
 + (NSString *)getSDKVersion
```




### setLogLevel

设置 Log 输出级别。

```
 + (void)setLogLevel:(TRTCLogLevel)level
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | TRTCLogLevel | 参见 TRTCLogLevel |




### setConsoleEnabled

启用或禁用控制台日志打印。

```
 + (void)setConsoleEnabled:(BOOL)enabled
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | BOOL | 指定是否启用 |




### setLogCompressEnabled

启用或禁用 Log 的本地压缩。

```
 + (void)setLogCompressEnabled:(BOOL)enabled
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | BOOL | 指定是否启用 |

__介绍__


开启压缩后，Log 存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读。禁用压缩后，Log 采用明文存储，可以直接用记事本打开阅读，但占用空间较大。






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


默认保存在 sandbox Documents/log 下，如需修改，必须在所有方法前调用。





### setLogDelegate

设置日志回调。

```
 + (void)setLogDelegate:(id< TRTCLogDelegate >)logDelegate
```




### showDebugView

显示仪表盘。

```
 - (void)showDebugView:(NSInteger)showType
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | NSInteger | 0：不显示；1：显示精简版；2：显示全量版 |

__介绍__


仪表盘是状态统计和事件消息浮层view，方便调试。





### setDebugViewMargin

设置仪表盘的边距。

```
 - (void)setDebugViewMargin:(NSString *)userId margin:(TXEdgeInsets)margin
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id |
| margin | TXEdgeInsets | 仪表盘内边距，注意这里是基于 parentView 的百分比，margin的取值范围是0 - 1 |

__介绍__


必须在 showDebugView 调用前设置才会生效。






## 属性列表
### delegate

设置回调接口 TRTCCloudDelegate，用户获得来自 TRTCCloud 的各种状态通知。

```
@property (nonatomic, weak) id< TRTCCloudDelegate > delegate;
```



### delegateQueue

设置驱动回调的队列，默认会采用 Main Queue。 也就是说，如果您不指定 delegateQueue，那么直接在 TRTCCloudDelegate 的回调函数中操作 UI 界面将是安全的。

```
@property (nonatomic, strong) dispatch_queue_t delegateQueue;
```

## 创建与销毁

### getTRTCShareInstance

创建 TRTCCloud 单例。

```
ITRTCCloud* getTRTCShareInstance()
```

### destroyTRTCShareInstance
释放 ITRTCCloud 单例对象。

```
void destroyTRTCShareInstance()
```


## 设置 TRTCCloudCallback 回调

### addCallback

添加事件回调。

```
void addCallback(ITRTCCloudCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCCloudCallback * | 事件回调指针 |




### removeCallback

移除事件回调。

```
void removeCallback(ITRTCCloudCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCCloudCallback * | 事件回调指针 |





## 房间相关接口函数

### enterRoom

进入房间。

```
void enterRoom(const TRTCParams & params, TRTCAppScene scene)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCParams & | 进房参数，详情参考 TRTCParams 定义 |
| scene | TRTCAppScene | 应用场景，目前支持视频通话（VideoCall）和在线直播（Live）两种场景 |

__说明__


不管进房是否成功，都必须与 exitRoom 配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。





### exitRoom

退出房间。

```
void exitRoom()
```




### connectOtherRoom

开启跨房连麦。

```
void connectOtherRoom(const char * params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const char * | JSON 形式的参数 {"roomId":910,"userId":"userA","sign":"sign string ..."} |




### disconnectOtherRoom

关闭跨房连麦。

```
void disconnectOtherRoom()
```





## 视频相关接口函数

### startLocalPreview

启动本地摄像头采集和预览。

```
void startLocalPreview(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | 承载预览画面的 HWND |




### stopLocalPreview

关闭本地摄像头采集和预览。

```
void stopLocalPreview()
```




### startRemoteView

启动渲染远端用户视频画面。

```
void startRemoteView(const char * userId, HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |
| rendHwnd | HWND | 承载预览画面的窗口句柄 |

__说明__


在 onUserVideoAvailable 回调时，调用这个接口。





### stopRemoteView

停止渲染远端用户画面。

```
void stopRemoteView(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |




### stopAllRemoteView

停止渲染所有远端用户画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭。

```
void stopAllRemoteView()
```




### muteLocalVideo

是否屏蔽本地视频。

```
void muteLocalVideo(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | true：关闭视频上行</br>false：开启视频上行 |

__介绍__


当屏蔽或重新开启本地视频后，房间里的其它成员会收到 onUserVideoAvailable 回调通知。 
        





### setVideoEncoderParam

设置视频编码器相关参数，该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。

```
void setVideoEncoderParam(const TRTCVideoEncParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCVideoEncParam & | 视频编码参数，详情请参考 TRTCCloudDef.h 中 TRTCVideoEncParam 的定义 |




### setNetworkQosParam

设置网络流控相关参数，该设置决定了 SDK 在各种网络环境下的调控策略（比如弱网下是“保清晰”还是“保流畅”）。

```
void setNetworkQosParam(const TRTCNetworkQosParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCNetworkQosParam & | 网络流控参数，详情请参考 TRTCCloudDef.h 中 TRTCNetworkQosParam 的定义 |




### setLocalViewFillMode

设置本地图像的渲染模式。

```
void setLocalViewFillMode(TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |




### setRemoteViewFillMode

设置远端图像的渲染模式。

```
void setRemoteViewFillMode(const char * userId, TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |




### setLocalViewRotation

设置本地图像的顺时针旋转角度。

```
void setLocalViewRotation(TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持90、180以及270旋转角度 |




### setRemoteViewRotation

设置远端图像的顺时针旋转角度。

```
void setRemoteViewRotation(const char * userId, TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |
| rotation | TRTCVideoRotation | 支持90、180以及270旋转角度 |




### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。

```
void setVideoEncoderRotation(TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持90、180以及270旋转角度 |




### enableSmallVideoStream

开启大小画面双路编码模式。

```
void enableSmallVideoStream(bool enable, const TRTCVideoEncParam & smallVideoParam)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | bool | 是否开启小画面编码 |
| smallVideoParam | const TRTCVideoEncParam & | 小流的视频参数，必须和 setLocalVideoQuality 接口的 params 参数具有相同的宽高比，也就是分辨率宽度和高度比值相同 |

__介绍__


如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面。





### setRemoteVideoStreamType

选择某一路的画面质量：当网络不好时可以切换到低清晰度的小画面。

```
void setRemoteVideoStreamType(const char * userId, TRTCVideoStreamType type)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |
| type | TRTCVideoStreamType | 大小流类型 |

__介绍__


如果对方没有开启双路视频模式，则此操作无效。





### setPriorRemoteVideoStreamType

设定观看方优先选择的视频质量。

```
void setPriorRemoteVideoStreamType(TRTCVideoStreamType type)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| type | TRTCVideoStreamType | 默认大小流类型 |

__介绍__


低端设备推荐优先选择低清晰度的小画面 如果对方没有开启双路视频模式，则此操作无效。





### setLocalVideoMirror

设置摄像头本地预览是否开镜像。

```
void setLocalVideoMirror(bool mirror)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mirror | bool | 是否开启预览镜像 |





## 音频相关接口函数

### startLocalAudio

开启本地音频流，该函数会启动麦克风采集，并将音频数据广播给房间里的其他用户。

```
void startLocalAudio()
```

__说明__


TRTC SDK 并不会默认打开本地的麦克风采集。 





### stopLocalAudio

关闭本地音频流。

```
void stopLocalAudio()
```




### muteLocalAudio

是否屏蔽本地音频。

```
void muteLocalAudio(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | true：关闭音频上行</br>false：开启音频上行 |

__说明__


屏蔽或重新开启本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知。 





### muteRemoteAudio

屏蔽指定远端音频。

```
void muteRemoteAudio(const char * userId, bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户 ID |
| mute | bool | 开关 |




### muteAllRemoteAudio

远端所有用户全部静音。

```
void muteAllRemoteAudio(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | 开关 |




### enableAudioVolumeEvaluation

启用或关闭音量大小提示。

```
void enableAudioVolumeEvaluation(uint32_t interval, uint32_t smoothLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | uint32_t | 建议设置为大于200毫秒，最小不小于20毫秒, 设置为0表示关闭 |
| smoothLevel | uint32_t | 灵敏度，取值范围：0 - 10, 数字越大，波动越灵敏 |

__介绍__


开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估。






## 摄像头相关接口函数

### getCameraDevicesList

查询摄像头列表。

```
ITRTCDeviceCollection * getCameraDevicesList()
```

__说明__


如果 delete ITRTCDeviceCollection* 指针会编译错误，SDK 维护 ITRTCDeviceCollection 对象的生命周期。 
ITRTCDeviceCollection 对象的生命周期。 





### setCurrentCameraDevice

设置要使用的摄像头。

```
void setCurrentCameraDevice(const char * deviceId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | const char * | 摄像头 ID，getCameraDevicesList 接口获取得到 |




### getCurrentCameraDevice

获取当前使用的摄像头。

```
const char * getCurrentCameraDevice()
```





## 音频设备相关接口函数

### getMicDevicesList

查询麦克风列表。

```
ITRTCDeviceCollection * getMicDevicesList()
```

__说明__


如果delete ITRTCDeviceCollection\*指针会编译错误，SDK维护 ITRTCDeviceCollection 对象的生命周期。 


### setCurrentMicDevice

选择指定的麦克风作为录音设备，不调用该接口时，默认选择索引为0的麦克风。

```
void setCurrentMicDevice(const char * micId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| micId | const char * | 麦克风 ID，getMicDevicesList 接口查询获取 |




### getCurrentMicDevice

获取当前选择的麦克风。

```
const char * getCurrentMicDevice()
```




### getCurrentMicDeviceVolume

查询已选择麦克风的音量。

```
uint32_t getCurrentMicDeviceVolume()
```




### setCurrentMicDeviceVolume

设置已选择麦克风的音量。

```
void setCurrentMicDeviceVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，取值范围：0 - 100 |




### getSpeakerDevicesList

查询扬声器列表。

```
ITRTCDeviceCollection * getSpeakerDevicesList()
```

__说明__


如果delete ITRTCDeviceCollection\*指针会编译错误，SDK 维护 ITRTCDeviceCollection 对象的生命周期。 





### setCurrentSpeakerDevice

选择指定的扬声器作为音频播放的设备，不调用该接口时，默认选择索引为0的扬声器。

```
void setCurrentSpeakerDevice(const char * speakerId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| speakerId | const char * | 麦克风 ID，getSpeakerDevicesList 接口查询获取 |




### getCurrentSpeakerDevice

获取已选择的扬声器。

```
const char * getCurrentSpeakerDevice()
```




### getCurrentSpeakerVolume

查询已选择扬声器的音量，注意查询的不是系统扬声器的音量大小。         

```
uint32_t getCurrentSpeakerVolume()
```




### setCurrentSpeakerVolume

设置 SDK 播放的音量，注意设置的不是系统扬声器的音量大小。

```
void setCurrentSpeakerVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，取值范围：0 - 100 |





## 美颜相关接口函数

### setBeautyStyle

设置美颜、美白、红润。

```
void setBeautyStyle(TRTCBeautyStyle style, uint32_t beauty, uint32_t white, uint32_t ruddiness)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| style | TRTCBeautyStyle | 美颜风格 |
| beauty | uint32_t | 美颜级别，取值范围：0 - 9，0表示关闭，值越大，效果越明显 |
| white | uint32_t | 美白级别，取值范围：0 - 9，0表示关闭，值越大，效果越明显 |
| ruddiness | uint32_t | 红润级别，取值范围：0 - 9，0表示关闭，值越大，效果越明显，该参数暂未生效 |




### setWaterMark

设置水印。

```
void setWaterMark(TRTCVideoStreamType streamType, const char * srcData, TRTCWaterMarkSrcType srcType, uint32_t nWidth, uint32_t nHeight, float xOffset, float yOffset, float fWidthRatio)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| streamType | TRTCVideoStreamType | 要设置水印的流类型(TRTCVideoStreamTypeBig、TRTCVideoStreamTypeSub) |
| srcData | const char * | 水印图片源数据（传 NULL 表示去掉水印） |
| srcType | TRTCWaterMarkSrcType | 水印图片源数据类型（传 NULL 时忽略该参数） |
| nWidth | uint32_t | 水印图片像素宽度（源数据为文件路径时忽略该参数） |
| nHeight | uint32_t | 水印图片像素高度（源数据为文件路径时忽略该参数） |
| xOffset | float | 水印显示的左上角 x 轴偏移 |
| yOffset | float | 水印显示的左上角 y 轴偏移 |
| fWidthRatio | float | 水印显示的宽度占画面宽度比例（水印按该参数等比例缩放显示） |

__说明__


大小流暂未支持。






## 辅流相关接口函数

### startRemoteSubStreamView

开始渲染远端用户辅流画面，对应于 startRemoteView() 用于观看远端的主路画面，该接口只能用于观看辅路（屏幕分享、远程播片）画面。

```
void startRemoteSubStreamView(const char * userId, HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |
| rendHwnd | HWND | 承载预览画面的 HWND |

__说明__


在 onUserSubStreamAvailable 回调时，调用这个接口。





### stopRemoteSubStreamView

停止渲染远端用户辅流画面。

```
void stopRemoteSubStreamView(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |




### setRemoteSubStreamViewFillMode

设置辅流画面的渲染模式对应于setRemoteViewFillMode() 于设置远端的主路画面，该接口用于设置远端的辅路（屏幕分享、远程播片）画面。

```
void setRemoteSubStreamViewFillMode(const char * userId, TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户的 ID |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |




### getScreenCaptureSources

【屏幕共享】枚举可共享的窗口列表。

```
ITRTCScreenCaptureSourceList * getScreenCaptureSources(const SIZE & thumbSize, const SIZE & iconSize)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| thumbSize | const SIZE & | 指定要获取的窗口缩略图大小，缩略图可用于绘制在窗口选择界面上 |
| iconSize | const SIZE & | 指定要获取的窗口图标大小 |

__说明__


如果delete ITRTCScreenCaptureSourceList\*指针会编译错误，SDK维护 ITRTCScreenCaptureSourceList 对象的生命周期。 





### selectScreenCaptureTarget

【屏幕共享】选择要分享的目标窗口或目标区域。

```
void selectScreenCaptureTarget(const TRTCScreenCaptureSourceInfo & source, const RECT & captureRect, bool captureMouse, bool highlightWindow)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| source | const TRTCScreenCaptureSourceInfo & | 指定分享源 |
| captureRect | const RECT & | 指定捕获的区域 |
| captureMouse | bool | 指定是否捕获鼠标指针 |
| highlightWindow | bool | 指定是否高亮正在共享的窗口以及当捕获图像被遮挡时高亮遮挡窗口提示用户移走遮挡 |


source 从 getScreenCaptureSources 接口获取。
以下为四种场景对应参数说明：

1. 共享整个屏幕 : source.type 为 Screen，captureRect 设为 { 0, 0, 0, 0 }
2. 共享指定区域 : source.type 为 Screen，captureRect 设为非 NULL，比如 { 100, 100, 300, 300 }
3. 共享整个窗口 : source.type 为 Window，captureRect 设为 { 0, 0, 0, 0 }
4. 共享窗口区域 : source.type 为 Window，captureRect 设为非 NULL，比如 { 100, 100, 300, 300 }

__说明__


您可以在屏幕分享的过程中掉用该函数来切换目标窗口或者调整目标区域。





### startScreenCapture

【屏幕共享】启动屏幕分享。

```
void startScreenCapture(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | 承载预览画面的 HWND |



### pauseScreenCapture

【屏幕共享】暂停屏幕分享。

```
void pauseScreenCapture()
```




### resumeScreenCapture

【屏幕共享】恢复屏幕分享。

```
void resumeScreenCapture()
```




### stopScreenCapture

【屏幕共享】关闭屏幕分享。

```
void stopScreenCapture()
```




### setSubStreamEncoderParam

设置辅路视频编码器参数，对应于 setVideoEncoderParam() 设置主路画面的编码质量 该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。

```
void setSubStreamEncoderParam(const TRTCVideoEncParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCVideoEncParam & | 辅流编码参数，详情请参考 TRTCCloudDef.h 中的 TRTCVideoEncParam 定义 |




### setSubStreamMixVolume

设置辅流的混音音量大小，这个数值越高，辅流音量占比就约高，麦克风音量占比就越小。

```
void setSubStreamMixVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的混音音量大小，取值范围：0 - 100 |





## 自定义采集和渲染

### enableCustomVideoCapture

启用视频自定义采集模式，即放弃 SDK 原来的视频采集流程，改用 sendCustomVideoData 向 SDK 塞入自己采集的视频画面。

```
void enableCustomVideoCapture(bool enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | bool | 是否启用 |




### sendCustomVideoData

发送自定义的SampleBuffer。

```
void sendCustomVideoData(TRTCVideoFrame * frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCVideoFrame * | 视频数据，仅支持 PixelBuffer I420 数据 |

__说明__


SDK内部不做帧率控制,请务必保证调用该函数的频率和 setVideoEncoderParam 中设置的帧率一致,否则编码器输出的码率会不受控制。





### setLocalVideoRenderCallback

设置本地视频自定义渲染。

```
int setLocalVideoRenderCallback(TRTCVideoPixelFormat pixelFormat, TRTCVideoBufferType bufferType, ITRTCVideoRenderCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式 |
| bufferType | TRTCVideoBufferType | 指定视频数据结构类型 |
| callback | ITRTCVideoRenderCallback * | 自定义渲染回调 |

__说明__


设置此方法，SDK 内部会把采集到的数据回调出来，SDK 跳过 HWND 渲染逻辑 调用 setLocalVideoRenderCallback(TRTCVideoPixelFormat_Unknown, TRTCVideoBufferType_Unknown, nullptr) 停止回调。





### setRemoteVideoRenderCallback

设置远端视频自定义渲染。

```
int setRemoteVideoRenderCallback(const char * userId, TRTCVideoPixelFormat pixelFormat, TRTCVideoBufferType bufferType, ITRTCVideoRenderCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式 |
| bufferType | TRTCVideoBufferType | 指定视频数据结构类型 |
| callback | ITRTCVideoRenderCallback * | 自定义渲染回调 |

__说明__


设置此方法，SDK 内部会把远端的数据解码后回调出来，SDK 跳过 HWND 渲染逻辑 调用 setRemoteVideoRenderCallback(userid,TRTCVideoPixelFormat_Unknown, TRTCVideoBufferType_Unknown, nullptr) 停止回调。 





### setAudioFrameCallback

设置音频数据的相关回调。

```
int setAudioFrameCallback(ITRTCAudioFrameCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCAudioFrameCallback * | 声音帧数据（PCM 格式）的回调 |

__说明__


设置此方法，SDK内部会把声音模块的数据（PCM 格式）回调出来，包括：
1. 本地麦克风录制的到的声音
2. 每一路远程用户的声音
3. 混合后的要送往喇叭进行播放的声音
本地麦克风录制的到的声音每一路远程用户的声音混合后的要送往喇叭进行播放的声音 调用 setAudioFrameCallback(nullptr) 停止回调。

### callExperimentalAPI

调用实验性 API 接口。

```
void callExperimentalAPI(const char * jsonStr)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| jsonStr | const char * | 接口及参数描述的 JSON 字符串 |

__说明__


该接口用于调用一些实验性功能。






## 自定义消息发送

### sendCustomCmdMsg

发送自定义消息给房间内所有用户。

```
bool sendCustomCmdMsg(uint32_t cmdId, const uint8_t * data, uint32_t dataSize, bool reliable, bool ordered)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdId | uint32_t | 消息 ID，取值范围：1 - 10 |
| data | const uint8_t * | 待发送的数据，最大支持1KB（1000字节）的数据大小 |
| dataSize | uint32_t | 待发送的数据大小 |
| reliable | bool | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传 |
| ordered | bool | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息 |

>?限制1：发送消息到房间内所有用户，每秒最多能发送30条消息 
>限制2：每个包最大为1KB，超过则很有可能会被中间路由器或者服务器丢弃
>限制3：每个客户端每秒最多能发送总计8KB数据。

请将 reliable 和 ordered 同时设置为 YES 或 NO, 暂不支持交叉设置。
有序性（ordered）是指相同 cmdID 的消息流一定跟发送方的发送顺序相同，
强烈建议不同类型的消息使用不同的 cmdID，这样可以在要求有序的情况下减小消息时延。

### sendSEIMsg

发送自定义消息给房间内所有用户。

```
bool sendSEIMsg(const uint8_t * data, uint32_t dataSize, int32_t repeatCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| data | const uint8_t * | 待发送的数据，最大支持1kb（1000字节）的数据大小 |
| repeatCount | int32_t | 发送数据次数 |


>?限制1：数据在接口调用完后不会被即时发送出去，而是从下一帧视频帧开始带在视频帧中发送。
>限制2：发送消息到房间内所有用户，每秒最多能发送30条消息 (与 sendCustomCmdMsg 共享限制) 。
>限制2：每个包最大为1KB，若发送大量数据，会导致视频码率增大，可能导致视频画质下降甚至卡顿 (与 sendCustomCmdMsg 共享限制)。
>限制4：每个客户端每秒最多能发送总计8KB数据 (与 sendCustomCmdMsg 共享限制)。
>限制5：若指定多次发送（repeatCount>1）,则数据会被带在后续的连续 repeatCount 个视频帧中发送出去，同样会导致视频码率增大。
>限制6：如果repeatCount>1，多次发送，接收消息 onRecvSEIMsg 回调也可能会收到多次相同的消息，需要去重。






## 背景混音相关接口函数

### playBGM

播放背景音乐。

```
void playBGM(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 音乐文件路径 |




### stopBGM

停止播放背景音乐。

```
void stopBGM()
```




### pauseBGM

暂停播放背景音乐。

```
void pauseBGM()
```




### resumeBGM

继续播放背景音乐。

```
void resumeBGM()
```




### getBGMDuration

获取音乐文件总时长，单位毫秒。

```
uint32_t getBGMDuration(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长 |




### setBGMPosition

设置 BGM 播放进度。

```
void setBGMPosition(uint32_t pos)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | uint32_t | 单位毫秒 |




### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
void setMicVolumeOnMixing(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量大小，100为正常音量，取值范围：0 - 200 |




### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
void setBGMVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量大小，100为正常音量，取值范围：0 - 200 |





## 设备和网络测试

### startSpeedTest

开始进行网络测速(视频通话期间请勿测试，以免影响通话质量)。

```
void startSpeedTest(uint32_t sdkAppId, const char * userId, const char * userSig)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sdkAppId | uint32_t | 应用标识 |
| userId | const char * | 用户标识 |
| userSig | const char * | 用户签名 |

__介绍__

打开后需要通过监听 ITRTCCloudCallback::onSpeedTest 回调获取测速结果
测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们选择最佳的服务器
同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络


__说明__


测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。





### stopSpeedTest

停止服务器测速。

```
void stopSpeedTest()
```




### startCameraDeviceTest

开启摄像头测试，会触发 onLocalVideoFrameAfterProcess 回调接口。

```
void startCameraDeviceTest(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | 承载预览画面的 HWND |




### stopCameraDeviceTest

停止摄像头测试。

```
void stopCameraDeviceTest()
```




### startMicDeviceTest

开启麦克风测试，回调接口 onTestMicVolume 获取测试数据。

```
void startMicDeviceTest(uint32_t interval)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | uint32_t | 反馈音量提示的时间间隔（ms），建议设置到大于200毫秒 |




### stopMicDeviceTest

关闭麦克风测试。

```
void stopMicDeviceTest()
```




### startSpeakerDeviceTest

开启扬声器测试，回调接口 onTestSpeakerVolume 获取测试数据。

```
void startSpeakerDeviceTest(const char * testAudioFilePath)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| testAudioFilePath | const char * | 音频文件的绝对路径，路径字符串使用 UTF-8 编码格式，支持文件格式: wav、mp3 |

__介绍__


该方法测试扬声器是否能正常工作。SDK 播放指定的音频文件，测试者如果能听到声音，说明播放设备能正常工作。
 




### stopSpeakerDeviceTest

停止扬声器测试。

```
void stopSpeakerDeviceTest()
```





## 混流转码并发布到CDN

### startPublishCDNStream

启动 CDN 发布：通过腾讯云将当前房间的音视频流发布到直播 CDN 上。

```
void startPublishCDNStream(const TRTCPublishCDNParam & param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | const TRTCPublishCDNParam & | 请参考 TRTCCloudDef.h 中关于 TRTCPublishCDNParam 的介绍 |

__介绍__


由于 TRTC 的线路费用是按照时长收费的，并且房间容量有限（< 1000人） 当您有大规模并发观看的需求时，将房间里的音视频流发布到低成本高并发的直播 CDN 上是一种较为理想的选择。
目前支持两种发布方案：
【1】需要您先调用 setMixTranscodingConfig 对多路画面进行混合，发布到 CDN 上的是混合之后的音视频流
【2】发布当前房间里的各路音视频画面，每一路画面都有一个独立的地址，相互之间无影响。





### stopPublishCDNStream

停止 CDN 发布。

```
void stopPublishCDNStream()
```




### setMixTranscodingConfig

启动(更新)云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。

```
void setMixTranscodingConfig(TRTCTranscodingConfig * config)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| config | TRTCTranscodingConfig * | 请参考 TRTCCloudDef.h 中关于 TRTCTranscodingConfig 的介绍 传入 NULL 取消云端混流转码 |

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
const char * getSDKVersion()
```



### setLogLevel

设置 Log 输出级别。

```
void setLogLevel(TRTCLogLevel level)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | TRTCLogLevel | 参见 TRTCLogLevel |




### setConsoleEnabled

启用或禁用控制台日志打印。

```
void setConsoleEnabled(bool enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | bool | 指定是否启用 |




### setLogCompressEnabled

启用或禁用 Log 的本地压缩。

```
void setLogCompressEnabled(bool enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | bool | 指定是否启用 |

__介绍__


开启压缩后，Log 存储体积明显减小，但需要腾讯云提供的 Python 脚本解压后才能阅读 禁用压缩后，Log 采用明文存储，可以直接用记事本打开阅读，但占用空间较大。 
        





### setLogDirPath

设置日志保存路径。

```
void setLogDirPath(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 存储日志的文件夹，例如 "D:\\Log"，utf-8 编码 |




### setLogCallback

设置日志回调。

```
void setLogCallback(ITRTCLogCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCLogCallback * | 日志回调 |




### showDebugView

显示仪表盘（状态统计和事件消息浮层 view），方便调试。

```
void showDebugView(int showType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | int | 0：不显示；1：显示精简版；2：显示全量版 |







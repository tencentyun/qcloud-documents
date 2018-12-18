## 设置 TRTCCloudCallback 回调

### addCallback
```
void addCallback(ITRTCCloudCallback * callback)
```


__功能__


添加事件回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCCloudCallback * | 事件回调  |

<br/>

### removeCallback
```
void removeCallback(ITRTCCloudCallback * callback)
```


__功能__


移除事件回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCCloudCallback * | 事件回调  |

<br/>


## 房间相关接口函数

### enterRoom
```
void enterRoom(const TRTCParams & params)
```


__功能__


进入房间         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCParams & | 进房参数，请参考 DOC-TO-DO  |

__说明__

不管进房是否成功，都必须与exitRoom配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题 

<br/>

### exitRoom
```
void exitRoom()
```


__功能__


退出房间         

<br/>


## 视频相关接口函数

### startLocalPreview
```
void startLocalPreview(HWND rendHwnd)
```


__功能__


启动本地摄像头采集和预览         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | 承载预览画面的 HWND  |

<br/>

### stopLocalPreview
```
void stopLocalPreview()
```


__功能__


关闭本地摄像头采集和预览         

<br/>

### startRemoteView
```
void startRemoteView(const char * userId, HWND rendHwnd)
```


__功能__


开始渲染远端用户画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识  |
| rendHwnd | HWND | - 承载预览画面的 HWND  |

<br/>

### stopRemoteView
```
void stopRemoteView(const char * userId)
```


__功能__


停止渲染远端用户画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识  |

<br/>

### stopAllRemoteView
```
void stopAllRemoteView()
```


__功能__


停止渲染所有远端用户画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭         

<br/>

### setLocalVideoQuality
```
void setLocalVideoQuality(const TRTCVideoEncParam & params, TRTCQosMode qosMode, TRTCVideoQosPreference qosPreference)
```


__功能__


设置画面质量参数         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCVideoEncParam & | 视频编码参数，详情请参考 TRTCCloudDef.h 中的  |
| qosMode | TRTCQosMode | 流控模式选择，默认选择【云控】模式，便于获得更好的效果，【终端】模式则用于特殊的调试场景  |
| qosPreference | TRTCVideoQosPreference | 画面质量偏好，有【流畅】和【清晰】两种模式可供选择，详情请参考 TRTCVideoQosPreference 的定义  |

<br/>

### muteLocalVideo
```
void muteLocalVideo(bool mute)
```


__功能__


是否屏蔽本地视频         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | true: 屏蔽视频采集和上行，false: 开启视频采集和上行  |

__介绍__

当屏幕本地视频后，房间里的其它成员会收到 onUserVideoAvailable 回调通知         

<br/>

### setLocalViewFillMode
```
void setLocalViewFillMode(TRTCVideoFillMode mode)
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
void setRemoteViewFillMode(const char * userId, TRTCVideoFillMode mode)
```


__功能__


设置远端图像的渲染模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识  |
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边）  |

<br/>

### setLocalViewRotation
```
void setLocalViewRotation(TRTCVideoRotation rotation)
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
void setRemoteViewRotation(const char * userId, TRTCVideoRotation rotation)
```


__功能__


设置远端图像的顺时针旋转角度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识  |
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度  |

<br/>

### setVideoOutputRotation
```
void setVideoOutputRotation(TRTCVideoRotation rotation)
```


__功能__


设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度  |

<br/>

### enableSmallVideoStream
```
void enableSmallVideoStream(bool enable, const TRTCVideoEncParam & smallVideoParam)
```


__功能__


开启大小画面双路编码模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | bool | 是否开启小画面编码  |
| smallVideoParam | const TRTCVideoEncParam & | 小流的视频参数，必须和 setLocalVideoQuality 接口的params参数具有相同的宽高比，也就是分辨率宽度和高度比值相同  |

__介绍__

如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面         

<br/>

### setRemoteVideoStreamType
```
void setRemoteVideoStreamType(const char * userId, TRTCVideoStreamType type)
```


__功能__


选择某一路的画面质量：当网络不好时可以切换到低清晰度的小画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识  |
| type | TRTCVideoStreamType | 大小流类型  |

__介绍__

如果对方没有开启双路视频模式，则此操作无效         

<br/>

### setPriorRemoteVideoStreamType
```
void setPriorRemoteVideoStreamType(TRTCVideoStreamType type)
```


__功能__


设定观看方优先选择的视频质量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| type | TRTCVideoStreamType | 默认大小流类型  |

__介绍__

低端设备推荐优先选择低清晰度的小画面 如果对方没有开启双路视频模式，则此操作无效         

<br/>


## 音频相关接口函数

### muteLocalAudio
```
void muteLocalAudio(bool mute)
```


__功能__


是否屏蔽本地音频         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | true: 关闭音频采集和上行 false: 开启音频采集以及音频上行  |

__说明__

当屏蔽本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知 

<br/>

### muteRemoteAudio
```
void muteRemoteAudio(const char * userId, bool mute)
```


__功能__


屏蔽指定远端音频         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户id  |
| mute | bool | 开关  |

<br/>

### muteAllRemoteAudio
```
void muteAllRemoteAudio(bool mute)
```


__功能__


远端所有用户全部静音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | 开关  |

<br/>

### enableAudioVolumeEvaluation
```
void enableAudioVolumeEvaluation(uint32_t interval, uint32_t smoothLevel)
```


__功能__


启用或关闭音量大小提示         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | uint32_t | 建议设置为大于 200 毫秒，最小不小于 20 毫秒, 设置为 0 表示关闭  |
| smoothLevel | uint32_t | 灵敏度，[0,10], 数字越大，波动越灵敏  |

__介绍__

开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估         

<br/>


## 摄像头相关接口函数

### getCameraDevicesList
```
TXStringList getCameraDevicesList()
```


__功能__


查询摄像头列表         

<br/>

### setCurrentCameraDevice
```
void setCurrentCameraDevice(const char * deviceId)
```


__功能__


设置要使用的摄像头         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | const char * | 摄像头ID，getCameraDevicesList 接口获取得到  |

<br/>

### getCurrentCameraDevice
```
TXString getCurrentCameraDevice()
```


__功能__


获取当前使用的摄像头         

<br/>


## 音频设备相关接口函数

### getMicDevicesList
```
TXStringList getMicDevicesList()
```


__功能__


查询麦克风列表         

<br/>

### setCurrentMicDevice
```
void setCurrentMicDevice(const char * micId)
```


__功能__


选择指定的麦克风作为录音设备，不调用该接口时，默认选择索引为0的麦克风         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| micId | const char * | 麦克风Id，getMicDevicesList 接口查询获取  |

<br/>

### getCurrentMicDevice
```
TXString getCurrentMicDevice()
```


__功能__


获取当前选择的麦克风         

<br/>

### getCurrentMicDeviceVolume
```
uint32_t getCurrentMicDeviceVolume()
```


__功能__


查询已选择麦克风的音量         

<br/>

### setCurrentMicDeviceVolume
```
void setCurrentMicDeviceVolume(uint32_t volume)
```


__功能__


设置已选择麦克风的音量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，范围是[0, 100]  |

<br/>

### getSpeakerDevicesList
```
TXStringList getSpeakerDevicesList()
```


__功能__


查询扬声器列表         

<br/>

### setCurrentSpeakerDevice
```
void setCurrentSpeakerDevice(const char * speakerId)
```


__功能__


选择指定的扬声器作为音频播放的设备，不调用该接口时，默认选择索引为0的扬声器         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| speakerId | const char * | 麦克风Id，getSpeakerDevicesList 接口查询获取  |

<br/>

### getCurrentSpeakerDevice
```
TXString getCurrentSpeakerDevice()
```


__功能__


获取已选择的扬声器         

<br/>

### getCurrentSpeakerVolume
```
uint32_t getCurrentSpeakerVolume()
```


__功能__


查询已选择扬声器的音量，注意查询得到不是系统扬声器的音量大小         

<br/>

### setCurrentSpeakerVolume
```
void setCurrentSpeakerVolume(uint32_t volume)
```


__功能__


设置SDK播放的音量，注意设置的不是系统扬声器的音量大小         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，范围是[0, 100]  |

<br/>


## 美颜相关接口函数

### setBeautyStyle
```
void setBeautyStyle(TRTCBeautyStyle style, uint32_t beauty, uint32_t white, uint32_t ruddiness)
```


__功能__


设置美颜、美白、红润         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| style | TRTCBeautyStyle | 美颜风格  |
| beauty | uint32_t | 美颜级别，取值范围 0 - 9: 0表示关闭，值越大，效果越明显  |
| white | uint32_t | 美白级别，取值范围 0 - 9: 0表示关闭，值越大，效果越明显  |
| ruddiness | uint32_t | 红润级别，取值范围 0 - 9: 0表示关闭，值越大，效果越明显，该参数暂未生效  |

<br/>


## 屏幕采集共享操作

### startScreenCapture
```
void startScreenCapture(HWND rendHwnd, const RECT & rendRect, HWND captureHwnd, const RECT & captureRect, bool captureGLOrDXWindow)
```


__功能__


启动屏幕分享         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | - 承载预览画面的 HWND  |
| rendRect | const RECT & | - 指定视频图像在 HWND 上的渲染区域  |
| captureHwnd | HWND | - 指定分享源  |
| captureRect | const RECT & | - 指定捕获的区域  |
| captureGLOrDXWindow | bool | - 无法直接获取某些特殊窗口（openGL渲染的窗口）的画面，captureGLOrDXWindow 设为 true 时，通过截取屏幕区域 实现捕获窗口，默认设为 false 共享整个屏幕 : captureHwnd 设为 NULL，captureRect 设为 { 0, 0, 0, 0 }。 共享指定窗口 : captureHwnd 设为非 NULL，captureRect 设为需要的区域 共享指定区域 : captureHwnd 设为 NULL，captureRect 设为非 NULL  |

<br/>

### resetScreenCaptureRect
```
void resetScreenCaptureRect(const RECT & captureRect)
```


__功能__


更新采集区域         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| captureRect | const RECT & | 指定捕获的区域  |

<br/>

### stopScreenCapture
```
void stopScreenCapture()
```


__功能__


关闭屏幕分享         

<br/>


## 自定义音视频数据

### setLocalVideoRenderCallback
```
void setLocalVideoRenderCallback(ITRTCVideoRenderCallback * callback, TRTCVideoPixelFormat pixelFormat)
```


__功能__


设置本地视频自定义渲染         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCVideoRenderCallback * | 自定义渲染回调。  |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式。  |

__说明__

设置此方法，SDK内部会把采集到的数据回调出来，SDK跳过HWND渲染逻辑。 退房、setLocalVideoRenderCallback(null, x)，停止回调 

<br/>

### setRemoteVideoRenderCallback
```
void setRemoteVideoRenderCallback(ITRTCVideoRenderCallback * callback, const char * userId, TRTCVideoPixelFormat pixelFormat)
```


__功能__


设置远端视频自定义渲染         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCVideoRenderCallback * | 自定义渲染回调。  |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式。  |

__说明__

设置此方法，SDK内部会把远端的数据解码后回调出来，SDK跳过HWND渲染逻辑。 退房、setLocalVideoRenderCallback(null, x)、远端用户退房，停止回调。。

<br/>

### setAudioFrameProcessCallback
```
void setAudioFrameProcessCallback(TRTCAudioFrameFormat format, ITRTCAudioFrameProcessCallback * callback)
```


__功能__


设置音频数据回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| format | TRTCAudioFrameFormat | 音频的格式  |
| callback | ITRTCAudioFrameProcessCallback * | 音频回调，设置为NULL表示不需要回调音频  |

__介绍__

这个接口会触发 onCaptureAudioFrame、 onRemoteAudioFrameBeforeMixing 和 onRemoteAudioFrameAfterMixing 回调接口         

<br/>

### enableCustomVideoCapture
```
void enableCustomVideoCapture(bool enable)
```


__功能__


启用视频自定义采集模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | bool | 是否启用  |

<br/>

### sendCustomVideoData
```
void sendCustomVideoData(const char * userId, TRTCVideoFrame * frame)
```


__功能__


发送客户自定义的视频数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |
| frame | TRTCVideoFrame * | 视频帧数据  |

<br/>

### enableCustomAudioCapture
```
void enableCustomAudioCapture(bool enable)
```


__功能__


启用音频自定义采集模式         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | bool | 是否启用  |

<br/>

### sendCustomAudioData
```
void sendCustomAudioData(const char * pcmBuffer)
```


__功能__


发送客户自定义的音频PCM数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pcmBuffer | const char * | pcm音频数据  |

__介绍__

目前SDK只支持16位采样的PCM编码,如果是单声道,请保证传入的PCM长度为2048；如果是双声道,请保证传入的PCM长度为4096         

<br/>


## 自定义消息发送

### sendCustomCmdMsg
```
bool sendCustomCmdMsg(uint32_t cmdId, const uint8_t * data, uint32_t dataSize, bool reliable, bool ordered)
```


__功能__


发送自定义消息给房间内所有用户         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdId | uint32_t | 消息ID，取值范围为 1 ~ 10  |
| data | const uint8_t * | 待发送的数据，最大支持 1KB（1000字节）的数据大小  |
| dataSize | uint32_t | 待发送的数据大小  |
| reliable | bool | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传  |
| ordered | bool | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息  |

__说明__

限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息 限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃 限制3：每个客户端每秒最多能发送总计 8 KB 数据

<br/>


## 背景混音相关接口函数

### playBGM
```
void playBGM(const char * path)
```


__功能__


播放背景音乐         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 音乐文件路径  |

<br/>

### stopBGM
```
void stopBGM()
```


__功能__


停止播放背景音乐         

<br/>

### pauseBGM
```
void pauseBGM()
```


__功能__


暂停播放背景音乐         

<br/>

### resumeBGM
```
void resumeBGM()
```


__功能__


继续播放背景音乐         

<br/>

### getBGMDuration
```
uint32_t getBGMDuration(const char * path)
```


__功能__


获取音乐文件总时长，单位毫秒         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 音乐文件路径，如果path为空，那么返回当前正在播放的music时长  |

<br/>

### setBGMPosition
```
void setBGMPosition(uint32_t pos)
```


__功能__


设置BGM播放进度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | uint32_t | 单位毫秒  |

<br/>

### setMicVolumeOnMixing
```
void setMicVolumeOnMixing(uint32_t volume)
```


__功能__


设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，范围是[0, 100]  |

<br/>


## 设备和网络测试

### startSpeedTest
```
void startSpeedTest(uint32_t sdkAppId, const char * userId, const char * userSig)
```


__功能__


开始进行网络测速(视频通话期间请勿测试，以免影响通话质量)         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| sdkAppId | uint32_t | 应用标识  |
| userId | const char * | 用户标识  |
| userSig | const char * | 用户签名  |

__介绍__

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们最佳的服务器 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络
注意：测速本身会消耗一定的流量，所以也会产生少量额外的流量费用

<br/>

### stopSpeedTest
```
void stopSpeedTest()
```


__功能__


停止服务器测速         

<br/>

### startCameraDeviceTest
```
void startCameraDeviceTest(HWND rendHwnd)
```


__功能__


开启摄像头测速，会触发 onLocalVideoFrameAfterProcess 回调接口         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | 承载预览画面的 HWND  |

<br/>

### stopCameraDeviceTest
```
void stopCameraDeviceTest()
```


__功能__


停止摄像头测速         

<br/>

### startMicDeviceTest
```
void startMicDeviceTest(uint32_t interval)
```


__功能__


开启麦克风测试，回调接口 onTestMicVolume 获取视频数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | uint32_t | 反馈音量提示的时间间隔（ms），建议设置到大于 200 毫秒  |

<br/>

### stopMicDeviceTest
```
void stopMicDeviceTest()
```


__功能__


关闭麦克风测试         

<br/>

### startSpeakerDeviceTest
```
void startSpeakerDeviceTest(const char * testAudioFilePath)
```


__功能__


开启扬声器测试，回调接口 onTestSpeakerVolume 获取视频数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| testAudioFilePath | const char * | 音频文件的绝对路径，路径字符串使用 UTF-8 编码格式，支持文件格式: wav、mp3  |

__介绍__

该方法测试扬声器是否能正常工作。SDK播放指定的音频文件，测试者如果能听到声音，说明播放设备能正常工作         

<br/>

### stopSpeakerDeviceTest
```
void stopSpeakerDeviceTest()
```


__功能__


停止扬声器测试         

<br/>


## 调试相关函数

### getSDKVersion
```
TXString getSDKVersion()
```


__功能__


获取SDK版本信息         

<br/>

### setLogLevel
```
void setLogLevel(TRTCLogLevel level)
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
void setConsoleEnabled(bool enabled)
```


__功能__


启用或禁用控制台日志打印         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | bool | 指定是否启用  |

<br/>

### setLogCompressEnabled
```
void setLogCompressEnabled(bool enabled)
```


__功能__


启用或禁用Log的本地压缩         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | bool | 指定是否启用  |

__介绍__

开启压缩后，log存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读 禁用压缩后，log采用明文存储，可以直接用记事本打开阅读，但占用空间较大。。

<br/>

### setLogDirPath
```
void setLogDirPath(const char * path)
```


__功能__


设置日志保存路径         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 存储日志的文件夹，例如 "D:\\Log"，utf-8编码  |

<br/>

### setLogCallback
```
void setLogCallback(ITRTCLogCallback * callback)
```


__功能__


设置日志回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCLogCallback * | 日志回调  |

<br/>

### showDebugView
```
void showDebugView(int showType)
```


__功能__


显示仪表盘（状态统计和事件消息浮层view），方便调试         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | int | 0: 不显示 1: 显示精简版 2: 显示全量版  |

<br/>




## TRTCCloud
```
 TRTCCloud()
```

<br/>

## ~TRTCCloud
```
 ~TRTCCloud()
```

<br/>



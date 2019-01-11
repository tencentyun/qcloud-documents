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

<br/>


### removeCallback

移除事件回调。

```
void removeCallback(ITRTCCloudCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCCloudCallback * | 事件回调指针 |

<br/>



## 房间相关接口函数

### enterRoom

进入房间。

```
void enterRoom(const TRTCParams & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCParams & | 进房参数，详情参考TRTCParams定义。 |

__说明__


不管进房是否成功，都必须与exitRoom配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。


<br/>


### exitRoom

退出房间。

```
void exitRoom()
```

<br/>



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

<br/>


### stopLocalPreview

关闭本地摄像头采集和预览。

```
void stopLocalPreview()
```

<br/>


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

<br/>


### stopRemoteView

停止渲染远端用户画面。

```
void stopRemoteView(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |

<br/>


### stopAllRemoteView

停止渲染所有远端用户画面，如果有屏幕分享，则屏幕分享的画面也会一并被关闭。

```
void stopAllRemoteView()
```

<br/>


### muteLocalVideo

是否屏蔽本地视频。

```
void muteLocalVideo(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | true: 关闭视频上行，false: 开启视频上行 |

__介绍__


当屏蔽或重新开启本地视频后，房间里的其它成员会收到 onUserVideoAvailable 回调通知。 
        


<br/>


### setVideoEncoderParam

设置视频编码器相关参数，该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。

```
void setVideoEncoderParam(const TRTCVideoEncParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCVideoEncParam & | 视频编码参数，详情请参考 TRTCCloudDef.h 中的 TRTCVideoEncParam 定义 |

<br/>


### setNetworkQosParam

设置网络流控相关参数，该设置决定了SDK在各种网络环境下的调控策略（比如弱网下是“保清晰”还是“保流畅”）。

```
void setNetworkQosParam(const TRTCNetworkQosParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| params | const TRTCNetworkQosParam & | 网络流控参数，详情请参考 TRTCCloudDef.h 中的 TRTCNetworkQosParam 定义 |

<br/>


### setLocalViewFillMode

设置本地图像的渲染模式。

```
void setLocalViewFillMode(TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mode | TRTCVideoFillMode | 填充（画面可能会被拉伸裁剪）还是适应（画面可能会有黑边） |

<br/>


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

<br/>


### setLocalViewRotation

设置本地图像的顺时针旋转角度。

```
void setLocalViewRotation(TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度 |

<br/>


### setRemoteViewRotation

设置远端图像的顺时针旋转角度。

```
void setRemoteViewRotation(const char * userId, TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 远端用户标识 |
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度 |

<br/>


### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。

```
void setVideoEncoderRotation(TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rotation | TRTCVideoRotation | 支持 90、180、270 旋转角度 |

<br/>


### enableSmallVideoStream

开启大小画面双路编码模式。

```
void enableSmallVideoStream(bool enable, const TRTCVideoEncParam & smallVideoParam)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enable | bool | 是否开启小画面编码 |
| smallVideoParam | const TRTCVideoEncParam & | 小流的视频参数，必须和 setLocalVideoQuality 接口的params参数具有相同的宽高比，也就是分辨率宽度和高度比值相同 |

__介绍__


如果当前用户是房间中的主要角色（比如主播、老师、主持人...），并且使用 PC 或者 Mac 环境，可以开启该模式 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流） 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源 对于同一房间的远程观众而言， 如果有些人的下行网络很好，可以选择观看【高清】画面 如果有些人的下行网络不好，可以选择观看【低清】画面。


<br/>


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


<br/>


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


<br/>


### setLocalVideoMirror

设置摄像头本地预览是否开镜像。

```
void setLocalVideoMirror(bool mirror)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mirror | bool | 是否开启预览镜像 |

<br/>



## 音频相关接口函数

### startLocalAudio

开启本地音频流，该函数会启动麦克风采集，并将音频数据广播给房间里的其他用户。

```
void startLocalAudio()
```

__说明__


TRTC SDK 并不会默认打开本地的麦克风采集。 


<br/>


### stopLocalAudio

关闭本地音频流。

```
void stopLocalAudio()
```

<br/>


### muteLocalAudio

是否屏蔽本地音频。

```
void muteLocalAudio(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | true: 关闭音频上行 false: 开启音频上行 |

__说明__


屏蔽或重新开启本地音频后，房间里的其它成员会收到 onUserAudioAvailable 回调通知。 


<br/>


### muteRemoteAudio

屏蔽指定远端音频。

```
void muteRemoteAudio(const char * userId, bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户id |
| mute | bool | 开关 |

<br/>


### muteAllRemoteAudio

远端所有用户全部静音。

```
void muteAllRemoteAudio(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| mute | bool | 开关 |

<br/>


### enableAudioVolumeEvaluation

启用或关闭音量大小提示。

```
void enableAudioVolumeEvaluation(uint32_t interval, uint32_t smoothLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | uint32_t | 建议设置为大于 200 毫秒，最小不小于 20 毫秒, 设置为 0 表示关闭 |
| smoothLevel | uint32_t | 灵敏度，[0,10], 数字越大，波动越灵敏 |

__介绍__


开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估。


<br/>



## 摄像头相关接口函数

### getCameraDevicesList

查询摄像头列表。

```
TXStringList getCameraDevicesList()
```

<br/>


### setCurrentCameraDevice

设置要使用的摄像头。

```
void setCurrentCameraDevice(const char * deviceId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | const char * | 摄像头ID，getCameraDevicesList 接口获取得到 |

<br/>


### getCurrentCameraDevice

获取当前使用的摄像头。

```
TXString getCurrentCameraDevice()
```

<br/>



## 音频设备相关接口函数

### getMicDevicesList

查询麦克风列表。

```
TXStringList getMicDevicesList()
```

<br/>


### setCurrentMicDevice

选择指定的麦克风作为录音设备，不调用该接口时，默认选择索引为0的麦克风。

```
void setCurrentMicDevice(const char * micId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| micId | const char * | 麦克风Id，getMicDevicesList 接口查询获取 |

<br/>


### getCurrentMicDevice

获取当前选择的麦克风。

```
TXString getCurrentMicDevice()
```

<br/>


### getCurrentMicDeviceVolume

查询已选择麦克风的音量。

```
uint32_t getCurrentMicDeviceVolume()
```

<br/>


### setCurrentMicDeviceVolume

设置已选择麦克风的音量。

```
void setCurrentMicDeviceVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，范围是[0, 100] |

<br/>


### getSpeakerDevicesList

查询扬声器列表。

```
TXStringList getSpeakerDevicesList()
```

<br/>


### setCurrentSpeakerDevice

选择指定的扬声器作为音频播放的设备，不调用该接口时，默认选择索引为0的扬声器。

```
void setCurrentSpeakerDevice(const char * speakerId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| speakerId | const char * | 麦克风Id，getSpeakerDevicesList 接口查询获取 |

<br/>


### getCurrentSpeakerDevice

获取已选择的扬声器。

```
TXString getCurrentSpeakerDevice()
```

<br/>


### getCurrentSpeakerVolume

查询已选择扬声器的音量，注意查询的不是系统扬声器的音量大小。         

```
uint32_t getCurrentSpeakerVolume()
```

<br/>


### setCurrentSpeakerVolume

设置SDK播放的音量，注意设置的不是系统扬声器的音量大小。

```
void setCurrentSpeakerVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 设置的音量大小，范围是[0, 100] |

<br/>



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
| beauty | uint32_t | 美颜级别，取值范围 0 - 9: 0表示关闭，值越大，效果越明显 |
| white | uint32_t | 美白级别，取值范围 0 - 9: 0表示关闭，值越大，效果越明显 |
| ruddiness | uint32_t | 红润级别，取值范围 0 - 9: 0表示关闭，值越大，效果越明显，该参数暂未生效 |

<br/>



## 音视频自定义接口

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


设置此方法，SDK内部会把采集到的数据回调出来，SDK跳过HWND渲染逻辑 调用setLocalVideoRenderCallback(TRTCVideoPixelFormat_Unknown, TRTCVideoBufferType_Unknown, NULL)停止回调。


<br/>


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


设置此方法，SDK内部会把远端的数据解码后回调出来，SDK跳过HWND渲染逻辑 调用setRemoteVideoRenderCallback(userid,TRTCVideoPixelFormat_Unknown, TRTCVideoBufferType_Unknown, nullptr)停止回调。 


<br/>


### setLocalVideoPreprocessCallback

设置本地视频的二次加工回调。

```
void setLocalVideoPreprocessCallback(ITRTCVideoPreprocessCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCVideoPreprocessCallback * | 自定义渲染回调 |

__说明__


设置之后，SDK会在送编码器之前将该帧视频画面回调出来，供您进行二次图像加工（比如叠加字幕，角标等等），之后SDK会将处理后的画面送入编码器 
注意：由于该回调过程是同步的，所以请注意控制二次加工的时间，不宜超过 20ms，否则会导致画面卡顿 
setLocalVideoPreprocessCallback(null)可以停止回调。


<br/>



## 自定义消息发送

### sendCustomCmdMsg

发送自定义消息给房间内所有用户。

```
bool sendCustomCmdMsg(uint32_t cmdId, const uint8_t * data, uint32_t dataSize, bool reliable, bool ordered)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| cmdId | uint32_t | 消息ID，取值范围为 1 ~ 10 |
| data | const uint8_t * | 待发送的数据，最大支持 1KB（1000字节）的数据大小 |
| dataSize | uint32_t | 待发送的数据大小 |
| reliable | bool | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传 |
| ordered | bool | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息 |

__说明__


限制1：发送消息到房间内所有用户，每秒最多能发送 30 条消息 限制2：每个包最大为 1 KB，超过则很有可能会被中间路由器或者服务器丢弃 限制3：每个客户端每秒最多能发送总计 8 KB 数据。


<br/>



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

<br/>


### stopBGM

停止播放背景音乐。

```
void stopBGM()
```

<br/>


### pauseBGM

暂停播放背景音乐。

```
void pauseBGM()
```

<br/>


### resumeBGM

继续播放背景音乐。

```
void resumeBGM()
```

<br/>


### getBGMDuration

获取音乐文件总时长，单位毫秒。

```
uint32_t getBGMDuration(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 音乐文件路径，如果path为空，那么返回当前正在播放的music时长 |

<br/>


### setBGMPosition

设置BGM播放进度。

```
void setBGMPosition(uint32_t pos)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| pos | uint32_t | 单位毫秒 |

<br/>


### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
void setMicVolumeOnMixing(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量大小，100为正常音量，值为0~200 |

<br/>


### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
void setBGMVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量大小，100为正常音量，值为0~200 |

<br/>



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


监听 
注意：测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。


<br/>


### stopSpeedTest

停止服务器测速。

```
void stopSpeedTest()
```

<br/>


### startCameraDeviceTest

开启摄像头测试，会触发 onLocalVideoFrameAfterProcess 回调接口。

```
void startCameraDeviceTest(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| rendHwnd | HWND | 承载预览画面的 HWND |

<br/>


### stopCameraDeviceTest

停止摄像头测试。         

```
void stopCameraDeviceTest()
```

<br/>


### startMicDeviceTest

开启麦克风测试，回调接口 onTestMicVolume 获取测试数据。

```
void startMicDeviceTest(uint32_t interval)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| interval | uint32_t | 反馈音量提示的时间间隔（ms），建议设置到大于 200 毫秒 |

<br/>


### stopMicDeviceTest

关闭麦克风测试。

```
void stopMicDeviceTest()
```

<br/>


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


该方法测试扬声器是否能正常工作。SDK播放指定的音频文件，测试者如果能听到声音，说明播放设备能正常工作。


<br/>


### stopSpeakerDeviceTest

停止扬声器测试。

```
void stopSpeakerDeviceTest()
```

<br/>



## 混流转码并发布到CDN

### startPublishCDNStream

启动CDN发布：通过腾讯云将当前房间的音视频流发布到直播CDN上。

```
void startPublishCDNStream(const TRTCPublishCDNParam & param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| param | const TRTCPublishCDNParam & | 请参考 TRTCCloudDef.h 中关于 TRTCPublishCDNParam 的介绍 |

__介绍__


由于 TRTC 的线路费用是按照时长收费的，并且房间容量有限（< 1000人） 当您有大规模并发观看的需求时，将房间里的音视频流发布到低成本高并发的直播CDN上是一种较为理想的选择。
目前支持两种发布方案：
【1】先混流在发布，TRTCPublishCDNParam.enableTranscoding = YES 需要您先调用startCloudMixTranscoding对多路画面进行混合，发布到CDN上的是混合之后的音视频流
【2】不混流直接发布，TRTCPublishCDNParam.enableTranscoding = NO 发布当前房间里的各路音视频画面，每一路画面都有一个独立的地址，相互之间无影响，调用startCloudMixTranscoding将无效。


<br/>


### stopPublishCDNStream

停止CDN发布。

```
void stopPublishCDNStream()
```

<br/>


### startCloudMixTranscoding

启动云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。

```
void startCloudMixTranscoding(const TRTCTranscodingConfig & config)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| config | const TRTCTranscodingConfig & | 请参考 TRTCCloudDef.h 中关于 TRTCTranscodingConfig 的介绍 |

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
void stopCloudMixTranscoding()
```

<br/>



## 调试相关函数

### getSDKVersion

获取SDK版本信息。

```
TXString getSDKVersion()
```

<br/>


### setLogLevel

设置log输出级别。

```
void setLogLevel(TRTCLogLevel level)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| level | TRTCLogLevel | 参见 TRTCLogLevel |

<br/>


### setConsoleEnabled

启用或禁用控制台日志打印。

```
void setConsoleEnabled(bool enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | bool | 指定是否启用 |

<br/>


### setLogCompressEnabled

启用或禁用Log的本地压缩。

```
void setLogCompressEnabled(bool enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| enabled | bool | 指定是否启用 |

__介绍__


开启压缩后，log存储体积明显减小，但需要腾讯云提供的 python 脚本解压后才能阅读 禁用压缩后，log采用明文存储，可以直接用记事本打开阅读，但占用空间较大。 
        


<br/>


### setLogDirPath

设置日志保存路径。

```
void setLogDirPath(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| path | const char * | 存储日志的文件夹，例如 "D:\\Log"，utf-8编码 |

<br/>


### setLogCallback

设置日志回调。

```
void setLogCallback(ITRTCLogCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| callback | ITRTCLogCallback * | 日志回调 |

<br/>


### showDebugView

显示仪表盘（状态统计和事件消息浮层view），方便调试。

```
void showDebugView(int showType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| showType | int | 0: 不显示 1: 显示精简版 2: 显示全量版 |

<br/>







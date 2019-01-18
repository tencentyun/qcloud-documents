
__功能__


TRTCCloudDelegate 是 TRTCCloud 的主要回调接口。


<br/>

## 通用事件回调

### onError

错误回调: SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```
 - (void)onError:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码 |
| errMsg | nullable NSString * | 错误信息 |
| extInfo | nullable NSDictionary * | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题 |

<br/>


### onWarning

警告回调。

```
 - (void)onWarning:(TXLiteAVWarning)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | TXLiteAVWarning | 警告码 |
| warningMsg | nullable NSString * | 警告信息 |
| extInfo | nullable NSDictionary * | 扩展信息字段，个别警告码可能会带额外的信息帮助定位问题 |

<br/>



## 房间事件回调

### onEnterRoom

加入房间。

```
 - (void)onEnterRoom:(NSInteger)elapsed 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| elapsed | NSInteger | 加入房间耗时 |

<br/>


### onExitRoom

离开房间 离开房间成功的回调。

```
 - (void)onExitRoom:(NSInteger)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | NSInteger | 离开房间原因 |

<br/>



## 成员事件回调

### onUserEnter

成员进入房间事件。

```
 - (void)onUserEnter:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识 |

<br/>


### onUserExit

成员离开房间事件。

```
 - (void)onUserExit:(NSString *)userId reason:(NSInteger)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识 |
| reason | NSInteger | 离开原因代码 |

<br/>


### onUserVideoAvailable

成员屏蔽自己的画面。

```
 - (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识 |
| available | BOOL | 画面是否开启 |

<br/>


### onUserAudioAvailable

成员屏蔽自己的声音。

```
 - (void)onUserAudioAvailable:(NSString *)userId available:(BOOL)available 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识 |
| available | BOOL | 声音是否开启 |

<br/>


### onUserVoiceVolume

成员语音音量回调 通过调用 TRTCCloud enableAudioVolumeEvaluation:smooth: 来开关这个回调。

```
 - (void)onUserVoiceVolume:(NSArray< TRTCVolumeInfo * > *)userVolumes totalVolume:(NSInteger)totalVolume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | NSArray< TRTCVolumeInfo * > * | 每位发言者的语音音量，取值范围 0~100 |
| totalVolume | NSInteger | 总的语音音量, 取值范围 0~100 |

<br/>



## 统计和质量回调

### onNetworkQuality

网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid == nil 代表自己当前的视频质量。

```
 - (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray< TRTCQualityInfo * > *)remoteQuality 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCQualityInfo * | 上行网络质量 |
| remoteQuality | NSArray< TRTCQualityInfo * > * | 下行网络质量 |

<br/>


### onStatistics

技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调。

```
 - (void)onStatistics:(TRTCStatistics *)statistics 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statistics | TRTCStatistics * | 统计数据，包括本地和远程的 |

__说明__


每2秒回调一次。


<br/>



## 音视频事件回调

### onFirstVideoFrame

首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面。

```
 - (void)onFirstVideoFrame:(NSString *)userId width:(int)width height:(int)height 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户Id |
| width | int | 画面宽度 |
| height | int | 画面高度 |

<br/>


### onFirstAudioFrame

首帧音频数据到达。

```
 - (void)onFirstAudioFrame:(NSString *)userId 
```

<br/>



## 服务器事件回调

### onConnectionLost

SDK 跟服务器的连接断开。

```
 - (void)onConnectionLost
```

<br/>


### onTryToReconnect

SDK 尝试重新连接到服务器。

```
 - (void)onTryToReconnect
```

<br/>


### onConnectionRecovery

SDK 跟服务器的连接恢复。

```
 - (void)onConnectionRecovery
```

<br/>



## 硬件设备事件回调


### onCameraDidReady

摄像头准备就绪。

```
 - (void)onCameraDidReady
```

<br/>


### onMicDidReady

麦克风准备就绪。

```
 - (void)onMicDidReady
```

<br/>


### onAudioRouteChanged

音频路由发生变化(仅iOS)，音频路由即声音由哪里输出（扬声器、听筒）。

```
 - (void)onAudioRouteChanged:(TRTCAudioRoute)route fromRoute:(TRTCAudioRoute)fromRoute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | TRTCAudioRoute | 当前音频路由 |
| fromRoute | TRTCAudioRoute | 变更前的音频路由 |

<br/>


### onDevice

本地设备通断回调，。

```
 - (void)onDevice:(NSString *)deviceId type:(TRTCMediaDeviceType)deviceType stateChanged:(NSInteger)state 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 设备id |
| deviceType | TRTCMediaDeviceType | 设备类型 |

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| state | NSInteger | 0: 设备断开 1: 设备连接 |

<br/>



## 自定义消息的接收回调

### onRecvCustomCmdMsgUserId

当房间中的某个用户使用 sendCustomCmdMsg 发送自定义消息时，房间中的其它用户可以通过 onRecvCustomCmdMsg 接口接收消息。

```
 - (void)onRecvCustomCmdMsgUserId:(NSString *)userId cmdID:(NSInteger)cmdID seq:(UInt32)seq message:(NSData *)message 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识 |
| cmdID | NSInteger | 命令ID |
| seq | UInt32 | 消息序号 |
| message | NSData * | 消息数据 |

<br/>


### onMissCustomCmdMsgUserId

TRTC所使用的传输通道为UDP通道，所以即使设置了 reliable，也做不到100不丢失，只是丢消息概率极低，能满足常规可靠性要求。 在过去的一段时间内（通常为5s），自定义消息在传输途中丢失的消息数量的统计，SDK 都会通过此回调通知出来。

```
 - (void)onMissCustomCmdMsgUserId:(NSString *)userId cmdID:(NSInteger)cmdID errCode:(NSInteger)errCode missed:(NSInteger)missed 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识 |
| cmdID | NSInteger | 命令ID |
| errCode | NSInteger | 错误码 |
| missed | NSInteger | 丢失的消息数量 |

__说明__


只有在发送端设置了可靠传输(reliable)，接收方才能收到消息的丢失回调。


<br/>



## 旁路转推和混流回调

### onStartPublishCDNStream

接口startPublishCDNStream的状态回调。

```
 - (void)onStartPublishCDNStream:(int)err errMsg:(NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| err | int | 错误码，参考 TXLiteAVCode.h |
| errMsg | NSString * | 错误详细信息 |

<br/>


### onStopPublishCDNStream

接口stopPublishCDNStream的状态回调。

```
 - (void)onStopPublishCDNStream:(int)err errMsg:(NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| err | int | 错误码，参考 TXLiteAVCode.h |
| errMsg | NSString * | 错误详细信息 |

<br/>


### onStartCloudMixTranscoding

接口startCloudMixTranscoding的状态回调。

```
 - (void)onStartCloudMixTranscoding:(int)err errMsg:(NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| err | int | 错误码，参考 TXLiteAVCode.h |
| errMsg | NSString * | 错误详细信息 |

<br/>


### onStopCloudMixTranscoding

接口stopCloudMixTranscoding的状态回调。

```
 - (void)onStopCloudMixTranscoding:(int)err errMsg:(NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| err | int | 错误码，参考 TXLiteAVCode.h |
| errMsg | NSString * | 错误详细信息 |

<br/>



## TRTCVideoRenderDelegate

__功能__


自定义视频渲染回调对象。


<br/>

### onRenderVideoFrame

自定义视频渲染回调。

```
 - (void)onRenderVideoFrame:(TRTCVideoFrame *_Nonnull)frame userId:(NSString *__nullable)userId streamType:(TRTCVideoStreamType)streamType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCVideoFrame *_Nonnull | 待渲染的视频帧信息 |
| userId | NSString *__nullable | 视频源的 userid，如果是本地视频回调，该参数可以不用理会 |
| streamType | TRTCVideoStreamType | 视频源类型，比如是摄像头画面还是屏幕分享画面等等 |

<br/>



## TRTCLogDelegate

__功能__


日志事件回调对象。


__介绍__


建议在一个比较早初始化的类中设置回调委托对象，如AppDelegate。


<br/>

### onLog

有日志打印时的回调。

```
 - (void)onLog:(nullable NSString *)log LogLevel:(TRTCLogLevel)level WhichModule:(nullable NSString *)module 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | nullable NSString * | 日志内容 |
| level | TRTCLogLevel | 日志等级 参见TRTCLogLevel |
| module | nullable NSString * | 值暂无具体意义，目前为固定值TXLiteAVSDK |

<br/>




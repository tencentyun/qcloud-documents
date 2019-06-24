
TRTCCloudListener @ TXLiteAVSDK。

腾讯云视频通话功能的事件回调接口。


## 通用事件回调
### onError

错误回调：SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。
```
void onError(int errCode, String errMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码 TXLiteAVError。 |
| errMsg | String | 错误信息。 |
| extraInfo | Bundle | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。 |


### onWarning

警告回调：用于告知您一些非严重性问题，比如出现了卡顿或者可恢复的解码失败。
```
void onWarning(int warningCode, String warningMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| warningCode | int | 错误码 TXLiteAVWarning。 |
| warningMsg | String | 警告信息。 |
| extraInfo | Bundle | 扩展信息字段，个别警告码可能会带额外的信息帮助定位问题。 |



## 房间事件回调
### onEnterRoom

加入房间的事件回调。
```
void onEnterRoom(long elapsed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| elapsed | long | 加入房间耗时，单位毫秒。 |


### onExitRoom

离开房间的事件回调。
```
void onExitRoom(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 离开房间原因。 |


### onSwitchRole

切换角色结果回调。
```
void onSwitchRole(final int errCode, final String errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | final int | 错误码。 |
| errMsg | final String | 错误信息。 |


### onConnectOtherRoom

请求跨房通话的结果回调。
```
void onConnectOtherRoom(final String userID, final int err, final String errMsg)
```


### onDisConnectOtherRoom

断开跨房通话的结果回调。
```
void onDisConnectOtherRoom(final int err, final String errMsg)
```



## 成员事件回调
### onUserEnter

有新的音视频用户加入房间。
```
void onUserEnter(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |

__介绍__

当有新的音视频用户（有开启音频或者视频上行的用户）加入房间后，房间里的其他用户会收到该通知。
由于单个 TRTC 的房间可以容纳很多人的加入，所以并不是任何用户加入房间后都会出发 onUserEnter 事件，这可能会造成性能上的灾难。 只有一个用户开启了音频或者视频上行的时候，房间里的其他用户才能收到该通知。
您可以在收到该通知后，在 UI 界面上增加一个用户的头像，但并不推荐立刻 startRemoteView， 因为该用户可能只有声音没有视频，onUserVideoAvailable 则是真正的宣告某个用户的画面可以显示了。

>!
>- 并不是所有用户加入房间都会触发此通知，只有开启音频或者视频上行的用户才会触发此通知。
>- 收到该通知后，并不推荐立刻 startRemoteView，因为可能该用户只开启了音频而没有开启视频。


### onUserExit

有用户从当前房间中离开。
```
void onUserExit(String userId, int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| reason | int | 离开原因代码，区分用户是正常离开，还是由于网络断线等原因离开。 |


### onUserVideoAvailable

userid 对应的远端主路（即摄像头）画面的状态通知。
```
void onUserVideoAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| available | boolean | 画面是否开启。 |

__介绍__

当 available 为 YES 时，您可以在这个回调中调用 startRemoteView 显示该 userId 的视频画面。


### onUserSubStreamAvailable

userid 对应的远端辅路（屏幕分享等）画面的状态通知。
```
void onUserSubStreamAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| available | boolean | 屏幕分享是否开启。 |

>?显示辅路画面使用的函数不是 startRemoteView 而是 startRemoteSubStreamView。



### onUserAudioAvailable

userid 对应的远端声音的状态通知。
```
void onUserAudioAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| available | boolean | true：音频可播放，false：音频被关闭。 |


### onUserVoiceVolume

用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。
```
void onUserVoiceVolume(ArrayList< TRTCCloudDef.TRTCVolumeInfo > userVolumes, int totalVolume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userVolumes | ArrayList< TRTCCloudDef.TRTCVolumeInfo > | 所有正在说话的房间成员的音量（取值范围0 - 100）。即 userVolumes 内仅包含音量不为0（正在说话）的用户音量信息。其中本地进房 userId 对应的音量，表示 local 的音量，也就是自己的音量。 |
| totalVolume | int | 所有远端成员的总音量, 取值范围 [0, 100]。 |

__介绍__

您可以通过调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 enableAudioVolumeEvaluation 接口来开关这个回调或者设置它的触发间隔. 需要注意的是，调用 enableAudioVolumeEvaluation 开启音量回调后，无论频道内是否有人说话，都会按设置的时间间隔调用这个回调;如果没有人说话，则 userVolumes 为空，totalVolume 为0。



## 统计和质量回调
### onNetworkQuality

网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。
```
void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality, ArrayList< TRTCCloudDef.TRTCQuality > remoteQuality)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | [TRTCCloudDef.TRTCQuality](https://cloud.tencent.com/document/product/647/32266#trtcquality) | 上行网络质量。 |
| remoteQuality | ArrayList< TRTCCloudDef.TRTCQuality > | 下行网络质量。 |

>?userid 为"" 代表自己当前的视频质量。


### onStatistics

技术指标统计回调:。
```
void onStatistics(TRTCStatistics statics)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statics | [TRTCStatistics](https://cloud.tencent.com/document/product/647/32266#trtcstatistics) | 状态数据。 |

__介绍__

如果您是熟悉音视频领域相关术语，可以通过这个回调获取 SDK 的所有技术指标。 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调。

>?每2秒回调一次。



## 音视频事件回调
### onFirstVideoFrame

首帧视频画面到达，界面此时可以结束 Loading，并开始显示视频画面。
```
void onFirstVideoFrame(String userId, int streamType, int width, int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| streamType | int | 视频流类型。 |
| width | int | 画面宽度。 |
| height | int | 画面高度。 |


### onFirstAudioFrame

首帧音频数据到达。
```
void onFirstAudioFrame(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |



## 服务器事件回调
### onConnectionLost

SDK 跟服务器的连接断开。
```
void onConnectionLost()
```


### onTryToReconnect

SDK 尝试重新连接到服务器。
```
void onTryToReconnect()
```


### onConnectionRecovery

SDK 跟服务器的连接恢复。
```
void onConnectionRecovery()
```


### onSpeedTest

服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。
```
void onSpeedTest(TRTCCloudDef.TRTCSpeedTestResult currentResult, int finishedCount, int totalCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| currentResult | [TRTCCloudDef.TRTCSpeedTestResult](https://cloud.tencent.com/document/product/647/32266#trtcspeedtestresult) | 当前完成的测速结果。 |
| finishedCount | int | 已完成测速的服务器数量。 |
| totalCount | int | 需要测速的服务器总数量。 |



## 硬件设备事件回调
### onCameraDidReady

摄像头准备就绪。
```
void onCameraDidReady()
```


### onMicDidReady

麦克风准备就绪。
```
void onMicDidReady()
```


### onAudioRouteChanged

音频路由发生变化，音频路由即声音由哪里输出（扬声器、听筒）。
```
void onAudioRouteChanged(int newRoute, int oldRoute)
```



## 自定义消息的接收回调
### onRecvCustomCmdMsg

收到自定义消息回调。
```
void onRecvCustomCmdMsg(String userId, int cmdID, int seq, byte [] message)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| cmdID | int | 命令 ID。 |
| seq | int | 消息序号。 |
| message | byte [] | 消息数据。 |

__介绍__

当房间中的某个用户使用 sendCustomCmdMsg 发送自定义消息时，房间中的其它用户可以通过 onRecvCustomCmdMsg 接口接收消息。


### onMissCustomCmdMsg

自定义消息丢失回调。
```
void onMissCustomCmdMsg(String userId, int cmdID, int errCode, int missed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| cmdID | int | 数据流 ID。 |
| errCode | int | 错误码，当前版本为-1。 |
| missed | int | 丢失的消息数量。 |

__介绍__

TRTC 所使用的传输通道为 UDP 通道，所以即使设置了 reliable，也做不到100不丢失，只是丢消息概率极低，能满足常规可靠性要求。 在过去的一段时间内（通常为5s），自定义消息在传输途中丢失的消息数量的统计，SDK 都会通过此回调通知出来。

>?只有在发送端设置了可靠传输（reliable），接收方才能收到消息的丢失回调。


### onRecvSEIMsg

收到 SEI 消息的回调。
```
void onRecvSEIMsg(String userId, byte [] data)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| data | byte [] | 数据。 |

__介绍__

当房间中的某个用户使用 sendSEIMsg 发送数据时，房间中的其它用户可以通过 onRecvSEIMsg 接口接收数据。



## CDN 旁路转推
### onStartPublishCDNStream

启动旁路推流到 CDN 完成的回调，对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 startPublishCDNStream() 接口。
```
void onStartPublishCDNStream(int err, String errMsg)
```

>?Start 回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标 CDN 有异常，还是有可能会转推失败。



### onStopPublishCDNStream

停止旁路推流到 CDN 完成的回调，对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 stopPublishCDNStream() 接口。
```
void onStopPublishCDNStream(int err, String errMsg)
```

>?Start 回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标 CDN 有异常，还是有可能会转推失败。



### onSetMixTranscodingConfig

设置云端的混流转码参数的回调，对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 setMixTranscodingConfig() 接口。
```
void onSetMixTranscodingConfig(int err, String errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| err | int | 0表示成功，其余值表示失败。 |
| errMsg | String | 具体错误原因。 |



## TRTCVideoRenderListener

__功能__

视频数据帧的自定义渲染回调。



### onRenderVideoFrame

自定义视频渲染回调。
```
void onRenderVideoFrame(String userId, int streamType, TRTCCloudDef.TRTCVideoFrame frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 视频源的 userId，如果是本地视频回调（setLocalVideoRenderListener），该参数可以不用理会。 |
| streamType | int | 视频流类型，比如是摄像头画面还是屏幕分享画面等等。 |
| frame | [TRTCCloudDef.TRTCVideoFrame](https://cloud.tencent.com/document/product/647/32266#trtcvideoframe) | 待渲染视频帧。 |



## TRTCAudioFrameListener

__功能__

声音数据帧的自定义处理回调（只读）。



### onCapturedAudioFrame

本地麦克风采集到的音频数据回调。
```
void onCapturedAudioFrame(TRTCCloudDef.TRTCAudioFrame frame)
```

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。


### onPlayAudioFrame

混音前的每一路远程用户的音频数据（比如您要对某一路的语音进行文字转换，必须要使用这里的原始数据，而不是混音之后的数据）。
```
void onPlayAudioFrame(TRTCCloudDef.TRTCAudioFrame frame, String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCCloudDef.TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32266#trtcaudioframe) | 音频数据。 |
| userId | String | 用户标识。 |

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。


### onMixedPlayAudioFrame

各路音频数据混合后送入喇叭播放的音频数据。
```
void onMixedPlayAudioFrame(TRTCCloudDef.TRTCAudioFrame frame)
```

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。



## TRTCLogListener

__功能__

日志相关回调。

__介绍__

建议在一个比较早初始化的类中设置回调对象，如 Application。



### onLog

有日志打印时的回调。
```
abstract void onLog(String log, int level, String module)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| log | String | 日志内容。 |
| level | int | 日志等级 参见 TRTC_LOG_LEVEL。 |
| module | String | 值暂无具体意义，目前为固定值 TXLiteAVSDK。 |




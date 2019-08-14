
TRTCCloudListener @ TXLiteAVSDK。

腾讯云视频通话功能的事件回调接口。


## 错误事件和警告事件
### onError

错误回调：SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。
```
void onError(int errCode, String errMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errMsg | String | 错误信息。 |
| extraInfo | Bundle | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。 |


### onWarning

警告回调：用于告知您一些非严重性问题，例如出现卡顿或者可恢复的解码失败。
```
void onWarning(int warningCode, String warningMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| warningCode | int | 错误码。 |
| warningMsg | String | 警告信息。 |
| extraInfo | Bundle | 扩展信息字段，个别警告码可能会带额外的信息帮助定位问题。 |



## 房间事件回调
### onEnterRoom

已加入房间的回调。
```
void onEnterRoom(long result)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| result | long | result > 0 时为进房耗时（ms），result < 0 时为进房错误码。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 enterRoom() 接口执行进房操作后，会收到来自 SDK 的 onEnterRoom(result) 回调：
- 如果加入成功，result 会是一个正数（result > 0），表示加入房间所消耗的时间，单位为毫秒（ms）。
- 如果加入失败，result 会是一个负数（result < 0），表示进房失败的错误码。进房失败的错误码含义请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。


>?在 Ver6.6 之前的版本，只有进房成功会抛出 onEnterRoom(result) 回调，进房失败由 [onError()](https://cloud.tencent.com/document/product/647/32265#onerror) 回调抛出。 在 Ver6.6 及之后改为：进房成功返回正的 result，进房失败返回负的 result，同时进房失败也会有 [onError()](https://cloud.tencent.com/document/product/647/32265#onerror) 回调抛出。



### onExitRoom

离开房间的事件回调。
```
void onExitRoom(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 离开房间原因，0：主动调用 exitRoom 退房；1：被服务器踢出当前房间；2：当前房间整个被解散。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 exitRoom() 接口会执行退出房间的相关逻辑，例如释放音视频设备资源和编解码器资源等。 待资源释放完毕，SDK 会通过 [onExitRoom()](https://cloud.tencent.com/document/product/647/32265#onexitroom) 回调通知到您。
如果您要再次调用 enterRoom() 或者切换到其他的音视频 SDK，请等待 [onExitRoom()](https://cloud.tencent.com/document/product/647/32265#onexitroom) 回调到来之后再执行相关操作。 否则可能会遇到音频设备被占用等各种异常问题。


### onSwitchRole

切换角色的事件回调。
```
void onSwitchRole(final int errCode, final String errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | final int | 错误码，0代表切换成功，其他请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。 |
| errMsg | final String | 错误信息。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 switchRole() 接口会切换主播和观众的角色，该操作会伴随一个线路切换的过程， 待 SDK 切换完成后，会抛出 [onSwitchRole()](https://cloud.tencent.com/document/product/647/32265#onswitchrole) 事件回调。


### onConnectOtherRoom

请求跨房通话（主播 PK）的结果回调。
```
void onConnectOtherRoom(final String userId, final int errCode, final String errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | final String | 要 PK 的目标主播 userid。 |
| errCode | final int | 错误码，ERR_NULL 代表切换成功，其他请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。 |
| errMsg | final String | 错误信息。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 ConnectOtherRoom() 接口会将两个不同房间中的主播拉通视频通话，也就是所谓的“主播PK”功能。 调用者会收到 [onConnectOtherRoom()](https://cloud.tencent.com/document/product/647/32265#onconnectotherroom) 回调来获知跨房通话是否成功， 如果成功，两个房间中的所有用户都会收到 PK 主播的 [onUserVideoAvailable()](https://cloud.tencent.com/document/product/647/32265#onuservideoavailable) 回调。


### onDisConnectOtherRoom

结束跨房通话（主播 PK）的结果回调。
```
void onDisConnectOtherRoom(final int errCode, final String errMsg)
```



## 成员事件回调
### onUserEnter

有用户（主播）加入当前房间。
```
void onUserEnter(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |

__介绍__

没有开启音视频上行的观众在加入房间时不会触发该通知，只有开启音视频上行的主播加入房间时才会触发该通知。通知参数中 userId 对应的用户一定已开启声音上行，但不一定已开启视频。
如果要显示远程画面，更推荐监听 [onUserVideoAvailable()](https://cloud.tencent.com/document/product/647/32265#onuservideoavailable) 事件回调。


### onUserExit

有用户（主播）离开当前房间。
```
void onUserExit(String userId, int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| reason | int | 离开原因代码，区分用户是正常离开，还是由于网络断线等原因离开。 |


### onUserVideoAvailable

用户是否开启摄像头视频。
```
void onUserVideoAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| available | boolean | 画面是否开启。 |

__介绍__

当您收到 onUserVideoAvailable(userId， true) 通知时，表示该路画面已经有可用的视频数据帧到达。 此时，您需要调用 startRemoteView(userid) 接口加载该用户的远程画面。 然后，您会收到名为 onFirstVideoFrame(userid) 的首帧画面渲染回调。
当您收到 onUserVideoAvailable(userId， false) 通知时，表示该路远程画面已经被关闭，可能由于该用户调用了 muteLocalVideo() 或 stopLocalPreview() 所致。

### onUserSubStreamAvailable

用户是否开启屏幕分享。
```
void onUserSubStreamAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| available | boolean | 屏幕分享是否开启。 |

>?显示辅路画面使用的函数是 startRemoteSubStreamView()，而非 startRemoteView()。



### onUserAudioAvailable

用户是否开启音频上行。
```
void onUserAudioAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户标识。 |
| available | boolean | 声音是否开启。 |


### onFirstVideoFrame

开始渲染本地或远程用户的首帧画面。
```
void onFirstVideoFrame(String userId, int streamType, int width, int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 本地或远程用户 ID，如果 userId == null 代表本地，userId != null 代表远程。 |
| streamType | int | 视频流类型：摄像头或屏幕分享。 |
| width | int | 画面宽度。 |
| height | int | 画面高度。 |

__介绍__

如果 userId 为 null，代表开始渲染本地采集的摄像头画面，需要您先调用 startLocalPreview 触发。 如果 userId 不为 null，代表开始渲染远程用户的首帧画面，需要您先调用 startRemoteView 触发。

>?只有当您调用 startLocalPreview()、startRemoteView() 或 startRemoteSubStreamView() 之后，才会触发该回调。



### onFirstAudioFrame

开始播放远程用户的首帧音频（本地声音暂不通知）。
```
void onFirstAudioFrame(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 远程用户 ID。 |


### onSendFirstLocalVideoFrame

首帧本地视频数据已经被送出。
```
void onSendFirstLocalVideoFrame(int streamType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| streamType | int | 视频流类型，大画面还是小画面或辅流画面（屏幕分享）。 |

__介绍__

SDK 会在 enterRoom() 并 startLocalPreview() 成功后开始摄像头采集，并将采集到的画面进行编码。 当 SDK 成功向云端送出第一帧视频数据后，会抛出这个回调事件。


### onSendFirstLocalAudioFrame

首帧本地音频数据已经被送出。
```
void onSendFirstLocalAudioFrame()
```

__介绍__

SDK 会在 enterRoom() 并 startLocalAudio() 成功后开始麦克风采集，并将采集到的声音进行编码。 当 SDK 成功向云端送出第一帧音频数据后，会抛出这个回调事件。



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


### onUserVoiceVolume

用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。
```
void onUserVoiceVolume(ArrayList< TRTCCloudDef.TRTCVolumeInfo > userVolumes, int totalVolume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userVolumes | ArrayList< TRTCCloudDef.TRTCVolumeInfo > | 所有正在说话的房间成员的音量，取值范围0 - 100。 |
| totalVolume | int | 所有远端成员的总音量, 取值范围0 - 100。 |

__介绍__

您可以通过调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 enableAudioVolumeEvaluation 接口来开关这个回调或者设置它的触发间隔。 调用 enableAudioVolumeEvaluation 开启音量回调后，无论频道内是否有人说话，都会按设置的时间间隔调用这个回调; 如果没有人说话，则 userVolumes 为空，totalVolume 为0。

>?userId 为 null 时表示自己的音量，userVolumes 内仅包含正在说话（音量不为0）的用户音量信息。




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

实时音视频使用 UDP 通道，即使设置了可靠传输（reliable）也无法确保100%不丢失，只是丢消息概率极低，能满足常规可靠性要求。在发送端设置了可靠传输（reliable）后，SDK 都会通过此回调通知过去时间段内（通常为5s）传输途中丢失的自定义消息数量统计信息。

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



## CDN 旁路转推回调
### onStartPublishCDNStream

启动旁路推流到 CDN 完成的回调。
```
void onStartPublishCDNStream(int err, String errMsg)
```

__介绍__

对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 startPublishCDNStream() 接口。

>?Start 回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标 CDN 有异常，还是有可能会转推失败。



### onStopPublishCDNStream

停止旁路推流到 CDN 完成的回调。
```
void onStopPublishCDNStream(int err, String errMsg)
```

__介绍__

对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 中的 stopPublishCDNStream() 接口。


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
| streamType | int | 视频流类型，例如是摄像头画面还是屏幕分享画面等等。 |
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

混音前的每一路远程用户的音频数据（例如您要对某一路的语音进行文字转换，必须要使用这里的原始数据，而不是混音之后的数据）。
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




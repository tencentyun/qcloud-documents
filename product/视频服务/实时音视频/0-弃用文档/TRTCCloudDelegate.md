TRTCCloudDelegate @ TXLiteAVSDK。
腾讯云视频通话功能的事件回调接口。

## 错误事件和警告事件
### onError

错误回调：SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。
```
- (void)onError:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | TXLiteAVError | 错误码。 |
| errMsg | nullable NSString * | 错误信息。 |
| extInfo | nullable NSDictionary * | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。 |


### onWarning

警告回调：用于告知您一些非严重性问题，例如出现了卡顿或者可恢复的解码失败。
```
- (void)onWarning:(TXLiteAVWarning)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| warningCode | TXLiteAVWarning | 警告码。 |
| warningMsg | nullable NSString * | 警告信息。 |
| extInfo | nullable NSDictionary * | 扩展信息字段，个别警告码可能会带额外的信息帮助定位问题。 |



## 房间事件回调
### onEnterRoom

已加入房间的回调。
```
- (void)onEnterRoom:(NSInteger)result 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| result | NSInteger | result > 0 时为进房耗时（ms），result < 0 时为进房错误码。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 enterRoom() 接口执行进房操作后，会收到来自 SDK 的 onEnterRoom(result) 回调： 
- 如果加入成功，result 会是一个正数（result > 0），表示加入房间所消耗的时间，单位为毫秒（ms）。
- 如果加入失败，result 会是一个负数（result < 0），表示进房失败的错误码。进房失败的错误码含义请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。

>?在 Ver6.6 之前的版本，只有进房成功会抛出 onEnterRoom(result) 回调，进房失败由 onError() 回调抛出。 在 Ver6.6 及之后改为：进房成功返回正的 result，进房失败返回负的 result，同时进房失败也会有 onError() 回调抛出。



### onExitRoom

离开房间的事件回调。
```
- (void)onExitRoom:(NSInteger)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | NSInteger | 离开房间原因，0：主动调用 exitRoom 退房；1：被服务器踢出当前房间；2：当前房间整个被解散。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 exitRoom() 接口会执行退出房间的相关逻辑，例如释放音视频设备资源和编解码器资源等。待资源释放完毕，SDK 会通过 onExitRoom() 回调通知到您。
如果您要再次调用 enterRoom() 或者切换到其他的音视频 SDK，请等待 onExitRoom() 回调到来之后再执行相关操作。 否则可能会遇到音频设备（例如 iOS 里的 AudioSession）被占用等各种异常问题。


### onSwitchRole

切换角色的事件回调。
```
- (void)onSwitchRole:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | TXLiteAVError | 错误码，ERR_NULL 代表切换成功，其他请参见[错误码](https://cloud.tencent.com/document/product/647/32257)。 |
| errMsg | nullable NSString * | 错误信息。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 switchRole() 接口会切换主播和观众的角色，该操作会伴随一个线路切换的过程， 待 SDK 切换完成后，会抛出 onSwitchRole() 事件回调。


### onConnectOtherRoom

请求跨房通话（主播 PK）的结果回调。
```
- (void)onConnectOtherRoom:(NSString *)userId errCode:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 要 PK 的目标主播 userid。 |
| errCode | TXLiteAVError | 错误码，ERR_NULL 代表切换成功，其他请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。 |
| errMsg | nullable NSString * | 错误信息。 |

__介绍__

调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 connectOtherRoom() 接口会将两个不同房间中的主播拉通视频通话，也就是所谓的“主播PK”功能。 调用者会收到 onConnectOtherRoom() 回调来获知跨房通话是否成功， 如果成功，两个房间中的所有用户都会收到 PK 主播的 onUserVideoAvailable() 回调。


### onDisconnectOtherRoom

结束跨房通话（主播 PK）的结果回调。
```
- (void)onDisconnectOtherRoom:(TXLiteAVError)errCode errMsg:(nullable NSString *)errMsg 
```



## 成员事件回调
### onRemoteUserEnterRoom

有用户加入当前房间。
```
- (void)onRemoteUserEnterRoom:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |

__介绍__

出于性能方面的考虑，在两种不同的应用场景下，该通知的行为会有差别：
- 视频通话场景（TRTCAppSceneVideoCall）：该场景下用户没有角色的区别，任何用户进入房间都会触发该通知。
- 在线直播场景（TRTCAppSceneLIVE）：在线直播场景不限制观众的数量，如果任何用户进出都抛出回调会引起很大的性能损耗，所以该场景下只有主播进入房间时才会触发该通知，观众进入房间不会触发该通知。



>?注意 onRemoteUserEnterRoom 和 onRemoteUserLeaveRoom 只适用于维护当前房间里的“成员列表”，如果需要显示远程画面，建议使用监听 onUserVideoAvailable() 事件回调。



### onRemoteUserLeaveRoom

有用户离开当前房间。
```
- (void)onRemoteUserLeaveRoom:(NSString *)userId reason:(NSInteger)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| reason | NSInteger | 离开原因，0表示用户主动退出房间，1表示用户超时退出，2表示被踢出房间。 |

__介绍__

与 onRemoteUserEnterRoom 相对应，在两种不同的应用场景下，该通知的行为会有差别：
- 视频通话场景（TRTCAppSceneVideoCall）：该场景下用户没有角色的区别，任何用户的离开都会触发该通知。
- 在线直播场景（TRTCAppSceneLIVE）：只有主播离开房间时才会触发该通知，观众离开房间不会触发该通知。




### onUserVideoAvailable

用户是否开启摄像头视频。
```
- (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| available | BOOL | 画面是否开启。 |

__介绍__

当您收到 onUserVideoAvailable(userid， YES) 通知时，表示该路画面已经有可用的视频数据帧到达。您需要调用 startRemoteView(userid) 接口加载该用户的远程画面。 此后，您会收到名为 onFirstVideoFrame(userid) 的首帧画面渲染回调。
当您收到 onUserVideoAvailable(userid， NO) 通知时，表示该路远程画面已被关闭，可能由于该用户调用了 muteLocalVideo() 或 stopLocalPreview()。




### onUserSubStreamAvailable

用户是否开启屏幕分享。
```
- (void)onUserSubStreamAvailable:(NSString *)userId available:(BOOL)available 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| available | BOOL | 屏幕分享是否开启。 |

>?显示辅路画面使用的函数是 startRemoteSubStreamView() 而非 startRemoteView()。



### onUserAudioAvailable

用户是否开启音频上行。
```
- (void)onUserAudioAvailable:(NSString *)userId available:(BOOL)available 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| available | BOOL | 声音是否开启。 |


### onFirstVideoFrame

开始渲染本地或远程用户的首帧画面。
```
- (void)onFirstVideoFrame:(NSString *)userId streamType:(TRTCVideoStreamType)streamType width:(int)width height:(int)height 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 本地或远程用户 ID，如果 userId == nil 代表本地，userId != nil 代表远程。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32261#trtcvideostreamtype) | 视频流类型：摄像头或屏幕分享。 |
| width | int | 画面宽度。 |
| height | int | 画面高度。 |

__介绍__

如果 userId == nil，代表开始渲染本地采集的摄像头画面，需要您先调用 startLocalPreview 触发。 如果 userId != nil，代表开始渲染远程用户的首帧画面，需要您先调用 startRemoteView 触发。

>?只有当您调用 startLocalPreivew()、startRemoteView() 或 startRemoteSubStreamView() 之后，才会触发该回调。



### onFirstAudioFrame

开始播放远程用户的首帧音频（本地声音暂不通知）。
```
- (void)onFirstAudioFrame:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 远程用户 ID。 |


### onSendFirstLocalVideoFrame

首帧本地视频数据已经被送出。
```
- (void)onSendFirstLocalVideoFrame:(TRTCVideoStreamType)streamType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32261#trtcvideostreamtype) | 视频流类型，主画面、小画面或辅流画面（屏幕分享）。 |

__介绍__

SDK 会在 enterRoom() 并 startLocalPreview() 成功后开始摄像头采集，并将采集到的画面进行编码。当 SDK 成功向云端送出第一帧视频数据后，会抛出这个回调事件。


### onSendFirstLocalAudioFrame

首帧本地音频数据已经被送出。
```
- (void)onSendFirstLocalAudioFrame
```

__介绍__

SDK 会在 enterRoom() 并 startLocalAudio() 成功后开始麦克风采集，并将采集到的声音进行编码。 当 SDK 成功向云端送出第一帧音频数据后，会抛出这个回调事件。


### onUserEnter

废弃接口：有主播加入当前房间。
```
- (void)onUserEnter:(NSString *)userId DEPRECATED_ATTRIBUTE 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |


__介绍__

该回调接口可以被看作是 onRemoteUserEnterRoom 的废弃版本，不推荐使用。请使用 onUserVideoAvailable 或 onRemoteUserEnterRoom 进行替代。

>?该接口已被废弃，不推荐使用。


### onUserExit

废弃接口： 有主播离开当前房间。
```
- (void)onUserExit:(NSString *)userId reason:(NSInteger)reason DEPRECATED_ATTRIBUTE 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| reason | NSInteger | 离开原因代码，用于区分用户正常离开或是由于网络断线等原因离开。 |

__介绍__

该回调接口可以被看作是 onRemoteUserLeaveRoom 的废弃版本，不推荐使用。请使用 onUserVideoAvailable 或 onRemoteUserEnterRoom 进行替代。

>?该接口已被废弃，不推荐使用。



## 统计和质量回调
### onNetworkQuality

网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。
```
- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray< TRTCQualityInfo * > *)remoteQuality 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | [TRTCQualityInfo](https://cloud.tencent.com/document/product/647/32261#trtcqualityinfo) * | 上行网络质量。 |
| remoteQuality | NSArray< [TRTCQualityInfo](https://cloud.tencent.com/document/product/647/32261#trtcqualityinfo) * > * | 下行网络质量。 |

>?userId == nil 代表自己当前的视频质量。


### onStatistics

技术指标统计回调。
```
- (void)onStatistics:(TRTCStatistics *)statistics 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statistics | [TRTCStatistics](https://cloud.tencent.com/document/product/647/32261#trtcstatistics) * | 统计数据，包括本地和远程的。 |

__介绍__

如果您是熟悉音视频领域相关术语，可以通过这个回调获取 SDK 的所有技术指标。 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调。

>?每2秒回调一次。



## 服务器事件回调
### onConnectionLost

SDK 跟服务器的连接断开。
```
- (void)onConnectionLost
```


### onTryToReconnect

SDK 尝试重新连接到服务器。
```
- (void)onTryToReconnect
```


### onConnectionRecovery

SDK 跟服务器的连接恢复。
```
- (void)onConnectionRecovery
```



## 硬件设备事件回调
### onCameraDidReady

摄像头准备就绪。
```
- (void)onCameraDidReady
```


### onMicDidReady

麦克风准备就绪。
```
- (void)onMicDidReady
```


### onAudioRouteChanged

音频路由发生变化（仅 iOS），音频路由即声音由哪里输出（扬声器、听筒）。
```
- (void)onAudioRouteChanged:(TRTCAudioRoute)route fromRoute:(TRTCAudioRoute)fromRoute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| route | [TRTCAudioRoute](https://cloud.tencent.com/document/product/647/32261#trtcaudioroute) | 当前音频路由。 |
| fromRoute | [TRTCAudioRoute](https://cloud.tencent.com/document/product/647/32261#trtcaudioroute) | 变更前的音频路由。 |


### onUserVoiceVolume

用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。
```
- (void)onUserVoiceVolume:(NSArray< TRTCVolumeInfo * > *)userVolumes totalVolume:(NSInteger)totalVolume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userVolumes | NSArray< [TRTCVolumeInfo](https://cloud.tencent.com/document/product/647/32261#trtcvolumeinfo) * > * | 所有正在说话的房间成员的音量，取值范围0 - 100。 |
| totalVolume | NSInteger | 所有远端成员的总音量, 取值范围0 - 100。 |

__介绍__

您可以通过调用 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 enableAudioVolumeEvaluation 接口来开关这个回调或者设置它的触发间隔。 需要注意的是，调用 enableAudioVolumeEvaluation 开启音量回调后，无论频道内是否有人说话，都会按设置的时间间隔调用这个回调; 如果没有人说话，则 userVolumes 为空，totalVolume 为0。

>?userId 为 nil 时表示自己的音量，userVolumes 内仅包含正在说话（音量不为0）的用户音量信息。



### onDevice

本地设备通断回调。
```
- (void)onDevice:(NSString *)deviceId type:(TRTCMediaDeviceType)deviceType stateChanged:(NSInteger)state 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceId | NSString * | 设备 ID。 |
| deviceType | [TRTCMediaDeviceType](https://cloud.tencent.com/document/product/647/32261#trtcmediadevicetype) | 设备类型。 |
| state | NSInteger | 0：设备断开；1：设备连接。 |



## 自定义消息的接收回调
### onRecvCustomCmdMsgUserId

收到自定义消息回调。
```
- (void)onRecvCustomCmdMsgUserId:(NSString *)userId cmdID:(NSInteger)cmdID seq:(UInt32)seq message:(NSData *)message 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| cmdID | NSInteger | 命令 ID。 |
| seq | UInt32 | 消息序号。 |
| message | NSData * | 消息数据。 |

__介绍__

当房间中的某个用户使用 sendCustomCmdMsg 发送自定义消息时，房间中的其它用户可以通过 onRecvCustomCmdMsg 接口接收消息。


### onMissCustomCmdMsgUserId

自定义消息丢失回调。
```
- (void)onMissCustomCmdMsgUserId:(NSString *)userId cmdID:(NSInteger)cmdID errCode:(NSInteger)errCode missed:(NSInteger)missed 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| cmdID | NSInteger | 命令 ID。 |
| errCode | NSInteger | 错误码。 |
| missed | NSInteger | 丢失的消息数量。 |

__介绍__

实时音视频使用 UDP 通道，即使设置了可靠传输（reliable）也无法确保100%不丢失，只是丢消息概率极低，能满足常规可靠性要求。在发送端设置了可靠传输（reliable）后，SDK 都会通过此回调通知过去时间段内（通常为5s）传输途中丢失的自定义消息数量统计信息。

>?只有在发送端设置了可靠传输（reliable），接收方才能收到消息的丢失回调。


### onRecvSEIMsg

收到 SEI 消息的回调。
```
- (void)onRecvSEIMsg:(NSString *)userId message:(NSData *)message 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户标识。 |
| message | NSData * | 数据。 |

__介绍__

当房间中的某个用户使用 sendSEIMsg 发送数据时，房间中的其它用户可以通过 onRecvSEIMsg 接口接收数据。



## CDN 旁路转推回调
### onStartPublishCDNStream

启动旁路推流到 CDN 完成的回调。
```
- (void)onStartPublishCDNStream:(int)err errMsg:(NSString *)errMsg 
```

__介绍__

对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 startPublishCDNStream() 接口。

>?Start 回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标 CDN 有异常，还是有可能会转推失败。



### onStopPublishCDNStream

停止旁路推流到 CDN 完成的回调。
```
- (void)onStopPublishCDNStream:(int)err errMsg:(NSString *)errMsg 
```

__介绍__

对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 stopPublishCDNStream() 接口。


### onSetMixTranscodingConfig

设置云端的混流转码参数的回调，对应于 [TRTCCloud](https://cloud.tencent.com/document/product/647/32259) 中的 setMixTranscodingConfig() 接口。
```
- (void)onSetMixTranscodingConfig:(int)err errMsg:(NSString *)errMsg 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| err | int | 0表示成功，其余值表示失败。 |
| errMsg | NSString * | 具体错误原因。 |



## 音效回调
### onAudioEffectFinished

播放音效结束回调。
```
- (void)onAudioEffectFinished:(int)effectId code:(int)code 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |
| code | int | 0表示播放正常结束；其他表示异常结束。 |



## 屏幕分享回调
### onScreenCaptureStarted

当屏幕分享开始时，SDK 会通过此回调通知。
```
- (void)onScreenCaptureStarted
```


### onScreenCapturePaused

当屏幕分享暂停时，SDK 会通过此回调通知。
```
- (void)onScreenCapturePaused:(int)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 原因，0：用户主动暂停；1：屏幕窗口不可见暂停。 |


### onScreenCaptureResumed

当屏幕分享恢复时，SDK 会通过此回调通知。
```
- (void)onScreenCaptureResumed:(int)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 恢复原因，0：用户主动恢复；1：屏幕窗口恢复可见从而恢复分享。 |


### onScreenCaptureStoped

当屏幕分享停止时，SDK 会通过此回调通知。
```
- (void)onScreenCaptureStoped:(int)reason 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 停止原因，0：用户主动停止；1：屏幕窗口关闭导致停止。 |



## TRTCVideoRenderDelegate 

__功能__

视频数据帧的自定义处理回调。



## 自定义视频渲染回调
### onRenderVideoFrame

自定义视频渲染回调。
```
- (void)onRenderVideoFrame:(TRTCVideoFrame *_Nonnull)frame userId:(NSString *__nullable)userId streamType:(TRTCVideoStreamType)streamType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCVideoFrame](https://cloud.tencent.com/document/product/647/32261#trtcvideoframe) *_Nonnull | 待渲染的视频帧信息。 |
| userId | NSString *__nullable | 视频源的 userId，如果是本地视频回调（setLocalVideoRenderDelegate），该参数可以忽略。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32261#trtcvideostreamtype) | 视频源类型，例如，使用摄像头画面或屏幕分享画面等。 |



## TRTCAudioFrameDelegate

__功能__

声音数据帧的自定义处理回调。



## 音频数据回调
### onCapturedAudioFrame

本地麦克风采集到的音频数据回调。
```
- (void)onCapturedAudioFrame:(TRTCAudioFrame *)frame 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32261#trtcaudioframe) * | 音频数据。 |

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据支持修改。
>- 此接口回调出的音频时间帧长固定为0.02s。 由时间帧长转化为字节帧长的公式为【采样率 × 时间帧长 × 声道数 × 采样点位宽】。 以 SDK 默认的音频录制格式48000采样率、单声道、16采样点位宽为例，字节帧长为【48000 × 0.02s × 1 × 16bit = 15360bit = 1920字节】。
>- 此接口回调出的音频数据包含背景音、音效、混响等前处理效果。


### onPlayAudioFrame

混音前的每一路远程用户的音频数据（例如您要对某一路的语音进行文字转换，必须要使用这里的原始数据，而不是混音之后的数据）。
```
- (void)onPlayAudioFrame:(TRTCAudioFrame *)frame userId:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32261#trtcaudioframe) * | 音频数据。 |
| userId | NSString * | 用户标识。 |

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。


### onMixedPlayAudioFrame

各路音频数据混合后送入喇叭播放的音频数据。
```
- (void)onMixedPlayAudioFrame:(TRTCAudioFrame *)frame 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32261#trtcaudioframe) * | 音频数据。 |

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据支持修改。
>- 此接口回调出的音频时间帧长固定为0.02s。 由时间帧长转化为字节帧长的公式为【采样率 × 时间帧长 × 声道数 × 采样点位宽】。 以 SDK 默认的音频播放格式48000采样率、双声道、16采样点位宽为例，字节帧长为【48000 × 0.02s × 2 × 16bit = 30720bit = 3840字节】。
>- 此接口回调出的音频数据是各路音频播放数据的混合，不包含耳返的音频数据。



## TRTCLogDelegate

__功能__

日志相关回调。

__介绍__

建议在一个比较早初始化的类中设置回调委托对象，例如 AppDelegate。



## Log 信息回调
### onLog

有日志打印时的回调。
```
- (void)onLog:(nullable NSString *)log LogLevel:(TRTCLogLevel)level WhichModule:(nullable NSString *)module 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| log | nullable NSString * | 日志内容。 |
| level | [TRTCLogLevel](https://cloud.tencent.com/document/product/647/32261#trtcloglevel) | 日志等级，参见 TRTCLogLevel。 |
| module | nullable NSString * | 值暂无具体意义，目前为固定值 TXLiteAVSDK。 |




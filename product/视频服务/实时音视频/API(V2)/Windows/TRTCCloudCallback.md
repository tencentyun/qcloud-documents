
TRTCCloudCallback @ TXLiteAVSDK。

__功能__

腾讯云视频通话功能的回调接口类。



## 通用事件回调
### onError

错误回调：SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。
```
void onError(TXLiteAVError errCode, const char * errMsg, void * extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | TXLiteAVError | 错误码。 |
| errMsg | const char * | 错误信息。 |
| extraInfo | void * | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。 |


### onWarning

警告回调：用于告知您一些非严重性问题，例如出现了卡顿或者可恢复的解码失败。
```
void onWarning(TXLiteAVWarning warningCode, const char * warningMsg, void * extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| warningCode | TXLiteAVWarning | 警告码。 |
| warningMsg | const char * | 警告信息。 |
| extraInfo | void * | 扩展信息字段，个别警告码可能会带额外的信息帮助定位问题。 |



## 房间事件回调
### onEnterRoom

已加入房间的回调。
```
void onEnterRoom(int result)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| result | int | result > 0 时为进房耗时（ms），result < 0 时为进房错误码。 |

__介绍__

调用 TRTCCloud 中的 enterRoom() 接口执行进房操作后，会收到来自 SDK 的 onEnterRoom(result) 回调： 如果加入成功，result 会是一个正数（result > 0），代表加入房间的时间消耗，单位是毫秒（ms）。 如果加入失败，result 会是一个负数（result < 0），代表进房失败的错误码。 进房失败的错误码含义请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。

调用 TRTCCloud 中的 enterRoom() 接口执行进房操作后，会收到来自 SDK 的 onEnterRoom(result) 回调：
- 如果加入成功，result 会是一个正数（result > 0），表示加入房间所消耗的时间，单位为毫秒（ms）。
- 如果加入失败，result 会是一个负数（result < 0），表示进房失败的错误码。 进房失败的错误码含义请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。

>?在 Ver6.6 之前的版本，只有进房成功会抛出 onEnterRoom(result) 回调，进房失败由 [onError()](https://cloud.tencent.com/document/product/647/32270#onerror) 回调抛出。 在 Ver6.6 及之后改为：进房成功返回正的 result，进房失败返回负的 result，同时进房失败也会有 [onError()](https://cloud.tencent.com/document/product/647/32270#onerror) 回调抛出。



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

调用 TRTCCloud 中的 exitRoom() 接口会执行退出房间的相关逻辑，例如释放音视频设备资源和编解码器资源等。 待资源释放完毕，SDK 会通过 [onExitRoom()](https://cloud.tencent.com/document/product/647/32270#onexitroom) 回调通知到您。
如果您要再次调用 enterRoom() 或者切换到其他的音视频 SDK，请等待 [onExitRoom()](https://cloud.tencent.com/document/product/647/32270#onexitroom) 回调到来后再执行相关操作。否则可能会遇到例如摄像头、麦克风设备被强占等各种异常问题。


### onSwitchRole

切换角色的事件回调。
```
void onSwitchRole(TXLiteAVError errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | TXLiteAVError | 错误码，ERR_NULL 代表切换成功，其他请查阅[错误码](https://cloud.tencent.com/document/product/647/32257)。 |
| errMsg | const char * | 错误信息。 |

__介绍__

调用 TRTCCloud 中的 switchRole() 接口会切换主播和观众的角色，该操作会伴随一个线路切换的过程， 待 SDK 切换完成后，会抛出 [onSwitchRole()](https://cloud.tencent.com/document/product/647/32270#onswitchrole) 事件回调。


### onConnectOtherRoom

请求跨房通话（主播 PK）的结果回调。
```
void onConnectOtherRoom(const char * userId, TXLiteAVError errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 要 PK 的目标主播 userId。 |
| errCode | TXLiteAVError | 错误码，ERR_NULL 代表切换成功，其他请查阅[错误码](https://cloud.tencent.com/document/product/647/32257)。 |
| errMsg | const char * | 错误信息。 |

__介绍__

调用 TRTCCloud 中的 connectOtherRoom() 接口会将两个不同房间中的主播拉通视频通话，也就是所谓的“主播PK”功能。 调用者会收到 [onConnectOtherRoom()](https://cloud.tencent.com/document/product/647/32270#onconnectotherroom) 回调来获知跨房通话是否成功， 如果成功，两个房间中的所有用户都会收到 PK 主播的 [onUserVideoAvailable()](https://cloud.tencent.com/document/product/647/32270#onuservideoavailable) 回调。


### onDisconnectOtherRoom

结束跨房通话（主播 PK）的结果回调。
```
void onDisconnectOtherRoom(TXLiteAVError errCode, const char * errMsg)
```



## 成员事件回调
### onUserEnter

有用户（主播）加入当前房间。
```
void onUserEnter(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |

__介绍__

没有开启音视频上行的观众在加入房间时不会触发该通知，只有开启音视频上行的主播加入房间时才会触发该通知。通知参数中 userId 对应的用户一定已开启声音上行，但不一定已开启视频。
如果需要显示远程画面，更推荐监听 [onUserVideoAvailable()](https://cloud.tencent.com/document/product/647/32270#onuservideoavailable) 事件回调。


### onUserExit

有用户（主播）离开当前房间。
```
void onUserExit(const char * userId, int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| reason | int | 离开原因代码，区分用户是正常离开，还是由于网络断线等原因离开。 |


### onUserVideoAvailable

用户是否开启摄像头视频。
```
void onUserVideoAvailable(const char * userId, bool available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| available | bool | 画面是否开启。 |

__介绍__

当您收到 onUserVideoAvailable(userId， YES) 通知时，代表该路画面已经有可用的视频数据帧到达。此时，您需要调用 startRemoteView(userId) 接口加载该用户的远程画面。然后，您还会收到名为 onFirstVideoFrame(userId) 的首帧画面渲染回调。
当您收到 onUserVideoAvailable(userId， NO) 通知时，代表该路远程画面已经被关闭，可能由于该用户调用了 muteLocalVideo() 或 stopLocalPreview()。

### onUserSubStreamAvailable

用户是否开启屏幕分享。
```
void onUserSubStreamAvailable(const char * userId, bool available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| available | bool | 屏幕分享是否开启。 |

>?显示辅路画面使用的函数不是 startRemoteView() 而是 startRemoteSubStreamView()。



### onUserAudioAvailable

用户是否开启音频上行。
```
void onUserAudioAvailable(const char * userId, bool available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| available | bool | 声音是否开启。 |


### onFirstVideoFrame

开始渲染本地或远程用户的首帧画面。
```
void onFirstVideoFrame(const char * userId, const TRTCVideoStreamType streamType, const int width, const int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 本地或远程用户 ID，如果 userId == null 代表本地，userId != null 代表远程。 |
| streamType | const TRTCVideoStreamType | 视频流类型：摄像头或屏幕分享。 |
| width | const int | 画面宽度。 |
| height | const int | 画面高度。 |

__介绍__

如果 userId 为 null，表示开始渲染本地采集的摄像头画面，需要您先调用 startLocalPreview 触发。 如果 userId 不为 null，表示开始渲染远程用户的首帧画面，需要您先调用 startRemoteView 触发。

>?只有当您调用 startLocalPreview()、startRemoteView() 或 startRemoteSubStreamView() 之后，才会触发该回调。



### onFirstAudioFrame

开始播放远程用户的首帧音频（本地声音暂不通知）。
```
void onFirstAudioFrame(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 远程用户 ID。 |


### onSendFirstLocalVideoFrame

首帧本地视频数据已经被送出。
```
void onSendFirstLocalVideoFrame(const TRTCVideoStreamType streamType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| streamType | const TRTCVideoStreamType | 视频流类型，主画面、小画面或辅流画面（屏幕分享）。 |

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
void onNetworkQuality(TRTCQualityInfo localQuality, TRTCQualityInfo * remoteQuality, uint32_t remoteQualityCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | [TRTCQualityInfo](https://cloud.tencent.com/document/product/647/32271#trtcqualityinfo) | 上行网络质量。 |
| remoteQuality | [TRTCQualityInfo](https://cloud.tencent.com/document/product/647/32271#trtcqualityinfo) * | 下行网络质量。 |
| remoteQualityCount | uint32_t | 下行网络质量的数组大小。 |

>?userId == null 代表自己当前的视频质量。


### onStatistics

技术指标统计回调。
```
void onStatistics(const TRTCStatistics & statis)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statis | const [TRTCStatistics](https://cloud.tencent.com/document/product/647/32271#trtcstatistics) & | 统计数据，包括本地和远程的。 |

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
void onSpeedTest(const TRTCSpeedTestResult & currentResult, uint32_t finishedCount, uint32_t totalCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| currentResult | const [TRTCSpeedTestResult](https://cloud.tencent.com/document/product/647/32271#trtcspeedtestresult) & | 当前完成的测速结果。 |
| finishedCount | uint32_t | 已完成测速的服务器数量。 |
| totalCount | uint32_t | 需要测速的服务器总数量。 |



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


### onUserVoiceVolume

用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。
```
void onUserVoiceVolume(TRTCVolumeInfo * userVolumes, uint32_t userVolumesCount, uint32_t totalVolume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userVolumes | [TRTCVolumeInfo](https://cloud.tencent.com/document/product/647/32271#trtcvolumeinfo) * | 所有正在说话的房间成员的音量，取值范围0 - 100。 |
| userVolumesCount | uint32_t | 房间成员数量。 |
| totalVolume | uint32_t | 所有远端成员的总音量, 取值范围0 - 100。 |

__介绍__

您可以通过调用 TRTCCloud 中的 enableAudioVolumeEvaluation 接口来开关这个回调或者设置它的触发间隔。调用 enableAudioVolumeEvaluation 开启音量回调后，无论频道内是否有人说话，都会按设置的时间间隔调用这个回调，如果没有人说话，则 userVolumes 为空，totalVolume 为0。

>?userId 为 null 时表示自己的音量，userVolumes 内仅包含正在说话（音量不为0）的用户音量信息。



### onDeviceChange

本地设备通断回调。
```
void onDeviceChange(const char * deviceId, TRTCDeviceType type, TRTCDeviceState state)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceId | const char * | 设备 ID。 |
| type | [TRTCDeviceType](https://cloud.tencent.com/document/product/647/32271#trtcdevicetype) | 设备类型。 |
| state | [TRTCDeviceState](https://cloud.tencent.com/document/product/647/32271#trtcdevicestate) | 事件类型。 |


### onTestMicVolume

麦克风测试音量回调。
```
void onTestMicVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 音量值，取值范围0 - 100。 |

__介绍__

麦克风测试接口 startMicDeviceTest 会触发这个回调。


### onTestSpeakerVolume

扬声器测试音量回调。
```
void onTestSpeakerVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 音量值，取值范围0 - 100。 |

__介绍__

扬声器测试接口 startSpeakerDeviceTest 会触发这个回调。



## 自定义消息的接收回调
### onRecvCustomCmdMsg

收到自定义消息回调。
```
void onRecvCustomCmdMsg(const char * userId, int32_t cmdID, uint32_t seq, const uint8_t * message, uint32_t messageSize)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| cmdID | int32_t | 命令 ID。 |
| seq | uint32_t | 消息序号。 |
| message | const uint8_t * | 消息数据。 |
| messageSize | uint32_t | 消息数据大小。 |

__介绍__

当房间中的某个用户使用 sendCustomCmdMsg 发送自定义消息时，房间中的其它用户可以通过 onRecvCustomCmdMsg 接口接收消息。


### onMissCustomCmdMsg

自定义消息丢失回调。
```
void onMissCustomCmdMsg(const char * userId, int32_t cmdID, int32_t errCode, int32_t missed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| cmdID | int32_t | 命令 ID。 |
| errCode | int32_t | 错误码。 |
| missed | int32_t | 丢失的消息数量。 |

__介绍__

TRTC 所使用的传输通道为 UDP 通道，所以即使设置了 reliable，也做不到100不丢失，只是丢消息概率极低，能满足常规可靠性要求。 在过去的一段时间内（通常为5s），自定义消息在传输途中丢失的消息数量的统计，SDK 都会通过此回调通知出来。

>?只有在发送端设置了可靠传输（reliable），接收方才能收到消息的丢失回调。


### onRecvSEIMsg

收到 SEI 消息的回调。
```
void onRecvSEIMsg(const char * userId, const uint8_t * message, uint32_t messageSize)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| message | const uint8_t * | 数据。 |
| messageSize | uint32_t | 数据大小。 |

__介绍__

当房间中的某个用户使用 sendSEIMsg 发送数据时，房间中的其它用户可以通过 onRecvSEIMsg 接口接收数据。



## CDN 旁路转推回调
### onStartPublishCDNStream

启动旁路推流到 CDN 完成的回调。
```
void onStartPublishCDNStream(int errCode, const char * errMsg)
```

__介绍__

对应于 TRTCCloud 中的 startPublishCDNStream() 接口。

>?Start 回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标 CDN 有异常，还是有可能会转推失败。



### onStopPublishCDNStream

停止旁路推流到 CDN 完成的回调。
```
void onStopPublishCDNStream(int errCode, const char * errMsg)
```

__介绍__

对应于 TRTCCloud 中的 stopPublishCDNStream() 接口。


### onSetMixTranscodingConfig

设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。
```
void onSetMixTranscodingConfig(int errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 0表示成功，其余值表示失败。 |
| errMsg | const char * | 具体错误原因。 |



## 屏幕分享回调
### onScreenCaptureCovered

当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。
```
void onScreenCaptureCovered()
```


### onScreenCaptureStarted

当屏幕分享开始时，SDK 会通过此回调通知。
```
void onScreenCaptureStarted()
```


### onScreenCapturePaused

当屏幕分享暂停时，SDK 会通过此回调通知。
```
void onScreenCapturePaused(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 停止原因，0：表示用户主动暂停；1：表示设置屏幕分享参数导致的暂停；2：表示屏幕分享窗口被最小化导致的暂停；3：表示屏幕分享窗口被隐藏导致的暂停。 |


### onScreenCaptureResumed

当屏幕分享恢复时，SDK 会通过此回调通知。
```
void onScreenCaptureResumed(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 停止原因，0：表示用户主动恢复，1：表示屏幕分享参数设置完毕后自动恢复；2：表示屏幕分享窗口从最小化被恢复；3：表示屏幕分享窗口从隐藏被恢复。 |


### onScreenCaptureStoped

当屏幕分享停止时，SDK 会通过此回调通知。
```
void onScreenCaptureStoped(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 停止原因，0：表示用户主动停止；1：表示屏幕分享窗口被关闭。 |



## 背景混音事件回调
### onPlayBGMBegin

开始播放背景音乐。
```
void onPlayBGMBegin(TXLiteAVError errCode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | TXLiteAVError | 错误码。 |


### onPlayBGMProgress

播放背景音乐的进度。
```
void onPlayBGMProgress(uint32_t progressMS, uint32_t durationMS)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| progressMS | uint32_t | 已播放时间。 |
| durationMS | uint32_t | 总时间。 |


### onPlayBGMComplete

播放背景音乐结束。
```
void onPlayBGMComplete(TXLiteAVError errCode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | TXLiteAVError | 错误码。 |




## ITRTCVideoRenderCallback

__功能__

自定义视频渲染回调。



### onRenderVideoFrame

自定义视频渲染回调。
```
void onRenderVideoFrame(const char * userId, TRTCVideoStreamType streamType, TRTCVideoFrame * frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32271#trtcvideostreamtype) | 流类型：即摄像头还是屏幕分享。 |
| frame | TRTCVideoFrame * | 视频帧数据。 |

__介绍__

可以通过 setLocalVideoRenderCallback 和 setRemoteVideoRenderCallback 接口设置自定义渲染回调。



## ITRTCAudioFrameCallback

__功能__

音频数据回调。



### onCapturedAudioFrame
```
void onCapturedAudioFrame(TRTCAudioFrame * frame)
```

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。


### onPlayAudioFrame

混音前的每一路远程用户的音频数据（例如您要对某一路的语音进行文字转换，必须要使用这里的原始数据，而不是混音之后的数据）。
```
void onPlayAudioFrame(TRTCAudioFrame * frame, const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | TRTCAudioFrame * | 音频数据。 |
| userId | const char * | 用户标识。 |

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。


### onMixedPlayAudioFrame
```
void onMixedPlayAudioFrame(TRTCAudioFrame * frame)
```

>?
>- 请不要在此回调函数中做任何耗时操作，建议直接拷贝到另一线程进行处理，否则会导致各种声音问题。
>- 此接口回调出的音频数据是只读的，不支持修改。



## ITRTCLogCallback

__功能__

日志相关回调。



### onLog

有日志打印时的回调。
```
void onLog(const char * log, TRTCLogLevel level, const char * module)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| log | const char * | 日志内容。 |
| level | [TRTCLogLevel](https://cloud.tencent.com/document/product/647/32271#trtcloglevel) | 日志等级 参见 TRTCLogLevel。 |
| module | const char * | 暂无具体意义，目前为固定值 TXLiteAVSDK。 |




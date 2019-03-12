## ITRTCCloudCallback
### 通用事件回调

#### onError

错误回调，SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```
void onError(TXLiteAVError errCode, const char * errMsg, void * arg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码 |
| errMsg | const char * | 错误信息 |
| arg | void * | 保留参数 |




#### onWarning

警告回调。

```
void onWarning(TXLiteAVWarning warningCode, const char * warningMsg, void * arg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | TXLiteAVWarning | 错误码 |
| warningMsg | const char * | 警告信息 |
| arg | void * | 保留参数 |





### 房间事件回调

#### onEnterRoom

进房成功通知。

```
void onEnterRoom(uint64_t elapsed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| elapsed | uint64_t | 进房耗时 |




#### onExitRoom

退房通知。

```
void onExitRoom(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 退出原因 |




#### onConnectOtherRoom

跨房连麦成功回调。

```
void onConnectOtherRoom(const char * userId, TXLiteAVError errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| errCode | TXLiteAVError | 错误码 |
| errMsg | const char * | 错误信息 |




#### onDisconnectOtherRoom

断开跨房连麦回调。

```
void onDisconnectOtherRoom(TXLiteAVError errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码 |
| errMsg | const char * | 错误信息 |





### 成员事件回调

#### onUserEnter

userId 对应的成员的进房通知，您可以在这个回调中调用 startRemoteView 显示该 userId 的视频画面。

```
void onUserEnter(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |




#### onUserExit

userId 对应的成员的退房通知，您可以在这个回调中调用 stopRemoteView 关闭该 userId 的视频画面。

```
void onUserExit(const char * userId, int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| reason | int | 退出原因 |




#### onUserVideoAvailable

userId 对应的远端主路（即摄像头）画面的状态通知。

```
void onUserVideoAvailable(const char * userId, bool available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| available | bool | true：视频可播放；false：视频被关闭 |




#### onUserSubStreamAvailable

userId 对应的远端辅路（屏幕分享等）画面的状态通知。

```
void onUserSubStreamAvailable(const char * userId, bool available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| available | bool | true：视频可播放；false：视频被关闭 |




#### onUserAudioAvailable

userId 对应的远端声音的状态通知。

```
void onUserAudioAvailable(const char * userId, bool available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| available | bool | true：音频可播放；false：音频被关闭 |




#### onUserVoiceVolume

userId 对应的成员语音音量，通过调用 TRTCCloud enableAudioVolumeEvaluation 来触发这个回调。

```
void onUserVoiceVolume(TRTCVolumeInfo * userVolumes, uint32_t userVolumesCount, uint32_t totalVolume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | TRTCVolumeInfo * | 每位发言者的语音音量，取值范围 [0, 100] |
| userVolumesCount | uint32_t | 发言者的人数，即 userVolumes 数组的大小 |
| totalVolume | uint32_t |总的语音音量，取值范围 [0, 100] |





### 统计和质量回调

#### onNetworkQuality

网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。

```
void onNetworkQuality(TRTCQualityInfo localQuality, TRTCQualityInfo * remoteQuality, uint32_t remoteQualityCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCQualityInfo | 上行网络质量 |
| remoteQuality | TRTCQualityInfo * | 下行网络质量的数组 |
| remoteQualityCount | uint32_t | 下行网络质量的数组大小 |




#### onStatistics

技术指标统计回调，每2秒回调一次。

```
void onStatistics(const TRTCStatistics & statis)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statis | const TRTCStatistics & | 状态数据 |

__介绍__


如果您是熟悉音视频领域相关术语，可以通过这个回调获取 SDK 的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调。






### 音视频事件回调

#### onFirstVideoFrame

首帧视频画面到达，界面此时可以结束 loading，并开始显示视频画面。

```
void onFirstVideoFrame(const char * userId, uint32_t width, uint32_t height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| width | uint32_t | 画面宽度 |
| height | uint32_t | 画面高度 |




#### onFirstAudioFrame

首帧音频数据到达。

```
void onFirstAudioFrame(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |




#### onPlayBGMBegin

开始播放背景音乐。

```
void onPlayBGMBegin(TXLiteAVError errCode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码 |




#### onPlayBGMProgress

播放背景音乐的进度。

```
void onPlayBGMProgress(uint32_t progressMS, uint32_t durationMS)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| progressMS | uint32_t | 已播放时间 |
| durationMS | uint32_t | 总时间 |




#### onPlayBGMComplete

播放背景音乐结束。

```
void onPlayBGMComplete(TXLiteAVError errCode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码 |





### 服务器事件回调

#### onConnectionLost

SDK 跟服务器的连接断开。

```
void onConnectionLost()
```




#### onTryToReconnect

SDK 尝试重新连接到服务器。

```
void onTryToReconnect()
```




#### onConnectionRecovery

SDK 跟服务器的连接恢复。

```
void onConnectionRecovery()
```




#### onSpeedTest

服务器测速的回调，SDK 对多个服务器IP做测速，每个 IP 的测速结果通过这个回调通知。

```
void onSpeedTest(const TRTCSpeedTestResult & currentResult, uint32_t finishedCount, uint32_t totalCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| currentResult | const TRTCSpeedTestResult & | 当前完成的测速结果 |
| finishedCount | uint32_t | 已完成测速的服务器数量 |
| totalCount | uint32_t | 需要测速的服务器总数量 |





### 硬件设备事件回调

#### onCameraDidReady

摄像头准备就绪，表示摄像头打开成功，如果打开失败，在 onError 中通知。

```
void onCameraDidReady()
```




#### onMicDidReady

麦克风准备就绪。

```
void onMicDidReady()
```




#### onDeviceChange

设备事件的回调。

```
void onDeviceChange(const char * deviceId, TRTCDeviceType type, TRTCDeviceState state)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | const char * | 设备 ID |
| type | TRTCDeviceType | 设备类型 |
| state | TRTCDeviceState | 事件类型 |




#### onTestMicVolume

麦克风测试音量回调，麦克风测试接口 startMicDeviceTest 会触发这个回调。

```
void onTestMicVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量值，取值范围 [0, 100] |




#### onTestSpeakerVolume

扬声器测试音量回调，扬声器测试接口 startSpeakerDeviceTest 会触发这个回调。

```
void onTestSpeakerVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量值，取值范围 [0, 100] |





### 自定义消息的接收回调

#### onRecvCustomCmdMsg

当房间中的某个用户使用 sendCustomCmdMsg 发送自定义消息时，房间中的其它用户可以通过 onRecvCustomCmdMsg 接口接收消息。

```
void onRecvCustomCmdMsg(const char * userId, int32_t cmdId, uint32_t seq, const uint8_t * msg, uint32_t msgSize)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| cmdId | int32_t | 命令 ID |
| seq | uint32_t | 消息序号 |
| msg | const uint8_t * | 消息数据 |
| msgSize | uint32_t | 消息数据大小 |




#### onMissCustomCmdMsg

TRTC 所使用的传输通道为 UDP 通道，所以即使设置了 reliable，也做不到100不丢失，只是丢消息概率极低，能满足常规可靠性要求。

```
void onMissCustomCmdMsg(const char * userId, int32_t cmdId, int32_t errCode, int32_t missed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| cmdId | int32_t | 命令 ID |
| errCode | int32_t | 错误码，当前版本为-1 |
| missed | int32_t | 丢失的消息数量 |

__介绍__


在过去的一段时间内（通常为5s），自定义消息在传输途中丢失的消息数量的统计，SDK 都会通过此回调通知出来。


__说明__


只有在发送端设置了可靠传输（reliable），接收方才能收到消息的丢失回调。





#### onRecvSEIMsg

当房间中的某个用户使用 sendSEIMsg 发送数据时，房间中的其它用户可以通过 onRecvSEIMsg 接口接收数据。

```
void onRecvSEIMsg(const char * userId, const uint8_t * message, uint32_t msgSize)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| message | const uint8_t * | 数据 |





### 旁路转推和混流回调

#### onStartPublishCDNStream

旁路推流到 CDN 的回调，对应于 TRTCCloud 的 startPublishCDNStream() 接口。

```
void onStartPublishCDNStream(int errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | int | 错误码，参考 TXLiteAVCode.h |
| errMsg | const char * | 错误详细信息 |

__说明__


Start 回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标服务器有异常，还是有可能会转推失败。





#### onStopPublishCDNStream

接口 stopPublishCDNStream 的状态回调。

```
void onStopPublishCDNStream(int errCode, const char * errMsg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | int | 错误码，参考 TXLiteAVCode.h |
| errMsg | const char * | 错误详细信息 |





### 屏幕分享回调

#### onScreenCaptureCovered

当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。

```
void onScreenCaptureCovered()
```




#### onScreenCaptureStarted

当屏幕分享开始时，SDK 会通过此回调通知。

```
void onScreenCaptureStarted()
```




#### onScreenCapturePaused

当屏幕分享暂停时，SDK 会通过此回调通知。

```
void onScreenCapturePaused(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 停止原因。0表示用户主动暂停，1表示设置屏幕分享参数导致的暂停，2表示屏幕分享窗口被最小化导致的暂停，3表示屏幕分享窗口被隐藏导致的暂停 |




#### onScreenCaptureResumed

当屏幕分享恢复时，SDK 会通过此回调通知。

```
void onScreenCaptureResumed(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 停止原因。0表示用户主动恢复，1表示屏幕分享参数设置完毕后自动恢复，2表示屏幕分享窗口从最小化被恢复，3表示屏幕分享窗口从隐藏被恢复 |




#### onScreenCaptureStoped

当屏幕分享停止时，SDK 会通过此回调通知。

```
void onScreenCaptureStoped(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 停止原因。0表示用户主动停止，1表示屏幕分享窗口被关闭 |






## ITRTCVideoRenderCallback
### 自定义视频的渲染回调

#### onRenderVideoFrame

可以通过 setLocalVideoRenderCallback 和 setRemoteVideoRenderCallback 接口设置自定义渲染回调。

```
void onRenderVideoFrame(const char * userId, TRTCVideoStreamType streamType, TRTCVideoFrame * frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识 |
| streamType | TRTCVideoStreamType | 流类型：即摄像头还是屏幕分享 |
| frame | TRTCVideoFrame * | 视频帧数据 |






## ITRTCAudioFrameCallback

音频相关回调。


__说明__

请按需定义相关函数实现，减少不必要的性能损耗。




### 自定义音频回调

#### onCapturedAudioFrame

本机采集到的声音回调。

```
void onCapturedAudioFrame(TRTCAudioFrame * frame)
```




#### onPlayAudioFrame

混音前的每一路声音（比如您要对某一路的语音进行文字转换，必须要使用这里的数据，混音后的数据不适合用于语音识别）。

```
void onPlayAudioFrame(TRTCAudioFrame * frame, const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCAudioFrame * | 音频数据 |
| userId | const char * | 用户标识 |

__说明__


此接口回调的音频数据不可修改。





#### onMixedPlayAudioFrame

经过混合后的声音。

```
void onMixedPlayAudioFrame(TRTCAudioFrame * frame)
```

__说明__


此接口回调的音频数据不可修改。







## ITRTCLogCallback
### Log 信息回调

#### onLog

日志回调。

```
void onLog(const char * log, TRTCLogLevel level, const char * module)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | const char * | 日志内容 |
| level | TRTCLogLevel | 日志类型 |
| module | const char * | 暂无具体意义，目前为固定值 TXLiteAVSDK |

## ITRTCCloudCallback
### 通用事件回调

#### onError
```
void onError(TXLiteAVError errCode, const char * errMsg, void * arg)
```


__功能__


错误回调，SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码  |
| errMsg | const char * | 错误信息  |
| arg | void * | 保留参数  |

<br/>

#### onWarning
```
void onWarning(TXLiteAVWarning warningCode, const char * warningMsg, void * arg)
```


__功能__


警告回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | TXLiteAVWarning | 错误码  |
| warningMsg | const char * | 警告信息  |
| arg | void * | 保留参数  |

<br/>


### 房间事件回调

#### onEnterRoom
```
void onEnterRoom(uint64_t elapsed)
```


__功能__


进房成功通知         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| elapsed | uint64_t | 进房耗时  |

<br/>

#### onExitRoom
```
void onExitRoom(int reason)
```


__功能__


退房通知         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 退出原因  |

<br/>


### 成员事件回调

#### onUserEnter
```
void onUserEnter(const char * userId)
```


__功能__


房间成员进房通知，在这个回调中调用 startRemoteView 接口         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |

<br/>

#### onUserExit
```
void onUserExit(const char * userId, int reason)
```


__功能__


房间成员退房通知，在这个回调中调用 stopRemoteView 接口         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |
| reason | int | 退出原因  |

<br/>

#### onUserVideoAvailable
```
void onUserVideoAvailable(const char * userId, bool available)
```


__功能__


远端用户屏蔽自己的画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |
| available | bool | true：视频可播放，false：视频被关闭  |

<br/>

#### onUserAudioAvailable
```
void onUserAudioAvailable(const char * userId, bool available)
```


__功能__


远端用户屏蔽自己的声音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |
| available | bool | true：音频可播放，false：音频被关闭  |

<br/>

#### onUserVoiceVolume
```
void onUserVoiceVolume(TRTCVolumeInfo * userVolumes, uint32_t userVolumesCount, uint32_t totalVolume)
```


__功能__


成员语音音量回调，通过调用 TRTCCloud enableAudioVolumeEvaluation:smooth: 来触发这个回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | TRTCVolumeInfo * | 每位发言者的语音音量，取值范围 [0, 100]  |
| userVolumesCount | uint32_t | 发言者的人数，即userVolumes数组的大小  |
| totalVolume | uint32_t | 总的语音音量, 取值范围 [0, 100]  |

<br/>


### 统计和质量回调

#### onNetworkQuality
```
void onNetworkQuality(TRTCQualityInfo localQuality, TRTCQualityInfo * remoteQuality, uint32_t remoteQualityCount)
```


__功能__


网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCQualityInfo | 上行网络质量  |
| remoteQuality | TRTCQualityInfo * | 下行网络质量的数组  |
| remoteQualityCount | uint32_t | 下行网络质量的数组大小  |

<br/>

#### onStatistics
```
void onStatistics(const TRTCStatistics & statis)
```


__功能__


技术指标统计回调，每2秒回调一次         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statis | const TRTCStatistics & | 状态数据  |

__介绍__

如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调         

<br/>


### 音视频事件回调

#### onFirstVideoFrame
```
void onFirstVideoFrame(const char * userId)
```


__功能__


首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |

<br/>

#### onFirstAudioFrame
```
void onFirstAudioFrame(const char * userId)
```


__功能__


首帧音频数据到达         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |

<br/>

#### onPlayBGMBegin
```
void onPlayBGMBegin(TXLiteAVError errCode)
```


__功能__


开始播放背景音乐         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码  |

<br/>

#### onPlayBGMProgress
```
void onPlayBGMProgress(uint32_t progressMS, uint32_t durationMS)
```


__功能__


播放背景音乐的进度         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| progressMS | uint32_t | 已播放时间  |
| durationMS | uint32_t | 总时间  |

<br/>

#### onPlayBGMComplete
```
void onPlayBGMComplete(TXLiteAVError errCode)
```


__功能__


播放背景音乐结束         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TXLiteAVError | 错误码  |

<br/>


### 服务器事件回调

#### onConnectionLost
```
void onConnectionLost()
```


__功能__


SDK 跟服务器的连接断开         

<br/>

#### onTryToReconnect
```
void onTryToReconnect()
```


__功能__


SDK 尝试重新连接到服务器         

<br/>

#### onConnectionRecovery
```
void onConnectionRecovery()
```


__功能__


SDK 跟服务器的连接恢复         

<br/>

#### onSpeedTest
```
void onSpeedTest(const TRTCSpeedTestResult & currentResult, uint32_t finishedCount, uint32_t totalCount)
```


__功能__


服务器测速的回调，SDK 对多个服务器IP做测速，每个IP的测速结果通过这个回调通知         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| currentResult | const TRTCSpeedTestResult & | 当前完成的测速结果  |
| finishedCount | uint32_t | 已完成测速的服务器数量  |
| totalCount | uint32_t | 需要测速的服务器总数量  |

<br/>


### 硬件设备事件回调

#### onCameraDidReady
```
void onCameraDidReady()
```


__功能__


摄像头准备就绪，表示摄像头打开成功，如果打开失败，在 onError 中通知         

<br/>

#### onDeviceChange
```
void onDeviceChange(const char * deviceId, TRTCDeviceType type, TRTCDeviceState state)
```


__功能__


设备事件的回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | const char * | 设备ID  |
| type | TRTCDeviceType | 设备类型  |
| state | TRTCDeviceState | 事件类型  |

<br/>

#### onTestMicVolume
```
void onTestMicVolume(uint32_t volume)
```


__功能__


麦克风测试音量回调，麦克风测试接口 startMicDeviceTest 会触发这个回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量值，取值范围 [0, 100]  |

<br/>

#### onTestSpeakerVolume
```
void onTestSpeakerVolume(uint32_t volume)
```


__功能__


扬声器测试音量回调，扬声器测试接口 startSpeakerDeviceTest 会触发这个回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| volume | uint32_t | 音量值，取值范围 [0, 100]  |

<br/>


### ~ITRTCCloudCallback
```
 ~ITRTCCloudCallback()
```

<br/>


## ITRTCVideoRenderCallback
### 自定义数据通道回调

#### onRenderVideoFrame
```
void onRenderVideoFrame(const char * userId, TRTCVideoFrame * frame)
```


__功能__


本地经过预处理后的视频数据，预处理做到事情可能有美颜、裁剪、缩放和旋转         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCVideoFrame * | 视频帧数据  |

<br/>


### ~ITRTCVideoRenderCallback
```
 ~ITRTCVideoRenderCallback()
```

<br/>


## ITRTCAudioFrameProcessCallback
### 自定义数据通道回调

#### onCaptureAudioFrame
```
void onCaptureAudioFrame(TRTCAudioFrame * frame)
```


__功能__


获取 SDK 本地采集的音频数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCAudioFrame * | 音频帧数据  |

<br/>

#### onRemoteAudioFrameBeforeMixing
```
void onRemoteAudioFrameBeforeMixing(const char * userId, TRTCAudioFrame * frame)
```


__功能__


获取 SDK 混音前要播放的音频数据         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |
| frame | TRTCAudioFrame * | 音频帧数据  |

<br/>

#### onRemoteAudioFrameAfterMixing
```
bool onRemoteAudioFrameAfterMixing(const char * userId, TRTCAudioFrame * frame)
```


__功能__


获取 SDK 混音后要播放的音频数据，如果您需要自己播放声音，只需要返回 false 即可接管声音的播放         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | const char * | 用户标识  |
| frame | TRTCAudioFrame * | 音频帧数据  |

<br/>


### ~ITRTCAudioFrameProcessCallback
```
 ~ITRTCAudioFrameProcessCallback()
```

<br/>


## ITRTCLogCallback
### Log 信息回调

#### onLog
```
void onLog(const char * log, TRTCLogLevel level, const char * module)
```


__功能__


日志回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | const char * | 日志内容  |
| level | TRTCLogLevel | 日志类型  |
| module | const char * | 暂无具体意义，目前为固定值TXLiteAVSDK  |

<br/>


### ~ITRTCLogCallback
```
 ~ITRTCLogCallback()
```

<br/>




__功能__


TRTCCloudListener 是 TRTCCloud 的主要回调接口。


<br/>

## 通用事件回调

### onError

错误回调: SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```
void onError(int errCode, String errMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | int | 错误码 TRTCErrorCode |
| errMsg | String | 错误信息 |
| extraInfo | Bundle | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误 |

<br/>


### onWarning

警告回调。

```
void onWarning(int warningCode, String warningMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | int | 错误码 TRTCWarningCode |
| warningMsg | String | 警告信息 |
| extraInfo | Bundle | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误 |

<br/>



## 房间事件回调

### onEnterRoom

加入房间。

```
void onEnterRoom(long elapsed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| elapsed | long | 加入房间耗时，单位毫秒 |

<br/>


### onExitRoom

离开房间 离开房间成功的回调。

```
void onExitRoom(int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 离开房间原因 |

<br/>



## 成员事件回调

### onUserEnter

userid对应的成员的进房通知，您可以在这个回调中调用 startRemoteView 显示该 userid 的视频画面。

```
void onUserEnter(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |

<br/>


### onUserExit

userid对应的成员的退房通知，您可以在这个回调中调用 stopRemoteView 关闭该 userid 的视频画面。

```
void onUserExit(String userId, int reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| reason | int | 退出原因 |

<br/>


### onUserVideoAvailable

userid对应的远端主路（即摄像头）画面的状态通知。

```
void onUserVideoAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| available | boolean | true：视频可播放，false：视频被关闭 |

<br/>


### onUserSubStreamAvailable

userid对应的远端辅路（屏幕分享等）画面的状态通知。

```
void onUserSubStreamAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| available | boolean | true：屏幕分享可播放，false：屏幕分享被关闭 |

<br/>


### onUserAudioAvailable

userid对应的远端声音的状态通知。

```
void onUserAudioAvailable(String userId, boolean available)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| available | boolean | true：音频可播放，false：音频被关闭 |

<br/>


### onUserVoiceVolume

userid对应的成员语音音量 通过调用 TRTCCloud enableAudioVolumeEvaluation 来开关这个回调。

```
void onUserVoiceVolume(ArrayList< TRTCCloudDef.TRTCVolumeInfo > userVolumes, int totalVolume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | ArrayList< TRTCCloudDef.TRTCVolumeInfo > | 每位发言者的语音音量，取值范围 [0, 100] |
| totalVolume | int | 总的语音音量, 取值范围 [0, 100] |

<br/>



## 统计和质量回调

### onNetworkQuality

网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid 为"" 代表自己当前的视频质量。

```
void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality, ArrayList< TRTCCloudDef.TRTCQuality > remoteQuality)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCCloudDef.TRTCQuality | 上行网络质量 |
| remoteQuality | ArrayList< TRTCCloudDef.TRTCQuality > | 下行网络质量 |

<br/>


### onStatistics

技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调。

```
void onStatistics(TRTCStatistics statics)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statics | TRTCStatistics | 状态数据 |

__说明__


每2秒回调一次。


<br/>



## 音视频事件回调

### onFirstVideoFrame

首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面。

```
void onFirstVideoFrame(String userId, int width, int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| width | int | 视频宽度 |
| height | int | 视频高度 |

<br/>


### onFirstAudioFrame

首帧音频数据到达。

```
void onFirstAudioFrame(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |

<br/>



## 服务器事件回调

### onConnectionLost

SDK 跟服务器的连接断开。

```
void onConnectionLost()
```

<br/>


### onTryToReconnect

SDK 尝试重新连接到服务器。

```
void onTryToReconnect()
```

<br/>


### onConnectionRecovery

SDK 跟服务器的连接恢复。

```
void onConnectionRecovery()
```

<br/>


### onSpeedTest

：6.4 服务器测速的回调，SDK 对多个服务器IP做测速，每个IP的测速结果通过这个回调通知。

```
void onSpeedTest(TRTCCloudDef.TRTCSpeedTestResult currentResult, int finishedCount, int totalCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| currentResult | TRTCCloudDef.TRTCSpeedTestResult | 当前完成的测速结果 |
| finishedCount | int | 已完成测速的服务器数量 |
| totalCount | int | 需要测速的服务器总数量 |

<br/>



## 硬件设备事件回调

### onCameraDidReady

摄像头准备就绪。

```
void onCameraDidReady()
```

<br/>


### onMicDidReady

麦克风准备就绪。

```
void onMicDidReady()
```

<br/>


### onAudioRouteChanged

音频路由发生变化，音频路由即声音由哪里输出（扬声器、听筒）。

```
void onAudioRouteChanged(int newRoute, int oldRoute)
```

<br/>



## 自定义消息的接收回调


### onRecvCustomCmdMsg

当房间中的某个用户使用 sendCustomCmdMsg 发送自定义消息时，房间中的其它用户可以通过 onRecvCustomCmdMsg 接口接收消息。

```
void onRecvCustomCmdMsg(String userId, int cmdID, int seq, byte [] message)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| cmdID | int | 命令ID |
| seq | int | 消息序号 |
| message | byte [] | 消息数据 |

__说明__


该消息由 sendCustomCmdMsg 发送。


<br/>


### onMissCustomCmdMsg

TRTC所使用的传输通道为UDP通道，所以即使设置了 reliable，也做不到100不丢失，只是丢消息概率极低，能满足常规可靠性要求。 在过去的一段时间内（通常为5s），自定义消息在传输途中丢失的消息数量的统计，SDK 都会通过此回调通知出来。

```
void onMissCustomCmdMsg(String userId, int cmdID, int errCode, int missed)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| cmdID | int | 数据流ID |
| errCode | int | 错误码，当前版本为-1 |
| missed | int | 丢失的消息数量 |

__说明__


只有在发送端设置了可靠传输(reliable)，接收方才能收到消息的丢失回调。


<br/>



## CDN旁路转推

### onStartPublishCDNStream

旁路推流到CDN的回调，对应于 TRTCCloud 的 startPublishCDNStream() 接口。

```
void onStartPublishCDNStream(int err, String errMsg)
```

__说明__


Start回调如果成功，只能说明转推请求已经成功告知给腾讯云，如果目标服务器有异常，还是有可能会转推失败。


<br/>


### onStopPublishCDNStream
```
void onStopPublishCDNStream(int err, String errMsg)
```

<br/>



## TRTCVideoRenderListener

__功能__


自定义视频渲染回调对象。


<br/>

### onRenderVideoFrame
```
void onRenderVideoFrame(String userId, int streamType, TRTCCloudDef.TRTCVideoFrame frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识 |
| streamType | int | 视频流类型 |
| frame | TRTCCloudDef.TRTCVideoFrame | 待渲染视频帧 |

<br/>



## ITRTCVideoPostProcessListener
### 本地视频的二次加工回调

#### onVideoPostProcess

经过 SDK 前处理后的视频数据，前处理包括对摄像头采集到的视频进行美颜、裁剪、缩放和旋转。

```
int onVideoPostProcess(TRTCCloudDef.TRTCVideoFrame frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCCloudDef.TRTCVideoFrame | 返回给用户处理的 自定义数据（目前只支持 纹理textureId） |

<br/>


#### onVideoPostProcessGLDestroy

自定义预处理，Opengl环境销毁通知回调; 用户可以在此回调里，进行opengl资源回收；保证跟sdk 的opengl 在同一个线程；否则可能会显存泄漏，或 崩溃。

```
void onVideoPostProcessGLDestroy()
```

<br/>



## TRTCLogListener

__功能__


日志事件回调对象。


__介绍__


建议在一个比较早初始化的类中设置回调对象，如Application。


<br/>

### onLog
```
abstract void onLog(String log, int level, String module)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | String | 日志内容 |
| level | int | 日志等级 参见TRTC_LOG_LEVEL |
| module | String | 值暂无具体意义，目前为固定值TXLiteAVSDK |

<br/>





TRTCCloudDelegate 是 TRTCCloud 的主要回调接口     
## 通用事件回调

### onError
```
void onError(int errCode, String errMsg, Bundle extraInfo)
```


__功能__


错误回调: SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | int | 错误码 TRTCErrorCode  |
| errMsg | String | 错误信息  |
| extraInfo | Bundle | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误  |

<br/>

### onWarning
```
void onWarning(int warningCode, String warningMsg, Bundle extraInfo)
```


__功能__


警告回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | int | 错误码 TRTCWarningCode  |
| warningMsg | String | 警告信息  |
| extraInfo | Bundle | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误  |

<br/>


## 房间事件回调

### onEnterRoom
```
void onEnterRoom(long elapsed)
```


__功能__


加入房间         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| elapsed | long | 加入房间耗时，单位毫秒  |

<br/>

### onExitRoom
```
void onExitRoom(int reason)
```


__功能__


离开房间 离开房间成功的回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| reason | int | 离开房间原因  |

<br/>


## 成员事件回调

### onUserEnter
```
void onUserEnter(String userId)
```


__功能__


成员进入房间事件         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |

<br/>

### onUserExit
```
void onUserExit(String userId, int reason)
```


__功能__


成员离开房间事件         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| reason | int | 退出原因  |

<br/>

### onUserVideoAvailable
```
void onUserVideoAvailable(String userId, boolean available)
```


__功能__


成员屏蔽自己的画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| available | boolean | true：视频可播放，false：视频被关闭  |

<br/>

### onUserAudioAvailable
```
void onUserAudioAvailable(String userId, boolean available)
```


__功能__


成员屏蔽自己的声音         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| available | boolean | true：音频可播放，false：音频被关闭  |

<br/>

### onUserVoiceVolume
```
void onUserVoiceVolume(ArrayList< TRTCCloudDef.TRTCVolumeInfo > userVolumes, int totalVolume)
```


__功能__


成员语音音量回调 通过调用 TRTCCloud enableAudioVolumeEvaluation 来开关这个回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | ArrayList< TRTCCloudDef.TRTCVolumeInfo > | 每位发言者的语音音量，取值范围 [0, 100]  |
| totalVolume | int | 总的语音音量, 取值范围 [0, 100]  |

<br/>


## 统计和质量回调

### onNetworkQuality
```
void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality, ArrayList< TRTCCloudDef.TRTCQuality > remoteQuality)
```


__功能__


网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid 为"" 代表自己当前的视频质量         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCCloudDef.TRTCQuality | 上行网络质量  |
| remoteQuality | ArrayList< TRTCCloudDef.TRTCQuality > | 下行网络质量  |

<br/>

### onStatistics
```
void onStatistics(TRTCStatistics statics)
```


__功能__


技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statics | TRTCStatistics | 状态数据  |

__说明__

每2秒回调一次 

<br/>


## 音视频事件回调

### onFirstVideoFrame
```
void onFirstVideoFrame(String userId)
```


__功能__


首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |

<br/>

### onFirstAudioFrame
```
void onFirstAudioFrame(String userId)
```


__功能__


首帧音频数据到达         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |

<br/>


## 服务器事件回调

### onConnectionLost
```
void onConnectionLost()
```


__功能__


SDK 跟服务器的连接断开         

<br/>

### onTryToReconnect
```
void onTryToReconnect()
```


__功能__


SDK 尝试重新连接到服务器         

<br/>

### onConnectionRecovery
```
void onConnectionRecovery()
```


__功能__


SDK 跟服务器的连接恢复         

<br/>

### onSpeedTest
```
void onSpeedTest(TRTCCloudDef.TRTCSpeedTestResult currentResult, int finishedCount, int totalCount)
```


__功能__


SDK 跟服务器的连接断开 （暂无） ：6.5 服务器测速的回调，SDK 对多个服务器IP做测速，每个IP的测速结果通过这个回调通知         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| currentResult | TRTCCloudDef.TRTCSpeedTestResult | 当前完成的测速结果  |
| finishedCount | int | 已完成测速的服务器数量  |
| currentResult | TRTCCloudDef.TRTCSpeedTestResult | 需要测速的服务器总数量  |

<br/>


## 硬件设备事件回调

### onCameraDidReady
```
void onCameraDidReady()
```


__功能__


摄像头准备就绪         

<br/>

### onAudioRouteChanged
```
void onAudioRouteChanged(int newRoute, int oldRoute)
```


__功能__


音频路由发生变化，音频路由即声音由哪里输出（扬声器、听筒）         

<br/>


## 自定义消息的接收回调


### onRecvCustomCmdMsg
```
void onRecvCustomCmdMsg(String roomNum, String userId, int cmdID, int seq, byte [] message)
```


__功能__


收到数据流消息         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomNum | String | 房间号  |
| userId | String | 用户标识  |
| cmdID | int | 命令ID  |
| seq | int | 消息序号  |
| message | byte [] | 消息数据  |

__说明__

该消息由 sendCustomCmdMsg 发送 

<br/>

### onRecvCustomCmdMsgError
```
void onRecvCustomCmdMsgError(String roomNum, String userId, int cmdID, int errCode, int missed)
```


__功能__


接收对方数据流消息错误的回调，只有发送端设置了可靠传输，该接口才起作用         

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomNum | String | 房间号  |
| userId | String | 用户标识  |
| cmdID | int | 数据流ID  |
| errCode | int | 错误码，当前版本为-1  |
| missed | int | 丢失的消息数量  |

<br/>


## TRTCLogDelegate

日志事件回调对象

建议在一个比较早初始化的类中设置回调对象，如Application     
### onLog
```
abstract void onLog(String log, int level, String module)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | String | 日志内容  |
| level | int | 日志等级 参见TRTC_LOG_LEVEL  |
| module | String | 值暂无具体意义，目前为固定值TXLiteAVSDK  |

<br/>


## TRTCVideoRenderDelegate

自定义视频渲染回调对象     
### onRenderVideoFrame
```
void onRenderVideoFrame(String userId, TRTCCloudDef.TRTCVideoFrame frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| frame | TRTCCloudDef.TRTCVideoFrame | 待渲染视频帧  |

<br/>



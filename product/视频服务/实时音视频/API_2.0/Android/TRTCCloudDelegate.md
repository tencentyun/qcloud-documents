<div id="trtc-doc">

# TRTCCloudDelegate

TRTCCloudDelegateTRTCCloud
## `onError`
`void onError(int errCode, String errMsg, Bundle extraInfo)`


__功能__


错误回调: SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | int | 错误码 TRTCErrorCode  |
| errMsg | String | 错误信息  |
| extraInfo | Bundle | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误  |

## `onWarning`
`void onWarning(int warningCode, String warningMsg, Bundle extraInfo)`


__功能__


警告回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | int | 错误码 TRTCWarningCode  |
| warningMsg | String | 警告信息  |
| extraInfo | Bundle | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误  |

## `onEnterRoom`
`void onEnterRoom(int roomId, String userId, long elapsed)`


__功能__


加入房间 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomId | int | 房间号  |
| userId | String | 用户标识  |
| elapsed | long | 加入房间耗时，单位毫秒  |

## `onExitRoom`
`void onExitRoom(int roomId, int reason)`


__功能__


离开房间 离开房间成功的回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomId | int | 房间号  |
| reason | int | 离开房间原因  |

## `onUserEnter`
`void onUserEnter(String userId)`


__功能__


成员进入房间事件 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |

## `onUserExit`
`void onUserExit(String userId, int reason)`


__功能__


成员离开房间事件 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| reason | int | 退出原因  |

## `onUserVideoAvailable`
`void onUserVideoAvailable(String userId, boolean available)`


__功能__


成员屏蔽自己的画面 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| available | boolean | true：视频可播放，false：视频被关闭  |

## `onUserAudioAvailable`
`void onUserAudioAvailable(String userId, boolean available)`


__功能__


成员屏蔽自己的声音 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |
| available | boolean | true：音频可播放，false：音频被关闭  |

## `onUserVoiceVolume`
`void onUserVoiceVolume(ArrayList< TRTCCloudDef.TRTCVolumeInfo > userVolumes, int totalVolume)`


__功能__


成员语音音量回调 通过调用 TRTCCloud

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | ArrayList< TRTCCloudDef.TRTCVolumeInfo > | 每位发言者的语音音量，取值范围 [0, 100]  |
| totalVolume | int | 总的语音音量, 取值范围 [0, 100]  |

## `onNetworkQuality`
`void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality, ArrayList< TRTCCloudDef.TRTCQuality > remoteQuality)`


__功能__


网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid 为"" 代表自己当前的视频质量 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCCloudDef.TRTCQuality | 上行网络质量  |
| remoteQuality | ArrayList< TRTCCloudDef.TRTCQuality > | 下行网络质量  |

## `onStatistics`
`void onStatistics(TRTCStatistics statics)`


__功能__


技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statics | TRTCStatistics | 状态数据  |

__说明__

每2秒回调一次 

## `onFirstVideoFrame`
`void onFirstVideoFrame(String userId)`


__功能__


首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |

## `onFirstAudioFrame`
`void onFirstAudioFrame(String userId)`


__功能__


首帧音频数据到达 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | String | 用户标识  |

## `onConnectionLost`
`void onConnectionLost()`


__功能__


SDK 跟服务器的连接断开 

## `onTryToReconnect`
`void onTryToReconnect()`


__功能__


SDK 尝试重新连接到服务器 

## `onConnectionRecovery`
`void onConnectionRecovery()`


__功能__


SDK 跟服务器的连接恢复 

## `onSpeedTest`
`void onSpeedTest(TRTCCloudDef.TRTCSpeedTestResult currentResult, int finishedCount, int totalCount)`


__功能__


SDK 跟服务器的连接断开 （暂无） ：6.5 服务器测速的回调，SDK 对多个服务器IP做测速，每个IP的测速结果通过这个回调通知 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| currentResult | TRTCCloudDef.TRTCSpeedTestResult | 当前完成的测速结果  |
| finishedCount | int | 已完成测速的服务器数量  |
| currentResult | TRTCCloudDef.TRTCSpeedTestResult | 需要测速的服务器总数量  |

## `onCameraDidReady`
`void onCameraDidReady()`


__功能__


摄像头准备就绪 

## `onAudioRouteChanged`
`void onAudioRouteChanged(int newRoute, int oldRoute)`


__功能__


音频路由发生变化，音频路由即声音由哪里输出（扬声器、听筒） 

## `onRecvCustomCmdMsg`
`void onRecvCustomCmdMsg(String roomNum, String userId, int cmdID, int seq, byte [] message)`


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

## `onRecvCustomCmdMsgError`
`void onRecvCustomCmdMsgError(String roomNum, String userId, int cmdID, int errCode, int missed)`


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


# TRTCLogDelegate

日志事件回调对象

建议在一个比较早初始化的类中设置回调对象，如Application 
## `onLog`
`abstract void onLog(String log, int level, String module)`

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | String | 日志内容  |
| level | int | 日志等级 参见TRTC_LOG_LEVEL  |
| module | String | 值暂无具体意义，目前为固定值TXLiteAVSDK  |



</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

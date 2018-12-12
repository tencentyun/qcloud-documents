<div id="trtc-doc">

# TRTCCloudDelegate

TRTCCloudDelegate 是 TRTCCloud
## `onError`
` - (void)onError:(TRTCErrorCode)errCode errMsg:(nullable NSString *)errMsg extInfo:(nullable NSDictionary *)extInfo `


__功能__


错误回调: SDK不可恢复的错误，一定要监听，并分情况给用户适当的界面提示 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| errCode | TRTCErrorCode | 错误码  |
| errMsg | nullable NSString * | 错误信息  |
| extInfo | nullable NSDictionary * | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题  |

## `onWarning`
` - (void)onWarning:(TRTCWarningCode)warningCode warningMsg:(nullable NSString *)warningMsg extInfo:(nullable NSDictionary *)extInfo `


__功能__


警告回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| warningCode | TRTCWarningCode | 警告码  |
| warningMsg | nullable NSString * | 警告信息  |
| extInfo | nullable NSDictionary * | 扩展信息字段，个别警告码可能会带额外的信息帮助定位问题  |

## `onEnterRoom`
` - (void)onEnterRoom:(UInt32)roomId userId:(NSString *)userId elapsed:(NSInteger)elapsed `


__功能__


加入房间 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomId | UInt32 | 房间号  |
| userId | NSString * | 用户标识  |
| elapsed | NSInteger | 加入房间耗时  |

## `onExitRoom`
` - (void)onExitRoom:(UInt32)roomId reason:(NSInteger)reason `


__功能__


离开房间 离开房间成功的回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomId | UInt32 | 房间号  |
| reason | NSInteger | 离开房间原因  |

## `onUserEnter`
` - (void)onUserEnter:(NSString *)userId `


__功能__


成员进入房间事件 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识  |

## `onUserExit`
` - (void)onUserExit:(NSString *)userId reason:(NSInteger)reason `


__功能__


成员离开房间事件 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识  |
| reason | NSInteger | 离开原因代码  |

## `onUserVideoAvailable`
` - (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available `


__功能__


成员屏蔽自己的画面 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识  |
| available | BOOL | 画面是否开启  |

## `onUserAudioAvailable`
` - (void)onUserAudioAvailable:(NSString *)userId available:(BOOL)available `


__功能__


成员屏蔽自己的声音 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userId | NSString * | 用户标识  |
| available | BOOL | 声音是否开启  |

## `onUserVoiceVolume`
` - (void)onUserVoiceVolume:(NSArray< TRTCVolumeInfo * > *)userVolumes totalVolume:(NSInteger)totalVolume `


__功能__


成员语音音量回调 通过调用 TRTCCloud

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| userVolumes | NSArray< TRTCVolumeInfo * > * | 每位发言者的语音音量，取值范围 0~100  |
| totalVolume | NSInteger | 总的语音音量, 取值范围 0~100  |

## `onNetworkQuality`
` - (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray< TRTCQualityInfo * > *)remoteQuality `


__功能__


网络质量: 该回调每 2 秒触发一次，统计当前网络的上行和下行质量 注：userid == nil 代表自己当前的视频质量 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| localQuality | TRTCQualityInfo * | 上行网络质量  |
| remoteQuality | NSArray< TRTCQualityInfo * > * | 下行网络质量  |

## `onStatistics`
` - (void)onStatistics:(TRTCStatistics *)statistics `


__功能__


技术指标统计回调: 如果您是熟悉音视频领域相关术语，可以通过这个回调获取SDK的所有技术指标， 如果您是首次开发音视频相关项目，可以只关注 onNetworkQuality 回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| statistics | TRTCStatistics * | 统计数据，包括本地和远程的  |

__说明__

每2秒回调一次 

## `onFirstVideoFrame`
` - (void)onFirstVideoFrame:(NSString *)userId `


__功能__


首帧视频画面到达，界面此时可以结束loading，并开始显示视频画面 

## `onFirstAudioFrame`
` - (void)onFirstAudioFrame:(NSString *)userId `


__功能__


首帧音频数据到达 

## `onConnectionLost`
` - (void)onConnectionLost`


__功能__


SDK 跟服务器的连接断开 

## `onTryToReconnect`
` - (void)onTryToReconnect`


__功能__


SDK 尝试重新连接到服务器 

## `onConnectionRecovery`
` - (void)onConnectionRecovery`


__功能__


SDK 跟服务器的连接恢复 

## `onCameraDidReady`
` - (void)onCameraDidReady`


__功能__


SDK 跟服务器的连接断开 （暂无） 7.1 摄像头准备就绪 

## `onAudioRouteChanged`
` - (void)onAudioRouteChanged:(TRTCAudioRoute)route fromRoute:(TRTCAudioRoute)fromRoute `


__功能__


音频路由发生变化(仅iOS)，音频路由即声音由哪里输出（扬声器、听筒） 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| route | TRTCAudioRoute | 当前音频路由  |
| fromRoute | TRTCAudioRoute | 变更前的音频路由  |

## `onDevice`
` - (void)onDevice:(NSString *)deviceId type:(TRTCMediaDeviceType)deviceType stateChanged:(NSInteger)state `


__功能__


本地设备通断回调， 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| deviceId | NSString * | 设备id  |
| deviceType | TRTCMediaDeviceType | 设备类型  |

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| state | NSInteger | 0: 设备断开 1: 设备连接  |

## `onRecvCustomCmdMsg`
` - (void)onRecvCustomCmdMsg:(NSString *)roomNum userId:(NSString *)userId cmdID:(NSInteger)cmdID seq:(UInt32)seq message:(NSData *)message `


__功能__


收到对端用户发来的消息 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomNum | NSString * | 房间号  |
| userId | NSString * | 用户标识  |
| cmdID | NSInteger | 命令ID  |
| seq | UInt32 | 消息序号  |
| message | NSData * | 消息数据  |

__说明__

该消息由 sendCustomCmdMsg 发送 

## `onRecvCustomCmdMsgError`
` - (void)onRecvCustomCmdMsgError:(NSString *)roomNum userId:(NSString *)userId cmdID:(NSInteger)cmdID errCode:(NSInteger)errCode missed:(NSInteger)missed `


__功能__


接收对方数据流消息错误的回调，只有发送端设置了可靠传输，该接口才起作用 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| roomNum | NSString * | 房间号  |
| userId | NSString * | 用户标识  |
| cmdID | NSInteger | 命令ID  |
| errCode | NSInteger | 错误码，当前版本为-1  |
| missed | NSInteger | 丢失的消息数量  |


# TRTCLogDelegate

日志事件回调对象

建议在一个比较早初始化的类中设置回调委托对象，如AppDelegate 
## `onLog`
` - (void)onLog:(nullable NSString *)log LogLevel:(TRTCLogLevel)level WhichModule:(nullable NSString *)module `


__功能__


有日志打印时的回调 

__参数__

| 参数 | 类型 | 含义 |
|-----|------|------|
| log | nullable NSString * | 日志内容  |
| level | TRTCLogLevel | 日志等级 参见TRTCLogLevel  |
| module | nullable NSString * | 值暂无具体意义，目前为固定值TXLiteAVSDK  |



</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

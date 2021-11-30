
__功能__

视频播放器。 

__介绍__

主要负责将直播流的音视频画面进行解码和本地渲染，包含如下技术特点：
- 针对腾讯云的拉流地址，可使用低延时拉流，实现直播连麦等相关场景。
- 针对腾讯云的拉流地址，可使用直播时移功能，能够实现直播观看与时移观看的无缝切换。
- 支持自定义的音视频数据处理，让您可以根据项目需要处理直播流中的音视频数据后，进行渲染以及播放。


 
## SDK 基础函数
### delegate

设置播放回调，见`TXLivePlayListener.h`文件中的详细定义。
```
@property (nonatomic, weak) id< TXLivePlayListener > delegate
```

### videoProcessDelegate

设置视频处理回调，见`TXVideoCustomProcessDelegate.h`文件中的详细定义。
```
@property (nonatomic, weak) id< TXVideoCustomProcessDelegate > videoProcessDelegate
```

### audioRawDataDelegate

设置音频处理回调，见`TXAudioRawDataDelegate.h`文件中的详细定义。
```
@property (nonatomic, weak) id< TXAudioRawDataDelegate > audioRawDataDelegate
```

### enableHWAcceleration

是否开启硬件加速，默认值：NO。
```
@property (nonatomic, assign) BOOL enableHWAcceleration
```

### config

设置 [TXLivePlayConfig](https://cloud.tencent.com/document/product/454/34760) 播放配置项，见`TXLivePlayConfig.h`文件中的详细定义。
```
@property (nonatomic, copy) TXLivePlayConfig * config
```

### recordDelegate

设置短视频录制回调，见`TXLiveRecordListener.h`文件中的详细定义。
```
@property (nonatomic, weak) id< TXLiveRecordListener > recordDelegate
```

### isAutoPlay

startPlay 后是否立即播放，默认 YES，只有点播有效。
```
@property (nonatomic, ) BOOL isAutoPlay
```


## 播放基础接口
### setupVideoWidget

创建 Video 渲染 View，该控件承载着视频内容的展示。
```
- (void)setupVideoWidget:(CGRect)frame containView:(TXView *)view insertIndex:(unsigned int)idx 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | CGRect | Widget 在父 view 中的 frame。 |
| view | TXView * | 父 view。 |
| idx | unsigned int | Widget 在父 view 上的层级位置。 |

__介绍__

变更历史：1.5.2版本将参数 frame 废弃，设置此参数无效，控件大小与参数 view 的大小保持一致，如需修改控件的大小及位置，请调整父 view 的大小及位置。 请参见 [绑定渲染界面](https://cloud.tencent.com/document/product/454/7880#step-2.EF.BC.9A.E6.B8.B2.E6.9F.93-view)。



### removeVideoWidget

移除 Video 渲染 Widget。
```
- (void)removeVideoWidget
```



### startPlay

启动从指定 URL 播放 RTMP 音视频流。
```
- (int)startPlay:(NSString *)url type:(TX_Enum_PlayType)playType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| url | NSString * | 完整的 URL（如果播放的是本地视频文件，这里传本地视频文件的完整路径）。 |
| playType | [TX_Enum_PlayType](https://cloud.tencent.com/document/product/454/34762#tx_enum_playtype) | 播放类型。 |

__返回__

0表示成功，其它为失败。



### stopPlay

停止播放音视频流。
```
- (int)stopPlay
```

__返回__

0：成功；其它：失败。



### isPlaying

是否正在播放。
```
- (BOOL)isPlaying
```

__返回__

YES 拉流中，NO 没有拉流。



### pause

暂停播放。
```
- (void)pause
```

__介绍__

适用于点播，直播（此接口会暂停数据拉流，不会销毁播放器，暂停后，播放器会显示最后一帧数据图像）。



### resume

继续播放，适用于点播，直播。
```
- (void)resume
```




## 视频相关接口
### setRenderRotation

设置画面的方向。
```
- (void)setRenderRotation:(TX_Enum_Type_HomeOrientation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | TX_Enum_Type_HomeOrientation | 方向。 |



### setRenderMode

设置画面的裁剪模式。
```
- (void)setRenderMode:(TX_Enum_Type_RenderMode)renderMode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| renderMode | TX_Enum_Type_RenderMode | 裁剪。 |



### snapshot

截屏。
```
- (void)snapshot:(void(^)(TXImage *))snapshotCompletionBlock 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| snapshotCompletionBlock | void(^)(TXImage *) | 通过回调返回当前图像。 |




## 音频相关接口
### setMute

设置静音。
```
- (void)setMute:(BOOL)bEnable 
```



### setVolume

设置音量。
```
- (void)setVolume:(int)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，取值范围 0 - 100。 |



### setAudioRoute

设置声音播放模式（切换扬声器，听筒）。
```
+ (void)setAudioRoute:(TXAudioRouteType)audioRoute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| audioRoute | TXAudioRouteType | 声音播放模式。 |



### setAudioVolumeEvaluationListener

设置音量大小回调接口。
```
- (void)setAudioVolumeEvaluationListener:(void(^)(int))volumeEvaluationListener
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volumeEvaluationListener | (void(^)(int)) | 音量大小回调接口。 |



### enableAudioVolumeEvaluation

启用音量大小评估。
```
void enableAudioVolumeEvaluation(int intervalMs)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | intervalMs 决定了 volumeEvaluationListener 回调的触发间隔，单位为ms，最小间隔为 100ms，如果小于等于 0 则会关闭回调，建议设置为 300ms。 |

__介绍__

开启后会在 volumeEvaluationListener 中获取到 SDK 对音量大小值的评估。



## 直播时移相关接口
### prepareLiveSeek

直播时移准备，拉取该直播流的起始播放时间。
```
- (int)prepareLiveSeek:(NSString *)domain bizId:(NSInteger)bizId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| domain | NSString * | 时移域名。 |
| bizId | NSInteger | 流 bizId。 |

__返回__

0：OK；-1：无播放地址；-2：appId 未配置。

__介绍__

使用时移功能需在播放开始后调用此方法，否则时移失败。

>!非腾讯云直播地址不能时移。



### resumeLive

停止时移播放，返回直播。
```
- (int)resumeLive
```

__返回__

0：成功；其它：失败。



### seek
```
- (int)seek:(float)time 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| time | float | 流时间，单位为秒。 |

__返回__

0：成功；其它：失败。




## 视频录制相关接口
### startRecord

开始录制短视频。
```
- (int)startRecord:(TXRecordType)recordType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| recordType | TXRecordType | 参见 TXRecordType 定义。 |

__返回__

0：成功；1：正在录制短视频；-2：videoRecorder 初始化失败。



### stopRecord

结束录制短视频。
```
- (int)stopRecord
```

__返回__

0：成功；1：不存在录制任务；-2：videoRecorder 未初始化。



### setRate

设置播放速率。
```
- (void)setRate:(float)rate 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rate | float | 正常速度为1.0；小于为慢速；大于为快速。最大建议不超过2.0。 |




## 更多实用接口
### setLogViewMargin

设置状态浮层 view 在渲染 view 上的边距。
```
- (void)setLogViewMargin:(TXEdgeInsets)margin 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| margin | TXEdgeInsets | 边距。 |



### showVideoDebugLog

是否显示播放状态统计及事件消息浮层 view。
```
- (void)showVideoDebugLog:(BOOL)isShow 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isShow | BOOL | 是否显示。 |



### switchStream

FLV 直播无缝切换。
```
- (int)switchStream:(NSString *)playUrl 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| playUrl | NSString * | 播放地址。 |

__返回__

0：成功；其它：失败。

>!playUrl 必须是当前播放直播流的不同清晰度，切换到无关流地址可能会失败。



### callExperimentalAPI

调用实验性 API 接口。
```
- (void)callExperimentalAPI:(NSString*)jsonStr
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| jsonStr | NSString * | jsonStr 接口及参数描述的 JSON 字符串。 |

__介绍__

该接口用于调用一些实验性功能。



## TX_Enum_PlayType

__功能__

支持的直播和点播类型。

>?点播播放请使用 [TXVodPlayer](https://cloud.tencent.com/document/product/881/20216#.E5.AF.B9.E6.8E.A5.E6.94.BB.E7.95.A5) 播放器，具体请参见头文件 TXVodPlayer.h。

| 枚举 | 含义 |
|-----|-----|
| PLAY_TYPE_LIVE_RTMP | RTMP 直播。 |
| PLAY_TYPE_LIVE_FLV | FLV 直播。 |
| PLAY_TYPE_VOD_FLV | FLV 点播。 |
| PLAY_TYPE_VOD_HLS | HLS 点播。 |
| PLAY_TYPE_VOD_MP4 | MP4点播。 |
| PLAY_TYPE_LIVE_RTMP_ACC | RTMP 直播加速播放。 |
| PLAY_TYPE_LOCAL_VIDEO | 本地视频文件。 |



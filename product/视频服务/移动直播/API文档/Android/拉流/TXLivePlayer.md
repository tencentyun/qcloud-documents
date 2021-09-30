

__功能__

视频播放器。

__介绍__

主要负责将直播流的音视频画面进行解码和本地渲染，包含如下技术特点：
- 针对腾讯云的拉流地址，可使用低延时拉流，实现直播连麦等相关场景。
- 针对腾讯云的拉流地址，可使用直播时移功能，能够实现直播观看与时移观看的无缝切换。
- 支持自定义的音视频数据处理，您可以根据项目需要处理直播流中的音视频数据，然后进行渲染以及播放。
- SDK 仅支持 Android 4.2 以上的版本。



## SDK 基础函数
### TXLivePlayer

创建 [TXLivePlayer](#txliveplayer) 实例。
```
 TXLivePlayer(Context context)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| context | Context | 上下文。 |

***

### setConfig

设置 [TXLivePlayer](#txliveplayer) 播放配置项。
```
void setConfig(TXLivePlayConfig config)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | [TXLivePlayConfig](https://cloud.tencent.com/document/product/454/34774) | 播放器配置项，请参见 [TXLivePlayConfig](https://cloud.tencent.com/document/product/454/34774)。 |

***

### setPlayListener

设置播放回调接口。
```
void setPlayListener(ITXLivePlayListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | [ITXLivePlayListener](https://cloud.tencent.com/document/product/454/34773) | 播放器回调，请参见 [ITXLivePlayListener](https://cloud.tencent.com/document/product/454/34773)。 |

***


## 播放基础接口
### setPlayerView

设置播放器的视频渲染 View。
```
void setPlayerView(TXCloudVideoView glRootView)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| glRootView | TXCloudVideoView | 视频渲染 View。 |

***

### startPlay

播放器开始播放。
```
int startPlay(String playUrl, int playType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| playUrl | String | 播放的流地址。 |
| playType | int | 播放类型。 |

__返回__

是否成功启动播放， 0：成功；-1：失败，playUrl 为空；-2：失败，playUrl 非法；-3：失败，playType 非法。

__介绍__

可播放的直播流连接：
- RTMP 直播流：PLAY_TYPE_LIVE_RTMP。
- FLV 直播流：PLAY_TYPE_LIVE_FLV。
- RTMP 加速流，用于连麦：PLAY_TYPE_LIVE_RTMP_ACC。

***

### stopPlay

停止播放。
```
int stopPlay(boolean isNeedClearLastImg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isNeedClearLastImg | boolean | true：清除；false：不清除。 |

__返回__

0：成功；非0：失败。

__介绍__

isNeedClearLastImg 提供是否清除最后一帧画面的逻辑：
- 推荐在正常停止播放时，进行清除。
- 异常播放，如网络异常等，而您希望等待重连服务器，继续播放时，推荐保留。

***

### isPlaying

是否正在播放。
```
boolean isPlaying()
```

__返回__

true：正在播放；false：未播放。

***

### pause

暂停播放。
```
void pause()
```

__介绍__

停止获取流数据，保留最后一帧画面。

***

### resume

恢复播放。
```
void resume()
```

__介绍__

重新获取数据，获取当前直播数据。

***

### setSurface

使用 Surface 模式用于本地渲染。
```
void setSurface(Surface surface)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| surface | Surface | 视频渲染 surface。 |

>?
>- 目前仅支持硬解。
>- 使用该接口需要 [setPlayerView(TXCloudVideoView)](#setplayerview) 传入 null。
>- 此功能为高级特性，除非您需要使用该特性，否则建议您使用 [setPlayerView(TXCloudVideoView)](#setplayerview)。

***

### setSurfaceSize

设置渲染 Surface 的大小。
```
void setSurfaceSize(int width, int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| width | int | 宽。 |
| height | int | 高。 |

>?
>- Surface 大小变化后，需要重新设定。
>- 此功能为高级特性，除非您需要使用该特性，否则建议您使用 [setPlayerView(TXCloudVideoView)](#setplayerview)。

***


## 播放配置接口
### setRenderMode

设置播放渲染模式。
```
void setRenderMode(int mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | int | 图像渲染模式，可以设置值为：TXLiveConstants#RENDER_MODE_FULL_FILL_SCREEN、TXLiveConstants#RENDER_MODE_ADJUST_RESOLUTION。 |

__介绍__

渲染模式有两种：
- 平铺模式：视频画面将会按照比例铺满屏幕，多余部分会被裁减掉，此模式下不会有黑边。
- 自适应模式：视频画面将等比例缩放，会居中显示，此模式可能会有黑边。

***

### setRenderRotation

设置图像渲染角度。
```
void setRenderRotation(int rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | int | 图像渲染角度，可设置值为：TXLiveConstants#RENDER_ROTATION_PORTRAIT、TXLiveConstants#RENDER_ROTATION_LANDSCAPE。 |

__介绍__

渲染角度有两种：
- 竖屏：播放是竖屏播放的时候使用。
- 横屏：播放是横屏播放的时候使用。

***

### enableHardwareDecode

开启硬件加速。
```
boolean enableHardwareDecode(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：启用视频硬解码， false：禁用视频硬解码。 |

__返回__

true：关闭或开启硬件加速成功；false：关闭或开启硬件加速失败。

***

### setMute

设置是否静音播放。
```
void setMute(boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：静音播放；false：不静音播放。 |

***

### setVolume

设置音量。
```
void setVolume(int volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，取值范围 0 - 100。 |

***

### setAudioRoute

设置声音播放模式。
```
void setAudioRoute(int audioRoute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| audioRoute | int | 声音播放模式，可设置值：TXLiveConstants#AUDIO_ROUTE_RECEIVER、TXLiveConstants#AUDIO_ROUTE_SPEAKER。 |

__介绍__

播放模式有两种：
- 听筒：声音将从听筒播出。
- 扬声器：声音将从扬声器播出。

***

### switchStream

FLV 多清晰度切换。
```
int switchStream(String playUrl)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| playUrl | String | 播放的流地址。 |

__介绍__

使用说明：
- 必须是腾讯云的直播地址。
- 必须是当前播放直播流的不同清晰度，切换到无关流地址可能会失败。

***


### setAudioVolumeEvaluationListener

设置音量大小回调接口。
```
void setAudioVolumeEvaluationListener(ITXAudioVolumeEvaluationListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | [ITXAudioVolumeEvaluationListener](#itxaudiovolumeevaluationlistener) | 音量大小回调接口。 |

***

### enableAudioVolumeEvaluation

启用音量大小评估。
```
void enableAudioVolumeEvaluation(int intervalMs)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | intervalMs 决定了 [onAudioVolumeEvaluationNotify](#onAudioVolumeEvaluationNotify) 回调的触发间隔，单位为ms，最小间隔为 100ms，如果小于等于 0 则会关闭回调，建议设置为 300ms。 |

__介绍__

开启后会在 [onAudioVolumeEvaluationNotify](#onAudioVolumeEvaluationNotify) 中获取到 SDK 对音量大小值的评估。

***

### callExperimentalAPI

调用实验性 API 接口。
```
void callExperimentalAPI(final String jsonStr)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| jsonStr | String | jsonStr 接口及参数描述的 JSON 字符串。 |

__介绍__

该接口用于调用一些实验性功能。

***


## 本地录制和截图
### setVideoRecordListener

设置录制回调接口。
```
void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | TXRecordCommon.ITXVideoRecordListener | 接口。 |

***

### startRecord

启动视频录制。
```
int startRecord(int recordType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| recordType | int | TXRecordCommon#RECORD_TYPE_STREAM_SOURCE |

__返回__

0表示成功，非0表示失败。

__介绍__

目前录制格式仅支持录制直播流，TXRecordCommon#RECORD_TYPE_STREAM_SOURCE。

***

### stopRecord

停止视频录制。
```
int stopRecord()
```

__返回__

0表示成功，非0表示失败。

***

### snapshot

播放过程中本地截图。
```
void snapshot(ITXSnapshotListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | [ITXSnapshotListener](#itxsnapshotlistener) | 截图回调。 |

***

[](id:addVideoRawData)
## 自定义数据处理
### addVideoRawData

设置软解码数据载体 Buffer。
```
boolean addVideoRawData(byte [] yuvBuffer)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| yuvBuffer | byte [] | - |

__介绍__

三个注意点：
- 该 Buffer 用于接受软解回调出来的 I420 格式的 YUV 数据。
- Buffer 大小 = width * height * 3 / 2。
- 视频 width 和 height，可通过 [ITXLivePlayListener#onPlayEvent(int， Bundle)](https://cloud.tencent.com/document/product/454/34773#onplayevent) 的 TXLiveConstants#PLAY_EVT_CHANGE_RESOLUTION 事件获取到。

***

### setVideoRawDataListener

设置软解码视频数据回调。
```
void setVideoRawDataListener(final ITXVideoRawDataListener listener)
```

>?
>- 此功能会有一定的性能开销，特别是在高分辨率的情况下。
>- 调用前需先调用 addVideoRawData 设置数据载体。
>- 除非您有特殊的需求，否则不建议您开启。

***

### setAudioRawDataListener

设置音频数据回调。
```
void setAudioRawDataListener(ITXAudioRawDataListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | [ITXAudioRawDataListener](#itxaudiorawdatalistener) | 音频数据回调。 |

>?
>- 音频播放器会在播放数据的前一刻，调用此函数，同步回调将要播放的数据。
>- 请不要在函数内做耗时操作，否则会影响声音播放的流畅性。

***


## 直播时移接口
### prepareLiveSeek

直播时移准备。
```
int prepareLiveSeek(String domain, int bizid)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| domain | String | 时移域名。 |
| bizid | int | 流 bizid。 |

__返回__

0：OK；-1：无直播地址；-2：appId 未配置。

__介绍__

使用说明：
- 非腾讯云直播地址不能时移。
- 使用时移功能需在播放开始后调用此方法，否则时移失败。

***

### seek

直播时移跳转。
```
void seek(int time)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| time | int | 视频流时间点，单位为秒。 |

__介绍__

直播流则会时移到该时间点。

***

### resumeLive

恢复直播播放。
```
int resumeLive()
```

__介绍__

从直播时移播放中，恢复到直播播放。

***


## 待废弃接口
### setAutoPlay

设置点播自动播放。
```
void setAutoPlay(boolean autoPlay)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| autoPlay | boolean | 自动播放开关。 |

__介绍__

待废弃，此接口仅针对点播视频使用，对直播视频无效；若您想使用点播功能，请使用 [TXVodPlayer](https://cloud.tencent.com/document/product/881/20216#.E5.AF.B9.E6.8E.A5.E6.94.BB.E7.95.A5) 进行点播播放。

***

### setRate

设置点播播放速率。
```
void setRate(float rate)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rate | float | - |

__介绍__

待废弃，此接口仅针对点播视频使用，对直播视频无效；若您想使用点播功能，请使用 [TXVodPlayer](https://cloud.tencent.com/document/product/881/20216#.E5.AF.B9.E6.8E.A5.E6.94.BB.E7.95.A5) 进行点播播放。

***




## ITXSnapshotListener

__功能__

截图回调接口类。



### onSnapshot

截图回调。
```
void onSnapshot(Bitmap bmp)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bmp | Bitmap | 当前视频图片。 |

***


## ITXVideoRawDataListener

__功能__

软解视频数据回调接口类。



### onVideoRawDataAvailable

软解码器解出一帧数据回调一次。
```
void onVideoRawDataAvailable(byte [] yuvBuffer, int width, int height, int timestamp)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| yuvBuffer | byte [] | I420 格式 YUV 数据。 |
| width | int | 视频宽度。 |
| height | int | 视频高度。 |
| timestamp | int | 视频 PTS。 |

__介绍__

需要在回调中再次调用 [addVideoRawData](#addVideoRawData)，将 buffer 塞给 SDK 来填充下一帧 YUV 数据。

***


## ITXAudioRawDataListener

__功能__

音频原始数据接口类。



### onPcmDataAvailable

音频播放数据回调，数据格式 ：PCM。
```
void onPcmDataAvailable(byte [] buf, long timestamp)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| buf | byte [] | pcm 数据。 |
| timestamp | long | 时间戳。 |

__介绍__

音频播放器会在播放数据的前一刻，调用此函数，同步回调将要播放的数据。因此在函数内部做耗时操作可能会影响播放。

***

### onAudioInfoChanged

音频播放信息回调。
```
void onAudioInfoChanged(int sampleRate, int channels, int bits)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sampleRate | int | 采样率。 |
| channels | int | 声道数。 |
| bits | int | 采样点大小。 |

***


## ITXAudioVolumeEvaluationListener

__功能__

播放器音量大小回调。


[](id:onAudioVolumeEvaluationNotify)
### onAudioVolumeEvaluationNotify

播放器音量大小回调。
```
void onAudioVolumeEvaluationNotify(int volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小, 取值范围 [0，100]。 |


